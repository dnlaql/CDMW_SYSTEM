def login_user(username, password):
    res = supabase.table("user").select("*").eq("username", username).execute()
    print("DEBUG USERNAME ONLY:", res.data)

    if res.data and len(res.data) > 0:
        return True, username
    else:
        return False, None
