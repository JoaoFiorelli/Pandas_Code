# Código para realizar um histograma horizontal

col_select = ["month", "var"]

var_dados_df = dados_df.filter(items=col_select)
var_dados_df = var_dados_df.loc[ var_dados_df["var"] != "" ]
tab_count = var_dados_df.groupby("var").count().reset_index().sort_values(by=["month"])
display(tab_count)

plt.figure(figsize=(9, 10))
plt.barh(tab_count["var"], tab_count["month"], color="red")
plt.title("Histograma da variável X", fontsize=14)
plt.ylabel("Variável X", fontsize=14)
plt.xlabel("Quantidade da variável X", fontsize=14)