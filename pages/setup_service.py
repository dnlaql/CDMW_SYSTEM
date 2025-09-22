import streamlit as st
from config.supabase_config import supabase

TABLE = "service_type"

def setup_service_page():
    st.header("⚙️ Setup: Jenis Servis")

    # --- Create Service ---
    with st.form("add_service"):
        new_service = st.text_input("Nama Servis Baru")
        add_btn = st.form_submit_button("Tambah Servis")

        if add_btn and new_service:
            supabase.table(TABLE).insert({"name": new_service}).execute()
            st.success(f"Servis '{new_service}' ditambah!")
            st.experimental_rerun()

    # --- List Services dalam table ---
    services = supabase.table(TABLE).select("*").order("id").execute().data

    if services:
        # Tukar ke list of dict untuk dataframe
        service_data = [{"ID": svc["id"], "Nama Servis": svc["name"], "Dibuat Pada": svc["created_at"]} for svc in services]
        st.table(service_data)  # atau st.dataframe(service_data) untuk sortable
    else:
        st.info("Tiada servis lagi. Sila tambah servis baru.")
