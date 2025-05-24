def transformar_em_excel(valores):
    import pandas as pd
    import os
    df = pd.DataFrame(valores)
    name_file = 'relatorio_xml.xlsx'
    if os.path.exists(name_file):
        df_excel = pd.read_excel(name_file)
        print('file open sucessefully!')
        # new_date = pd.DataFrame(valores)
        new_df = pd.concat([df_excel, df], ignore_index=True)
        new_df.to_excel(name_file, index=False)
    else:
        df.to_excel(name_file, index=False)

