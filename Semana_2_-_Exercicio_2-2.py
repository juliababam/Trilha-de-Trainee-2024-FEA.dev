import pandas as pd
import matplotlib.pyplot as plt

# Dados fornecidos
dados_vendas = {
    "Data": [
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
        "2024-01-04",
        "2024-01-05",
        "2024-01-06",
        "2024-01-07",
        "2024-01-08",
        "2024-01-09",
        "2024-01-10",
        "2024-02-01",
        "2024-02-02",
        "2024-02-03",
        "2024-02-04",
        "2024-02-05",
        "2024-02-06",
        "2024-02-07",
        "2024-02-08",
        "2024-02-09",
        "2024-02-10",
        "2024-03-01",
        "2024-03-02",
        "2024-03-03",
        "2024-03-04",
        "2024-03-05",
        "2024-03-06",
        "2024-03-07",
        "2024-03-08",
        "2024-03-09",
        "2024-03-10",
    ],
    "Valor": [
        150.25,
        89.99,
        120.50,
        75.00,
        200.75,
        145.00,
        95.25,
        220.40,
        185.90,
        300.00,
        50.00,
        175.75,
        110.00,
        130.50,
        90.25,
        210.80,
        175.40,
        95.00,
        120.75,
        150.00,
        80.25,
        200.50,
        170.00,
        100.75,
        130.00,
        220.00,
        195.50,
        85.75,
        140.00,
        250.75,
    ],
}

# Criando o DataFrame
df_vendas = pd.DataFrame(dados_vendas)

# Convertendo coluna 'Data' para datetime
df_vendas["Data"] = pd.to_datetime(df_vendas["Data"])

# Adicionando coluna com dias da semana
df_vendas["Dia da semana"] = df_vendas["Data"].dt.day_name()

# Agrupamento por semana
df_semanas = df_vendas.groupby(df_vendas["Dia da semana"])["Valor"].sum()

# Gráfico
plt.figure(figsize=(10, 5))
df_semanas.plot(kind="bar")
plt.xlabel("Dia da semana")
plt.ylabel("Valor")
plt.title("Vendas por dia da semana durante o período")
plt.xticks(rotation=45)
plt.show()

# Exibindo o DataFrame
print(df_semanas)
