# Implemente o diagrama de classes abaixo.

# Classe Paciente
# Atributos:
# nome
# cpf
# idade
# Métodos:
# não possui
# Classe Medico
# Atributos:
# nome
# crm
# especializacao
# Métodos:
# não possui
# Classe Exame
# Atributos:
# medico: objeto da classe Medico
# paciente: objeto da classe Paciente
# descricao
# resultado
# Métodos:
# imprimir_exame(): exibe um relatório com os dados do exame (inclusive os dados do médico e do paciente)

class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade 
        
class Medico:
    def __init__(self, nome, crm, especilizacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especilizacao
        
class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado 
        
    def imprimir_exame(self):
        print(self.medico.nome) 
        print(self.medico.crm)
        print(self.medico.especializacao)
        print(self.paciente.nome)
        print(self.paciente.cpf)
        print(self.paciente.idade)
        print(self.descricao)
        print(self.resultado)
        
          
        
        

paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)

