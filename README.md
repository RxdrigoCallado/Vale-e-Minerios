# Vale-e-Minérios
No código disponibilizado, usei as linguagens Python e R para mostrar a correlação e a oscilação entre do preço da ação da Vale e a variação no valor dos minérios negociados pela mesma (levando em consideração os pesos de cada minério vendido pela empresa). 
Python: baixa o preço e variação de cada minério, da ação da Vale e exportando-os para uma planilha Excel no local destino via GUI, podendo selecionar a importação dos dados selecionando quantos dias atrás a partir de sua data atual ou uma janela de tempo entre duas datas específicas.  
Para usar o código R e o gráfico, substitua o "x" no código R (dados_dispersao <- read.csv("x")) para o caminho do arquivo Excel (ex: "C:\\Users\\Usuario\\Desktop\\dados_dispersao.csv" com barras duplas) no código R.
R: utiliza os dados exportados via planilha Excel do código Python e os transforma em um gráfico de dispersão com curvas de tendência para análise de correlação dos preço e ver tendencias.
