from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Log de Performance"}


class RegistroFoco(BaseModel):
    nivel_foco: int
    tempo_minutos: int
    comentario: str

registro_foco_list: list[RegistroFoco] = []

@app.get("/diagnostico-produtividade")
def read_item(q: str | None = None):
    nivel_foco_list: list[int] = [rf.nivel_foco for rf in registro_foco_list]
    media_nivel_foco: float = sum(nivel_foco_list) / len(nivel_foco_list)

    tempo_total_focado: float = sum([rf.tempo_minutos for rf in registro_foco_list])
    
    return {media_nivel_foco, tempo_total_focado}


@app.post("/registro-foco")
def update_item(body: RegistroFoco):
    registro_foco_list.append(body)
    return status.HTTP_201_CREATED