def ler_arquivo_xml(nome_xml):
    global tree
    import xml.etree.ElementTree as ET
    try:
        # carrega o xml
        tree = ET.parse(nome_xml)

    except FileNotFoundError:
        nome_xml += '.xml'

        # carrega o xml
        tree = ET.parse(nome_xml)

    finally:
        root = tree.getroot()
        #formata e declara o namespace
        namespace = root.tag.split('}')[0].strip('{')
        ns = {'nfe': namespace}

        #extrai as informações do evento
        info = {}

        inf_evento = root.find('.//nfe:infEvento', ns)
        det_evento = root.find('.//nfe:detEvento', ns)

        info['CNPJ'] = inf_evento.findtext('nfe:CNPJ', default='', namespaces=ns)
        info['chNFe'] = inf_evento.findtext('nfe:chNFe', default='', namespaces=ns)
        info['dhEvento'] = inf_evento.findtext('nfe:dhEvento', default='', namespaces=ns)
        info['descEvento'] = det_evento.findtext('nfe:descEvento', default='', namespaces=ns)
        info['xJust'] = det_evento.findtext('nfe:xJust', default='', namespaces=ns)
        info['nProt'] = det_evento.findtext('nfe:nProt', default='', namespaces=ns)

        #extrai informações do SEFAZ
        inf_retorno = root.find('.//nfe:retEvento/nfe:infEvento', ns)

        info['xMotivo'] = inf_retorno.findtext('nfe:xMotivo', default='', namespaces=ns)
        info['dhRegEvento'] = inf_retorno.findtext('nfe:dhRegEvento', default='', namespaces=ns)
        info['nProtRetorno'] = inf_retorno.findtext('nfe:nProt', default='', namespaces=ns)

        print(info)


