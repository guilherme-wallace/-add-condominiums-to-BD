from public.obter_dados_condominio import *
from public.processar_dados_condominios import *
from public.inserir_dados_no_banco import *

#Pega os dados do comdominios do IXC
arquivo_saida_pega = 'src/pegacondsResultado.txt'
obter_dados_condominio(arquivo_saida_pega)

#Formata dos dados obtidos pelo IXC em Json
pegacondsResultado='src/pegacondsResultado.txt'
condsRegistrados='src/condsRegistrados.json'
dadosFiltradosArquivo='src/dadosFiltrados.json'
arquivo_saida_formata='src/dados.csv'

processar_dados_condominios(pegacondsResultado, condsRegistrados, dadosFiltradosArquivo, arquivo_saida_formata)


#Insere os condominios no banco de dados do Intranet
arquivo_csv='src/dados.csv'
nome_da_tabela='condominio'
inserir_dados_no_banco(arquivo_csv, nome_da_tabela)
