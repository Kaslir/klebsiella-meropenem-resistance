# Results and conclusions

1. **Data acquisition:** obtained 1,169 BioSample-matched isolates from NCBI, with laboratory meropenem phenotypes and AMRFinderPlus annotations. The approved assembly/standard candidate cohort contained 807 isolates.
2. **Cleaning and exploration:** retained 749 isolates after all specified checks: 371 resistant and 378 susceptible. All three binary predictors are complete in the final table; unresolved calls were excluded, not imputed.
3. **Biological associations:** blaNDM had the largest marginal sample odds ratio (59.75). There were 61 resistant isolates among 407 without the selected complete gene calls. Associations are exploratory and do not prove causation or explain all resistance.
4. **Prediction:** training-only grouped CV selected Random Forest. On 151 held-out isolates it achieved accuracy 0.901, precision 0.915, resistant recall 0.878, and F1 0.897. Baseline F1 was 0.000. The highest observed learned-model test F1 was from Logistic Regression and Random Forest; test ranking does not revise the CV choice or establish statistical superiority.

**Research question:** the selected features provide better held-out F1 than the simple baseline in this selected cohort. They provide incomplete information and are insufficient for reliable clinical susceptibility prediction on their own. The study-held-out results should be read alongside this primary result.

**Limits and next steps:** preserve the limitations in notebook stage 8, verify sequence quality and uncertain calls, standardize phenotype/annotation provenance, and seek independent lineage/geographic validation. This is research only.
