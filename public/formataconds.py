import json
import csv


pegacondsResultado = 'pegacondsResultado.txt'

with open(pegacondsResultado, 'r', encoding='utf-8') as arquivo:
    pegacondsResultadoConteudo = arquivo.read()


#--------------------------------------------------------------------------------------------------------------------------
respostaPegacondsResultado = f'{pegacondsResultadoConteudo}'

dados = json.loads(respostaPegacondsResultado)

registros = dados.get('registros', [])

registros_json = json.dumps(registros, indent=4, ensure_ascii=False)

condsRegistrados = 'condsRegistrados.json'

with open(condsRegistrados, 'w', encoding='utf-8') as arquivo:
    arquivo.write(registros_json)

print(f"Os registros foram salvos em {condsRegistrados}.")

#--------------------------------------------------------------------------------------------------------------------------
condsRegistradosRentrada = 'condsRegistrados.json'

with open(condsRegistradosRentrada, 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)

dadosFiltrados = [
    {
        "id": registro["id"],
        "condominio": registro["condominio"],
        "id_cidade": registro["id_cidade"],
        "endereco": registro["endereco"],
        "numero": registro["numero"],
        "cep": registro["cep"],
        "bairro": registro["bairro"]
    }
    for registro in dados_json
]

dadosFiltrados_json = json.dumps(dadosFiltrados, indent=4, ensure_ascii=False)

dadosFiltradosArquivo = 'dadosFiltrados.json'

with open(dadosFiltradosArquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(dadosFiltrados_json)

print(f"Os dados filtrados foram salvos em {dadosFiltradosArquivo}.")


#--------------------------------------------------------------------------------------------------------------------------
dadosFiltradosRentrada = 'dadosFiltrados.json'

with open(dadosFiltradosRentrada, 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)

arquivo_saida = 'dados.csv'

campos = ["id", "condominio", "id_cidade", "endereco", "numero", "cep", "bairro"]

with open(arquivo_saida, 'w', newline='', encoding='utf-8') as csvfile:
    escritor_csv = csv.DictWriter(csvfile, fieldnames=campos)

    escritor_csv.writeheader()

    for registro in dados_json:
        escritor_csv.writerow({campo: registro[campo] for campo in campos})

print(f"Os dados foram convertidos e salvos em {arquivo_saida}.")