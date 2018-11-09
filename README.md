# informações gerais
Este e um projeto final da materia de Data Science (Catlógica de Santa Catarina - 2018/2).

# author
Daniel abraão Silva Costa <dascbh@gmail.com>

# objetivo
Montar uma análise completa que contemple desde a escolha do dataset até o desenvolvimento de um storytelling explicando os aspectos observados na amostra.

# tema escolhido
Mercado de acoes - Utilizei uma source uma base de dados propria que mantenho em outro projeto pssoal, aonde coleto dados diariamente da bolsa americana NASDAQ. Para efeitos dadicos e de simplificacao, disponibilizei apenas as cotacoes do periodo entre 01-10-2018 e 15-10-2018 e do ativo AMD (https://www.amd.com/en).

# url do dataset
https://s3-sa-east-1.amazonaws.com/danielabraao-01/quotes-AMD-01-to-15-OUT-2018.csv

# tarefa para a turma
1) Carregar o dataset diretamente via URL.
2) Criar um mecanismo de gráfico simples para mostrar a evolução do preço durante o dia.
3) Criar um gráfico simples com a evolução do preço ao longo do range de datas de todo dataset.

# link do post no medium
(Pendente)


-----


# sobre a analise
Esta analise tem como objetivo gerar um metodo de visualizacao grafica simples e funcional para as quotacoes diarias de um ativo da bolsa, mostrando a evolucao do preco ao longo do(s) periodo(s) e assim evidenciar potenciais relacoes ou comportamentos que o ativo venha a apresentar ao ter seus indicadores comparados.

Pode parecer uma atividade simples, porem quando se trata de mercado financeiro e em especial bolsa de valores americana (NASDAQ) nao e. Na internet sao pouquissimas as fontes de dados recentes e atualizados, alem de quase nao existirem ferramentas gratuitas que geram graficos on-demand para periodos passados.

# etapas do desenvolvimento da analise
1) obtencao, validacao e limpeza do dataset
2) construcao do recurso para selecao de data e range de horario
3) idexacao e preparacao dos dados para melhor utilizacao ao longo da analise
4) montagem dos graficos basicos (evolucao do preco, evolucao do volume e relacionamento preco vs volume)
5) aperfeicoamento dos graficos (inclusao de linha de tendencia, medias moveis, legenda, etc)
6) documentacao e conclusao

# conclusoes
grafico de evolucao do preco - funcinou dentro do esperado, em instantes e possivel visualizar a evolucao dos precos em um periodo parcial ou completo do dia. ao adicionar as medias movieis o grafico ficou ainda mais util e atraente.

grafico de volume - funcinou dentro do esperado, e possivel observar os picos de valores de volume ao longo do periodo. um fato observado foi que o dataset traz em cada linha de quotacao o valor acumulado do volume no periodo, ou seja, a somatoria do anterior mais o ultimo e nao o valor individual por quotacao.

relacao preco vs volume - fica evidente que existe uma relacao entre o volume e o preco, porem na forma que os dados estao apresentados nesta base de dados nao existe evidencia concreta garantido que os dois caminham juntos em movimentos de alta e baixa. o campo volume neste caso e cumulativo, ou seja, em cada cotacao voce tera um acrescimo sobre a quantidade apresentada na cotacao anterior, desta forma o volume sera sempre crescente. para que tenhamos uma visao mais concreta sobre esta relacao, seria necessario gerar uma coluna adicional de volume contemplando o valor da diferenca (ou quantidade acrescida por quotacao) e nao o somatorio, desta forma poderiamos verificar, por exemplo, se termos montantes de volume maior sendo acrescentados significa tambem maior variacao no preco. este pode ser um exercicio evolutivo para outra analise.
