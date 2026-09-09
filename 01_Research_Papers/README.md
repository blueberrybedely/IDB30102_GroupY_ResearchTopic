# Research Papers

This folder contains reviewed research papers relevant to our topic.  
Each file includes:
- Notes and summaries of selected papers
- Key findings from each study
- Links to open-access sources (if available)

Purpose: To collect and organize the academic references that support our research proposal.

### Paper 1:
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
* **DOI / Link:**

 ### Paper 2:
* **Author(s):** Li et al.
* **Year:** 2026
* **Objective/Problem:** Detect cybersecurity threats in power systems and provide early warnings before attacks occur. 
* **Method / Approach:** Multi-modal Large Language Model (MM-LLM) with cross-modal attention.
* **Functionality / Process:** Combines SCADA logs, PMU data, network traffic, and grid topology to identify threats across different data sources. 
* **Dataset / Tools:** SWaT, MSU Power System, and Tennessee Eastman Process (TEP) datasets; 2,028,029 combined samples. 
* **Main Findings:** Achieved 95.4% accuracy, a 95.2% F1-score, 2.7% FPR, and 13.2 ms latency, with up to 4.5 minutes early warning. 
* **Limitation:** Requires greater computational resources and uses multiple heterogeneous datasets that require preprocessing and alignment. 
* **Relevance / Research Gap:** Improve multi-modal cybersecurity detection while reducing computational requirements for practical deployment. 
* **DOI / Link:**

 ### Paper 3:
* **Author(s):** Balaba et al.
* **Year:** 2025
* **Objective/Problem:** Detect cyberattacks or anomalies in ICS network traffic.
* **Method / Approach:** Unsupervised heterogeneous GNN autoencoder.
* **Functionality / Process:** Converts network traffic into host-connection graphs and detects anomalies using reconstruction error. 
* **Dataset / Tools:** CIC Modbus Dataset 2023. Network captures and attack logs from a simulated substation. 
* **Main Findings:** Achieved an F1-score of 0.98 and performed better than some traditional ML methods. 
* **Limitation:** Saliency maps may be difficult to understand. Graph generation depends on specific protocols. 
* **Relevance / Research Gap:** Improve the explanations and make graph generation work with more industrial protocols. 
* **DOI / Link:**

 ### Paper 4:
* **Author(s):** Salazar Buttiglione et al.
* **Year:** 2025
* **Objective/Problem:** Develop a real-time data capture probe for anomaly detection in ICPSs.
* **Method / Approach:** Real-time data capture probe with LSTM-based anomaly detection.
* **Functionality / Process:** Captures Modbus traffic, extracts physical data, and sends it to LSTM models to detect anomalies. 
* **Dataset / Tools:** Water Distribution Testbed (WDT) dataset.
* **Main Findings:** Wait times remained below 100 ms, and CPU usage stayed below 10%, showing real-time processing capability.
* **Limitation:** Tested in a controlled laboratory water-distribution testbed; currently focuses on physical anomalies. 
* **Relevance / Research Gap:** Add cyberattack detection to complement the current physical anomaly detection.
* **DOI / Link:**

 ### Paper 5:
* **Author(s):** Narsing and Srinivasan
* **Year:** 2025
* **Objective/Problem:** Detect known and zero-day attacks in SCADA and IoT networks using AI-based anomaly detection.
* **Method / Approach:** AI-based anomaly detection framework with edge and centralised AI models.
* **Functionality / Process:** Collects network/system data, preprocesses and normalises it, detects abnormal behaviour in real time, and triggers intrusion response. 
* **Dataset / Tools:** Real industrial datasets and synthetic adversarial cases from a cyber-physical testbed.
* **Main Findings:** The proposed AI model achieved 94.5% overall accuracy, 97.6% for known threats, and 91.3% for unknown threats.
* **Limitation:** AI model has higher CPU, memory, and power usage due to computational requirements 
* **Relevance / Research Gap:** Future work could use federated learning, digital twins, and quantum-resistant cryptography and improve interoperability across different SCADA/IIoT platforms.
* **DOI / Link:**

   ### Paper 6:
* **Author(s):** Cobilean et al.
* **Year:** 2023
* **Objective/Problem:** Address limited anomalous data and lack of explainability in deep learning-based anomaly detection for CPS.
* **Method / Approach:** Informed deep learning by integrating prior knowledge into the dataset,model architecture or loss function.
* **Functionality / Process:** Uses physical equations, simulations, and system relationships to improve training, constrain model outputs and detect abnormal CPS behaviour
* **Dataset / Tools:** Various CPS data sources, simulations, testbeds and examples from wind farms, smart grids,industrial CPS and water distribution systems.
* **Main Findings:** Informed deep learning can improve anomaly detection when data is limited while increasing model explainability and trust.
* **Limitation:** Requires accurate prior knowledge and multidisciplinary expertise. Incorrect constraints can cause underfitting, overfitting or difficult optimisation.
* **Relevance / Research Gap:** Need to determine suitable prior knowledge and constraints for different CPS environments while maintaining effective detection with limited data.
* **DOI / Link:**

   ### Paper 7:
