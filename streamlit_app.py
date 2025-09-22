import streamlit as st
from auth.login import login_user
from config.supabase_config import supabase

st.set_page_config(page_title="Workshop Dashboard", layout="wide")

st.title("🔧 Workshop Dashboard")

# ---------------- Session State ----------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# ---------------- Login Form ----------------
if not st.session_state["logged_in"]:
    st.subheader("Please Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, user_username = login_user(username, password)
        if success:
            st.session_state["logged_in"] = True
            st.session_state["user_username"] = user_username
            st.success(f"Welcome {user_username}!")
            st.experimental_rerun()
        else:
            st.error("Login failed!")

# ---------------- Dashboard ----------------
else:
    st.sidebar.title("📂 Navigation")
    choice = st.sidebar.radio("Go to:", ["Dashboard", "Invoice", "Customer Management])

    if choice == "Dashboard":
        st.header("Welcome to Dashboard 👋")
        st.info("Please select a module from the sidebar.")

    elif choice == "Invoice":
        from pages.invoice import invoice_page
        invoice_page()
