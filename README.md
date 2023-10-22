# Vale-e-Minerios
No codigo disponibilizado, usei as linguagens Python e R para mostrar a correlação e a oscilacao entre do preço da ação da Vale e a variação no valor dos minerios negociados pela mesma (levando em consideração os pesos de cada minerio vendido da empresa). 
Python: baixa o preco e variação de cada minerio, da ação da Vale e exportando-os para um planilha excel no local destino via GUI, podendo selecionar a importação dos dados selecinando quantos dias atras a partir de sua data atual ou uma janela de tempo entre duas datas especificas.  
Para usar o codigo R e o grafico, substitua o "x" no codigo R (dados_dispersao <- read.csv("x")) para o caminho do arquivo excel (ex: "C:\\Users\\Usuario\\Desktop\\dados_dispersao.csv" com barras duplas) no codigo R.
R: ultiliza os dados exportados via planilha excel do codigo Python e os tranforma em um grafico de dispersao com curvas de tendencia para analise de correlação dos preço e ver tendencias.
