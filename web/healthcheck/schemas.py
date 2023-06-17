from pydantic import BaseModel


class HealthcheckResponse(BaseModel):
    is_ok: bool
