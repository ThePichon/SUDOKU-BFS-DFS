# SudokuBFS.py con lectura desde CSV y GUI con Tkinter
import csv
from collections import deque
import time
import tkinter as tk
from tkinter import messagebox

# Leer el tablero desde un archivo CSV
def leer_sudoku_desde_csv(ruta):
    with open(ruta, newline='') as file:
        reader = csv.reader(file)
        return [[int(num) for num in row] for row in reader]

# Comprobar si se puede colocar el número en la posición
def valido(sudoku, fila, col, val):
    for i in range(9):
        if sudoku[fila][i] == val or sudoku[i][col] == val:
            return False
    GFila, GCol = fila // 3 * 3, col // 3 * 3
    for y in range(3):
        for x in range(3):
            if sudoku[GFila + y][GCol + x] == val:
                return False
    return True

# Encontrar la posición vacía
def vacio(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                return (y, x)
    return None

# Resolver con BFS
def BFS(sudoku):
    cola = deque()
    cola.append(sudoku)
    while cola:
        curr_sudoku = cola.popleft()
        pos = vacio(curr_sudoku)
        if not pos:
            return curr_sudoku
        for val in range(1, 10):
            if valido(curr_sudoku, pos[0], pos[1], val):
                NSudoku = [fila[:] for fila in curr_sudoku]
                NSudoku[pos[0]][pos[1]] = val
                cola.append(NSudoku)
    return None

# Mostrar el tablero en la GUI
def mostrar_tablero(canvas, tablero):
    canvas.delete("all")
    for i in range(9):
        for j in range(9):
            x0, y0 = j * 50, i * 50
            x1, y1 = x0 + 50, y0 + 50
            canvas.create_rectangle(x0, y0, x1, y1, outline="black")
            if tablero[i][j] != 0:
                canvas.create_text(x0 + 25, y0 + 25, text=str(tablero[i][j]), font=("Arial", 16))

# Función para ejecutar la resolución y actualizar GUI
def resolver_y_mostrar():
    global sudoku, canvas
    inicio = time.time()
    solucion = BFS(sudoku)
    fin = time.time()
    if solucion:
        mostrar_tablero(canvas, solucion)
        messagebox.showinfo("Sudoku Resuelto", f"\u00a1Sudoku resuelto con BFS en {fin - inicio:.2f} segundos!")
    else:
        messagebox.showerror("Error", "No se pudo resolver el Sudoku")

# Cargar tablero y mostrar GUI
sudoku = leer_sudoku_desde_csv("sudoku_input.csv")
root = tk.Tk()
root.title("Sudoku BFS")
canvas = tk.Canvas(root, width=450, height=450)
canvas.pack()
mostrar_tablero(canvas, sudoku)
boton = tk.Button(root, text="Resolver Sudoku", command=resolver_y_mostrar)
boton.pack(pady=10)
root.mainloop()
