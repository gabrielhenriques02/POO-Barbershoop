from pessoa import Pessoa

class Administrador:
    def __init__(self, id, nome, celular, email, ativo, nivel_acesso, criado_em):

        super().__init__(id, nome, celular, email)

        self.ativo = ativo
        self.nivel_acesso = nivel_acesso
        self.criado_em = criado_em

    def cadastro_profissionais(self):

         print (f"Cliente {self.nome} cadastrado.")
    
    def gerenciar_servico(self):

        print() #editar
