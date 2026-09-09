# Comparison of Existing Anomaly Detection Techniques

| Technique / Model | Operational Domain | Primary Advantage | Key Limitation | Suitability for Real-Time Edge SCADA |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Isolation Forest** | Unsupervised (Network/Process) | $O(n \log n)$ training complexity; fast inference (~21 ms) | High false positive rate due to axis-parallel cutting hyperplanes | **High** (Low compute, but needs geometric extension) |
| **Extended Isolation Forest (EIF)** | Unsupervised (Spatio-Temporal) | Cuts along arbitrary slopes; captures inter-sensor correlations | Slight increase in tree-building complexity over standard iForest | **Very High** (Optimal balance of speed and multi-sensor accuracy) |
| **LSTM / BiGRU Autoencoders** | Deep Learning (Time-Series) | High accuracy on complex non-linear sequence dependencies | High inference latency ($>100\text{ ms}$); memory intensive for PLCs | **Low–Medium** (Requires dedicated GPU/edge accelerator) |
| **One-Class SVM (OC-SVM)** | Kernel-based Boundary | Robust against minor noise outliers | $O(n^2)$ scaling complexity; fails on large-scale streaming data | **Low** (Does not scale to high-frequency telemetry) |
| **Hybrid MM-LLM / GNN** | Multi-Modal Deep Learning | Exceptional detection rate ($>98\%$) and context awareness | High computational overhead; black-box decision process | **Unsuitable** (Cannot run on embedded SCADA/RTU hardware) |
