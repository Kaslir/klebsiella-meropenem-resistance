"""Download a new discovery snapshot; never overwrite the frozen study data.

Usage: python src/refresh_ncbi.py --output data/new_snapshot
The NCBI browser backend can change; validate response counts and identities.
"""
import argparse
import hashlib
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def retrieve(collection, query, limit):
    params = dict(action='retrieve', collection=collection, filter=query,
                  fl='*', limit=limit)
    url = 'https://www.ncbi.nlm.nih.gov/pathogens/pathogens-srv/?' + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=90) as response:
                result = json.load(response)
            assert result.get('success'), result
            data = result['ngout']['data']
            assert len(data['content']) == data['totalCount'], 'Response truncated; add pagination.'
            time.sleep(0.5)
            return result
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 ** (attempt + 1))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Choose a new output directory; existing data will not be overwritten.')
    query = 'antibiotic:meropenem AND scientific_name:"Klebsiella pneumoniae"'
    ast = retrieve('ast', query, 100000)
    samples = sorted({r['biosample_acc'] for r in ast['ngout']['data']['content']})
    genomes = []
    for start in range(0, len(samples), 100):
        batch = samples[start:start + 100]
        found = retrieve('isolates', 'biosample_acc:(' + ' OR '.join(batch) + ')', 10000)
        genomes.extend(found['ngout']['data']['content'])
        print(f'Fetched {min(start+100,len(samples))}/{len(samples)} BioSamples')
    assert len(genomes) == len({g['biosample_acc'] for g in genomes})
    assert {g['biosample_acc'] for g in genomes} == set(samples)
    args.output.mkdir(parents=True)
    for name, data in [('ncbi_ast_full.json', ast), ('ncbi_matched_isolates.json', genomes)]:
        (args.output/name).write_text(json.dumps(data, indent=2), encoding='utf-8')
    manifest = {'retrieved_utc': datetime.now(timezone.utc).isoformat(), 'query': query,
                'sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in args.output.glob('*.json')}}
    (args.output/'manifest.json').write_text(json.dumps(manifest, indent=2))
    print('New snapshot saved. Do not substitute it for the frozen study without rerunning all analyses.')


if __name__ == '__main__':
    main()
