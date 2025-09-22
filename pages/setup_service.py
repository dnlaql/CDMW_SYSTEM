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

    # --- List Services ---
    services = supabase.table(TABLE).select("*").order("id").execute().data

    if services:
        for svc in services:
            col1, col2 = st.columns([3,1])
            with col1:
                st.write(f"- {svc['name']}")
            with col2:
                if st.button("❌", key=f"del_{svc['id']}"):
                    supabase.table(TABLE).delete().eq("id", svc["id"]).execute()
                    st.warning(f"Servis '{svc['name']}' dipadam!")
                    st.experimental_rerun()
    else:
        st.info("Tiada servis lagi. Sila tambah baru.")
