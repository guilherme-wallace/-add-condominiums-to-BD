import requests
import base64
import json
from route.dadosDeconexao import hostIntranet, urlIXC, tokenIXC

def obter_dados_condominio(arquivo_saida):
    # Configurações de conexão
    host = hostIntranet
    url = urlIXC.format(host)
    token = tokenIXC

    # Parâmetros da requisição
    payload = {
        'qtype': 'cliente_condominio.id',
        'query': '0',
        'oper': '>',
        'page': '1',
        'rp': '10000',
        'sortname': 'cliente_condominio.id',
        'sortorder': 'asc'
    }

    # Cabeçalhos da requisição
    headers = {
        'ixcsoft': 'listar',
        'Authorization': 'Basic {}'.format(base64.b64encode(token).decode('utf-8')),
        'Content-Type': 'application/json'
    }

    # Realiza a requisição
    response = requests.get(url, data=json.dumps(payload), headers=headers)

    # Salva a resposta no arquivo especificado
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(response.text)

    print(f"A resposta foi salva no arquivo '{arquivo_saida}'.")

