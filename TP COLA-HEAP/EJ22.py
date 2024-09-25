from collections import deque

class PersonajeMCU:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

    def __repr__(self):
        return f"{self.nombre_personaje}, {self.nombre_superheroe}, {self.genero}"

class Cola:
    def __init__(self):
        self.items = deque()

    def encolar(self, personaje):
        self.items.append(personaje)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        for personaje in self.items:
            print(personaje)

    def tamano(self):
        return len(self.items)
    
# Crear la cola de personajes MCU
cola_mcu = Cola()

cola_mcu.encolar(PersonajeMCU('Tony Stark', 'Iron Man', 'M'))
cola_mcu.encolar(PersonajeMCU('Steve Rogers', 'Capitán América', 'M'))
cola_mcu.encolar(PersonajeMCU('Natasha Romanoff', 'Black Widow', 'F'))
cola_mcu.encolar(PersonajeMCU('Carol Danvers', 'Capitana Marvel', 'F'))
cola_mcu.encolar(PersonajeMCU('Scott Lang', 'Ant-Man', 'M'))
cola_mcu.encolar(PersonajeMCU('Sam Wilson', 'Falcon', 'M'))

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
print("PUNTO A")
def nombre_personaje_de_superheroe(cola, nombre_superheroe):
    for personaje in cola.items:
        if personaje.nombre_superheroe == nombre_superheroe:
            print(f"El nombre del personaje de {nombre_superheroe} es {personaje.nombre_personaje}")

nombre_personaje_de_superheroe(cola_mcu, 'Capitana Marvel')

# b. Mostrar los nombre de los superhéroes femeninos
print("PUNTO B")
def femeninas(cola, genero):
    for personaje in cola.items:
        if personaje.genero == genero:
            print(f"Son mujeres los personajes {personaje.nombre_personaje}")

femeninas(cola_mcu, 'F')

# c. Mostrar los nombres de los personajes masculinos
print("PUNTO C")
def Masculinos(cola, genero):
    for personaje in cola.items:
        if personaje.genero == genero:
            print(f"Son hombres los personajes {personaje.nombre_personaje}")

Masculinos(cola_mcu, 'M')

# d. Determinar el nombre del superhéroe del personaje Scott Lang
print("PUNTO D")
def super_scot(cola, nombre_superheroe):
    for personaje in cola.items:
        if personaje.nombre_personaje == nombre_superheroe:
            print(f"El superhéroe del personaje {nombre_superheroe} es {personaje.nombre_superheroe}")

super_scot(cola_mcu, "Scott Lang")

# e. Mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S
print("PUNTO E")
def letrainicial(cola, letra):
    for personaje in cola.items:
        if personaje.nombre_personaje.startswith(letra) or personaje.nombre_superheroe.startswith(letra):
            print(personaje)

letrainicial(cola_mcu, 'S')


# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes
print("PUNTO F")
def buscar_nombre(cola, nombre_superheroe):
    for i in range(len(cola.items)):  
        if cola.items[i].nombre_personaje == nombre_superheroe:  
            print(f"{nombre_superheroe} se encuentra en la cola")
            return  
    print(f"{nombre_superheroe} no se encuentra en la cola.") 

buscar_nombre(cola_mcu, "Carol Danvers")

# HEAP
# 5. hundir(montículo, índice). Hunde el dato almacenado en el montículo desde el índice indicado
# hasta que cumpla la propiedad de orden
def hundir(self, i):
        n = len(self.heap)
        while i * 2 <= n - 1:
            j = self.heap[i * 2]
            if i * 2 + 1 < n and self.heap[i * 2 + 1] > j:
                j = self.heap[i * 2 + 1]
            if self.heap[i] < j:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
