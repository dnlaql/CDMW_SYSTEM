import streamlit as st
from config.supabase_config import supabase

# =========================
# Function untuk login user
# =========================
def login_user(username, password):
    res = supabase.table("user_test") \
        .select("*") \
        .eq("username", username) \
        .eq("password", password) \
        .execute()

    if res.data and len(res.data) > 0:
        return True, res.data[0]["username"], res.data[0]["role"]
    else:
        return False, None, None

# =========================
# MAIN APP
# =========================
st.title("CDMW System")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user_username" not in st.session_state:
    st.session_state["user_username"] = None
if "user_role" not in st.session_state:
    st.session_state["user_role"] = None

# =========================
# LOGIN PAGE
# =========================
if not st.session_state["logged_in"]:
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, user_username, user_role = login_user(username, password)
        if success:
            st.session_state["logged_in"] = True
            st.session_state["user_username"] = user_username
            st.session_state["user_role"] = user_role
            st.success(f"Welcome {user_username}! (Role: {user_role})")
        else:
            st.error("Login failed!")

# =========================
# INVOICE PAGE
# =========================
else:
    st.sidebar.write(f"👤 Logged in as: {st.session_state['user_username']} ({st.session_state['user_role']})")
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user_username"] = None
        st.session_state["user_role"] = None
        st.rerun()

    st.subheader("🧾 Invoice Form")

    customer_name = st.text_input("Customer Name")
    customer_phone = st.text_input("Phone Number")
    item_desc = st.text_area("Item Description")
    amount = st.number_input("Amount (RM)", min_value=0.0, format="%.2f")

    if st.button("Generate Invoice"):
        if customer_name and customer_phone and item_desc and amount > 0:
            st.success("✅ Invoice Generated!")
            st.write("### Invoice Preview")
            st.write(f"**Customer:** {customer_name}")
            st.write(f"**Phone:** {customer_phone}")
            st.write(f"**Item:** {item_desc}")
            st.write(f"**Amount:** RM {amount:.2f}")
        else:
            st.error("⚠️ Please fill all fields before generating invoice.")
