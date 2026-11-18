# Methodology and findings

## Design and provenance

Retrospective secondary analysis of public K. pneumoniae records with meropenem AST. The approved question asks
whether three resistance-gene presence features predict laboratory R/S status. One BioSample is one observation.
NCBI AST labels are independently submitted laboratory results; AMRFinderPlus outputs supply genomic features.
No sequences, labels, accession numbers or results were synthesized. Raw sequence processing was not rerun.

The frozen query returned 1,172 tests across 1,169 BioSamples, each matched to one isolate record and the same
Pathogen Detection target. Three additional AST rows are repeat tests with agreeing labels. Sequential exclusions:
51 non-binary phenotypes, 213 without assembly accessions, 98 without known testing standard, and 58 uncertain
gene-call records. This leaves 749 (371 resistant, 378 susceptible). All 807 candidates passed the broad provider
assembly-statistic screen: 4–7 Mb, at most 500 contigs and N50 at least 20 kb. These screens do not establish
genome completeness or absence of contamination. The missing-value and exclusion audit is saved per isolate.

## Feature and outcome definitions

KPC and NDM families include numbered variants; OXA-48 is exact. Complete calls count as present. A target fragment
without a complete call is uncertain; generic OXA without exact OXA-48 evidence makes the third feature uncertain.
After successful annotation and these checks, no target hit is operational absence, not proof of biological absence.
Other OXA alleles are not silently grouped into OXA-48. R=1 and S=0; intermediate, not-defined and susceptible-dose-
dependent outcomes are excluded. Source labels, MIC inequalities and testing-standard metadata are preserved;
breakpoint editions are not known and no contemporary reclassification was attempted. Annotation modes and
reference database versions vary and are tabulated. No imputation or scaling is needed for binary features.

## Biological analysis

Descriptive plots cover outcomes, genes, within-outcome prevalence and gene combinations. Two-sided Fisher
tests, marginal odds ratios, conditional exact confidence intervals and three-test BH adjustment are reported.
These inferential quantities assume independence that may not hold across bacterial lineages; they are exploratory,
not causal or population-structure-adjusted evidence. Literature comparison fulfills the biological interpretation
stage. The NCBI-derived 2026 study may share source isolates and is not treated as independent validation.

KPC carriers: 118/122 resistant (96.72%); NDM: 165/170 (97.06%); exact OXA-48: 69/92 (75.00%).
The marginal sample odds ratios are 43.61, 59.75 and 3.53 respectively. These are not the fitted logistic coefficients.
Among 407 isolates with none of the selected complete calls, 61 (14.99%) are resistant. Other mechanisms remain
possible, but this analysis does not establish which caused each resistant phenotype.

## Prediction and leakage safeguards

The first seeded five-fold StratifiedGroupKFold split provides 598 training and 151 test observations.
Known PDS cluster versions are collapsed to accession roots; no known cluster crosses the main split or a CV fold.
The 244 retained isolates without supplied clusters receive unique BioSample groups; unknown relatedness and
repeated patients remain possible. Source BioProjects can cross the main split. A connected study-and-cluster
partition would place most data in a dominant group, so it is not the primary evaluation.

Predictors are limited to three binary genes. IDs, phenotype-derived counts, other drug phenotypes, source and
cluster labels are not predictors. No feature selection, threshold search or hyperparameter tuning uses the test set.
All model choices were fixed before evaluation. Identity preprocessing is wrapped in a pipeline. Logistic Regression
uses C=1, L2 regularization and balanced weights. Random Forest uses 300 trees, depth 3, leaf size 5 and balanced
weights. The majority-class baseline is fit separately on each training fold. Five-fold grouped training CV selects
by resistant F1, then recall; the primary threshold remains 0.5.

## Results and interpretation

Random Forest has mean CV F1 0.860 versus Logistic Regression 0.845 and was selected before test evaluation.
Both learned models make identical test classifications: TN=71, FP=6, FN=9, TP=65. Accuracy=0.9007,
precision=0.9155, resistant recall=0.8784, F1=0.8966. The baseline predicts susceptible throughout
(TN=77, FN=74), accuracy=0.5099 and resistant recall/F1=0. The test result does not establish superiority of
one learned model: only three features and eight possible patterns limit their distinctions. Probability outputs
can differ even when classifications and ranking metrics agree. Scores are not calibrated clinical probabilities.

Cluster bootstrap intervals quantify some test-set dependence but cannot account for unobserved clusters or
selection bias. The same resampled clusters are used for each model. For subgroups without resistant cases,
resistant recall/F1 and balanced accuracy/AUC are undefined; they are saved blank, not interpreted as zero recall.
Precision uses zero when no resistant predictions exist, as an explicit computational convention.

Five largest studies are separately held out, with overlapping known clusters purged from training. These are
sensitivity checks, not independent external validation. PRJNA278886 gives 36.36% resistant recall and 90.48%
accuracy for both learned models. Thus aggregate accuracy masks important failures under study shift.

## Conclusions and limitations

The features improve held-out prediction relative to the simple baseline in this selected cohort, but three genes
do not explain all resistance or establish clinical safety. Main limitations: public-data selection, missing standard
editions, mixed annotations, incomplete genomes, uncertainty exclusions, lineage/study effects, missing patient
grouping, limited feature space and no independent prospective validation. Future work should standardize
annotation and AST provenance, check sequences, and validate across independent studies and lineages before
considering additional approved mechanisms or alternative thresholds. Conclusions by objective are in results/conclusions.md.

## References

- NCBI AST documentation: https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/
- NCBI AMRFinderPlus interpretation: https://github.com/ncbi/amr/wiki/Interpreting-results
- Vijayakumar and Ramaiah (2026): https://doi.org/10.3389/fmicb.2026.1851170
- scikit-learn grouped stratification: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html
- NCBI data policy: https://www.ncbi.nlm.nih.gov/home/about/policies/

### Combination detail and additional metric definition

NDM plus exact OXA-48 without KPC: 35/35 resistant; KPC plus NDM without exact OXA-48: 7/7 resistant. Small denominators preclude claims of perfect generalization. Exact OXA-48 alone: 34/57 resistant (59.65%). The saved pr_auc column is average precision, not trapezoidal precision-recall area.
