col_select = ["reason", "month"]

only_2019_count_df = only_2019_df.filter(items=col_select)
tab_count_2019 = only_2019_count_df.groupby("month").count()

only_2020_count_df = only_2020_df.filter(items=col_select)
tab_count_2020 = only_2020_count_df.groupby("month").count()

only_2021_count_df = only_2021_df.filter(items=col_select)
tab_count_2021 = only_2021_count_df.groupby("month").count()

tab_count_p1_total = pd.merge(tab_count_2019, tab_count_2020, how = 'inner', on = 'month')
tab_count_total = pd.merge(tab_count_p1_total, tab_count_2021, how = 'outer', on = 'month')
new_columns = tab_count_total.columns.values
new_columns[0] = 'quant_2019'
new_columns[1] = 'quant_2020'
new_columns[2] = 'quant_2021'
tab_count_total.columns = new_columns

# Normalizando pela base de clientes de cada mês

tab_count_total["quant_norm_2019"] = (tab_count_total["quant_2019"]*100)/(dados_accounts_df["2019"])
tab_count_total["quant_norm_2020"] = (tab_count_total["quant_2020"]*100)/(dados_accounts_df["2020"])
tab_count_total["quant_norm_2021"] = (tab_count_total["quant_2021"]*100)/(dados_accounts_df["2021"])

display(tab_count_total)
print("\n")

fig1, f1_axes = plt.subplots(ncols=2, nrows=1, figsize=(18,6))

f1_axes[0].plot(tab_count_total["quant_2019"], "ro--")
f1_axes[0].plot(tab_count_total["quant_2020"], "bo--")
f1_axes[0].plot(tab_count_total["quant_2021"], "go--")

f1_axes[0].set_title("Vista Mensal Absoluta", fontsize=16)
f1_axes[0].set_xlabel('mês', fontsize=14)
f1_axes[0].set_ylabel('Quantidade', fontsize=14)
f1_axes[0].grid(True)
f1_axes[0].legend([2019,2020,2021])

f1_axes[1].plot(tab_count_total["quant_norm_2019"], "ro--")
f1_axes[1].plot(tab_count_total["quant_norm_2020"], "bo--")
f1_axes[1].plot(tab_count_total["quant_norm_2021"], "go--")

f1_axes[1].set_title("Vista Mensal Normalizada", fontsize=16)
f1_axes[1].set_xlabel('mês', fontsize=14)
f1_axes[1].set_ylabel('% em relação a base', fontsize=14)
f1_axes[1].grid(True)
f1_axes[1].legend([2019,2020,2021])