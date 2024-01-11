from fastapi import APIRouter

extend_test = APIRouter()


@extend_test.get("/test", tags=["扩展接口"], description="测试接口", summary="测试接口")
async def test():
    return {"message": "Hello World"}
