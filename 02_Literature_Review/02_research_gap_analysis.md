# Synthesized Research Gap Analysis

Based on the critical review of 40 recent studies (2022–2026), four interconnected research gaps were identified:

### 1. The Geometry-Spatio-Temporal Gap in Unsupervised Tree Models
Standard Isolation Forest partitions feature spaces along axis-aligned hyperplanes ($x_i \le c$). In SCADA networks—where physical process laws tie sensor values together (e.g., $P \propto T$)—stealthy Man-in-the-Middle (MITM) attacks alter combinations of values while keeping individual variables within valid range bounds. Existing tree models fail to detect these diagonal payload anomalies without dynamic slope partitioning.

### 2. High False Alarm Rates from Non-Malicious Process Transitions
Traditional threshold-based and baseline ML anomaly detectors do not incorporate temporal rate-of-change ($\Delta S / \Delta t$) or rolling statistical windows. Consequently, routine industrial state shifts (e.g., valve actuation, pump spin-up) are frequently misclassified as cyberattacks, inducing operator alert fatigue.

### 3. The Detection-Response Decoupling Gap
Over 85% of reviewed literature focuses exclusively on **passive threat detection** (outputting an anomaly score or binary flag). In critical infrastructure, detection without immediate automated response allows physical process degradation before an operator intervenes. There is a lack of integrated frameworks combining lightweight detection algorithms with automated safe-state fallback triggers.

### 4. Edge Resource Constraints vs. Operational Real-Time Latency
Deep learning architectures (GNNs, Transformers, Autoencoders) report high F1-scores but exhibit inference latencies ranging from 80 ms to over 500 ms, exceeding the real-time response window for SCADA control loops ($<30\text{ ms}$).

---

### **Formulated Research Gap Statement**
> *"Current unsupervised SCADA anomaly detection models either suffer from high false-alarm rates due to axis-aligned feature partitioning, or rely on heavy deep-learning models that exceed the real-time latency budget of edge-deployed PLCs. Furthermore, existing frameworks remain decoupled from automated mitigation mechanisms required to ensure active physical resilience during active payload injection attacks."*
