import logging
from datetime import datetime
from public.obter_dados_condominio import obter_dados_condominio
from public.processar_dados_condominios import processar_dados_condominios
from public.inserir_dados_no_banco import inserir_dados_no_banco

# Configuração do logger
logging.basicConfig(filename='src/executa_script.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Início da execução do script.")

        # Pega os dados dos condomínios do IXC
        arquivo_saida_pega = 'src/pegacondsResultado.txt'
        obter_dados_condominio(arquivo_saida_pega)
        logging.info(f"Dados obtidos e salvos em {arquivo_saida_pega}.")

        # Formata os dados obtidos pelo IXC em JSON
        pegacondsResultado = 'src/pegacondsResultado.txt'
        condsRegistrados = 'src/condsRegistrados.json'
        dadosFiltradosArquivo = 'src/dadosFiltrados.json'
        arquivo_saida_formata = 'src/dados.csv'
        processar_dados_condominios(pegacondsResultado, condsRegistrados, dadosFiltradosArquivo, arquivo_saida_formata)
        logging.info(f"Dados formatados e salvos em {arquivo_saida_formata}.")

        # Insere os condomínios no banco de dados do Intranet
        arquivo_csv = 'src/dados.csv'
        nome_da_tabela = 'condominio'
        inserir_dados_no_banco(arquivo_csv, nome_da_tabela)
        logging.info("Condomínios inseridos no banco de dados com sucesso.")

    except Exception as e:
        logging.error(f"Erro durante a execução do script: {e}")

    logging.info("Execução do script concluída.")

if __name__ == "__main__":
    main()
