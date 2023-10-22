library(ggplot2)
library(tidyverse)

dados_dispersao <- read.csv("x")

# Calculate the correlation between Cobre and VALE3
correlation <- cor(dados_dispersao$Cobre, dados_dispersao$VALE3)

# Create a new column for color based on Cobre and VALE3 variables
dados_dispersao$color_variable <- ifelse(dados_dispersao$Cobre > dados_dispersao$VALE3, "Metais", "VALE3")

# Create the scatter plot with color and shape aesthetics, and a smooth curve
ggplot(dados_dispersao, aes(Cobre, VALE3, color = color_variable, shape = color_variable)) +
  geom_point(size = 3) +
  geom_smooth(method = "loess", se = FALSE, color = "black") +
  labs(title = "Gráfico de Dispersão",
       x = "Variações diárias dos Metais",
       y = "Variações diárias da VALE3") +
  scale_color_manual(values = c("Metais" = "red", "VALE3" = "blue")) +
  scale_shape_manual(values = c("Metais" = 16, "VALE3" = 17)) +
  guides(color = "none", shape = guide_legend(override.aes = list(color = c("red", "blue")))) +
  theme(legend.position = "bottom") +
  annotate("text", x = 0, y = max(dados_dispersao$VALE3), 
           label = paste("Correlação:", round(correlation, 2)),
           hjust = 0, vjust = 1, color = "purple")

