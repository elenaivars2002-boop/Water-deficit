# Single-basin / study-catchment notebooks

**Start here:** [`pipeline_study_basins.ipynb`](pipeline_study_basins.ipynb) — full Steps 1–7 for the six thesis basins (CH000127, DESN1585, FR002785, GB000215, SE000197, ES000700).

| Notebook | Role |
|----------|------|
| `pipeline_study_basins.ipynb` | End-to-end baseline + future pipeline |
| `prepare_eastream_inputs.ipynb` | Historical rainplusmelt + PET |
| `calibrate_validate_dpwm.ipynb` | PSO calibration |
| `run_dpwm.ipynb` | Baseline simulation |
| `compute_seasonal_thresholds.ipynb` | Q20/Q50/Q80/Q90 thresholds |
| `bias_correction.ipynb` | EURO-CORDEX bias correction |
| `run_future_dpwm.ipynb` | Future forcing + simulation |
| `compute_q80_deficits.ipynb` | Future vs baseline Q80 deficits |
| `plot_future_hydrograph.ipynb` | Future hydrograph figures |
| `run_hydro_plots.ipynb` | Baseline hydrographs |
| `compare_extraction_methods.ipynb` | Areal vs nearest CORDEX extraction |
| `run_future_pipeline_6basins.ipynb` | Shortcut future pipeline |
| `sweep_objective_settings.ipynb` | Calibration objective experiments |

For thousands of basins, use [`../batch_running/`](../batch_running/).
