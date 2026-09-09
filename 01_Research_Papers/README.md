# Research Papers

This folder contains reviewed research papers relevant to our topic.  
Each file includes:
- Notes and summaries of selected papers
- Key findings from each study
- Links to open-access sources (if available)

Purpose: To collect and organize the academic references that support our research proposal.

### Paper 1: Quantifying the performance of cluster based anomaly detection in smart grid control.
* **Author(s):** Sreejith et al.
* **Year:** 2024
* **Objective/Problem:** Detect zero-day cyberattacks in power systems and quantify anomaly detection performance. 
* **Method / Approach:** Cluster-based Hypothesis Test (CHT).
* **Functionality / Process:** Projects normal data into a signal space, forms a normal-data cluster, calculates the distance of new data from the cluster, and flags anomalies above a threshold. 
* **Dataset / Tools:** Load Frequency Control (LFC) data; 39-bus, 3-area test system; New England ISO load forecast data. 
* **Main Findings:** Accurately detected anomalies with low false-positive rates; detection speed was around 90 ms. 
* **Limitation:** Evaluation is based on a simulated 39-bus power-system model and attack data. 
* **Relevance / Research Gap:** Improve the explainability of anomaly-
detection models using power-system knowledge. 
* **DOI / Link:** https://doi.org/10.1109/PESGM51994.2024.10688731

 ### Paper 2:  Multivariate time series anomaly detection in cyber-physical systems using sparse attention
* **Author(s):** Li et al.
* **Year:** 2026
* **Objective/Problem:** Detect cybersecurity threats in power systems and provide early warnings before attacks occur. 
* **Method / Approach:** Multi-modal Large Language Model (MM-LLM) with cross-modal attention.
* **Functionality / Process:** Combines SCADA logs, PMU data, network traffic, and grid topology to identify threats across different data sources. 
* **Dataset / Tools:** SWaT, MSU Power System, and Tennessee Eastman Process (TEP) datasets; 2,028,029 combined samples. 
* **Main Findings:** Achieved 95.4% accuracy, a 95.2% F1-score, 2.7% FPR, and 13.2 ms latency, with up to 4.5 minutes early warning. 
* **Limitation:** Requires greater computational resources and uses multiple heterogeneous datasets that require preprocessing and alignment. 
* **Relevance / Research Gap:** Improve multi-modal cybersecurity detection while reducing computational requirements for practical deployment. 
* **DOI / Link:** https://doi.org/10.13052/jcsm2245-1439.1463

 ### Paper 3: Graph-based anomaly detection in industrial control systems
* **Author(s):** Balaba et al.
* **Year:** 2025
* **Objective/Problem:** Detect cyberattacks or anomalies in ICS network traffic.
* **Method / Approach:** Unsupervised heterogeneous GNN autoencoder.
* **Functionality / Process:** Converts network traffic into host-connection graphs and detects anomalies using reconstruction error. 
* **Dataset / Tools:** CIC Modbus Dataset 2023. Network captures and attack logs from a simulated substation. 
* **Main Findings:** Achieved an F1-score of 0.98 and performed better than some traditional ML methods. 
* **Limitation:** Saliency maps may be difficult to understand. Graph generation depends on specific protocols. 
* **Relevance / Research Gap:** Improve the explanations and make graph generation work with more industrial protocols. 
* **DOI / Link:** https://doi.org/10.1109/USBEREIT65494.2025.11054098

 ### Paper 4:  A real-time data capture probe for anomaly detection in industrial cyber-physical systems
* **Author(s):** Salazar Buttiglione et al.
* **Year:** 2025
* **Objective/Problem:** Develop a real-time data capture probe for anomaly detection in ICPSs.
* **Method / Approach:** Real-time data capture probe with LSTM-based anomaly detection.
* **Functionality / Process:** Captures Modbus traffic, extracts physical data, and sends it to LSTM models to detect anomalies. 
* **Dataset / Tools:** Water Distribution Testbed (WDT) dataset.
* **Main Findings:** Wait times remained below 100 ms, and CPU usage stayed below 10%, showing real-time processing capability.
* **Limitation:** Tested in a controlled laboratory water-distribution testbed; currently focuses on physical anomalies. 
* **Relevance / Research Gap:** Add cyberattack detection to complement the current physical anomaly detection.
* **DOI / Link:** https://doi.org/10.1109/CSR64739.2025.11129988

 ### Paper 5:  MFAD: A Multimodal Feature Fusion-Enhanced Time Series Anomaly Detection Framework in Industrial Cyber-Physical Systems
