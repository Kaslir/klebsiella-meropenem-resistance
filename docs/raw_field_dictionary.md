# Raw source field dictionary

All fields in the retrieved snapshots are listed. Only the documented analysis variables are used. Optional fields can be absent. For unused provider internal fields, no biological interpretation is asserted.

| Collection | Field | Description |
|---|---|---|
| AST | `_version_` | Provider internal bookkeeping/display field. Preserved for provenance; its detailed semantics are not relied on or interpreted in this study. |
| AST | `antibiotic` | Drug tested; meropenem throughout this AST subset. |
| AST | `bioproject_acc` | Originating NCBI BioProject accession. |
| AST | `biosample_acc` | BioSample accession identifying the biological sample; primary join key. |
| AST | `collection_date` | Submitter-supplied collection date; may be partial or absent. |
| AST | `creation_date` | Record creation timestamp in the provider system. |
| AST | `disk_diffusion` | Laboratory inhibition-zone diameter in millimetres; not an MIC. |
| AST | `epi_type` | Provider clinical/environmental classification. |
| AST | `geo_loc_name` | Geographic origin string, possibly including subnational detail. |
| AST | `host` | Host organism, where supplied; not a predictor. |
| AST | `id` | Provider row identifier; AST and isolate collections have different row identities. |
| AST | `isolation_source` | Material or site from which the isolate was obtained. |
| AST | `measurement_sign` | Comparison operator attached to MIC or disk measurement; preserve inequalities. |
| AST | `mic` | Minimum inhibitory concentration in mg/L; read with measurement_sign. |
| AST | `phenotype` | Submitted laboratory susceptibility category, not a gene-derived prediction. |
| AST | `platform` | Laboratory susceptibility-test platform. |
| AST | `reagent` | Laboratory method version or reagent information. |
| AST | `scientific_name` | Submitted organism name. |
| AST | `standard` | Submitted testing standard (CLSI/EUCAST); does not specify a verified edition here. |
| AST | `target_acc` | Pathogen Detection target accession, including version. |
| AST | `target_creation_date` | Date the target entered the Pathogen Detection system. |
| AST | `taxgroup_name` | Pathogen Detection organism group name. |
| AST | `vendor` | Manufacturer of the susceptibility testing equipment/reagent. |
| isolate | `AMR_genotypes` | AMRFinderPlus resistance calls including gene symbols and call statuses. |
| isolate | `AMR_genotypes_core` | Subset of resistance calls in the core AMRFinderPlus scope. |
| isolate | `AST_phenotypes` | Other submitted antibiotic phenotypes; excluded from predictors to prevent leakage. |
| isolate | `IFSAC_category` | Food-source categorization supplied by the provider; unused. |
| isolate | `LibraryLayout` | Sequencing library layout, e.g. paired-end. |
| isolate | `Platform` | Sequencing platform; distinct from lowercase AST platform. |
| isolate | `Run` | Sequence Read Archive run accession(s). |
| isolate | `_version_` | Provider internal bookkeeping/display field. Preserved for provenance; its detailed semantics are not relied on or interpreted in this study. |
| isolate | `amrfinderplus_analysis_type` | Annotation mode, including nucleotide-only or combined evidence. |
| isolate | `amrfinderplus_applied` | Provider indicator that AMRFinderPlus was applied. |
| isolate | `amrfinderplus_version` | AMRFinderPlus software version. |
| isolate | `asm_acc` | Genome assembly accession. |
| isolate | `asm_display_name` | Provider assembly display label. |
| isolate | `asm_level` | Assembly-level designation, e.g. contig. |
| isolate | `asm_stats_contig_n50` | Provider contig N50 length in base pairs. |
| isolate | `asm_stats_length_bp` | Provider total assembly length in base pairs. |
| isolate | `asm_stats_n_contig` | Provider number of assembly contigs. |
| isolate | `assembly_method` | Assembler name/version as supplied. |
| isolate | `assembly_uid` | NCBI Assembly numeric record identifier. |
| isolate | `attribute_package` | BioSample submission package name. |
| isolate | `bioproject_acc` | Originating NCBI BioProject accession. |
| isolate | `bioproject_center` | Submitting BioProject organization. |
| isolate | `biosample_acc` | BioSample accession identifying the biological sample; primary join key. |
| isolate | `cluster_size` | Provider cluster membership count; not necessarily the size in this subset. |
| isolate | `clustered` | Provider clustering indicator. |
| isolate | `collected_by` | Submitter-supplied collecting organization. |
| isolate | `collection_date` | Submitter-supplied collection date; may be partial or absent. |
| isolate | `complete_fl` | Provider internal bookkeeping/display field. Preserved for provenance; its detailed semantics are not relied on or interpreted in this study. |
| isolate | `creation_date` | Record creation timestamp in the provider system. |
| isolate | `epi_type` | Provider clinical/environmental classification. |
| isolate | `erd_group` | Provider relatedness/cluster identifier; fallback group key. |
| isolate | `erd_group_acc` | Unversioned relatedness/cluster accession. |
| isolate | `food_origin` | Food-origin metadata, where supplied; unused. |
| isolate | `fullasm_id` | Provider internal bookkeeping/display field. Preserved for provenance; its detailed semantics are not relied on or interpreted in this study. |
| isolate | `geo_loc_name` | Geographic origin string, possibly including subnational detail. |
| isolate | `host` | Host organism, where supplied; not a predictor. |
| isolate | `host_disease` | Submitter host-disease metadata; unused. |
| isolate | `id` | Provider row identifier; AST and isolate collections have different row identities. |
| isolate | `isolate_identifiers` | List of isolate aliases; not assumed to be patient identifiers. |
| isolate | `isolate_name_alias` | Alternative isolate name. |
| isolate | `isolation_source` | Material or site from which the isolate was obtained. |
| isolate | `kmer_group` | Versioned organism analysis group; not used as an isolate relatedness cluster. |
| isolate | `kmer_group_acc` | Unversioned organism analysis group accession. |
| isolate | `lat_lon` | Submitted latitude/longitude; unused. |
| isolate | `major_contributor` | Provider internal bookkeeping/display field. Preserved for provenance; its detailed semantics are not relied on or interpreted in this study. |
| isolate | `mindiff` | Provider internal bookkeeping/display field. Preserved for provenance; its detailed semantics are not relied on or interpreted in this study. |
| isolate | `minsame` | Provider internal bookkeeping/display field. Preserved for provenance; its detailed semantics are not relied on or interpreted in this study. |
| isolate | `new` | Provider internal bookkeeping/display field. Preserved for provenance; its detailed semantics are not relied on or interpreted in this study. |
| isolate | `number_amr_genes` | Provider count of resistance gene calls; excluded from predictors. |
| isolate | `number_core_amr_genes` | Provider count of core-scope resistance calls. |
| isolate | `number_drugs_intermediate` | Count of intermediate drug phenotypes; excluded from predictors. |
| isolate | `number_drugs_resistant` | Count of resistant drug phenotypes; excluded from predictors. |
| isolate | `number_drugs_susceptible` | Count of susceptible drug phenotypes; excluded from predictors. |
| isolate | `number_drugs_tested` | Count of drugs tested; excluded from predictors. |
| isolate | `number_stress_genes` | Provider count of stress-response calls. |
| isolate | `number_virulence_genes` | Provider count of virulence calls. |
| isolate | `ontological_term` | Provider source ontology term; unused. |
| isolate | `parent_group` | Versioned PDS relatedness cluster; used after removing version suffix. |
| isolate | `property` | List of provider flags indicating available data categories. |
| isolate | `refgene_db_version` | AMRFinderPlus reference gene database version. |
| isolate | `sample_name` | Submitter sample label. |
| isolate | `scientific_name` | Submitted organism name. |
| isolate | `sort_order` | Provider internal bookkeeping/display field. Preserved for provenance; its detailed semantics are not relied on or interpreted in this study. |
| isolate | `source_type` | Provider source classification; unused. |
| isolate | `species_taxid` | NCBI species taxonomy identifier; required to equal 573. |
| isolate | `sra_center` | SRA submitting organization. |
| isolate | `sra_release_date` | SRA release timestamp. |
| isolate | `strain` | Submitter strain label. |
| isolate | `stress_genotypes` | Detected stress-response gene calls; unused. |
| isolate | `target_acc` | Pathogen Detection target accession, including version. |
| isolate | `target_creation_date` | Date the target entered the Pathogen Detection system. |
| isolate | `taxgroup_name` | Pathogen Detection organism group name. |
| isolate | `taxgroup_name_short` | Short organism-group name. |
| isolate | `taxid` | Submitted taxonomic identifier; may differ from species_taxid. |
| isolate | `tree_node_ids` | Provider phylogenetic tree node identifiers; unused. |
| isolate | `updatedate` | Provider last-update timestamp. |
| isolate | `virulence_genotypes` | Detected virulence-gene calls; unused. |
| isolate | `wgs_acc_prefix` | Whole-genome shotgun accession prefix. |
| isolate | `wgs_master_acc` | Whole-genome shotgun master accession. |

Sources: [AST documentation](https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/) and [Isolates Browser help](https://www.ncbi.nlm.nih.gov/pathogens/pathogens_help/).
