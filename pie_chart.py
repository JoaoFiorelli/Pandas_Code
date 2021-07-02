def func_label(pct, all_data):
    absolute = int(pct/100.*np.sum(all_data))
    # fazendo legenda do gráfico com % e valor absoluto
    return "{:.1f}%\n({:d})".format(pct, absolute)


label=list(tab_dados["var"])

fig1, ax1 = plt.subplots()
# Usar autopct='%1.1f%%' para mostrar apenas a porcentagem, sem o valor absoluto.
ax1.pie(tab_dados["var2"], labels=label, autopct=lambda pct: func_label(pct, tab_dados["var2"]),
        shadow=False, startangle=90)
ax1.axis('equal')
ax1.set_title("Gráfico de setores")
plt.show()
