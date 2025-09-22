import streamlit as st
from config.supabase_config import supabase

TABLE = "service_type"

def setup_service_page():
    st.header("⚙️ Setup: Jenis Servis")

    # --- Tambah servis baru ---
    with st.form("add_service"):
        new_service = st.text_input("Nama Servis Baru")
        add_btn = st.form_submit_button("Tambah Servis")
        if add_btn and new_service:
            supabase.table(TABLE).insert({"name": new_service}).execute()
            st.success(f"Servis '{new_service}' ditambah!")
            st.experimental_rerun()

    st.markdown("---")

    # --- Papar servis dalam table dengan emoji button ---
    services = supabase.table(TABLE).select("*").order("id").execute().data
    if services:
        st.subheader("Senarai Jenis Servis")

        for svc in services:
            col1, col2, col3 = st.columns([4,1,1])  # Adjust ratio supaya cantik
            with col1:
                st.text(svc["name"])
            with col2:
                if st.button("💾", key=f"update_{svc['id']}"):
                    # Update logic (contoh rename)
                    new_name = st.text_input(f"Edit {svc['name']}", value=svc["name"], key=f"edit_{svc['id']}")
                    supabase.table(TABLE).update({"name": new_name}).eq("id", svc["id"]).execute()
                    st.success(f"Servis '{new_name}' dikemaskini!")
                    st.experimental_rerun()
            with col3:
                if st.button("❌", key=f"delete_{svc['id']}"):
                    supabase.table(TABLE).delete().eq("id", svc["id"]).execute()
                    st.warning(f"Servis '{svc['name']}' dipadam!")
                    st.experimental_rerun()
    else:
        st.info("Tiada servis lagi.")
