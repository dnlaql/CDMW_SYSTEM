from config.supabase_config import supabase

def login_user(username, password):
    """
    Check user login based on table 'user'
    Return True + username kalau berjaya, False kalau gagal
    """
    res = supabase.table("user").select("*").eq("username", username).eq("password", password).execute()
    if res.data and len(res.data) > 0:
        return True, username
    else:
        return False, None
