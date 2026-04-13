from fastapi import Depends,HTTPException
from core.permissions import get_scopes_for_role

def get_current_user():
    return {
        "id" : 1,
        "username" : "hithesh",
        "role" : "admin"
    }

def get_current_user_with_scopes(user = Depends(get_current_user)):
    user["scopes"] = get_scopes_for_role(user["role"])
    return user

def require_scope(scope: str):
    def checker(
            user = Depends(get_current_user_with_scopes)
    ):
        if scope not in user["scopes"]:
            raise HTTPException(
                status_code=403,
                detail="Forbidden"
            )
        return user
    return checker

