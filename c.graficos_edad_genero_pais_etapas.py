# Código Python de la tercera solución

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Cancer', fontsize=16, fontweight='bold')

# Histograma de la columna/variable : age
axes[0, 0].hist(df["age"], bins=5, color="skyblue", edgecolor="black")
axes[0, 0].set_title("Distribucion de la edad")
axes[0, 0].set_xlabel("Edad")
axes[0, 0].set_ylabel("Frecuencia")
axes[0, 0].grid(True, alpha=0.3)

# Diagrama de tipo pie de la variable/columna : gender
genero_counts = df["gender"].value_counts()
axes[0, 1].pie(
    genero_counts,
    labels=genero_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[0, 1].set_title("Distribucion del genero")

# Distribucion de paises (Columna : country) en un diagrama de barras
pais_counts = df["country"].value_counts()
axes[1, 0].bar(pais_counts.index, pais_counts.values, color="salmon")
axes[1, 0].set_title("Pacientes por pais")
axes[1, 0].set_ylabel("Numero de pacientes")
axes[1, 0].tick_params(axis='x', rotation=90)

# Distribucion de la etapa del cancer (columna cancer_stage)  en un diagrama de barras.
etapa_counts = df["cancer_stage"].value_counts()
axes[1, 1].bar(etapa_counts.index, etapa_counts.values, color="lightgreen")
axes[1, 1].set_title("Distribucion de la etapa del cancer")
axes[1, 1].set_ylabel("Numero de observaciones")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