* **Author(s):** Hao et al.
* **Year:** 2023
* **Objective/Problem:** Detect cyberattacks, malicious behaviours and network anomalies in ICS-CPs in real time with low computational complexity.
* **Method / Approach:** Hybrid SARIMA + LSTM anomaly detection with dynamic thresholds.
* **Functionality / Process:** SARIMA predicts short term traffic and creates dynamic thresholds. LSTM models long-term background traffic and supplements the thresholds. Grubbs test identifies anomalies and calculates anomaly duration/degree.
* **Dataset / Tools:** Real-time ICS-CPS testbed data collected for more than 72 hours at 1ms sampling rate, covering power generation,natural gas pipeline and urban railway
* **Main Findings:** Achieved 95% overall detection accuracy, 98.4% PPV and 95.4% NPV. The hybrid model reduced false alarms and had an average processing time of ≤ 0.11 s. 
* **Limitation:** Tested mainly on a scaled-down ICS-CPS testbed; transferability to different real industrial environments still requires further validation. 
* **Relevance / Research Gap:** Further test the model on more diverse real-world industrial systems, improve transferability, and compare it with more state-of-the-art anomaly detection methods.
* **DOI / Link:**


  ### Paper 8:
* **Author(s):** Vaughn et al.
* **Year:** 2024
* **Objective/Problem:** Improve anomaly detection in CPS by reducing false positives and identifying the most relevant features for different cyberattacks. 
* **Method / Approach:** Genetic Algorithm (GA)-based feature selection with dynamic thresholding, combined with Random Forest (RF), Gaussian Naive Bayes (GNB), and K-Nearest Neighbors (KNN). SMOTE was also used to handle class imbalance.
* **Functionality / Process:** Dataset is cleaned and merged according to time → ML models are evaluated → GA selects important features using a fitness function → dynamic threshold updates feature importance → selected features are used for anomaly detection. 
* **Dataset / Tools:** Hardware-in-the-Loop Water Distribution Testbed (WDT) Dataset, containing network and physical data for normal conditions and four attack types. 
* **Main Findings:** GA feature selection improved the performance of the ML models. RF achieved 95.2% accuracy after GA feature selection. With SMOTE, RF achieved 99.8% for MITM and 100% for DOS attack detection. GA was most promising when combined with RF
* **Limitation:** Lack of real CPS attack data; WDT/testbed may not fully represent the complexity of real CPS. GA also has interpretability, computational resource, and compatibility issues for real-world deployment.
* **Relevance / Research Gap:** Future work should develop a more sophisticated fitness function, explore hybrid deep-learning models, and test additional CPS datasets to determine whether the findings generalize beyond water distribution systems. 


* **DOI / Link:**

   ### Paper 9:
* **Author(s):** Cobilean et al.
* **Year:** 2023
* **Objective/Problem:** Address limited anomalous data and lack of explainability in deep learning-based anomaly detection for CPS.
* **Method / Approach:** Informed deep learning by integrating prior knowledge into the dataset,model architecture or loss function.
* **Functionality / Process:** Uses physical equations, simulations, and system relationships to improve training, constrain model outputs and detect abnormal CPS behaviour
* **Dataset / Tools:** Various CPS data sources, simulations, testbeds and examples from wind farms, smart grids,industrial CPS and water distribution systems.
* **Main Findings:** Informed deep learning can improve anomaly detection when data is limited while increasing model explainability and trust.
* **Limitation:** Requires accurate prior knowledge and multidisciplinary expertise. Incorrect constraints can cause underfitting, overfitting or difficult optimisation.
* **Relevance / Research Gap:** Need to determine suitable prior knowledge and constraints for different CPS environments while maintaining effective detection with limited data.
* **DOI / Link:**

 ### Paper 10:
* **Author(s):** Cobilean et al.
* **Year:** 2023
* **Objective/Problem:** Address limited anomalous data and lack of explainability in deep learning-based anomaly detection for CPS.
* **Method / Approach:** Informed deep learning by integrating prior knowledge into the dataset,model architecture or loss function.
* **Functionality / Process:** Uses physical equations, simulations, and system relationships to improve training, constrain model outputs and detect abnormal CPS behaviour
* **Dataset / Tools:** Various CPS data sources, simulations, testbeds and examples from wind farms, smart grids,industrial CPS and water distribution systems.
* **Main Findings:** Informed deep learning can improve anomaly detection when data is limited while increasing model explainability and trust.
* **Limitation:** Requires accurate prior knowledge and multidisciplinary expertise. Incorrect constraints can cause underfitting, overfitting or difficult optimisation.
* **Relevance / Research Gap:** Need to determine suitable prior knowledge and constraints for different CPS environments while maintaining effective detection with limited data.
* **DOI / Link:**
