import streamlit as st
from auth.login import login_user
from config.supabase_config import supabase
from datetime import datetime

# ---------------- Debug User List ----------------
st.subheader("📋 Debug User List")
users = supabase.table("user_test").select("*").execute()
st.write(users.data)
