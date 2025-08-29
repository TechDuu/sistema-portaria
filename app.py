import csv
import os

ARQUIVO = "visitantes.csv"

def inicializar_arquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["Nome", "Documento", "Apartamento/Destino"])

def registrar_visitante():
    nome = input("Nome do visitante: ")
    documento = input("Documento (RG/CPF): ")
    destino = input("Apartamento/Destino: ")

    with open(ARQUIVO, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([nome, documento, destino])

    print(f"\n✅ Visitante {nome} registrado com sucesso!\n")

def listar_visitantes():
    print("\n📋 Lista de Visitantes Registrados:\n")
    with open(ARQUIVO, mode="r", encoding="utf-8") as f:
        leitor = csv.reader(f)
        for i, linha in enumerate(leitor):
            if i == 0:
                continue  # pula cabeçalho
            print(f"- {linha[0]} | Documento: {linha[1]} | Destino: {linha[2]}")
    print()

def menu():
    while True:
        print("=== Sistema de Controle de Portaria ===")
        print("1. Registrar Visitante")
        print("2. Listar Visitantes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_visitante()
        elif opcao == "2":
            listar_visitantes()
        elif opcao == "3":
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    inicializar_arquivo()
    menu()
