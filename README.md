# 🛠️ Industrial AI: Predictive Maintenance Dashboard

An end-to-end Machine Learning solution designed to monitor machinery health, predict potential failures, and estimate **Remaining Useful Life (RUL)**. This project transforms raw sensor data into actionable industrial insights through a high-performance interactive dashboard.

---

## 🌟 Key Features
- **Regression (RUL Prediction):** Estimates the exact number of operational hours remaining before a machine requires service.
- **Classification (Failure Detection):** Categorizes machine status as **'Normal'** or **'Needs Maintenance'** using Random Forest.
- **Unsupervised Clustering:** Employs **KMeans** for **Anomaly Detection** to identify irregular sensor patterns that suggest underlying issues.
- **Interactive UI:** A "fascinating" dark-themed dashboard built with **Streamlit**, featuring custom CSS Glassmorphism and **Lottie Animations**.

## 📊 Technical Stack
- **Frontend:** [Streamlit](https://streamlit.io), Streamlit Option Menu, Lottie (JavaScript-based animations)
- **Machine Learning:** [Scikit-Learn](https://scikit-learn.org) (Random Forest, KMeans, StandardScaler)
- **Data Processing:** [Pandas](https://pandas.pydata.org), NumPy
- **Visualizations:** [Seaborn](https://seaborn.pydata.org), Matplotlib

## ⚙️ Installation & Setup
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

**Features**

- Home: Welcome page providing an overview of the application.
- Historical Data: View historical data of machinery sensor readings and operational hours.
- Input Data: Submit input data for prediction, either manually or by generating random values.
- Results: Display predictions for remaining useful life (RUL), maintenance status, and anomaly detection based on the input data.
- Visualizations: Visualize historical sensor data and operational hours through histograms, scatter plots, and line charts. Optionally overlay generated input values on visualizations.

**HOME PAGE**
<img width="1366" height="688" alt="Screenshot (37)" src="https://github.com/user-attachments/assets/b2c22a9d-95f5-46a8-8af9-12079e7a2bc8" />


**HISTORICAL DATA PAGE**
<img width="1351" height="678" alt="Screenshot (39)" src="https://github.com/user-attachments/assets/368d18a2-04e2-4367-bcdf-5be1bf5c50bd" />


**INPUT DATA PAGE**
<img width="1353" height="695" alt="Screenshot (41)" src="https://github.com/user-attachments/assets/9ce8df8d-a6b0-40e8-afe8-cf32bd744359" />
<img width="1353" height="672" alt="Screenshot (45)" src="https://github.com/user-attachments/assets/b7474a13-6601-4985-9538-8e267b11d325" />


**RESULTS PAGE**
<img width="1335" height="679" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/7b20711c-5e0c-4a40-a4b3-7d3407a47c3b" />
<img width="1365" height="720" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/1f4e9b4e-0a03-4046-a355-2be7cfb549d3" />


**VISUALIZATION PAGE**
<img width="1352" height="504" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/bf11e927-495d-4367-95f4-6b321e7ed7c3" />
<img width="1352" height="519" alt="Screenshot (57)" src="https://github.com/user-attachments/assets/05c36c1b-cc1b-4b09-a4ab-19b5ec864ee4" />
<img width="1352" height="557" alt="Screenshot (58)" src="https://github.com/user-attachments/assets/06b9a6b1-7292-4d6a-92ca-00ac65fe2d6c" />
<img width="1324" height="545" alt="Screenshot (59)" src="https://github.com/user-attachments/assets/eec75431-10ef-4686-a7c9-ca78dd9a5064" />
<img width="1366" height="547" alt="Screenshot (60)" src="https://github.com/user-attachments/assets/4ca799fe-3364-4a3c-9a8f-069a11e0d4db" />
<img width="1347" height="714" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/5478ecbc-6aa3-44dc-ab73-9d1ec61719c2" />
<img width="1366" height="543" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/42379f6d-cb73-4293-9c13-017ea20cbfe0" />
<img width="1341" height="683" alt="Screenshot (63)" src="https://github.com/user-attachments/assets/a88e3e88-3585-4f47-9431-5ade9ee29382" />



**🚀 Future Considerations**
- Integration of Time-Series Forecasting using LSTM (Deep Learning).
- Transitioning from static plots to interactive Plotly JavaScript charts.
- Deployment to Streamlit Community Cloud for global access.
- Real-time API integration for live industrial sensor feeds.






Developed with ❤️ and Python from Richard 😎😎😎.
