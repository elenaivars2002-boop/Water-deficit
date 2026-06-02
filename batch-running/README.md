# Batch notebooks (~3750 catchments)

**Start here:** [`batch_baseline_thresholds.ipynb`](batch_baseline_thresholds.ipynb) — same seven steps as the study pipeline, with per-basin outputs and `SKIP_EXISTING`.

| Notebook | Role |
|----------|------|
| `batch_baseline_thresholds.ipynb` | Full resumable batch pipeline (Steps 1–7) |
| `prepare_batch_forcing.ipynb` | Per-basin historical forcing (1976–2005) |
| `calibrate_batch_dpwm.ipynb` | Per-basin PSO calibration |
| `extract_estreams_meteorology_from_zip.ipynb` | One-off meteo extraction from zip archives |

Equivalent six-basin workflow: [`../single_basin_running/pipeline_study_basins.ipynb`](../single_basin_running/pipeline_study_basins.ipynb).

CLI mirrors the notebook steps, e.g.:

```text
python prepare_batch_forcing.py --skip_existing --workers 8
python calibrate_batch_dpwm.py --skip_existing --workers 8
python run_batch_baseline_dpwm.py --min_kge_invq 0.5 --skip_existing --workers 8
python compute_batch_thresholds.py --min_kge_invq 0.5 --skip_existing --workers 8
```
