# Filtrando dados por ano e mostrando o total de linhas

only_2019_df = dados_df.loc[dados_df["year"] == "2,019"]
only_2020_df = dados_df.loc[dados_df["year"] == "2,020"]
only_2021_df = dados_df.loc[dados_df["year"] == "2,021"]

total = dados_df.shape[0]
total_2019 = only_2019_df.shape[0]
total_2020 = only_2020_df.shape[0]
total_2021 = only_2021_df.shape[0]

display(only_2019_df)
display(only_2020_df)
display(only_2021_df)

print(f"\nO total desde 2019 foi: {total}")
print(f"\nO total em 2019 foi de {total_2019}.")
print(f"\nO total em 2020 foi de {total_2020}.")
print(f"\nO total em 2021 foi de {total_2021}.")
