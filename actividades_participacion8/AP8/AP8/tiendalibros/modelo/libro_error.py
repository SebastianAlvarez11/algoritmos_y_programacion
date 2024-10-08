from tiendalibros.modelo.libro import Libro


class LibroError(Exception):
    def __init__(self, libro: Libro, isbn: str):
        self.libro = libro
        self.isbn = isbn
