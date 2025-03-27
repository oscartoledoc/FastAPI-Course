class Node:
    def __init__(self, data):
        self.data = data  # Dato del nodo
        self.next = None  # Puntero al siguiente nodo

class LinkedList:
    def __init__(self):
        self.head = None  # Primer nodo (cabeza)
        self.tail = None  # Último nodo (cola)

# To added to the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Crea un nuevo nodo
        new_node.next = self.head  # Conecta el nuevo nodo con la antigua cabeza
        self.head = new_node  # El nuevo nodo se convierte en la cabeza

# To added to the end of the list
    def append_final(self, data):
        new_node = Node(data)
        
        if not self.head:  # Si la lista está vacía
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # El último nodo actual apunta al nuevo nodo
            self.tail = new_node       # Se actualiza la cola al nuevo nodo

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Uso
ll = LinkedList()
ll.append_final(1)
ll.append_final(2)
ll.append_final(3)
ll.insert_at_beginning(10)
ll.print_list()
