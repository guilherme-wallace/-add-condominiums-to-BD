import csv
import pymysql
from route.dadosDeconexao import configuracao_dbIntranet

def inserir_dados_no_banco(arquivo_csv, nome_da_tabela):
    # Configuração da conexão com o banco de dados
    configuracao_db = configuracao_dbIntranet
    conexao = pymysql.connect(**configuracao_db)

    # Lista para armazenar os nomes dos condomínios inseridos
    condominios_inseridos = []

    try:
        with conexao.cursor() as cursor:
            # Abrindo o arquivo CSV
            with open(arquivo_csv, 'r', encoding='utf-8') as csvfile:
                leitor_csv = csv.DictReader(csvfile)

                # Inserindo cada linha no banco de dados somente se o condomínio não existir
                for linha in leitor_csv:
                    # Verifica se o condomínio já existe
                    query_verificacao = f"SELECT COUNT(*) FROM {nome_da_tabela} WHERE condominioId = %s"
                    cursor.execute(query_verificacao, (linha['id'],))
                    resultado = cursor.fetchone()

                    if resultado[0] == 0:  # Se o condomínio não existir
                        # Insere no banco de dados
                        query_insercao = f"""
                        INSERT INTO {nome_da_tabela} (condominioId, condominio, cidadeId, endereco, numero, cep, bairro)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """
                        cursor.execute(query_insercao, (
                            linha['id'],
                            linha['condominio'],
                            linha['id_cidade'],
                            linha['endereco'],
                            linha['numero'],
                            linha['cep'],
                            linha['bairro']
                        ))
                        # Adiciona o nome do condomínio à lista
                        condominios_inseridos.append(linha['condominio'])

            # Confirmando as inserções
            conexao.commit()

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

    finally:
        # Fechando a conexão com o banco de dados
        conexao.close()

    # Exibe os condomínios que foram inseridos
    if condominios_inseridos:
        resposta_for_log = "Condomínios inseridos no banco de dados:\n"
        resposta_for_log += "\n".join(f"- {condominio}" for condominio in condominios_inseridos)
        print ("Condomínio inserido no banco de dados:\n", resposta_for_log)
    else:
        resposta_for_log = "Nenhum novo condomínio foi inserido."
        print("Nenhum novo condomínio foi inserido.")

    return resposta_for_log

# Exemplo de chamada da função
# resposta = inserir_dados_no_banco('dados.csv', 'condominio')
# print(resposta)
