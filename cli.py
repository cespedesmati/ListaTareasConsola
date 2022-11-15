import typer
from rich.console import Console
from rich.table import Table

from database import addTarea, deleteTarea, updateTarea, completarTarea, getTareas
from model import TareaModel

consola = Console()
app = typer.Typer()


@app.command(short_help="agregar tarea")
def agregar(tarea: str, categoria: str):
    typer.echo(f"agregando {tarea}, {categoria}")
    nueva = TareaModel(tarea, categoria)
    addTarea(nueva)
    listar()


@app.command(short_help="marca una tarea como completada")
def completar(posicion: int):
    typer.echo(f"tarea {posicion} completada")
    completarTarea(posicion - 1)
    listar()


@app.command(short_help="eliminar tarea")
def borrar(posicion: int):
    typer.echo(f"eliminando {posicion}")
    deleteTarea(posicion - 1)
    listar()


@app.command(short_help="actualizar tarea")
def actualizar(posicion: int, tarea: str = None, categoria: str = None):
    typer.echo(f"actualizando {posicion}")
    updateTarea(posicion - 1, tarea, categoria)
    listar()


@app.command(short_help="listar tareas")
def listar():
    tareas = getTareas()
    consola.print("[bold magenta]Tareas![/bold magenta]", "📚")

    tabla = Table(show_header=True, header_style="bold purple")
    tabla.add_column("#", style="dim", width=6)
    tabla.add_column("Todo", min_width=20)
    tabla.add_column("Categoria", min_width=12, justify="right")
    tabla.add_column("Terminado", min_width=12, justify="right")

    def getColor(categoria):
        COLORES = {"Estudio": "cyan", "Trabajo": "red", "Entretenimiento": "yellow", "Compras": "green"}
        return COLORES[categoria] if categoria in COLORES else "white"

    for index, tarea in enumerate(tareas, start=1):
        color = getColor(tarea.categoria)
        isTerminada = "✅" if tarea.estado == 2 else "🛑"
        tabla.add_row(str(index), tarea.tarea, f"[{color}]{tarea.categoria}[/{color}]", isTerminada)

    consola.print(tabla)


if __name__ == "__main__":
    app()
