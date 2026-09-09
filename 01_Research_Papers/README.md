# Research Papers

This folder contains reviewed research papers relevant to our topic.  
Each file includes:
- Notes and summaries of selected papers
- Key findings from each study
- Links to open-access sources (if available)

Purpose: To collect and organize the academic references that support our research proposal.

### Paper 1: Real-time dynamic security monitoring for SCADA networks using machine learning
* **Full Title:** Real-time dynamic security monitoring for SCADA networks using machine learning
* **Author(s):** Hao, W., Yao, P., Yang, T., & Yang, Q.
* **Year:** 2022
* **Research Problem:** High false-alarm rates and slow response times in detecting non-stationary cyber-physical attack payloads across Industrial Control System (ICS) networks.
* **Method / Technique:** Distributed ARIMA feature modeling combined with NSGA-III multi-objective defense resource optimization.
* **Dataset / Tools:** Electrical Cyber-Physical System (ECPS) testbed network capture, Python, Wireshark.
* **Main Findings:** Achieved lower latency ($<100\text{ ms}$) and dynamic Pareto optimization of security resources across 4,000+ asset candidate strategies.
* **Limitation:** Restricted primarily to physical network packet analysis without deep application payload inspection (e.g., Modbus function codes).
* **Relevance to Proposed Research:** Proves the necessity of low-latency anomaly scoring for streaming SCADA telemetry; informs the temporal feature construction in our preprocessing pipeline.
* **DOI / Link:** https://doi.org/10.1016/j.ijepes.2022.108201
