from fastapi import APIRouter,Depends
from auth.dependencies import require_scope

router = APIRouter(prefix="/posts",tags=["posts"])

@router.get("/")
async def list_posts(
    user = Depends(require_scope("posts:read"))):
        return {
            "message" : "visible posts",
            "user" : user
        }

@router.post("/")
async def create_post(
        user = Depends(require_scope("posts:write"))
):
        return{
                "message" : "post created",
                "user" : user
        }

@router.delete("/{post_id}")
async def delete_post(
        post_id: int,
        user=Depends(require_scope("posts:delete"))
):
        return {
                "message" : f"Deleted {post_id}",
                "users" : user
        }

