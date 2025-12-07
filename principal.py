# import src.dicionarios
from src import dicionarios # Importacaoção de arquivo
from src.dicionarios import exemplo_basico # Importação de função


def main():
    dicionarios.solicitar_dados_alunos()
    # dicionarios.exemplo_basico() 
    # exemplo_basico()


if __name__ == "__main__":
    main()
