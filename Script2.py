def ingresar_elementos():
    elementos = input("Ingrese los elementos separados por espacios: ").strip().split()
    return [int(elemento) for elemento in elementos]

def contar_valles(recorrido):
    altitud = 0
    valles = 0
    
    for paso in recorrido:
        if paso == 'U':
            altitud += 1
            if altitud == 0:
                valles += 1
        else:
            altitud -= 1
    
    return valles

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo_actual):
        if valor <= nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.derecho)

    def preorden(self):
        return self._preorden_recursivo(self.raiz)

    def _preorden_recursivo(self, nodo):
        if nodo is None:
            return []
        return [nodo.valor] + self._preorden_recursivo(nodo.izquierdo) + self._preorden_recursivo(nodo.derecho)

    def inorden(self):
        return self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo):
        if nodo is None:
            return []
        return self._inorden_recursivo(nodo.izquierdo) + [nodo.valor] + self._inorden_recursivo(nodo.derecho)

    def postorden(self):
        return self._postorden_recursivo(self.raiz)

    def _postorden_recursivo(self, nodo):
        if nodo is None:
            return []
        return self._postorden_recursivo(nodo.izquierdo) + self._postorden_recursivo(nodo.derecho) + [nodo.valor]

# Función para contar montañas y valles
def contar_montanas_y_valles():
    recorrido_usuario = input("Ingrese la lista de pasos (U para arriba, D para abajo): ").strip().upper()
    numero_valles = contar_valles(recorrido_usuario)
    print("Número de valles:", numero_valles)

# Función para trabajar con árbol binario ordenado
def trabajar_con_arbol():
    arbol = ArbolBinarioOrdenado()
    elementos = ingresar_elementos()
    for elemento in elementos:
        arbol.agregar(elemento)

    print("Recorrido pre-orden:", arbol.preorden())
    print("Recorrido in-orden:", arbol.inorden())
    print("Recorrido post-orden:", arbol.postorden())

# Función principal del menú
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Contar montañas y valles")
        print("2. Trabajar con árbol binario ordenado")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            contar_montanas_y_valles()
        elif opcion == "2":
            trabajar_con_arbol()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el menú
menu()

