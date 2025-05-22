
# Proyecto Final: Resolución de Sudoku con BFS y DFS

**Autor:** César Omar Martín Rodríguez

Este proyecto resuelve un Sudoku de 9x9 utilizando dos algoritmos clásicos de búsqueda:

- Búsqueda en Anchura (BFS)
- Búsqueda en Profundidad (DFS)

Incluye una interfaz gráfica interactiva con **Tkinter**, lectura del tablero desde un archivo **CSV**, y visualización en tiempo real del proceso de resolución.

---

## Estructura del Repositorio

```
ProyectoSudoku/
├── sudoku_input.csv     # Archivo con el tablero inicial (9x9)
├── SudokuBFS.py         # Resolución con BFS + GUI
├── SudokuDFS.py         # Resolución con DFS + GUI
├── Informe.pdf          # Informe técnico en formato IEEE
└── README.md            # Este archivo
```

---

## Requisitos

- **Python 3.x**
- Librerías necesarias:
  - `tkinter` (incluida con Python)
  - `csv` (estándar)
  - `time`
  - `collections` (deque)

---

## Instrucciones de Ejecución

1. **Verifica el archivo de entrada**

Asegúrate de tener el archivo `sudoku_input.csv` con el siguiente formato:

- 9 filas
- 9 valores separados por comas (del 0 al 9)
- El número `0` representa una celda vacía

2. **Ejecutar el programa con BFS**
```bash
python SudokuBFS.py
```

3. **Ejecutar el programa con DFS**
```bash
python SudokuDFS.py
```

---

## Interfaz Gráfica

Al ejecutar cualquiera de los programas:

- Se abrirá una ventana con el tablero original
- Presiona el botón **"Resolver Sudoku"** para iniciar la resolución
- El tablero se irá actualizando en tiempo real
- Al finalizar, se mostrará un mensaje con el **tiempo de ejecución**

---

## Ejemplo de Entrada (`sudoku_input.csv`)

```csv
7,0,0,8,0,3,0,0,5
0,0,5,0,7,0,3,0,0
0,4,0,0,6,0,0,2,0
5,0,0,0,0,0,0,0,1
0,6,4,0,0,0,2,9,0
2,0,0,0,0,0,0,0,6
0,7,0,0,2,0,0,8,0
0,0,8,0,3,0,6,0,0
6,0,0,4,0,9,0,0,7
```

---

## Resultados Esperados

- El Sudoku se resuelve correctamente
- La solución se muestra visualmente en la misma ventana
- Se imprime el tiempo total de ejecución en segundos

---

## Autor

Desarrollado por **César Omar Martín Rodríguez**  
Proyecto académico con fines educativos.

---

## Licencia

Este proyecto es de uso **libre para fines académicos**.  
Distribúyelo, estúdialo y mejóralo libremente ✨
