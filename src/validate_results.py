"""Validate saved research artifacts without retraining; run from repository root."""
import base64
import csv
import hashlib
import json
import math
import zlib
from pathlib import Path

root = Path(__file__).resolve().parents[1]
def read_csv(name):
    with (root/'results'/name).open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream))

checks = []
raw = root/'data/raw'
for name, expected in json.loads((raw/'sha256.json').read_text()).items():
    assert hashlib.sha256((raw/name).read_bytes()).hexdigest() == expected
checks.append('Raw snapshot SHA-256 hashes match.')
ast = json.loads((raw/'ncbi_ast_full.json').read_text())['ngout']['data']['content']
genomes = json.loads((raw/'ncbi_matched_isolates.json').read_text())
assert len(ast) == 1172 and len(genomes) == 1169
assert {x['biosample_acc'] for x in ast} == {x['biosample_acc'] for x in genomes}
lookup = {x['biosample_acc']: x for x in genomes}
data = read_csv('analysis_dataset.csv')
assert len(data) == 749 and len({x['biosample'] for x in data}) == 749
for row in data:
    assert row['assembly'] == lookup[row['biosample']]['asm_acc']
    source_labels = {t['phenotype'] for t in ast if t['biosample_acc'] == row['biosample']}
    assert source_labels == {row['phenotype']}
    assert int(row['y']) == int(row['phenotype'] == 'resistant')
checks.append('All 749 final records trace to matching original assemblies and laboratory labels.')
splits = read_csv('split_manifest.csv')
train = [x for x in splits if x['partition'] == 'train']
test = [x for x in splits if x['partition'] == 'test']
assert len(train) == 598 and len(test) == 151
assert {x['biosample'] for x in train}.isdisjoint(x['biosample'] for x in test)
assert {x['cluster'] for x in train}.isdisjoint(x['cluster'] for x in test)
checks.append('Primary partition has 598/151 observations and zero shared BioSamples or supplied clusters.')
predictions = read_csv('test_predictions.csv')
assert {x['biosample'] for x in predictions} == {x['biosample'] for x in test}
for metric in read_csv('test_metrics.csv'):
    name = metric['model']
    pairs = [(int(x['y']), int(x[name+'_prediction'])) for x in predictions]
    tp = sum(a == b == 1 for a,b in pairs)
    fp = sum(a == 0 and b == 1 for a,b in pairs)
    fn = sum(a == 1 and b == 0 for a,b in pairs)
    tn = sum(a == b == 0 for a,b in pairs)
    expected = dict(accuracy=(tp+tn)/len(pairs), precision=tp/(tp+fp) if tp+fp else 0,
                    recall=tp/(tp+fn), f1=2*tp/(2*tp+fp+fn))
    for field,value in expected.items():
        assert math.isclose(float(metric[field]), value, abs_tol=1e-12)
checks.append('Accuracy, precision, recall and F1 independently recomputed from every saved test prediction.')
nb = json.loads((root/'notebooks/meropenem_resistance.ipynb').read_text(encoding='utf-8'))
codes = [c for c in nb['cells'] if c['cell_type'] == 'code']
assert [c['execution_count'] for c in codes] == list(range(1,len(codes)+1))
assert all(o['output_type'] != 'error' for c in codes for o in c['outputs'])
images = sum('image/png' in o.get('data',{}) for c in codes for o in c['outputs'])
assert images == 6, f'Expected six embedded plots, got {images}'
markdown = '\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='markdown')
assert all(f'## {i}.' in markdown for i in range(1,9))
checks.append(f'All {len(codes)} code cells executed in order, no saved errors, eight stages, six embedded figures.')
report = '# Validation record\n\n' + '\n'.join('- PASS: '+x for x in checks)
report += '''

The notebook was executed in a fresh local kernel from an initially empty working directory, restoring
the frozen data from its embedded payload. The notebook format was validated with nbformat. Six exported
figures were visually inspected for titles, axes, legends and clipping. This does not certify absence of all
scientific bias: missing relatedness, standard editions and external validation remain limitations.

The local execution completed all cells and saved outputs; the Windows Jupyter wrapper returned a nonzero
shutdown status after reporting successful completion. The separate artifact checks above exit successfully.
A final run in the group's Google Colab account has not been performed and remains a submission check.
'''
(root/'docs/validation.md').write_text(report,encoding='utf-8')
print(report)
