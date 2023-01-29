import pandas as pd

caminho = r'C:\Users\maira\Impulso\analises_sisab\municipios_nao_atingiram_nenhuma_meta\2022Q3\2022Q3.csv'

df = pd.read_csv(caminho)

municipios = df['municipio_id_sus'].value_counts().index.to_list()


def analise_sisab (df:pd.DataFrame, municipios:list):
    for municipio in municipios:

        colunas =['municipio_id_sus','nome', 'uf_sigla', 'periodo_codigo','indicadores_nome','nota_porcentagem','meta']
        df_consolidado = pd.DataFrame(columns=colunas)

        df_municipio = df.loc[df['municipio_id_sus']==municipio]
        df_fora_meta = df_municipio.loc[df_municipio['nota_porcentagem']<df_municipio['meta']]
        contagem = df_fora_meta['indicadores_nome'].count

        if contagem == 7:
            df_consolidado = df_consolidado.append(df_municipio,ignore_index=True)

    return df_consolidado


data = analise_sisab(df, municipios)
print(data)