import mysql.connector
import json
from route.dadosDeconexao import configuracao_dbIntranet

configuracao_db = configuracao_dbIntranet

conn = mysql.connector.connect(**configuracao_db)
cursor = conn.cursor(dictionary=True)

query = """
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
    t.technologyId = 4;
"""

cursor.execute(query)

results = cursor.fetchall()

cursor.close()
conn.close()

with open('resultadoConsultaBanco.json', 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)

print("Consulta realizada e resultado salvo em 'resultadoConsultaBanco.json'")