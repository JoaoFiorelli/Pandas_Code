# Código para retirada de dados de um histograma abaixo de um limite (cut)

dados_df = dados_df.loc[ dados_df['city'] != "" ]
tab_final = dados_df.groupby("city").count().reset_index().sort_values(by=['freq'])
display(tab_final)

cut = 2

for row in tab_final.values:
  if row[1] < cut:
    selecion = tab_final.loc[tab_final["city"] == row[0]].reset_index()
    ex = selecion["index"]
    tab_final = tab_final.drop(ex)
