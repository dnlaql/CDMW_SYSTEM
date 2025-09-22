from config.supabase_config import supabase

def login_user(username, password):
    """
    Check user login from table 'user_test'
    Return True + username kalau berjaya, False kalau gagal
    """
    res = supabase.table("user_test") \
        .select("*") \
        .eq("username", username) \
        .eq("password", password) \
        .execute()

    if res.data and len(res.data) > 0:
        return True, username
    else:
        return False, None
