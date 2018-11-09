# informações gerais
Este e um projeto final da matéria de Data Science (Católica de Santa Catarina - 2018/2).

# autor
Daniel abraão Silva Costa <dascbh@gmail.com>

# objetivo
Montar uma análise completa que contemple desde à escolha do dataset até o desenvolvimento e storytelling explicando os aspectos observados na amostra.

# tema escolhido
Mercado de ações - Utilizei como source uma base de dados própria que mantenho em outro projeto pessoal, aonde coleto dados diariamente da bolsa americana NASDAQ. Para efeitos didáticos e de simplificação, disponibilizei apenas as cotações do período entre 01-10-2018 e 15-10-2018 e do ativo AMD (https://www.amd.com/en).

# url do dataset
https://s3-sa-east-1.amazonaws.com/danielabraao-01/quotes-AMD-01-to-15-OUT-2018.csv

# tarefa para a turma
1) Carregar o dataset diretamente via URL.
2) Criar um mecanismo de gráfico simples para mostrar a evolução do preço durante o dia.
3) Criar um gráfico simples com a evolução do preço ao longo do range de datas de todo dataset.

# link do post no medium
(Pendente)


-----


# sobre a análise
Esta análise tem como objetivo gerar um método de visualização gráfica simples e funcional para as quotações diárias de um ativo da bolsa, mostrando a evolução do preço ao longo do(s) periodo(s) e assim evidenciar potenciais relações ou comportamentos que ele venha apresentar ao ter seus indicadores comparados.

Pode parecer uma atividade simples, porém quando se trata de mercado financeiro e em especial bolsa de valores americana (NASDAQ) é bastante difícil ter esse tipo de informação/visualização. Na internet, são pouquíssimas as fontes de dados atualizados, além de quase não existirem ferramentas gratuitas que geram gráficos on-demand para períodos passados.

# etapas do desenvolvimento
1) obtenção, validação e limpeza do dataset
2) construção do recurso para seleção de data e range de horário
3) indexação e preparação dos dados para melhor utilização ao longo da análise
4) montagem dos gráficos básicos (evolução do preço, evolução do volume e relacionamento preço vs volume)
5) aperfeicoamento dos gráficos (inclusão de linha de tendência, médias móveis, legenda, etc)
6) documentação e conclusão

# concluões
gráfico de evolução do preço - funcinou dentro do esperado, em instantes é possível visualizar a evolução dos preços em um período parcial ou completo do dia. ao adicionar as médias movieis o grafico ficou ainda mais útil e atraente.

gráfico de volume - funcinou dentro do esperado, é possivel observar os picos de valores de volume ao longo do período. um fato observado foi que o dataset traz em cada linha de cotação o valor acumulado do volume no período, ou seja, a somatória do anterior mais o último, e não o valor individual por cotação.

relação preço vs volume - fica evidente que existe uma relação entre o volume e o preço, porém na forma que os dados estão apresentados na base de dados, não existe evidência concreta garantido que os dois caminham juntos em movimentos de alta e baixa. o campo volume neste caso é cumulativo, ou seja, em cada cotação existirá um acréscimo sobre a quantidade apresentada na cotacão anterior, desta forma o volume será sempre crescente. para que tenhamos uma visão mais concreta sobre essa relação, seria necessário gerar uma coluna adicional de volume contemplando o valor da diferença (ou quantidade acrescida por cotação) e não o acumulado, desta forma poderíamos verificar, por exemplo, se montantes de volume maior sendo acrescentados significa também maior variação no preço. este pode ser um exercicio evolutivo para outra analise.
