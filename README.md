# 🛠️ Industrial AI Predictive Maintenance Dashboard

# 📌 Problem Statement
In industrial environments, unplanned equipment downtime is one of the most significant contributors to operational loss. Managing machinery health is often reactive, relying on scheduled checks rather than real-time data. Fragmented sensor readings (Temperature, Pressure, Vibration) make it difficult for engineers to see a clear picture of equipment degradation. Without a centralized AI-driven tool, it is nearly impossible to accurately forecast the Remaining Useful Life (RUL) of a machine or identify anomalies before a catastrophic failure occurs.

# 💡 The Solution: Proactive Intelligence
The Predictive Maintenance Dashboard is a high-performance Python application that transforms raw sensor data into actionable maintenance intelligence. By utilizing Random Forest and KMeans Clustering, the dashboard provides a 360-degree view of fleet health. It empowers stakeholders to move from "Fix-when-broken" to "Predict-and-Prevent," enhancing operational uptime, reducing maintenance costs, and ensuring safety through data-driven forecasting.

# 🛠️ Project Workflow (ML & ETL)
1. Strategic Planning: Structured project goals using the AIMS grid to align machine learning outputs with industrial KPIs.
2. Data Engineering (Pandas): Handled missing values using forward-filling (ffill) and standardized features with StandardScaler to ensure model stability.
   <img width="1353" height="720" alt="Screenshot (103)" src="https://github.com/user-attachments/assets/38398ad9-3275-4028-8476-d86cde8a2c44" />
   <img width="1350" height="732" alt="Screenshot (104)" src="https://github.com/user-attachments/assets/7c864675-137e-4e05-adcc-e514f5b665a3" />

3. Predictive Modeling (Regression): Trained a Random Forest Regressor to predict the exact number of operational hours remaining (RUL).
   <img width="1353" height="723" alt="Screenshot (105)" src="https://github.com/user-attachments/assets/9bf33bfa-784a-4542-b02e-685f9f64a27b" />

4. Risk Classification: Implemented a Random Forest Classifier to categorize machine status as "Normal" or "Needs Maintenance."
   <img width="1353" height="723" alt="Screenshot (106)" src="https://github.com/user-attachments/assets/95d4845c-795f-4efb-aa33-e836bf01478d" />

5. Anomaly Detection (Unsupervised): Used KMeans Clustering to automatically flag irregular sensor patterns that deviate from standard operating procedures.
   <img width="1353" height="723" alt="Screenshot (107)" src="https://github.com/user-attachments/assets/9fd5e6be-325b-4d80-b151-1ff5d6a5fce7" />

6. Interactive UI (Streamlit & Plotly): Architected a "Bento-style" dashboard using custom CSS and high-fidelity Plotly gauges for real-time monitoring.
    <img width="1366" height="688" alt="Screenshot (37)" src="https://github.com/user-attachments/assets/31e91a0d-aca6-4c7e-8764-11c314424480" />


# 📊 Key Dashboard Insights
1. Health Gauges: Interactive Plotly indicators that visualize Remaining Useful Life against critical safety thresholds (Red/Yellow/Green zones).
2. Live KPI Metrics: Real-time tracking of System Uptime, Failure Probability %, and Active Anomaly Counts.
3. Sensor Variance Heatmaps: Deep-dive visualizations showing the correlation between different sensor readings and operational hours.
4. Diagnostic Tool: An "On-Demand" feature allowing engineers to input manual sensor readings to get an instant AI-driven health forecast.

# 🚀 Future Roadmap
1. IoT Edge Integration: Transitioning from static CSV datasets to live MQTT/API streams for real-time sensor ingestion.
2. Advanced Neural Networks: Implementing LSTM (Long Short-Term Memory) networks for improved time-series forecasting.
3. Mobile Alert System: Integrating automated SMS or Email alerts when failure probability crosses a specific risk threshold.

