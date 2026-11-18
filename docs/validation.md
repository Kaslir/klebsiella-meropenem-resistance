# Validation record

- PASS: Raw snapshot SHA-256 hashes match.
- PASS: All 749 final records trace to matching original assemblies and laboratory labels.
- PASS: Primary partition has 598/151 observations and zero shared BioSamples or supplied clusters.
- PASS: Accuracy, precision, recall and F1 independently recomputed from every saved test prediction.
- PASS: All 11 code cells executed in order, no saved errors, eight stages, six embedded figures.

The notebook was executed in a fresh local kernel from an initially empty working directory, restoring
the frozen data from its embedded payload. The notebook format was validated with nbformat. Six exported
figures were visually inspected for titles, axes, legends and clipping. This does not certify absence of all
scientific bias: missing relatedness, standard editions and external validation remain limitations.

The local execution completed all cells and saved outputs; the Windows Jupyter wrapper returned a nonzero
shutdown status after reporting successful completion. The separate artifact checks above exit successfully.
A final run in the group's Google Colab account has not been performed and remains a submission check.
