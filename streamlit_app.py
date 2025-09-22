import streamlit as st
from auth.auth import login_user
from config.supabase_config import supabase
from datetime import datetime

st.title("Bengkel Staff Login")

# ---------------- Login Form ----------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, user_email = login_user(email, password)
        if success:
            st.session_state["logged_in"] = True
            st.session_state["user_email"] = user_email
            st.success(f"Welcome {user_email}!")
        else:
            st.error("Login failed!")

# ---------------- Job Sheet Form ----------------
if st.session_state["logged_in"]:
    st.subheader("Job Sheet Form")
    with st.form("job_form"):
        customer = st.text_input("Nama Customer")
        plate = st.text_input("Plat Kereta")
        service = st.selectbox("Jenis Servis", ["Oil Change", "Brake Service", "Tires"])
        labour = st.number_input("Labour Charge (RM)", 0)
        spare = st.number_input("Sparepart Cost (RM)", 0)
        
        submitted = st.form_submit_button("Submit Job")
        
        if submitted:
            job_number = f"INV{datetime.now().strftime('%Y%m%d%H%M%S')}"
            total = labour + spare
            
            supabase.table("job_sheet").insert({
                "job_number": job_number,
                "customer_name": customer,
                "car_plate": plate,
                "service_type": service,
                "labour_charge": labour,
                "sparepart_cost": spare,
                "total_cost": total,
                "created_at": datetime.now()
            }).execute()
            
            st.success(f"Job submitted! Invoice No: {job_number}, Total RM {total}")
