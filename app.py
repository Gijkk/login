def login(username: str, password: str) -> bool:
    if not username or not password:
        return False
    
    # Demo: user cố định
    if username == "admin" and password == "123456":
        return True
    return False
