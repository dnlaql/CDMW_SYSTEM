from config.supabase_config import supabase

def login_user(username, password):
    """
    Check user login from table 'user_test'
    Return True + username kalau berjaya, False kalau gagal
    """
    res = supabase.table("user_test").select("*").ilike("username", username).ilike("password", password).execute()

    # Debug kalau nak tengok apa Supabase return
    # print("DEBUG LOGIN:", res)

    if res.data and len(res.data) > 0:
        return True, username
    else:
        return False, None
