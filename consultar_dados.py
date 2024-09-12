import mysql.connector
import json
from route.dadosDeconexao import configuracao_dbIntranet

def consultar_dados(arquivo_saida='src/resultadoConsultaBanco.json', tecnologia_id=4):
    # Conexão com o banco de dados
    configuracao_db = configuracao_dbIntranet
    conn = mysql.connector.connect(**configuracao_db)
    cursor = conn.cursor(dictionary=True)

    # Query SQL para buscar os dados
    query = f"""
    SELECT DISTINCT
        c.condominioId,
        c.condominio,
        c.cidadeId,
        c.endereco,
        c.numero,
        c.cep,
        c.bairro,
        t.technology
    FROM 
        condominio c
    JOIN 
        `group` g ON g.groupId = c.condominioId
    JOIN 
        block b ON b.groupId = g.groupId
    JOIN 
        technology t ON t.technologyId = b.technologyId
    WHERE 
        t.technologyId = {tecnologia_id};
    """

    # Executando a consulta
    cursor.execute(query)
    results = cursor.fetchall()

    # Fechando conexão com o banco de dados
    cursor.close()
    conn.close()

    # Salvando o resultado em um arquivo JSON
    with open(arquivo_saida, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print(f"Consulta realizada e resultado salvo em '{arquivo_saida}'.")

# Exemplo de chamada da função
consultar_dados()
