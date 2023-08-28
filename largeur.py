from queue import Queue
import tkinter as tk
import time
import tkinter.messagebox
goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)

# Fonction pour trouver le chemin optimal de la case vide du début jusqu'à la fin
def taquin_larg(puzzle):
    # Convertir la puzzle en tuple pour une meilleure performance
    puzzle = tuple(puzzle)
    # La configuration finale que nous essayons d'atteindre
    goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    # Définir la file pour la recherche en largeur
    q = Queue()
    # Ajouter le puzzle initial à la file
    q.put((puzzle, []))
    # Déjà visité des états
    visited = set()
    visited.add(puzzle)

    while not q.empty():
        # Obtenir le prochain élément de la file
        (state, path) = q.get()

        # Si nous avons atteint l'état final, renvoyer le chemin
        if state == goal:
            return path

        # Déplacer les cases du puzzle
        zero_pos = state.index(0)
        for move in moves(zero_pos):
            new_state = list(state)
            new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
            new_state = tuple(new_state)

            # Si nous n'avons pas encore visité cet état, l'ajouter à la file
            if new_state not in visited:
                q.put((new_state, path + [move]))
                visited.add(new_state)

    # Si nous ne trouvons pas de solution, renvoyer None
    return None

# Fonction pour trouver les mouvements possibles pour une case donnée
def moves(position):
    moves = []
    if position % 3 > 0:
        moves.append(position - 1)
    if position % 3 < 2:
        moves.append(position + 1)
    if position // 3 > 0:
        moves.append(position - 3)
    if position // 3 < 2:
        moves.append(position + 3)
    return moves
def make(state,path):
    l=[]
    t=state[:]
    for i in path:
        li=list(t)[:]
        x=li.index(0)
        print(x)
        li[i],li[x]=li[x],li[i]
        print(li)
        t=tuple(li)
        l.append(t)
    return l
def update_buttons(state, buttons):
    for i in range(9):
        j=i%3
        z=i//3
        elem=state[i]
        buttons[z][j].config(text=str(elem) if elem != 0 else "")
def animate_solution(solution_path, buttons):
    for state in solution_path:
        if state is not(None):
            update_buttons(state, buttons)
            window.update()
            time.sleep(1)
def solve(state, buttons):
    solution_path = make(puzzle,taquin_larg(state))
    animate_solution(solution_path, buttons)
    tkinter.messagebox.showinfo("Iterations", f"It took {len(solution_path)} iterations to solve the puzzle.")

def create_gui(state):
    global window
    window = tk.Tk()
    window.title("jeux de taquin")

    buttons = [[None for _ in range(3)] for _ in range(3)]

    for i in range(9):
        button = tk.Button(window, text=str(state[i]) if state[i] != 0 else "", width=10, height=5)
        j=i%3
        z=i//3
        button.grid(row=z, column=j)
        buttons[z][j] = button

    solve_button = tk.Button(window, text="Solve", command=lambda: solve(state, buttons), width=10, height=2)
    solve_button.grid(row=3, column=1)

    window.mainloop()
def debut():
    lf=[]
    while True:
        for i in range(3):
            print("donner la ligne "+str(i+1)+" de jeu")
            for j in range(3):
                x=int(input("donner le num"+str(i*3+j+1)+":"))
                lf.append(x)
        try:
            x=lf.index(0)
            break
        except:
            continue
    return lf;
def is_solvable(state):
    inversions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[j] and state[i] and state[i] > state[j]:
                inversions += 1
    blank_index = state.index(0)
    if len(state) % 2 == 0:
        return (inversions + blank_index // int(len(state) ** 0.5)) % 2 == 0
    else:
        return inversions % 2 == 0
puzzle = tuple(debut())
if __name__ == "__main__":
    solution_path = taquin_larg(puzzle)
    if solution_path is not None:
        create_gui(puzzle)
    else:
        tkinter.messagebox.showinfo("!","No solution found")

