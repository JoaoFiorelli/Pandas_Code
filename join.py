tab_count_p1_total = pd.merge(tab_count_2019, tab_count_2020, how = 'inner', on = 'month')
tab_count_total = pd.merge(tab_count_p1_total, tab_count_2021, how = 'outer', on = 'month')
new_columns = tab_count_total.columns.values
new_columns[0] = '2019'
new_columns[1] = '2020'
new_columns[2] = '2021'
tab_count_total.columns = new_columns