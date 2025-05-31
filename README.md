# 📄 Leitor de XML de NF-e

Este projeto automatiza a leitura de arquivos XML de Nota Fiscal Eletrônica (NF-e), extraindo informações relevantes e gerando relatórios organizados em planilhas Excel.  
Ideal para empresas e profissionais que precisam processar grandes volumes de notas fiscais de forma rápida e prática.

---

## 🚀 Tecnologias utilizadas

- Python
- xml.etree.ElementTree (leitura de XML)
- pandas (manipulação de dados)
- openpyxl (exportação para Excel)
- os, glob (automação de arquivos)

---

## 💡 Funcionalidades

- ✅ Leitura automática de múltiplos arquivos XML
- ✅ Extração de dados como:
  - CNPJ do emitente
  - Nome do emitente
  - Valor total da nota
  - Data de emissão
  - Itens e produtos
- ✅ Geração de planilha Excel com os dados organizados
- ✅ Estrutura modular com scripts separados
- ✅ Interface simples por linha de comando

---

## ▶️ Como executar

```bash
# 1. Clone o repositório
git clone https://github.com/Pedrao01/Leitor_de_XML_de_NF-e.git

# 2. Acesse a pasta do projeto
cd Leitor_de_XML_de_NF-e

# 3. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Execute o script principal
python codigo_principal.py
