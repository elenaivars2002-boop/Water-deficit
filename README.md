# Notebooks

| Folder | Use when |
|--------|----------|
| [`single_basin_running/`](single_basin_running/) | Six study catchments (or a few basins): full pipeline, plots, calibration experiments |
| [`batch_running/`](batch_running/) | ~3750 basins from `basins_selection.csv`: forcing, calibration, thresholds, future deficits |

**Main entry points**

- Single: `single_basin_running/pipeline_study_basins.ipynb`
- Batch: `batch_running/batch_baseline_thresholds.ipynb`

All notebooks use `notebooks/project_root.py` (or the same parent-walk logic) to find the repo root (`data/csv_estream/`).
