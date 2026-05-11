from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()

class RegistroFoco(BaseModel):
    nivel_foco: int = Field(ge=1, le=5)
    tempo_minutos: int = Field(ge=1)
    comentario: str

registro_foco_list: list[RegistroFoco] = []

@app.get("/diagnostico-produtividade")
def diagnostico_produtividade():
    if (len(registro_foco_list) == 0):
        return {"mensagem": "nenhum registro adicionado"}

    nivel_foco_list: list[int] = [rf.nivel_foco for rf in registro_foco_list]
    media_nivel_foco: float = sum(nivel_foco_list) / len(nivel_foco_list)

    tempo_total_focado: float = sum([rf.tempo_minutos for rf in registro_foco_list])
    
    return {"media_nivel_foco": media_nivel_foco, "total_minutos_focados": tempo_total_focado}

@app.get("/registros")
def listar_registros(termo_busca: str | None = None, nivel_foco: int | None = None, tempo_minutos: int | None = None):
    registros_filtrados: list[RegistroFoco] = registro_foco_list

    if termo_busca is not None:
        registros_filtrados = [r for r in registros_filtrados if termo_busca.lower() in r.comentario.lower()]

    if nivel_foco is not None:
        registros_filtrados = [r for r in registros_filtrados if r.nivel_foco == nivel_foco]

    if tempo_minutos is not None:
        registros_filtrados = [r for r in registros_filtrados if r.tempo_minutos == tempo_minutos]

    return registros_filtrados
  
@app.post("/registro-foco")
def registro_foco(body: RegistroFoco):
    registro_foco_list.append(body)
    return status.HTTP_201_CREATED