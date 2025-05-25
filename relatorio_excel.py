def transformar_em_excel(valores):
    import pandas as pd
    import os
    from openpyxl import load_workbook

    df = pd.DataFrame(valores)
    name_file = 'relatorio_xml.xlsx'

    #caso o arquivo exista
    if os.path.exists(name_file):
        df_excel = pd.read_excel(name_file)
        print('file open sucessefully!')
        new_df = pd.concat([df_excel, df], ignore_index=True)
        new_df.to_excel(name_file, index=False)
        
    #caso o arquivo não exista
    else:
        df.to_excel(name_file, index=False)

    wb = load_workbook(name_file)
    ws = wb.active
    #ajsuta a coluna de acordo com o tamaho da linha
    for col in ws.columns:
        len_max = max(len(str(cell.value)) if cell.value is not None else 0 for cell in col)
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = len_max + 2
    wb.save(name_file)
