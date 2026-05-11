from pydantic import BaseModel, Field

class RegistroFoco(BaseModel):
    nivel_foco: int = Field(ge=1, le=5)
    tempo_minutos: int = Field(ge=1)
    comentario: str