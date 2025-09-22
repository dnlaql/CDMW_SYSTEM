from config.supabase_config import supabase

def login_user(username, password):
    res = supabase.table("user_test") \
        .select("*") \
        .eq("username", username) \
        .eq("password", password) \
        .execute()

    if res.data and len(res.data) > 0:
        return True, res.data[0]["username"]  # ambil username dari DB
    else:
        return False, None