* **Author(s):** Narsing and Srinivasan
* **Year:** 2025
* **Objective/Problem:** Detect known and zero-day attacks in SCADA and IoT networks using AI-based anomaly detection.
* **Method / Approach:** AI-based anomaly detection framework with edge and centralised AI models.
* **Functionality / Process:** Collects network/system data, preprocesses and normalises it, detects abnormal behaviour in real time, and triggers intrusion response. 
* **Dataset / Tools:** Real industrial datasets and synthetic adversarial cases from a cyber-physical testbed.
* **Main Findings:** The proposed AI model achieved 94.5% overall accuracy, 97.6% for known threats, and 91.3% for unknown threats.
* **Limitation:** AI model has higher CPU, memory, and power usage due to computational requirements 
* **Relevance / Research Gap:** Future work could use federated learning, digital twins, and quantum-resistant cryptography and improve interoperability across different SCADA/IIoT platforms.
* **DOI / Link:** https://doi.org/10.1109/ICFT66708.2025.11336547

   ### Paper 6: Informed deep learning for anomaly detection in cyber-physical systems
* **Author(s):** Cobilean et al.
* **Year:** 2023
* **Objective/Problem:** Address limited anomalous data and lack of explainability in deep learning-based anomaly detection for CPS.
* **Method / Approach:** Informed deep learning by integrating prior knowledge into the dataset,model architecture or loss function.
* **Functionality / Process:** Uses physical equations, simulations, and system relationships to improve training, constrain model outputs and detect abnormal CPS behaviour
* **Dataset / Tools:** Various CPS data sources, simulations, testbeds and examples from wind farms, smart grids,industrial CPS and water distribution systems.
* **Main Findings:** Informed deep learning can improve anomaly detection when data is limited while increasing model explainability and trust.
* **Limitation:** Requires accurate prior knowledge and multidisciplinary expertise. Incorrect constraints can cause underfitting, overfitting or difficult optimisation.
* **Relevance / Research Gap:** Need to determine suitable prior knowledge and constraints for different CPS environments while maintaining effective detection with limited data.
* **DOI / Link:** https://doi.org/10.1109/ICIT58465.2023.10143126

   ### Paper 7:  Hybrid statistical-machine learning for real-time anomaly detection in industrial cyber-physical systems.
* **Author(s):** Hao et al.
* **Year:** 2023
* **Objective/Problem:** Detect cyberattacks, malicious behaviours and network anomalies in ICS-CPs in real time with low computational complexity.
* **Method / Approach:** Hybrid SARIMA + LSTM anomaly detection with dynamic thresholds.
* **Functionality / Process:** SARIMA predicts short term traffic and creates dynamic thresholds. LSTM models long-term background traffic and supplements the thresholds. Grubbs test identifies anomalies and calculates anomaly duration/degree.
* **Dataset / Tools:** Real-time ICS-CPS testbed data collected for more than 72 hours at 1ms sampling rate, covering power generation,natural gas pipeline and urban railway
* **Main Findings:** Achieved 95% overall detection accuracy, 98.4% PPV and 95.4% NPV. The hybrid model reduced false alarms and had an average processing time of ≤ 0.11 s. 
* **Limitation:** Tested mainly on a scaled-down ICS-CPS testbed; transferability to different real industrial environments still requires further validation. 
* **Relevance / Research Gap:** Further test the model on more diverse real-world industrial systems, improve transferability, and compare it with more state-of-the-art anomaly detection methods.
* **DOI / Link:** https://doi.org/10.1109/TASE.2021.3073396


  ### Paper 8:  Anomaly detection in cyber-physical systems based on genetic algorithm with dynamic thresholding detection.
