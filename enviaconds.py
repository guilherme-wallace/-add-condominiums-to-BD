import csv
import pymysql
from dadosDeconexao import configuracao_dbIntranet

configuracao_db = configuracao_dbIntranet

arquivo_csv = 'dados.csv'

nome_da_tabela = 'condominio'

conexao = pymysql.connect(**configuracao_db)

try:
    with conexao.cursor() as cursor:
        with open(arquivo_csv, 'r', encoding='utf-8') as csvfile:
            leitor_csv = csv.DictReader(csvfile)
            
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
        
        conexao.commit()

finally:
    conexao.close()

print("Dados inseridos com sucesso no banco de dados.")