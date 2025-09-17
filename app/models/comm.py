from pydantic import BaseModel, EmailStr, Field

class SendCode(BaseModel):
    email: EmailStr = Field(..., description="用户邮箱地址")
    code_type: str
    class Config:
        from_attributes = True