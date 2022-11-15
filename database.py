import sqlite3
from typing import List
import datetime
from model import TareaModel

db = sqlite3.connect("appTareas.db")
cursor = db.cursor()


def creatTabla():
    cursor.execute(""" CREATE TABLE IF NOT EXISTS appTareas (
        tarea text,
        categoria text,
        fechaInicio text,
        fechaFin text,
        estado integer,
        posicion integer )
    """)


creatTabla()


def getTareas() -> List[TareaModel]:
    cursor.execute('select * from appTareas')
    registros = cursor.fetchall()
    tareas = []
    for tarea in registros:
        tareas.append(TareaModel(*tarea))  # * desarma el paquete y los pasa al constructor por separado
    return tareas


def completarTarea(posicion: int):
    with db:
        cursor.execute('UPDATE appTareas SET estado = 2, fechaFin = fechaFin WHERE posicion = :posicion',
                       {'posicion': posicion, 'tareaFin': datetime.datetime.now().isoformat()})


def addTarea(tarea: TareaModel):
    cursor.execute("SELECT COUNT(*) FROM appTareas")
    totalTareas = cursor.fetchone()[0]
    tarea.posicion = totalTareas if totalTareas else 0  # 1ra posicion aray en 0 pero pantalla en 1
    with db:
        cursor.execute("INSERT INTO appTareas VALUES (:tarea, :categoria, :fechaInicio, :fechaFin, :estado, :posicion)",
                       {"tarea": tarea.tarea, "categoria": tarea.categoria, "fechaInicio": tarea.fechaInicio,
                        "fechaFin": tarea.fechaFin,
                        "estado": tarea.estado, "posicion": tarea.posicion})


def updateTarea(posicion: int, tarea: str, categoria: str):
    with db:
        if tarea is not None and categoria is not None:
            cursor.execute('UPDATE appTareas SET tarea = :tarea, categoria = :categoria WHERE posicion = :posicion',
                           {'posicion': posicion, 'tarea': tarea, 'categoria': categoria})
        elif tarea is not None:
            cursor.execute('UPDATE appTareas SET tarea = :tarea WHERE posicion = :posicion',
                           {'posicion': posicion, 'tarea': tarea})
        elif categoria is not None:
            cursor.execute('UPDATE appTareas SET categoria = :categoria WHERE posicion = :posicion',
                           {'posicion': posicion, 'categoria': categoria})


def deleteTarea(posicion):
    cursor.execute('select count(*) from appTareas')
    totalTareas = cursor.fetchone()[0]
    with db:
        cursor.execute("DELETE from appTareas WHERE posicion=:posicion", {"posicion": posicion})
        for p in range(posicion + 1, totalTareas):
            cambiarLugar(p, p - 1, False)
            # si no cambiamos el lugar el resto queda con distinto index entre el que se muestra en pantalla
            # y el que tiene en el array ahora


def cambiarLugar(viejaPosicion: int, nuevaPosicion: int, commit=True):
    cursor.execute('UPDATE appTareas SET posicion = :nuevaPosicion WHERE posicion = :viejaPosicion',
                   {'viejaPosicion': viejaPosicion, 'nuevaPosicion': nuevaPosicion})
    if commit:
        db.commit()
