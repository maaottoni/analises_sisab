import pandas as pd

caminho = r'C:\Users\maira\Impulso\analises_sisab\municipios_nao_atingiram_nenhuma_meta\2022Q3\2022Q3.csv'

df = pd.read_csv(caminho)
df['municipio_uf'] = df['nome'] + "-" + df['uf_sigla']


municipios = df['municipio_id_sus'].value_counts().index.to_list()


def analise_sisab (df:pd.DataFrame, municipios:list):
    colunas =['municipio_id_sus','nome', 'uf_sigla', 'periodo_codigo','indicadores_nome','nota_porcentagem','meta']
    df_consolidado = pd.DataFrame(columns=colunas)
    
    for municipio in municipios:

        df_municipio = df.loc[df['municipio_id_sus']==municipio]
        #print(df_municipio)
        df_fora_meta = df_municipio.loc[df_municipio['nota_porcentagem']<df_municipio['meta']]
        contagem = df_fora_meta['indicadores_nome'].count()

        if contagem == 7:
            df_consolidado = df_consolidado.append(df_municipio,ignore_index=True)
    
    #df_consolidado =df_consolidado[['municipio_id_sus','municipio_uf', 'periodo_codigo','indicadores_nome','nota_porcentagem','meta']]

    return df_consolidado


#data = analise_sisab(df, municipios)
#print(data['municipio_uf'].nunique())
#print(df)
#data.to_csv(r'C:\Users\maira\Impulso\analises_sisab\municipios_nao_atingiram_nenhuma_meta\2022Q3\2022Q3_municipios_nao_atingiram_nenhuma_meta.csv')

selecao = df.loc[df['municipio_id_sus']==421550]
print(selecao)