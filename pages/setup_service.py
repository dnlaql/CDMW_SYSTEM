import streamlit as st
from config.supabase_config import supabase
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode
import pandas as pd

TABLE = "service_type"

def setup_service_page():
    st.header("⚙️ Setup: Jenis Servis (Interactive Table)")

    # --- Tambah Servis ---
    with st.form("add_service"):
        new_service = st.text_input("Nama Servis Baru")
        add_btn = st.form_submit_button("Tambah Servis")

        if add_btn and new_service:
            try:
                supabase.table(TABLE).insert({"name": new_service}).execute()
                st.success(f"Servis '{new_service}' ditambah!")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Gagal tambah servis: {e}")

    st.markdown("---")

    # --- Fetch data ---
    try:
        services = supabase.table(TABLE).select("*").order("id").execute().data
        if not services:
            st.info("Tiada servis lagi. Sila tambah servis baru.")
            return

        df = pd.DataFrame(services)
        df["Action"] = ""  # Placeholder untuk buttons

        # --- Configure AgGrid ---
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_selection(selection_mode="single", use_checkbox=True)
        gb.configure_columns(["id", "name", "created_at"], editable=False)
        gb.configure_column("name", editable=True)
        gb.configure_column("Action", header_name="Actions", editable=False, cellRenderer=JsCode('''
            class BtnCellRenderer {
                init(params) {
                    this.params = params;
                    this.eGui = document.createElement('div');
                    this.eGui.innerHTML = `
                        <button style="margin-right:5px;" class="update-btn">💾</button>
                        <button class="delete-btn">❌</button>
                    `;
                }
                getGui() { return this.eGui; }
                refresh() { return false; }
            }
        '''))
        gb.configure_grid_options(domLayout='normal')
        gridOptions = gb.build()

        grid_response = AgGrid(
            df,
            gridOptions=gridOptions,
            update_mode=GridUpdateMode.NO_UPDATE,
            allow_unsafe_jscode=True
        )

        # --- Handle update/delete manually based on selection ---
        selected = grid_response.get("selected_rows")
        if selected:
            row = selected[0]
            row_id = row["id"]
            new_name = row["name"]

            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"💾 Update '{new_name}'", key=f"update_{row_id}"):
                    supabase.table(TABLE).update({"name": new_name}).eq("id", row_id).execute()
                    st.success(f"Servis '{new_name}' dikemaskini!")
                    st.experimental_rerun()
            with col2:
                if st.button(f"❌ Delete '{new_name}'", key=f"delete_{row_id}"):
                    supabase.table(TABLE).delete().eq("id", row_id).execute()
                    st.warning(f"Servis '{new_name}' dipadam!")
                    st.experimental_rerun()

    except Exception as e:
        st.error(f"Gagal fetch servis: {e}")
