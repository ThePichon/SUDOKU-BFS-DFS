# SudokuDFS.py con lectura desde CSV y GUI con Tkinter
import csv
import time
import tkinter as tk
from tkinter import messagebox

# Leer el tablero desde un archivo CSV
def leer_sudoku_desde_csv(ruta):
    with open(ruta, newline='') as file:
        reader = csv.reader(file)
        return [[int(num) for num in row] for row in reader]

# Determinar en qué grid (cuadro 3x3) está una coordenada
def cordenadaGrid(val):
    return val // 3

def celda(x, y, sudoku):
    GridCol = cordenadaGrid(x)
    GridFila = cordenadaGrid(y)
    Grid = []
    for fila in sudoku[GridFila *3: GridFila *3 + 3]:
        for col in fila[GridCol *3: GridCol *3 + 3]:
            Grid.append(col)
    return Grid

# Verificar si se puede colocar un número en una posición
def chichepuede(x, y, v, sudoku):
    if v in sudoku[y]:
        return False
    col = [fila[x] for fila in sudoku]
    if v in col:
        return False
    if v in celda(x, y, sudoku):
        return False
    return True

# Resolver Sudoku con DFS
solucion = None

def resolver(sudoku):
    global solucion
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for valor in range(1,10):
                    if chichepuede(x, y, valor, sudoku):
                        sudoku[y][x] = valor
                        resolver(sudoku)
                        sudoku[y][x] = 0
                return
    solucion = [fila[:] for fila in sudoku]

# Mostrar tablero en canvas
def mostrar_tablero(canvas, tablero):
    canvas.delete("all")
    for i in range(9):
        for j in range(9):
            x0, y0 = j * 50, i * 50
            x1, y1 = x0 + 50, y0 + 50
            canvas.create_rectangle(x0, y0, x1, y1, outline="black")
            if tablero[i][j] != 0:
                canvas.create_text(x0 + 25, y0 + 25, text=str(tablero[i][j]), font=("Arial", 16))

# Ejecutar y mostrar solución en GUI
def resolver_y_mostrar():
    global sudoku, canvas
    inicio = time.time()
    resolver(sudoku)
    fin = time.time()
    if solucion:
        mostrar_tablero(canvas, solucion)
        messagebox.showinfo("Sudoku Resuelto", f"¡Sudoku resuelto con DFS en {fin - inicio:.2f} segundos!")
    else:
        messagebox.showerror("Error", "No se pudo resolver el Sudoku")

# Ejecutar GUI
sudoku = leer_sudoku_desde_csv("sudoku_input.csv")
root = tk.Tk()
root.title("Sudoku DFS")
canvas = tk.Canvas(root, width=450, height=450)
canvas.pack()
mostrar_tablero(canvas, sudoku)
boton = tk.Button(root, text="Resolver Sudoku", command=resolver_y_mostrar)
boton.pack(pady=10)
root.mainloop()
