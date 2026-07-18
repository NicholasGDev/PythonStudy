class TestePython:
    
    
    def __init__(self, nome: str = "", idade: int = 0, logradouro: list = [], rg: str = "", cpf: str = "", telefone: str = ""):
        self.nome = nome
        self.idade = idade
        self.logradouro = logradouro
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        
    def digite_nome(self):
        self.nome = input("Digite o nome: ")

    def digite_idade(self):
        self.idade = int(input("Digite a idade: "))
    
    def digite_logradouro(self):
        self.logradouro = input("Digite o logradouro: ").split(",")

    def digite_rg(self):
        self.rg = input("Digite o RG: ")

    def digite_cpf(self):
        self.cpf = input("Digite o CPF: ")

    def digite_telefone(self):
        self.telefone = input("Digite o telefone: ")
        
    def exibir_dados(self):
        print(f"SEU Nome: {self.nome}")
        print(f"SUA Idade: {self.idade}")
        print(f"SEU Logradouro: {', '.join(self.logradouro)}")
        print(f"SEU RG: {self.rg}")
        print(f"SEU CPF: {self.cpf}")
        print(f"SEU Telefone: {self.telefone}")
        