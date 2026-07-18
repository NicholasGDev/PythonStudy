from firstStudy.TestePython import TestePython

class Main:
    
    def __init__(self):
        self.teste = TestePython()

    def run(self):
        teste = TestePython()
        while teste.nome == "" or teste.idade == 0 or teste.logradouro == [] or teste.rg == "" or teste.cpf == "" or teste.telefone == "":
            print("\n--- Digite os dados do teste ---")
            teste.digite_nome()
            teste.digite_idade()
            teste.digite_logradouro()
            teste.digite_rg()
            teste.digite_cpf()
            teste.digite_telefone()
            teste.exibir_dados()

if __name__ == "__main__":
    main = Main()
    main.run()