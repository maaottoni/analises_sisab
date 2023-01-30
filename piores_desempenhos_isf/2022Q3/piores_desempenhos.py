import pandas as pd

setembro = r'piores_desempenhos_isf\2022Q3\202209-setembro.csv'
outubro = r'piores_desempenhos_isf\2022Q3\202212-outubro.csv'
novembro = r'piores_desempenhos_isf\2022Q3\202211-novembro.csv'
dezembro = r'piores_desempenhos_isf\2022Q3\202212-dezembro.csv'

set2022 = pd.read_csv(setembro)
set2022 = set2022.rename(columns={'isf_nota':'isf_setembro'})
set2022 = set2022[['municipio_id_sus','uf_sigla','municipio_nome','isf_setembro']]

out2022 = pd.read_csv(outubro)
out2022 = out2022.rename(columns={'isf_nota':'isf_outubro'})
out2022 = out2022[['municipio_id_sus','isf_outubro']]

nov2022 = pd.read_csv(novembro)
nov2022 = nov2022.rename(columns={'isf_nota':'isf_novembro'})
nov2022 = nov2022[['municipio_id_sus','isf_novembro']]


dez2022 = pd.read_csv(dezembro)
dez2022 = dez2022.rename(columns={'isf_nota':'isf_dezembro'})
dez2022 = dez2022[['municipio_id_sus','isf_dezembro']]




df = set2022.merge(out2022, how='outer', on='municipio_id_sus')
df = df.merge(nov2022,how='outer',on='municipio_id_sus')
df = df.merge(dez2022,how='outer',on='municipio_id_sus')
df['media'] = (df['isf_setembro'] + df['isf_outubro'] + df['isf_novembro'] + df['isf_dezembro'])/4
df['municipio_uf'] = df['municipio_nome'] + '-' + df['uf_sigla']
df = df.sort_values(by='media', ascending=True).reset_index(drop=True)
df=df[['municipio_id_sus', 'uf_sigla','municipio_uf', 'isf_setembro',  'isf_outubro',  'isf_novembro',  'isf_dezembro',   'media' ]]
df_100 = df.iloc[:100]

#df = df[['municipio_id_sus','uf_sigla_x','municipio_nome_x','isf_setembro','isf_outubro']]

print(df_100)