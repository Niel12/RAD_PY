class Pessoa:
    def __init__(self, cpf, nome, nascimento, usa_oculos):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.usa_oculos = usa_oculos
class Marca:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.id = None
        self.sigla = sigla
class Veiculo:
    def __init__(self, placa, ano, cor, motor, proprietario):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.propietario = propietario 
