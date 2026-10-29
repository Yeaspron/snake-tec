#Snake
Videojuego Snake desarrollado en Python utilizando Turtle Graphics.

## Integrantes
- Yerik Escobar Aspron Master
- Diego Lemus Mejía: Colab

## Objetivo
Modificar el videojuego para incorporar:
1. Movimiento aleatorio de la comida.
2. Cinco colores posibles para la serpiente y la comida.
3. Colores diferentes en cada ejecución.

## Controles
- Flecha arriba: subir
- Flecha abajo: bajar
- Flecha izquierda: izquierda
- Flecha derecha: derecha

## Contribución de Diego: colores aleatorios

### Autor y rol

- Nombre: Diego Lemus Mejía.
- Matrícula: A01665486.
- Usuario de GitHub: a01665486-debug.
- Rol: Fork.
- Dueño del repositorio original: Yerik Escobar Asprón.

La contribución se desarrolla en la rama `feat/colores-aleatorios`
de mi fork y se propone al repositorio original mediante un pull request.

### Fuente original

[Snake de Grant Jenks](https://grantjenks.com/docs/freegames/snake.html).

### Funcionalidad implementada

Se definió una lista de cinco colores: azul, verde, morado,
naranja y negro. Al iniciar el programa, `random.sample` selecciona
dos colores distintos: uno para la serpiente y otro para la comida.

La selección se realiza fuera de la función `move`, de modo que
los colores permanecen durante la partida. Al ejecutar nuevamente
el programa se realiza otra selección aleatoria, que puede coincidir
con una combinación utilizada anteriormente.

El rojo no está incluido en la lista y se conserva únicamente
como indicador de choque.

### Instalación con ambiente virtual

Desde la carpeta del repositorio, en Terminal de macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install freegames
```

Para ejecutar el archivo modificado:

```bash
python snake.py
```

En sesiones posteriores solo es necesario entrar a la carpeta
y activar el ambiente:

```bash
source .venv/bin/activate
```

Para desactivarlo:

```bash
deactivate
```

La carpeta `.venv/` no se incluye en el repositorio.

### Controles

- Flecha arriba: subir.
- Flecha abajo: bajar.
- Flecha izquierda: mover a la izquierda.
- Flecha derecha: mover a la derecha.

### Reparto del trabajo

- Yerik: movimiento aleatorio de la comida y control de límites.
- Diego: selección y aplicación de colores aleatorios distintos.

Ambas funcionalidades se desarrollan en ramas separadas y pueden
trabajarse simultáneamente. Después se integran mediante pull requests
y se prueba su funcionamiento conjunto.

### Pruebas de mi funcionalidad

| Prueba | Resultado esperado | Resultado observado |
|---|---|---|
| Iniciar una partida | Serpiente y comida tienen colores diferentes | Correcto |
| Revisar la lista | Ambos colores están entre los cinco permitidos | Correcto |
| Jugar durante varios movimientos | Los colores no cambian durante la partida | Correcto |
| Reiniciar varias veces | Se realiza una nueva selección, con posibles repeticiones | Correcto |
| Moverse y recoger comida | Se conserva el funcionamiento del juego | Correcto |

No se observaron errores durante las pruebas manuales realizadas.

### Validación después del merge

Pendiente de probar los colores junto con el movimiento de la comida
cuando ambas funcionalidades estén integradas.
