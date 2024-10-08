from tiendalibros.modelo.libro_error import LibroError

class LibroExistenteError(LibroError):
    def __init__(self, libro):
        super().__init__(libro)
    
    def es(self)->str:
        return f"El libro con titulo {self.libro} y isbn: {self.isbn} ya existe en el catálogo"

