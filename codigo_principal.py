from ler_xml import ler_arquivo_xml
try:
    nome_xml = str(input('nome do arquivo: '))
    ler_arquivo_xml(nome_xml)
except NameError:
    print('nome do arquivo está errado!')

