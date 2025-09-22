def login_user(username, password):
    # Buat dummy login dulu
    if username == "admin" and password == "123":
        return {"username": username, "role": "admin"}
    return None
