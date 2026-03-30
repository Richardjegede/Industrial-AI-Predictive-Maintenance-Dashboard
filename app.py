import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objects as go

# ---------- 1. PAGE CONFIG & THEME ----------
st.set_page_config(page_title="Industrial AI | Predictive Dashboard", layout="wide")

# Custom CSS for Bento Metric Cards & Dark Theme UI
st.markdown("""
<style>
    /* Main Background & Font */
    .stApp { background-color: #0E1117; }
    
    /* Bento Metric Card Styling */
    div[data-testid="stMetric"] {
        background: #111827;
        border: 1px solid #374151;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease-in-out;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
    }
    
    /* Global Text & Metric Colors */
    h1, h2, h3 { color: #F3F4F6 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMetricLabel"] { color: #9CA3AF !important; font-size: 14px !important; }
    [data-testid="stMetricValue"] { color: #3B82F6 !important; font-size: 2rem !important; }
</style>
""", unsafe_allow_html=True)

data = pd.read_csv('machinery_data.csv')
data.fillna(method='ffill', inplace=True)

# Feature selection and normalization
features = ['sensor_1', 'sensor_2', 'sensor_3', 'operational_hours']
target_rul = 'RUL'
target_maintenance = 'maintenance'
scaler = StandardScaler()
data[features] = scaler.fit_transform(data[features])

# Split data for regression and classification
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(data[features], data[target_rul], test_size=0.2, random_state=42)
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(data[features], data[target_maintenance], test_size=0.2, random_state=42)

# Train models
reg_model = RandomForestRegressor(n_estimators=100, random_state=42)
reg_model.fit(X_train_reg, y_train_reg)
clf_model = RandomForestClassifier(n_estimators=100, random_state=42)
clf_model.fit(X_train_clf, y_train_clf)
kmeans = KMeans(n_clusters=2, random_state=42)
data['cluster'] = kmeans.fit_predict(data[features])

# Prediction function
def predict_maintenance(features):
    rul_pred = reg_model.predict([features])
    maint_pred = clf_model.predict([features])
    cluster_pred = kmeans.predict([features])
    return {
        'RUL Prediction': rul_pred[0],
        'Maintenance Prediction': 'Needs Maintenance' if maint_pred[0] == 1 else 'Normal',
        'Anomaly Detection': 'Anomaly' if cluster_pred[0] == 1 else 'Normal'
    }

# ---------- 3. NAVIGATION ----------
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Historical Data", "Input Data", "Results", "Visualizations"],
        icons=["house", "table", "input-cursor", "check2-circle", "bar-chart-line"],
        menu_icon="cast", default_index=0,
        styles={"container": {"padding": "5!important", "background-color": "#111827"},
                "icon": {"color": "#3B82F6", "font-size": "20px"}, 
                "nav-link-selected": {"background-color": "#1F2937"}}
    )

# ---------- 4. PAGE LOGIC ----------
if selected == "Home":
    # Hero Section
    st.markdown("""
        <div style="background-color:#1e3a8a; padding:2rem; border-radius:1rem; margin-bottom:2rem; text-align:center;">
            <h1>🛡️ Welcome to the Predictive Maintenance Dashboard</h1>
            <p style="color:#bfdbfe;">This application provides predictive maintenance insights for industrial machinery. 
    Use the navigation menu to explore different sections of the app.</div>
    """, unsafe_allow_html=True)

    st.subheader("📊 Fleet Health Overview")
elif selected == "Historical Data":
    st.title("📂 Historical Data")
    st.write(data.head(10))

