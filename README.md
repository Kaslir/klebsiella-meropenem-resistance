# Meropenem resistance prediction in Klebsiella pneumoniae

| Group Members |
| Elijah Njugi, 146412 | 
| Kisotu Samwel Lemayian, 152170 |
| Billiart Mwangi, 164099 | 
| Grace Wairimu, 165899 |
| Samson Aira, 166456 | 
| Kevin Renana, 168377 | 


An undergraduate Computing Bioinformatics project using real NCBI laboratory susceptibility records and
AMRFinderPlus annotations. The group approved KPC family, NDM family and exact blaOXA-48 predictors.
All eight lecturer-required stages appear in the executed notebook, with saved outputs and six figures.

## Run in Google Colab

1. Open https://colab.research.google.com/ and choose File → Upload notebook.
2. Upload `notebooks/meropenem_resistance.ipynb`.
3. Choose Runtime → Run all. A CPU runtime is sufficient. No GPU, API token, Google Drive mount or extra data upload is required.
4. Save/download the executed notebook. Generated CSVs, figures and conclusions are in the runtime's `results/` directory.

The frozen raw data are embedded in the notebook with SHA-256 checks; the same files are in `data/raw/`.
The notebook uses installed scientific packages, installing missing packages if necessary. Exact tested versions
are in requirements.txt; changes in Colab package versions may cause small numerical differences.
The notebook was executed from beginning to end in a fresh local Jupyter kernel and an empty working directory.
It has not been run inside the user's Google Colab account; a final Colab run remains a submission check.

## Local reproduction

Use Python 3.13 (tested), create a virtual environment, then run `python -m pip install -r requirements.txt`.
Open the notebook in Jupyter/VS Code and run all cells. Run from the repository root to place outputs in its results folder.
Do not substitute a current download for the frozen snapshot and assume the results will remain unchanged.

## Verified findings

- 1,169 matched BioSamples; 807 eligible candidates with assembly accession and recorded testing standard.
- 749 after uncertain gene calls are excluded: 371 resistant and 378 susceptible.
- 598 training and 151 test isolates, with no known PDS cluster shared across the main split.
- Random Forest was selected using training-only grouped CV. Logistic Regression and Random Forest tie on the test set:
  accuracy 90.07%, precision 91.55%, resistant recall 87.84%, F1 89.66%; each misses 9 of 74 resistant test isolates.
- The majority baseline has 50.99% accuracy and zero resistant recall/F1; it predicts all test isolates susceptible.
- blaNDM has the largest marginal sample odds ratio. 61 resistant isolates lack the three selected complete gene calls.
- Study-held-out recall varies strongly; for PRJNA278886 it is 36.36%, despite 90.48% accuracy.

This is research evidence, not a clinical susceptibility tool. The three features cannot fully explain resistance.
No model was tuned on test performance. See the notebook and methodology for limitations and selection decisions.

## Repository contents
- `notebooks/`: executed, self-contained main deliverable.
- `data/raw/`: original NCBI snapshots and checksums.
- `src/refresh_ncbi.py`: separate live-data acquisition utility; does not overwrite study data.
- `results/`: QC audit, final dataset, figures, gene associations, split manifest, CV/test/study metrics and conclusions.
- `docs/`: methodology, variable dictionary, validation record and individual reflection guidance.

## Attribution and use

Raw data: NCBI Pathogen Detection, snapshot 18 November 2026. Cite source BioProjects in the dataset manifest
and the references in the notebook. NCBI's molecular-data policy notes possible submitter rights;
the data are not assigned a new blanket license here. This project was prepared with AI assistance and must
be reviewed and understood by the group before submission, following university requirements.
