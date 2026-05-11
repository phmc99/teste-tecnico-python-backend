from app.models.registro_foco import RegistroFoco

def calcular_diagnostico(registros: list[RegistroFoco]):
    if len(registros) == 0:
        return {"mensagem": "nenhum registro adicionado"}

    media_nivel_foco: int | float = (
        sum([r.nivel_foco for r in registros]) / len(registros)
    )

    tempo_total_focado: int = sum([
        r.tempo_minutos for r in registros
    ])

    return {
        "media_nivel_foco": media_nivel_foco,
        "total_minutos_focados": tempo_total_focado
    }