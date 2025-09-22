from config.supabase_config import supabase

def login_user(username, password):
    username = username.strip()
    password = password.strip()

    res = supabase.table("user_test") \
        .select("*") \
        .eq("username", username) \
        .eq("password", password) \
        .execute()

    print("DEBUG INPUT:", username, password)
    print("DEBUG RESPONSE:", res)

    if res.data and len(res.data) > 0:
        return True, username
    else:
        return False, None
