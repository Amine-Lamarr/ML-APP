import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ======================== Page Configuration ========================
st.set_page_config(page_title="📱 Addiction Prediction", layout="centered")

# ======================== Custom Styling ========================
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7f7;
    }
    .stApp {
        font-family: 'Segoe UI', sans-serif;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        color: #1f77b4;
    }
    .important {
        color: #e74c3c;
        font-weight: bold;
    }
    .subtle {
        color: #7f8c8d;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ======================== Load Resources ========================
model = joblib.load("lightmodel.joblib")
scalers = joblib.load("scalers.joblib")
encoders = joblib.load("encoded.joblib")

selected_features = [
    'Age', 'Gender', 'Daily_Usage_Hours', 'Sleep_Hours', 'Academic_Performance',
    'Social_Interactions', 'Self_Esteem', 'Screen_Time_Before_Bed',
    'Phone_Checks_Per_Day', 'Apps_Used_Daily', 'Time_on_Social_Media',
    'Time_on_Gaming', 'Phone_Usage_Purpose_Gaming',
    'Phone_Usage_Purpose_Other', 'Phone_Usage_Purpose_Social Media'
]

# ======================== Sidebar User Info ========================
st.sidebar.title("👤 User Info")
user_name = st.sidebar.text_input("Enter your name", placeholder="e.g. Amine")

user_guess = st.sidebar.slider("How addicted do YOU think you are? 🤔", 0.0, 10.0, step=0.5)

st.sidebar.markdown("---")
st.sidebar.markdown("📱 **Fun Questions**")

q1 = st.sidebar.radio("Do you sleep with your phone in hand?", ["No 😇", "Sometimes 😅", "Always 💀"])
q2 = st.sidebar.radio("Have you cried over low battery?", ["Never 😂", "Maybe once... 😬", "Yes 😭"])
q3 = st.sidebar.radio("Use phone in the toilet?", ["Who doesn't? 🚽📱", "Ew no", "Sometimes..."])

# ======================== Page Title ========================
st.title("📱 Phone Addiction AI Prediction")
st.markdown("Fill in your information to predict your addiction level 🎯")

# ======================== Main Page Inputs ========================
user_input = {}

col1, col2 = st.columns(2)

with col1:
    user_input["Age"] = st.number_input("Age", min_value=10, max_value=25, step=1)
    user_input["Gender"] = st.radio("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    user_input["Daily_Usage_Hours"] = st.slider("Daily Phone Usage (hours)", 0.0, 12.0, step=0.5)
    user_input["Sleep_Hours"] = st.slider("Sleep Hours", 0.0, 12.0, step=0.5)
    user_input["Academic_Performance"] = st.slider("Academic Performance", 50, 100, step=1)
    user_input["Social_Interactions"] = st.slider("Social Interactions", 0, 10, step=1)
    user_input["Self_Esteem"] = st.slider("Self Esteem", 1, 10, step=1)
    user_input["Screen_Time_Before_Bed"] = st.slider("Screen Time Before Bed (hrs)", 0.0, 3.0, step=0.1)

with col2:
    user_input["Phone_Checks_Per_Day"] = st.slider("Phone Checks Per Day", 0, 200, step=1)
    user_input["Apps_Used_Daily"] = st.slider("Apps Used Daily", 0, 30, step=1)
    user_input["Time_on_Social_Media"] = st.slider("Time on Social Media (hrs)", 0.0, 8.0, step=0.5)
    user_input["Time_on_Gaming"] = st.slider("Time on Gaming (hrs)", 0.0, 8.0, step=0.5)

    user_input["Phone_Usage_Purpose_Gaming"] = 1 if st.checkbox("Uses phone mainly for Gaming") else 0
    user_input["Phone_Usage_Purpose_Other"] = 1 if st.checkbox("Uses phone mainly for Other reasons") else 0
    user_input["Phone_Usage_Purpose_Social Media"] = 1 if st.checkbox("Uses phone mainly for Social Media") else 0

# ======================== Preprocessing ========================
df = pd.DataFrame([user_input])

# for col, scaler in scalers.items():
#     if col in df.columns:
#         df[[col]] = scaler.transform(df[[col]])
for col, scaler in scalers.items():
    if col in df.columns:
        df[[col]] = scaler.transform(df[[col]])


# ======================== Prediction ========================
if st.button("🔎 Predict Addiction Level"):
    prediction = model.predict(df[selected_features])[0]
    prediction_scaled = prediction * 10
    name = user_name.strip() if user_name.strip() else "User"

    st.markdown(f"## 👋 Hello, <span class='important'>{name}</span>!", unsafe_allow_html=True)
    st.markdown("## 🧠 <span class='important'>Predicted Addiction Level</span>", unsafe_allow_html=True)
    st.markdown(f"<p class='result'>📊 {prediction_scaled:.2f} / 10</p>", unsafe_allow_html=True)

    st.markdown("### 🎯 Your Own Guess:")
    st.markdown(f"👉 You guessed: **{user_guess} / 10**")
    diff = abs(user_guess - prediction_scaled)
    if diff < 1:
        st.success("👏 Great guess! You know yourself well.")
    else:
        st.warning("Not even close... AI knows you better! haha")

    st.markdown("---")
    st.markdown("### 😂 Fun Answers:")
    st.markdown(f"- **Sleep with phone?** {q1}")
    st.markdown(f"- **Cried over battery?** {q2}")
    st.markdown(f"- **Toilet usage?** {q3}")

    st.markdown("---")
    st.markdown("### 📋 <span class='subtle'>Input Summary</span>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([user_input]))