* **Author(s):** Vaughn et al.
* **Year:** 2024
* **Objective/Problem:** Improve anomaly detection in CPS by reducing false positives and identifying the most relevant features for different cyberattacks. 
* **Method / Approach:** Genetic Algorithm (GA)-based feature selection with dynamic thresholding, combined with Random Forest (RF), Gaussian Naive Bayes (GNB), and K-Nearest Neighbors (KNN). SMOTE was also used to handle class imbalance.
* **Functionality / Process:** Dataset is cleaned and merged according to time → ML models are evaluated → GA selects important features using a fitness function → dynamic threshold updates feature importance → selected features are used for anomaly detection. 
* **Dataset / Tools:** Hardware-in-the-Loop Water Distribution Testbed (WDT) Dataset, containing network and physical data for normal conditions and four attack types. 
* **Main Findings:** GA feature selection improved the performance of the ML models. RF achieved 95.2% accuracy after GA feature selection. With SMOTE, RF achieved 99.8% for MITM and 100% for DOS attack detection. GA was most promising when combined with RF
* **Limitation:** Lack of real CPS attack data; WDT/testbed may not fully represent the complexity of real CPS. GA also has interpretability, computational resource, and compatibility issues for real-world deployment.
* **Relevance / Research Gap:** Future work should develop a more sophisticated fitness function, explore hybrid deep-learning models, and test additional CPS datasets to determine whether the findings generalize beyond water distribution systems. 
* **DOI / Link:** https://doi.org/10.1109/icABCD62167.2024.10645284

   ### Paper 9: Improving SCADA cybersecurity: A deep learning technique for anomaly detection
* **Author(s):** Madhu G.C et al.
* **Year:** 2025
* **Objective/Problem:** Improve SCADA security by detecting and blocking cyberattacks. 
* **Method / Approach:** MLP + XGBoost ensemble with SMOTE. 
* **Functionality / Process:** Collect traffic → preprocess data → detect abnormal traffic → block threats using firewall rules. 
* **Dataset / Tools:** Simulated SCADA network; 63,900 data points + 28,000 unseen data. 
* **Main Findings:** IAchieved 100% testing accuracy and 99.3% accuracy on unseen data. 
* **Limitation:** Uses simulated data; needs more real-world testing. 
* **Relevance / Research Gap:** Test with real SCADA data and different environments. 
* **DOI / Link:** https://doi.org/10.1109/MPSecICETA64837.2025.11118388

 ### Paper 10:  Anomaly detection in cyber-physical systems using long-short term memory autoencoders: A case study with Man-in-the-Middle (MiTM) attack
* **Author(s):** Sun et al.
* **Year:** 2025
* **Objective/Problem:** Detect MiTM attacks and anomalies in power system CPS. 
* **Method / Approach:** LSTM Autoencoder with feature selection and data normalization. 
* **Functionality / Process:** Preprocess data → train LSTM autoencoder → reconstruct normal data → calculate MSE → detect anomalies above the threshold. 
* **Dataset / Tools:** RESLab testbed; multi-sensor cyber and physical data from a 2000-bus power grid. 
* **Main Findings:** The model detected MiTM attacks effectively. Highest F1-score reached 0.983 in UC1. 
* **Limitation:** Performance changed with polling rate and number of outstations. Some false positives and false negatives occurred. 
* **Relevance / Research Gap:** Future work should improve real-time detection and add attack localization. 
* **DOI / Link:** https://doi.org/10.1109/TPEC63981.2025.10906975

 ### Paper 11:  Securing cyber-physical systems with two-level anomaly detection strategy
* **Author(s):** Zeeshan Ahmad & Andrei Petrovski 
* **Year:** 2024
* **Objective/Problem:** Improve CPS security by detecting both cyber and physical anomalies
* **Method / Approach:** Two-level CNN-LSTM and Gradient Boosting Machine (GBM). 
* **Functionality / Process:** Level 1 detects normal or abnormal data → Level 2 identifies the exact anomaly type.  
* **Dataset / Tools:** Water Distribution Testbed (WDT) dataset with network and physical data. 
* **Main Findings:** Achieved 100% F1-score on network data and 97.35% on physical data. 
* **Limitation:** Uses testbed data; real-time performance has not been tested. 
* **Relevance / Research Gap:** Test the method in real-time CPS and explore unsupervised ML/DL methods. 
* **DOI / Link:** https://doi.org/10.1109/ICPS59941.2024.10639983

 ### Paper 12: Multivariate time series anomaly detection in cyber-physical systems using sparse attention. 
