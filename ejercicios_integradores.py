def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 30
num2 = 47
resultado = mcd(num1, num2)
print(f"El MCD de {num1} y {num2} es {resultado}")


def mcm(a, b):
    return abs(a * b) // mcd(a, b)

num1 = 10
num2 = 12
resultado = mcm(num1, num2)
print(f"El MCM de {num1} y {num2} es {resultado}")

def contar_palabras(cadena):
    # Convertir la cadena a minúsculas y dividirla en palabras
    palabras = cadena.lower().split()
    print(palabras)
    # Crear un diccionario para almacenar la frecuencia de cada palabra
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

print(contar_palabras("caca pis pis culo caca pis"))

def palabra_mas_repetida(frecuencia):
    # Inicializar variables para la palabra más repetida y su frecuencia
    max_palabra = None
    max_frecuencia = 0
    for palabra, freq in frecuencia.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            max_palabra = palabra
    return max_palabra, max_frecuencia

frecuencia = contar_palabras("caca pis pis culo caca pis")
# print(palabra_mas_repetida(frecuencia))


def get_int():
    while True:
        try:
            valor = int(input("Introduce un número entero: "))
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

# Ejemplo de uso
numero = get_int()
print(f"El número introducido es: {numero}")

def get_int_recursivo():
    try:
        valor = int(input("Introduce un número entero: "))
        return valor
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
        return get_int_recursivo()

# Ejemplo de uso
numero_recursivo = get_int_recursivo()
print(f"El número introducido es: {numero_recursivo}")


class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Setters y getters para nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre:
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    # Setters y getters para edad
    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0 and edad <= 105:
            self.edad = edad
        else:
            raise ValueError("La edad debe ser un entero no negativo")

    # Setters y getters para DNI
    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 8 and dni[:-1].isdigit():
            self.dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de 8 dígitos")

    # Método mostrar
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    # Método es_mayor_de_edad
    def es_mayor_de_edad(self):
        return self.edad >= 18

# Ejemplo de uso
persona = Persona()
persona.set_nombre("Juan")
persona.get_nombre()
persona.set_edad(25)
persona.set_dni("12345678")
persona.mostrar()
print(f"Es mayor de edad: {persona.es_mayor_de_edad()}")


class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        if titular is not None:
            self.titular = titular
        else:
            raise ValueError("El titular de la cuenta es obligatorio")
        self.cantidad = cantidad

    # Setters y getters para titular
    def get_titular(self):
        return self.titular

    # No implementamos un setter para titular ya que no se permite cambiar el titular de la cuenta una vez creada

    # Setters y getters para cantidad
    def get_cantidad(self):
        return self.cantidad

    # No implementamos un setter directo para cantidad, ya que solo se puede modificar mediante ingresar o retirar

    # Método mostrar
    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()}")  # Mostrar el nombre del titular de la cuenta
        print(f"Cantidad: {self.cantidad}")

    # Método ingresar
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser un número positivo")

    # Método retirar
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser un número positivo")

# Ejemplo de uso
# Creamos una persona
titular = Persona("Juan", 30, "12345678A")

# Creamos una cuenta para esa persona
cuenta = Cuenta(titular, 1000.0)

# Mostramos los datos de la cuenta
cuenta.mostrar()

# Ingresamos dinero en la cuenta
cuenta.ingresar(500)

# Retiramos dinero de la cuenta
cuenta.retirar(200)

# Mostramos los datos de la cuenta actualizados
cuenta.mostrar()


class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    # Setters y getters para bonificacion
    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        if isinstance(bonificacion, (int, float)) and bonificacion >= 0:
            self.bonificacion = bonificacion
        else:
            raise ValueError("La bonificación debe ser un número no negativo")

    # Método es_titular_valido
    def es_titular_valido(self):
        return 18 <= self.titular.get_edad() < 25

    # Método retirar (sobrescribir)
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero de una Cuenta Joven")

    # Método mostrar (sobrescribir)
    def mostrar(self):
        print("Cuenta Joven")
        print(f"Titular: {self.titular.get_nombre()}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Bonificación: {self.bonificacion}%")

# Ejemplo de uso


# Creamos una persona
titular = Persona("Juan", 20, "12345678A")

# Creamos una cuenta joven para esa persona
cuenta_joven = CuentaJoven(titular, 1000.0, 10.0)

# Mostramos los datos de la cuenta joven
cuenta_joven.mostrar()

# Ingresamos dinero en la cuenta joven
cuenta_joven.ingresar(500)

# Intentamos retirar dinero de la cuenta joven
cuenta_joven.retirar(200)

# Mostramos los datos de la cuenta joven actualizados
cuenta_joven.mostrar()
