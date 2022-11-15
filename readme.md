#### Seguimiento de lista de tareas por consola

Desarrollado en python usando typer ,rich y sqlite3

Se manejaj todo por consola contiene columnas para id, la tarea , su categoria, y si esta completada

hay 4 categorias iniciales c/u con su propio color Estudio, Trabajo, Entretenimiento, Compras, se aceptan categorias con otros nombres, apareceran en color blanco

Hay que activar el entorno virtual, la app se maneja con el archivo cli.py + comandos 

```powershell
.\env\Scripts\activate

python .\cli.py mostrar
```

Comandos

```powershell
listar : muestra todas las tareas
    - python .\cli.py mostrar

agregar : acepta 2 parametros, la tarea y su categoria
    - python .\cli.py "tareax" "categoriax"

actualizar : acepta 3 parametros el id  tarea y categoria 
    - python .\cli.py actualizar 3 "tareaActualizada" "categoriax"

completar : cambia el icono en la columna Terminado, hay que indicar su id
    - python .\cli.py completar 2

borrar : elimina una tarea, se debe indicar el id
    - python .\cli.py borrar 4
```


![](img/ejemplo.png)
