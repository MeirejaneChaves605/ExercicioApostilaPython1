class Autor:
    """
    Representa um autor com nome e nacionalidade.
    """
    def __init__(self, nome: str, nacionalidade: str):
        self.nome = nome
        self.nacionalidade = nacionalidade

class Livro:
    """
    Representa um livro com título, ano e um autor.
    Esta classe demonstra o conceito de **agregação** com a classe Autor,
    pois um Autor pode existir independentemente de um Livro.
    """
    def __init__(self, titulo: str, ano: int, autor: Autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' ({self.ano}) por {self.autor.nome}"

class Biblioteca:
    """
    Representa uma biblioteca com nome e um catálogo de livros.
    Esta classe demonstra o conceito de **composição** com a classe Livro,
    pois a biblioteca é responsável por criar e gerenciar o ciclo de vida dos livros.
    Se a biblioteca for destruída, seus livros também serão (neste contexto).
    """
    def __init__(self, nome: str):
        self.nome = nome
        self._livros = {}

    def adicionar_livro(self, titulo: str, ano: int, autor: Autor):
        """Cria e adiciona um novo livro à biblioteca."""
        if titulo in self._livros:
            print(f"O livro '{titulo}' já existe na biblioteca.")
            return None
        livro = Livro(titulo, ano, autor)
        self._livros[titulo] = livro
        return livro

    def remover_livro(self, titulo: str):
        """Remove um livro da biblioteca."""
        if titulo in self._livros:
            del self._livros[titulo]
            print(f"Livro '{titulo}' removido com sucesso.")
        else:
            print(f"O livro '{titulo}' não foi encontrado.")

    def buscar_livro(self, titulo: str):
        """Busca um livro pelo título."""
        return self._livros.get(titulo)

    def listar_livros(self):
        """Lista todos os livros no catálogo."""
        if not self._livros:
            print("A biblioteca não possui livros.")
        else:
            print(f"\nCatálogo da {self.nome}:")
            for livro in self._livros.values():
                print(f"- {livro}")

class Usuario:
    """
    Representa um usuário com nome e uma associação a uma biblioteca.
    Esta classe demonstra o conceito de **associação** com a classe Biblioteca,
    pois um usuário pode estar associado a uma biblioteca, mas ambas as classes
    podem existir de forma independente.
    """
    def __init__(self, nome: str, biblioteca: Biblioteca):
        self.nome = nome
        self.biblioteca = biblioteca

    def pegar_livro_emprestado(self, titulo: str):
        """
        Pega um livro emprestado da biblioteca associada.
        Esta é uma demonstração de **dependência**, pois o método
        depende temporariamente da existência de um objeto Livro para
        sua execução, mas não mantém uma referência permanente a ele.
        """
        livro = self.biblioteca.buscar_livro(titulo)
        if livro:
            print(f"\n{self.nome} pegou o livro '{livro.titulo}' emprestado da {self.biblioteca.nome}.")
            return livro
        else:
            print(f"\n{self.nome} não conseguiu pegar o livro '{titulo}' emprestado, pois ele não foi encontrado.")
            return None

# --- Exemplo de Uso ---
# 1. Criação dos objetos
biblioteca_central = Biblioteca("Biblioteca Central de SP")
autor_machado = Autor("Machado de Assis", "Brasileiro")
autor_tolkien = Autor("J.R.R. Tolkien", "Britânico")

# 2. Composição: A biblioteca cria e gerencia os livros
biblioteca_central.adicionar_livro("Dom Casmurro", 1899, autor_machado)
biblioteca_central.adicionar_livro("O Senhor dos Anéis", 1954, autor_tolkien)

# 3. Associação: O usuário se associa à biblioteca
usuario_ana = Usuario("Ana", biblioteca_central)

# 4. Agregação: Livros e autores existem independentemente
# Podemos criar um autor e um livro sem que eles estejam
# imediatamente associados a uma biblioteca.
autor_dumas = Autor("Alexandre Dumas", "Francês")
livro_dumas = Livro("O Conde de Monte Cristo", 1844, autor_dumas)

# 5. Dependência: O usuário usa o objeto Livro temporariamente
livro_dom_casmurro = usuario_ana.pegar_livro_emprestado("Dom Casmurro")
livro_nao_existente = usuario_ana.pegar_livro_emprestado("Livro Inexistente")

# 6. Demonstração dos métodos
biblioteca_central.listar_livros()
biblioteca_central.remover_livro("Dom Casmurro")
biblioteca_central.listar_livros()