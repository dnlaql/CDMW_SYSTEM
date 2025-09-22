import streamlit as st
from pages.dashboard import dashboard_page
from pages.invoice import invoice_page
from pages.setup_service import setup_service_page

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.title("Bengkel Staff Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # TODO: tukar dengan login_user()
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.session_state["user_username"] = username
            st.success(f"Welcome {username}!")
        else:
            st.error("Login failed!")

else:
    # ---------------- SIDEBAR ----------------
    st.sidebar.title("📌 Menu")

    menu = st.sidebar.radio(
        "Navigate",
        ["Dashboard", "Invoice", "Setup"],
        label_visibility="collapsed"
    )

    if menu == "Dashboard":
        dashboard_page()
    elif menu == "Invoice":
        invoice_page()
    elif menu == "Setup":
        st.sidebar.subheader("⚙️ Setup Options")
        setup_menu = st.sidebar.radio(
            "Setup Menu",
            ["Jenis Servis"],
            label_visibility="collapsed"
        )

        if setup_menu == "Jenis Servis":
            setup_service_page()
