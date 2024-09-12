import csv
import pymysql
from route.dadosDeconexao import configuracao_dbIntranet

def inserir_dados_no_banco(arquivo_csv, nome_da_tabela):
    # Configuração da conexão com o banco de dados
    configuracao_db = configuracao_dbIntranet
    conexao = pymysql.connect(**configuracao_db)

    try:
        with conexao.cursor() as cursor:
            # Abrindo o arquivo CSV
            with open(arquivo_csv, 'r', encoding='utf-8') as csvfile:
                leitor_csv = csv.DictReader(csvfile)
                
                # Inserindo cada linha no banco de dados
                for linha in leitor_csv:
                    query = f"""
                    INSERT INTO {nome_da_tabela} (condominioId, condominio, cidadeId, endereco, numero, cep, bairro)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    cursor.execute(query, (
                        linha['id'],
                        linha['condominio'],
                        linha['id_cidade'],
                        linha['endereco'],
                        linha['numero'],
                        linha['cep'],
                        linha['bairro']
                    ))
            
            # Confirmando as inserções
            conexao.commit()

    finally:
        # Fechando a conexão com o banco de dados
        conexao.close()

    print("Dados inseridos com sucesso no banco de dados.")

# Exemplo de chamada da função
inserir_dados_no_banco()
