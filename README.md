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
   python -m venv venv
   .\venv\Scripts\activate

3. **Install Dependencies:**
   pip install -r requirements.txt

4.python -m streamlit run app.py

**🚀 Future Considerations**
- Integration of Time-Series Forecasting using LSTM (Deep Learning).
- Transitioning from static plots to interactive Plotly JavaScript charts.
- Deployment to Streamlit Community Cloud for global access.
- Real-time API integration for live industrial sensor feeds.


Developed with ❤️ and Python from Richard 😎😎😎.
