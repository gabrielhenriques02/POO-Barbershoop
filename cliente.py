class Cliente (Pessoa)
    def __init__ (self, id, nome, celular, email):
        super().__init__(id, nome, celular, email)
        self.pontos_fidelidade = 0
        self.agendamentos = []

    def cadastro_cliente(self):
        print (f"Cliente {self.nome} cadastrado.")

    def solicitar_agendamento(self, agendamento):
        self.agendamentos.append(agendamento)

    def consultar_agendamento(self):
        return.self.agendamento
