ROLE_SCOPES = {
    "viewer" : [
        "posts:read"
    ],
    "editor" : [
        "posts:read",
        "posts:write"
    ],
    "admin" : [
        "posts:read",
        "posts:write",
        "posts:delete",
        "users:read"
    ]
}

def get_scopes_for_role(role: str) -> list[str]:
    return ROLE_SCOPES.get(role,[])