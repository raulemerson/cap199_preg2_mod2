# Código Python de la cuarto solución

plt.figure(figsize=(12, 5))

# Boxplot de age
plt.subplot(1, 3, 1)
plt.boxplot(df["age"], vert=True)
plt.title("Boxplot de Age")
plt.ylabel("Age")

# Boxplot de bmi
plt.subplot(1, 3, 2)
plt.boxplot(df["bmi"], vert=True)
plt.title("Boxplot de BMI")
plt.ylabel("BMI")

# Boxplot de cholesterol_level
plt.subplot(1, 3, 3)
plt.boxplot(df["cholesterol_level"], vert=True)
plt.title("Boxplot de Cholesterol Level")
plt.ylabel("Cholesterol Level")

plt.tight_layout()
plt.show()
