from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro, cantidad_a_comprar:int):
        super().__init__(libro)
        self.cantidad_a_comprar = cantidad_a_comprar

    def es(self)->str:
        return f"El libro con titulo {self.libro} y isbn: {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"
