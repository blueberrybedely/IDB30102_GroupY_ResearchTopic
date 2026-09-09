# Summary of Methods, Datasets, and Evaluation Metrics

### 1. Identified Methods & Algorithms
* **Extended Isolation Forest (EIF):** Core baseline for low-latency, slope-partitioned anomaly detection.
* **Rolling Window Preprocessing:** Extraction of spatio-temporal features ($\text{Mean}_{5s}$, $\text{Std}_{5s}$, $\Delta S/\Delta t$).
* **Automated Rule-Based Mitigation:** Safe-state actuation triggers initiated when anomaly scores exceed dynamic threshold $\tau$.

### 2. Benchmark Datasets
* **SWaT (Secure Water Treatment):** 11 days of continuous operational data (7 days normal, 4 days under 36 physical/cyber attack scenarios).
* **HAI (Hardware-In-the-Loop Augmented ICS Security Dataset):** Multi-stage boiler and turbine control telemetry.
* **CIC Modbus 2023:** Network-level packet captures containing Modbus TCP injection and MITM attack vectors.

### 3. Standard Evaluation Metrics
To ensure consistency with literature standards, the proposed methodology uses:

$$\text{Precision} = \frac{TP}{TP + FP}$$

$$\text{Recall} = \frac{TP}{TP + FN}$$

$$F_1\text{-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

$$\text{Inference Latency} = t_{\text{output}} - t_{\text{input}} \quad (\text{Target: } <30\text{ ms})$$

---

### 4. Key Methodological References Supporting Proposed Chapter 3
1. **Agure & Nggada (2025):** Validates the use of EIF for multi-sensor industrial process anomaly scoring.
2. **Shrivasta & Mathur (2026):** Establishes the architectural pattern for linking ML threat scores to automated mitigation routines.
3. **Peng et al. (2026):** Defines real-time performance thresholds ($<30\text{ ms}$) for edge-deployed SCADA monitoring.
