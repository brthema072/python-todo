import os

class Tarefa:
    def __init__(self, nome, feito):
        self.nome = nome
        self.feito = feito

    def __str__(self):
        estado = "☑" if self.feito else "☐"
        return f"{estado} {self.nome}"

print("===== MEU GERENCIADOR DE TAREFAS =====")

print("Olá! Bem-vindo ao gerenciador.")

nome = input("Digite seu nome: ")

print(f"Olá, {nome}! Vamos organizar suas tarefas.\n")

menu = int(input("1. Adicionar tarefa\n2. Listar tarefas\n3. Concluir tarefa\n4. Remover tarefa\n0. Sair\n"))
tarefas = []

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

while menu != 0:
    limpar_terminal()

    if menu == 1:
        tarefa = input("Qual tarefa deseja cadastrar? ")
        tarefas.append(Tarefa(tarefa, False))

        
        menu = int(input("\n1. Adicionar tarefa\n2. Listar tarefas\n3. Concluir tarefa\n4. Remover tarefa\n0. Sair\n"))
    elif menu == 2:
        for indice, tarefa in enumerate(tarefas):
            print(f"{indice}. {tarefa}")
            
        menu = int(input("\n1. Adicionar tarefa\n2. Listar tarefas\n3. Concluir tarefa\n4. Remover tarefa\n0. Sair\n"))
    elif menu == 3:
        indiceTarefa = int(input("Digite o indice da tarefa que deseja concluir: "))
        tarefas[indiceTarefa].feito = True

        menu = int(input("\n1. Adicionar tarefa\n2. Listar tarefas\n3. Concluir tarefa\n4. Remover tarefa\n0. Sair\n"))
    elif menu == 4:
        indiceTarefa = int(input("Digite o indice da tarefa que deseja remover da lista: "))
        del tarefas[indiceTarefa]

        menu = int(input("\n1. Adicionar tarefa\n2. Listar tarefas\n3. Concluir tarefa\n4. Remover tarefa\n0. Sair\n"))
        