elif selected == "Input Data":
    st.title("🔧 Input Features")
    st.markdown("Use the sliders to input the sensor readings and operational hours or generate random values.")

    if 'generated_values' not in st.session_state:
        st.session_state['generated_values'] = None

    if st.button('Generate Random Values'):
        sensor_1 = np.random.uniform(data['sensor_1'].min(), data['sensor_1'].max())
        sensor_2 = np.random.uniform(data['sensor_2'].min(), data['sensor_2'].max())
        sensor_3 = np.random.uniform(data['sensor_3'].min(), data['sensor_3'].max())
        operational_hours = np.random.uniform(data['operational_hours'].min(), data['operational_hours'].max())
        st.session_state['generated_values'] = [sensor_1, sensor_2, sensor_3, operational_hours]
        st.success("Random values generated successfully!")

    if st.session_state['generated_values'] is not None:
        st.write("**Generated Values:**")
        st.write(f"Sensor 1: {st.session_state['generated_values'][0]:.2f}")
        st.write(f"Sensor 2: {st.session_state['generated_values'][1]:.2f}")
        st.write(f"Sensor 3: {st.session_state['generated_values'][2]:.2f}")
        st.write(f"Operational Hours: {st.session_state['generated_values'][3]:.2f}")

        if st.button('Use Generated Values'):
            st.session_state['input_features'] = st.session_state['generated_values']
            st.success("Generated values have been used. Navigate to the Results page to see the predictions.")

    st.markdown("**Or manually input values:**")
    sensor_1 = st.slider('Sensor 1', float(data['sensor_1'].min()), float(data['sensor_1'].max()), float(data['sensor_1'].mean()))
    sensor_2 = st.slider('Sensor 2', float(data['sensor_2'].min()), float(data['sensor_2'].max()), float(data['sensor_2'].mean()))
    sensor_3 = st.slider('Sensor 3', float(data['sensor_3'].min()), float(data['sensor_3'].max()), float(data['sensor_3'].mean()))
    operational_hours = st.slider('Operational Hours', int(data['operational_hours'].min()), int(data['operational_hours'].max()), int(data['operational_hours'].mean()))

    if st.button('Submit'):
        st.session_state['input_features'] = [sensor_1, sensor_2, sensor_3, operational_hours]
        st.success("Input data submitted successfully! Navigate to the Results page to see the predictions.")

elif selected == "Results":
    st.title("📊 Prediction Results")
    if 'input_features' not in st.session_state:
        st.warning("Please input data first in the 'Input Data' section.")
    else:
        input_features = st.session_state['input_features']
        prediction = predict_maintenance(input_features)
        st.write(f"**Remaining Useful Life (RUL):** {prediction['RUL Prediction']:.2f} hours")
        st.write(f"**Maintenance Status:** {prediction['Maintenance Prediction']}")
        st.write(f"**Anomaly Detection:** {prediction['Anomaly Detection']}")
        if prediction['Maintenance Prediction'] == 'Needs Maintenance':
            st.error('⚠️ Maintenance is required!')
        if prediction['Anomaly Detection'] == 'Anomaly':
            st.warning('⚠️ Anomaly detected in sensor readings!')

