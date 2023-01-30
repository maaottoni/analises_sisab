select municipio_id_sus, uf_sigla, municipio_nome, isf_nota, periodo_data_inicio
from dados_publicos.egestor_financiamento_desempenho_isf 
where periodo_data_inicio = '2022-09-01'