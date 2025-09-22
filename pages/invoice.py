import streamlit as st
from datetime import datetime
from config.supabase_config import supabase

def invoice_page():
    st.header("🧾 Create New Invoice")

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
                "created_at": datetime.now().isoformat()
            }).execute()
            
            st.success(f"✅ Job submitted! Invoice No: {job_number}, Total RM {total}")
