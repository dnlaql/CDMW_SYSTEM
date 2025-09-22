from config.supabase_config import supabase

def login_user(username, password):
    res = supabase.table("user_test") \
        .select("*") \
        .eq("username", username) \
        .eq("password", password) \
        .execute()

    # Debug apa yang keluar
    print("DEBUG DATA:", res.data)
    
    if res.data and len(res.data) > 0:
        return True, username
    else:
        return False, None
