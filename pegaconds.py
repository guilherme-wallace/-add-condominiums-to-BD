import requests
import base64
import json
from dadosDeconexao import hostIntranet, urlIXC, tokenIXC

host = hostIntranet
url = urlIXC.format(host)
token = tokenIXC

payload = {
    'qtype': 'cliente_condominio.id',
    'query': '0',
    'oper': '>',
    'page': '1',
    'rp': '10000',
    'sortname': 'cliente_condominio.id',
    'sortorder': 'asc'
}

headers = {
    'ixcsoft': 'listar',
    'Authorization': 'Basic {}'.format(base64.b64encode(token).decode('utf-8')),
    'Content-Type': 'application/json'
}

response = requests.get(url, data=json.dumps(payload), headers=headers)

#print(response.text)

with open('pegacondsResultado.txt', 'w', encoding='utf-8') as f:
    f.write(response.text)

print("A resposta foi salva no arquivo 'pegacondsResultado.txt'")