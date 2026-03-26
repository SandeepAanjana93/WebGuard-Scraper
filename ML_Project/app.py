import streamlit as st
import pandas as pd
import joblib
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="HR Analytics System", layout="wide")

# ---------------- HIDE SIDEBAR ----------------
st.markdown("""
<style>
[data-testid="stSidebar"] {display:none;}

body {
    background: linear-gradient(120deg,#d4fc79,#96e6a1);
}

.big-title {
    font-size:40px;
    font-weight:bold;
}

.card {
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0 0 20px rgba(0,0,0,0.15);
}

.stButton>button {
    width:100%;
    border-radius:8px;
    height:45px;
    font-size:16px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    col1, col2 = st.columns([1.2,1])

    with col1:
        st.markdown("<div class='big-title'>Corporate HR Analytics</div>", unsafe_allow_html=True)
        st.write("""
        This AI-powered HR Analytics platform helps organizations analyze employee data,
        monitor workforce trends, and predict employee attrition risks.

        🔹 Real-time workforce insights  
        🔹 Attrition risk prediction  
        🔹 Salary & performance analytics  
        🔹 Data-driven HR decision support  
        """)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🔐 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            c.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password))
            data = c.fetchone()
            if data:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Username or Password")

        st.markdown("---")
        st.subheader("📝 Register")

        new_user = st.text_input("Create Username")
        new_pass = st.text_input("Create Password", type="password")

        if st.button("Register"):
            c.execute("INSERT INTO users VALUES (?,?)", (new_user,new_pass))
            conn.commit()
            st.success("Account Created! Now Login.")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DASHBOARD ----------------
else:
    st.title("📊 HR Analytics Dashboard")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    df = pd.read_csv("cleaned_data.csv")
    model = joblib.load("attrition_model.pkl")

    st.subheader("Employee Data Overview")
    st.dataframe(df.head())

    col1, col2 = st.columns(2)
    col1.metric("Total Employees", len(df))
    col2.metric("Attrition Rate", f"{df['Attrition'].mean()*100:.2f}%")

    st.subheader("Attrition Distribution")
    st.bar_chart(df["Attrition"].value_counts())

    st.subheader("Monthly Income Distribution")
    st.line_chart(df["MonthlyIncome"])

    st.subheader("🔮 Attrition Prediction")

    X = df.drop("Attrition", axis=1)
    idx = st.slider("Select Employee", 0, len(df)-1, 0)
    sample = X.iloc[[idx]]

    if st.button("Predict"):
        pred = model.predict(sample)
        prob = model.predict_proba(sample)

        stay_prob = prob[0][0] * 100
        leave_prob = prob[0][1] * 100

        if pred[0] == 1:
            st.error(f"⚠️ Employee May Leave\n\nProbability: {leave_prob:.2f}%")
            st.progress(int(leave_prob))
        else:
            st.success(f"✅ Employee Will Stay\n\nProbability: {stay_prob:.2f}%")
            st.progress(int(stay_prob))

    st.caption("Corporate HR Analytics • ML Project")