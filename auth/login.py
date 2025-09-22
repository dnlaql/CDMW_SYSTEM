from config.supabase_config import supabase

def login_user(username, password):
    """
    Check user login based on table 'user'
    Return True + email kalau berjaya, False kalau gagal
    """
    res = supabase.table("user").select("*").eq("username", email).eq("password", password).execute()
    if res.data and len(res.data) > 0:
        return True, email
    else:
        return False, None