elif selected == "Visualizations":
    st.title("📊 Data Insights & Analytics")

    # --- ROW 1: RUL GAUGE ---
    # This gauge is much more compelling than a standard text number
    avg_rul = data["RUL"].mean()
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = avg_rul,
        title = {'text': "Average Remaining Useful Life (Hrs)"},
        gauge = {
            'axis': {'range': [0, data["RUL"].max()]},
            'bar': {'color': "#00cc96"},
            'steps': [
                {'range': [0, 50], 'color': "#ef553b"}, # Red for critical
                {'range': [50, 150], 'color': "#fecb52"} # Yellow for warning
            ],
        }
    ))
    fig_gauge.update_layout(height=350, template="plotly_dark")
    st.plotly_chart(fig_gauge, use_container_width=True)

    st.markdown("---")

    # --- ROW 2: INTERACTIVE HISTOGRAM ---
    st.subheader("Interactive Sensor Distribution")
    # This is the code you asked about - it replaces static histplots
    fig_hist = px.histogram(
        data, 
        x=["sensor_1", "sensor_2", "sensor_3"], 
        marginal="box", 
        barmode="overlay", 
        template="plotly_dark",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    fig_hist.update_layout(
        xaxis_title="Sensor Values",
        yaxis_title="Frequency",
        legend_title="Sensor Type"
    )
    st.plotly_chart(fig_hist, use_container_width=True)


    # Histogram for sensor readings
    st.subheader("Histogram of Sensor Readings")
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    sns.histplot(data['sensor_1'], bins=30, ax=axs[0], kde=True)
    axs[0].set_title('Sensor 1')
    sns.histplot(data['sensor_2'], bins=30, ax=axs[1], kde=True)
    axs[1].set_title('Sensor 2')
    sns.histplot(data['sensor_3'], bins=30, ax=axs[2], kde=True)
    axs[2].set_title('Sensor 3')
    st.pyplot(fig)

    # Scatter plot for sensor readings vs operational hours
    st.subheader("Scatter Plot of Sensor Readings vs Operational Hours")
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].scatter(data['operational_hours'], data['sensor_1'], alpha=0.5)
    axs[0].set_title('Operational Hours vs Sensor 1')
    axs[0].set_xlabel('Operational Hours')
    axs[0].set_ylabel('Sensor 1')
    axs[1].scatter(data['operational_hours'], data['sensor_2'], alpha=0.5)
    axs[1].set_title('Operational Hours vs Sensor 2')
    axs[1].set_xlabel('Operational Hours')
    axs[1].set_ylabel('Sensor 2')
    axs[2].scatter(data['operational_hours'], data['sensor_3'], alpha=0.5)
    axs[2].set_title('Operational Hours vs Sensor 3')
    axs[2].set_xlabel('Operational Hours')
    axs[2].set_ylabel('Sensor 3')
    st.pyplot(fig)

    # Line chart for RUL over time
    st.subheader("Line Chart of RUL Over Time")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data['operational_hours'], data['RUL'], marker='o', linestyle='-')
    ax.set_title('RUL Over Operational Hours')
    ax.set_xlabel('Operational Hours')
    ax.set_ylabel('RUL')
    st.pyplot(fig)

    if 'input_features' in st.session_state:
        input_features = st.session_state['input_features']

        # Overlay generated input values if available
        if input_features is not None:
            # Histogram for sensor readings with generated input
            st.subheader("Histogram of Sensor Readings with Generated Input")
            fig, axs = plt.subplots(1, 3, figsize=(15, 5))
            sns.histplot(data['sensor_1'], bins=30, ax=axs[0], kde=True)
            axs[0].set_title('Sensor 1')
            axs[0].axvline(input_features[0], color='red', linestyle='--', label='Generated Value')
            sns.histplot(data['sensor_2'], bins=30, ax=axs[1], kde=True)
            axs[1].set_title('Sensor 2')
            axs[1].axvline(input_features[1], color='red', linestyle='--', label='Generated Value')
            sns.histplot(data['sensor_3'], bins=30, ax=axs[2], kde=True)
            axs[2].set_title('Sensor 3')
            axs[2].axvline(input_features[2], color='red', linestyle='--', label='Generated Value')
            plt.legend()
            st.pyplot(fig)

            # Scatter plot for sensor readings vs operational hours with generated input
            st.subheader("Scatter Plot of Sensor Readings vs Operational Hours with Generated Input")
            fig, axs = plt.subplots(1, 3, figsize=(15, 5))
            axs[0].scatter(data['operational_hours'], data['sensor_1'], alpha=0.5)
            axs[0].set_title('Operational Hours vs Sensor 1')
            axs[0].set_xlabel('Operational Hours')
            axs[0].set_ylabel('Sensor 1')
            axs[0].axvline(input_features[3], color='red', linestyle='--', label='Generated Value')
            axs[0].legend()
            axs[1].scatter(data['operational_hours'], data['sensor_2'], alpha=0.5)
            axs[1].set_title('Operational Hours vs Sensor 2')
            axs[1].set_xlabel('Operational Hours')
            axs[1].set_ylabel('Sensor 2')
            axs[1].axvline(input_features[3], color='red', linestyle='--', label='Generated Value')
            axs[1].legend()
            axs[2].scatter(data['operational_hours'], data['sensor_3'], alpha=0.5)
            axs[2].set_title('Operational Hours vs Sensor 3')
            axs[2].set_xlabel('Operational Hours')
            axs[2].set_ylabel('Sensor 3')
            axs[2].axvline(input_features[3], color='red', linestyle='--', label='Generated Value')
            axs[2].legend()
            st.pyplot(fig)

            # Line chart for RUL over time with generated input
            st.subheader("Line Chart of RUL Over Time with Generated Input")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data['operational_hours'], data['RUL'], marker='o', linestyle='-')
            ax.set_title('RUL Over Operational Hours')
            ax.set_xlabel('Operational Hours')
            ax.set_ylabel('RUL')
            ax.axvline(input_features[3], color='red', linestyle='--', label='Generated Value')
            ax.legend()
            st.pyplot(fig)