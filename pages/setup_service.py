import streamlit as st
from config.supabase_config import supabase
from datetime import datetime

TABLE = "service_type"

def setup_service_page():
    st.header("⚙️ Setup: Jenis Servis")

    # --- Tambah Servis ---
    with st.form("add_service"):
        new_service = st.text_input("Nama Servis Baru")
        add_btn = st.form_submit_button("Tambah Servis")

        if add_btn and new_service:
            try:
                supabase.table(TABLE).insert({"name": new_service}).execute()
                st.success(f"Servis '{new_service}' ditambah!")
                st.experimental_rerun()  # rerun selepas tambah
            except Exception as e:
                st.error(f"Gagal tambah servis: {e}")

    st.markdown("---")

    # --- Papar Servis dalam Table + Edit/Delete ---
    try:
        services = supabase.table(TABLE).select("*").order("id").execute().data
        if services:
            st.subheader("Senarai Jenis Servis")

            for svc in services:
                col1, col2, col3 = st.columns([3,3,1])
                with col1:
                    svc_name = st.text_input(f"Nama Servis {svc['id']}", value=svc["name"], key=f"edit_{svc['id']}")
                with col2:
                    if st.button("💾 Update", key=f"update_{svc['id']}"):
                        try:
                            supabase.table(TABLE).update({"name": svc_name}).eq("id", svc["id"]).execute()
                            st.success(f"Servis '{svc_name}' dikemaskini!")
                            st.experimental_rerun()
                        except Exception as e:
                            st.error(f"Gagal update: {e}")
                with col3:
                    if st.button("❌ Delete", key=f"del_{svc['id']}"):
                        try:
                            supabase.table(TABLE).delete().eq("id", svc["id"]).execute()
                            st.warning(f"Servis '{svc['name']}' dipadam!")
                            st.experimental_rerun()
                        except Exception as e:
                            st.error(f"Gagal delete: {e}")
        else:
            st.info("Tiada servis lagi. Sila tambah servis baru.")
    except Exception as e:
        st.error(f"Gagal fetch servis: {e}")