* **Author(s):** Yuhao Li et al.
* **Year:** 2025
* **Objective/Problem:** Detect anomalies in CPS time series data efficiently. 
* **Method / Approach:** Sparse Attention Transformer with 1D-CNN and POT. 
* **Functionality / Process:** Embed time series → detect temporal patterns → calculate anomaly score → use dynamic threshold to identify anomalies.  
* **Dataset / Tools:** SWaT, MSL, SMAP and SMD datasets. 
* **Main Findings:** Achieved an average F1-score of 94.28% and improved F1 by up to 29.52% over some baseline methods. 
* **Limitation:** Tested mainly on benchmark datasets; real-time CPS performance needs further testing. 
* **Relevance / Research Gap:** Test the model in more CPS environments and improve thresholding for real time detection. 
* **DOI / Link:** https://doi.org/10.1109/IECON58223.2025.11221241

   ### Paper 13:   An explainable GAN framework for secure anomaly detection in cyber-physical systems
* **Author(s):** Nishant Kumar et al.
* **Year:** 2025
* **Objective/Problem:** Detect CPS anomalies while providing clear explanations for security operators.
* **Method / Approach:** XAI-GAN using GAN, SHAP, Grad-CAM and attention.
* **Functionality / Process:** Preprocess data → generate normal data → classify anomalies → generate explanations → issue alerts. 
* **Dataset / Tools:** SWaT, N-BaIoT and ICS datasets. 
* **Main Findings:** Achieved 93.8% accuracy, 91.2% F1-score and 0.943 AUC-ROC, with low detection latency. 
* **Limitation:** Tested mainly on benchmark datasets; further validation across different CPS environments is needed. 
* **Relevance / Research Gap:** Improve portability, real-time performance and explainability for different CPS environments. 
* **DOI / Link:** https://doi.org/10.1109/ICCCA66364.2025.11325514

   ### Paper 14:  Causal graph profiling via structural divergence for robust anomaly detection in cyber-physical systems
* **Author(s):** Arun Vignesh Malarkkan et al.
* **Year:** 2025
* **Objective/Problem:** Detect cyberattacks in CPS despite class imbalance, noise and changing data patterns. 
* **Method / Approach:** CGDAD using causal graphs and structural divergence. 
* **Functionality / Process:** Learn normal/attack causal graphs → create graph for test segment → compare graphs → classify anomaly.  
* **Dataset / Tools:** SWaT, WADI, Tennessee Eastman (TE), SMD 
* **Main Findings:** CGDAD-DYNOTEARS achieved the best overall results across the four datasets and improved detection of complex and delayed attacks. 
* **Limitation:** Performance depends on good causal graph learning, suitable time-lag selection and quality data. Scaling to large sensor networks can also be costly.
* **Relevance / Research Gap:** Need continuous causal learning, better scalability and domain adaptation for different industrial CPS environments. 
* **DOI / Link:** https://doi.org/10.1109/BigData66926.2025.11401886

  
   ### Paper 15:  Semi-supervised denoising-aware contrastive learning for time series anomaly detection in cyber-physical systems.
* **Author(s):** Jiyu Tian et al.
* **Year:** 2025
* **Objective/Problem:** Detect anomalies in CPS time-series data despite limited labels, complex sensor-actuator interactions and noise. 
* **Method / Approach:** SSDCL – Semi-Supervised Denoising-Aware Contrastive Learning using SCAug and DEHCL. 
* **Functionality / Process:** Unlabeled data → SCAug creates semantically consistent positive pairs → denoising using Bayesian/Unscented Kalman filtering → DEHCL learns robust spatio-temporal representations → use only 5% labeled anomaly data to fine-tune classifier → classify normal/abnorma
* **Dataset / Tools:** PUMP, SWaT, WADI 
* **Main Findings:** Achieved 97.5% F1 (PUMP), 93.0% (SWaT), 74.4% (WADI) and outperformed the compared SOTA ADCPS methods. It was especially effective for datasets with complex interactions such as WADI. 
* **Limitation:** Limited anomaly labels are not fully utilized during self-supervised training. Sensor-actuator transmission delays/clock synchronization can affect cosine similarity in SCAug. The datasets may also not fully represent real-world CPS complexity. 
* **Relevance / Research Gap:** Future work should better utilize limited labeled anomaly knowledge, handle sensor-actuator transmission delays, and validate the method on more realistic real-world CPS environments. 
* **DOI / Link:** https://doi.org/10.1109/TIFS.2025.3588674
