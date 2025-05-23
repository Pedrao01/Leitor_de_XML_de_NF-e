from ler_xml import ler_arquivo_xml
from relatorio_excel import transformar_em_excel
try:
    nome_xml = str(input('nome do arquivo: '))
    valores = ler_arquivo_xml(nome_xml)
    transformar_em_excel(valores)
except NameError:
    print('nome do arquivo está errado!')

