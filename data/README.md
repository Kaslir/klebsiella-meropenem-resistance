# Data provenance

The raw JSON files are the frozen NCBI browser downloads from 18 November 2026 used in Phase 2.
They contain public bacterial genome/annotation metadata and submitted laboratory susceptibility data.
No human genomic sequences are included. These public records can still contain contextual host/location
metadata; the model uses only three bacterial gene features. Avoid adding unnecessary patient-linked fields.

- `raw/ncbi_ast_full.json`: AST backend response (1,172 meropenem tests; 1,169 BioSamples).
- `raw/ncbi_matched_isolates.json`: one matched isolate metadata record per BioSample.
- `raw/sha256.json`: byte-level snapshot integrity hashes, also enforced by the notebook's embedded copy.

The notebook embeds compressed copies so it runs in Colab without a private Drive dependency.
`results/data_dictionary.csv` describes analysis variables; `docs/raw_field_dictionary.md` describes source fields.
The frozen 807-candidate cohort becomes 749 after uncertain gene calls are excluded. No assemblies were
independently reassembled or screened for contamination; provider quality statistics are used.

NCBI's molecular-data policy: https://www.ncbi.nlm.nih.gov/home/about/policies/
NCBI imposes no use/distribution restrictions of its own but notes possible submitter or country-of-origin
intellectual-property claims. Do not describe this dataset as CC0 or apply a code license to third-party data.
Cite NCBI and originating projects. BioProject accessions appear in the QC and analysis tables.

Refreshing: `python src/refresh_ncbi.py --output data/new_snapshot` downloads a separate current snapshot.
That does not update the notebook's embedded frozen data. A new snapshot is a new analysis and requires
rebuilding the embedded data, checking provenance, and rerunning every stage.
