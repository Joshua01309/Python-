import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos_problemas_graficos\pedos.csv')
sns.lineplot(x = 'fecha', y = 'pedos', data = df)

# punto maximo
plt.plot('01-09', 17, 'o')
plt.show()