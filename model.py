import datetime


class TareaModel:
    def __init__(self, tarea, categoria, fechaInicio = None, fechaFin = None, estado = None, posicion = None):
        self.tarea = tarea
        self.categoria = categoria
        self.fechaInicio = fechaInicio if fechaInicio is not None else datetime.datetime.now().isoformat()
        self.fechaFin = fechaFin if fechaFin is not None else None
        self.estado = estado if estado is not None else 1  # 1 = pendiente #2 = terminada
        self.posicion = posicion if posicion is not None else None

    def __repr__(self) -> str:
        return f"({self.tarea}, {self.categoria}, {self.fechaInicio}, {self.fechaFin}, {self.estado}, {self.posicion}"
