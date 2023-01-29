select s.municipio_id_sus, lcm.nome, lcm.uf_sigla, s.periodo_codigo, s.indicadores_nome , s.nota_porcentagem, ir.meta
from dados_publicos.sisab_indicadores_municipios_equipes_validas s 
join listas_de_codigos.municipios lcm on s.municipio_id_sus = lcm.id_sus 
join previne_brasil.indicadores_regras ir on s.indicadores_regras_id  = ir.id 
where periodo_codigo = '2022.Q3' 
