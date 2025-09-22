st.subheader("📋 Debug User List")

users = supabase.table("user_test").select("*").execute()

st.write(users.data)
