import pandas as pd

caminho = r'piores_desempenhos_isf\2022Q3\2022Q3.csv'

df = pd.read_csv(caminho)
df['nota'] = (df['nota_porcentagem']/df['meta'])*10
df.loc[df['nota']>10,'nota']=10
#df.to_csv(r'piores_desempenhos_isf\2022Q3\isf_2022Q3.csv')
#print(df)

isf = r'piores_desempenhos_isf\2022Q3\isf_2022Q3_corrigir.csv'
df_isf = pd.read_csv(isf)
df_isf = df_isf.drop(columns=['peso','meta','nota','indicadores_nome','resultado','isf_calculado','isf_calculado_erro']).dropna().reset_index(drop=True)
df_isf['isf_calculado_final'] = df_isf['isf_calculado_final'].round(2)
df_isf = df_isf.sort_values(by='isf_calculado_final', ascending=True).reset_index(drop=True)
df_100 = df_isf.iloc[:100]
#df_100.to_csv(r'piores_desempenhos_isf\2022Q3\piores_desempenhos_2022Q3.csv')

print(df_100)   