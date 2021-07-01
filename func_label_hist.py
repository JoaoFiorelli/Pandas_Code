# Adiciona rótulos nas barras de gráficos em barra.
# Exemplo de gráfico utilizado pela função:
# conjunto_dados = plt.barh(tab["var_1"], tab["var_2"], color="red")

def autolabel(conjunto_dados):
  for i in conjunto_dados:
    w = i.get_width()
    plt.annotate('{}'.format(w),
                 xy = (w, i.get_y()+i.get_height()/2),
                 xytext = (7,-3),
                 textcoords = 'offset points',
                 ha = 'center')
    
def autolabel_vertical(conjunto_dados):
  for i in conjunto_dados:
     h = i.get_height()
     plt.annotate('{}'.format(h),
                 xy = (i.get_x()+i.get_width()/2, h),
                 xytext = (0,3),
                 textcoords = 'offset points',
                 ha = 'center')