from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.carro_compra import CarroCompras

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()
    
    def adicionar_libro_a_catalogo(self, isbn:str, titulo:str, precio:float, existencias:int)-> Libro:
        if isbn in self.catalogo:
            raise LibroExistenteError(LibroExistenteError)
        nuevo_libro = Libro(titulo, isbn, precio, existencias)
        self.catalogo = nuevo_libro
        return nuevo_libro
    
    def agregar_libro_a_carrito(self, libro: Libro, cantidad:int):
        if libro.existencias == 0:
            raise LibroExistenteError
        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError
        self.carrito.agregar_item(libro, cantidad)
        libro.existencias -= cantidad

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)




    # Defina metodo inicializador __init__

    # Defina metodo adicionar_libro_a_catalogo

    # Defina metodo agregar_libro_a_carrito

    # Defina metodo retirar_item_de_carrito
