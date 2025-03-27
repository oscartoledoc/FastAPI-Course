from collections import deque


history = deque()

def visit_page(page):
    history.append(page)
    print(f"Visitaste: {page}")

def go_back():
    if history:
        history.pop()   # remove the last element
        actual_page = history[-1] # Last element
        print(f"Ahora estás en {actual_page}")
    else:
        print("No hay historial")

visit_page("Google")
visit_page("YouTube")
visit_page("Facebook")
visit_page("Twitter")
print("########################")
go_back()  # Volviendo de YouTube
go_back()  # Volviendo de Google
go_back()  # No hay historial

