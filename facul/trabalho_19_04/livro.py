class Livro: 
    def __init__(self, titulo, autor, isbn, genero, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.disponivel = disponivel
    
    def getTitulo(self):
        return self.titulo
    
    def setTitulo(self, titulo):
        self.titulo = titulo
    
    def getAutor(self):
        return self.autor
    
    def setAutor(self, autor):
        self.autor = autor
    
    def getIsbn(self):
        return self.isbn
    
    def setIsbn(self, isbn):
        self.isbn = isbn
    
    def getGenero(self):
        return self.genero
    
    def setGenero(self, genero):
        self.genero = genero
    
    def getDisponivel(self):
        return self.disponivel
    
    def setDisponivel(self, disponivel):
        self.disponivel = disponivel
        