# 🎓 Key Learnings
1. Full-Stack AI Development: Managed the entire lifecycle from raw data cleaning in Python to deploying a professional web-based UI.
2. Model Optimization: Gained deep experience in feature scaling and split-testing models to ensure 95%+ accuracy in maintenance classification.
3. Industrial UX Design: Learned how to create "Compelling" visuals using Bento Grid layouts and Dark Theme aesthetics for high-pressure environments.
4. Independent Execution: I architected and coded this entire solution independently. It required a deep dive into both data science and web styling, and the result is something I'm incredibly proud of! 😎🎂

# 📊 Technical Stack
- **Frontend:** [Streamlit](https://streamlit.io), Streamlit Option Menu, Lottie (JavaScript-based animations)
- **Machine Learning:** [Scikit-Learn](https://scikit-learn.org) (Random Forest, KMeans, StandardScaler)
- **Data Processing:** [Pandas](https://pandas.pydata.org), NumPy
- **Visualizations:** [Seaborn](https://seaborn.pydata.org), Matplotlib

# ⚙️ Installation & Setup
Follow these steps to run the dashboard locally:

1. **Clone the Repository:**
   ```bash
   
   git clone https://github.com
   
   cd Industrial-AI-Predictive-Maintenance-Dashboard
   
2. **Create & Activate Virtual Environment:**
   ```bash
   
   python -m venv venv
   
   .\venv\Scripts\activate

3. **Install Dependencies:**
   ```bash
   
   pip install -r requirements.txt
   
4. python -m streamlit run app.py

# Features

- Home: Welcome page providing an overview of the application.
- Historical Data: View historical data of machinery sensor readings and operational hours.
- Input Data: Submit input data for prediction, either manually or by generating random values.
- Results: Display predictions for remaining useful life (RUL), maintenance status, and anomaly detection based on the input data.
- Visualizations: Visualize historical sensor data and operational hours through histograms, scatter plots, and line charts. Optionally overlay generated input values on visualizations.

*HOME PAGE*
<img width="1366" height="688" alt="Screenshot (37)" src="https://github.com/user-attachments/assets/b2c22a9d-95f5-46a8-8af9-12079e7a2bc8" />


*HISTORICAL DATA PAGE*
<img width="1351" height="678" alt="Screenshot (39)" src="https://github.com/user-attachments/assets/368d18a2-04e2-4367-bcdf-5be1bf5c50bd" />


*INPUT DATA PAGE*
<img width="1353" height="695" alt="Screenshot (41)" src="https://github.com/user-attachments/assets/9ce8df8d-a6b0-40e8-afe8-cf32bd744359" />
<img width="1353" height="672" alt="Screenshot (45)" src="https://github.com/user-attachments/assets/b7474a13-6601-4985-9538-8e267b11d325" />


*RESULTS PAGE*
<img width="1335" height="679" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/7b20711c-5e0c-4a40-a4b3-7d3407a47c3b" />
<img width="1365" height="720" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/1f4e9b4e-0a03-4046-a355-2be7cfb549d3" />


*VISUALIZATION PAGE*
<img width="1352" height="504" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/bf11e927-495d-4367-95f4-6b321e7ed7c3" />
<img width="1352" height="519" alt="Screenshot (57)" src="https://github.com/user-attachments/assets/05c36c1b-cc1b-4b09-a4ab-19b5ec864ee4" />
<img width="1352" height="557" alt="Screenshot (58)" src="https://github.com/user-attachments/assets/06b9a6b1-7292-4d6a-92ca-00ac65fe2d6c" />
<img width="1324" height="545" alt="Screenshot (59)" src="https://github.com/user-attachments/assets/eec75431-10ef-4686-a7c9-ca78dd9a5064" />
<img width="1366" height="547" alt="Screenshot (60)" src="https://github.com/user-attachments/assets/4ca799fe-3364-4a3c-9a8f-069a11e0d4db" />
<img width="1347" height="714" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/5478ecbc-6aa3-44dc-ab73-9d1ec61719c2" />
<img width="1366" height="543" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/42379f6d-cb73-4293-9c13-017ea20cbfe0" />
<img width="1341" height="683" alt="Screenshot (63)" src="https://github.com/user-attachments/assets/a88e3e88-3585-4f47-9431-5ade9ee29382" />






Developed with ❤️ and Python from Richard 😎😎😎.
