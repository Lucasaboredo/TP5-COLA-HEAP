# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks
from collections import deque

class Personaje:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __repr__(self):
        return f"{self.nombre} de {self.planeta}"

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

    def ver_primero(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        for personaje in self.items:
            print(personaje)

cola_personajes = Cola()

cola_personajes.encolar(Personaje('Luke Skywalker', 'Tatooine'))
cola_personajes.encolar(Personaje('Han Solo', 'Corellia'))
cola_personajes.encolar(Personaje('Leia Organa', 'Alderaan'))
cola_personajes.encolar(Personaje('Yoda', 'Dagobah'))
cola_personajes.encolar(Personaje('Jar Jar Binks', 'Naboo'))
cola_personajes.encolar(Personaje('Chewbacca', 'Kashyyyk'))
cola_personajes.encolar(Personaje('Wicket', 'Endor'))

#A mostrar los personajes del planeta Alderaan, Endor y Tatooine
print("Punto A")
def mostrar_personajes_planeta(cola, planetas):
    for personaje in cola.items:
        if personaje.planeta in planetas:
            print(personaje)

planeta_solicitados = ['Alderaan', 'Endor', 'Tatooine']
mostrar_personajes_planeta(cola_personajes, planeta_solicitados)

# Indicar el plantea natal de Luke Skywalker y Han Solo
print("Punto B")
def mostrar_nombres(cola, nombres):
    for personaje in cola.items:
        if personaje.nombre in nombres:
            print(f"{personaje.nombre} nacio en {personaje.planeta}")

nombres_solicitados = ['Luke Skywalker', 'Han Solo']
mostrar_nombres(cola_personajes, nombres_solicitados)

# Insertar un nuevo personaje antes del maestro Yoda
print("Punto C")

def insertar_personaje_antes_maestro(cola, personaje): 
    for i in range(len(cola.items)):
        if cola.items[i].nombre == 'Yoda':
            cola.items.insert(i, personaje)
            break
        elif i == len(cola.items) - 1:
            print("El maestro Yoda no se encuentra en la cola")

nuevo_personaje = Personaje('R2-D2', 'Naboo')
insertar_personaje_antes_maestro(cola_personajes, nuevo_personaje)
cola_personajes.mostrar()

#eliminar el personaje ubicado después de Jar Jar Binks
print("Punto D")

def eliminar_personaje(cola, personaje):
    for i in range(len(cola.items)):
        if cola.items[i].nombre == 'Chewbacca':
            cola.items.popleft(i, personaje)
            break
        elif i == len(cola.items) - 1:
            print("El personaje no se encuentra en la cola")

eliminar_personaje(cola_personajes, 'Chewbacca')
cola_personajes.mostrar()
