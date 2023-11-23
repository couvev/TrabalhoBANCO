from datetime import date
import json

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Cliente({self.cpf}, {self.nome})"

class Conta:
    def __init__(self, cpf, numero, saldo):
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
        self.extrato = []
    
    def adicionar_extrato(self, extrato):
        self.extrato.append(extrato)
    
    def __str__(self):
        return f"Conta({self.cpf}, {self.numero}, {self.saldo}, {self.extrato})"
    
    def obter_extrato(self):
        return self.extrato

class Extrato:
    def __init__(self, data, informacao):
        self.data = data
        self.informacao = informacao

class Historico:
    def __init__(self, data, informacao):
        self.data = data
        self.informacao = informacao