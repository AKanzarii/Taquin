import tkinter as tk
import time
import tkinter.messagebox
def get_blank(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)

def move_up(board):
    blank_row, blank_col = get_blank(board)
    if blank_row == 0:
        return None
    else:
        new_board = [row[:] for row in board]
        new_board[blank_row][blank_col], new_board[blank_row - 1][blank_col] = new_board[blank_row - 1][blank_col], new_board[blank_row][blank_col]
        return new_board

def move_down(board):
    blank_row, blank_col = get_blank(board)
    if blank_row == len(board) - 1:
        return None
    else:
        new_board = [row[:] for row in board]
        new_board[blank_row][blank_col], new_board[blank_row + 1][blank_col] = new_board[blank_row + 1][blank_col], new_board[blank_row][blank_col]
        return new_board

def move_left(board):
    blank_row, blank_col = get_blank(board)
    if blank_col == 0:
        return None
    else:
        new_board = [row[:] for row in board]
        new_board[blank_row][blank_col], new_board[blank_row][blank_col - 1] = new_board[blank_row][blank_col - 1], new_board[blank_row][blank_col]
        return new_board

def move_right(board):
    blank_row, blank_col = get_blank(board)
    if blank_col == len(board[0]) - 1:
        return None
    else:
        new_board = [row[:] for row in board]
        new_board[blank_row][blank_col], new_board[blank_row][blank_col + 1] = new_board[blank_row][blank_col + 1], new_board[blank_row][blank_col]
        return new_board

def get_successors(board):
    successors = []
    for move in [move_up, move_down, move_left, move_right]:
        puzzle = move(board)
        if puzzle is not None:
            successors.append(puzzle)
    return successors

def solve(board, depth_limit):
    stack = [(board, [])]
    visited = set()
    print(depth_limit)
    while stack:
        board, moves = stack.pop()
        visited.add(str(board))
        if board == [[1, 2, 3], [8, 0, 4], [7,6 , 5]]:
            return moves
        elif len(moves) < depth_limit:
            for successor in get_successors(board):
                if str(successor) not in visited:
                    new_moves = moves[:]
                    new_moves.append(successor)
                    stack.append((successor, new_moves))
    return None
def back_to_list(st):
    l1=[]
    l2=[]
    l3=[]
    lf=[]
    j=0
    for i in st:
        if i in ('0123654789'):
            x=int(i)
            if j <3:
                l1.append(x)
            elif j <6:
                l2.append(x)
            
            elif j <9:
                l3.append(x)
            j+=1
    lf.append(l1)
    lf.append(l2)
    lf.append(l3)
    print(lf)
    return lf
            
def solve_puzzle(state,d, buttons):
    solution_path = solve(state,d)
    animate_solution(solution_path, buttons)
    if solution_path is not None:
        tkinter.messagebox.showinfo("Iterations", f"It took {len(solution_path)} iterations to solve the puzzle.")


def update_buttons(state, buttons):
    for i, row in enumerate(state):
        for j, elem in enumerate(row):
            buttons[i][j].config(text=str(elem) if elem != 0 else "")

def animate_solution(solution_path, buttons):
    try:
        for state in solution_path:
            update_buttons(state, buttons)
            window.update()
            time.sleep(1)
    except:
        print("No solutions at this level")
def debut():
    lf=[]
    for i in range(3):
        l=[]
        print("donner la ligne "+str(i+1)+" de jeu")
        for j in range(3):
            while True:
                x=int(input("donner le num"+str(i*3+j+1)+":"))
                if x>-1 and x<10:
                    l.append(x)
                    break
                else:
                    continue
                                
        lf.append(l)

    return lf                
def create_gui(state,d):
    global window
    window = tk.Tk()
    window.title("jeux de taquin")

    buttons = [[None for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text=str(state[i][j]) if state[i][j] != 0 else "", width=10, height=5)
            button.grid(row=i, column=j)
            buttons[i][j] = button

    solve_button = tk.Button(window, text="Solve", command=lambda: solve_puzzle(state,d, buttons), width=10, height=2)
    solve_button.grid(row=3, column=1)

    window.mainloop()
puzzle = debut()
print(puzzle)
d=int(input("limite de recherche? "))
if __name__ == "__main__":
    solution_path = solve(puzzle,d)
    if solution_path is not None:
        create_gui(puzzle,d)
    else:
        tkinter.messagebox.showinfo("!","No solution found")


