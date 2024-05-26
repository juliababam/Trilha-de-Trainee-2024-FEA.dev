import pandas as pd

# Criação da tabela com eventos e datas
data = {
    "Evento": [
        "Domingo Sangrento",
        "Revolução de Fevereiro",
        "Abdicação do Czar Nicolau II",
        "Revolução de Outubro",
        "Tratado de Brest-Litovsk",
        "Início da Guerra Civil Russa",
        "Fundação da União Soviética",
    ],
    "Data": [
        "1905-01-22",
        "1917-03-08",
        "1917-03-15",
        "1917-11-07",
        "1918-03-03",
        "1918-06-01",
        "1922-12-30",
    ],
}

df = pd.DataFrame(data)

# Convertendo a coluna 'Data' para datetime
df["Data"] = pd.to_datetime(df["Data"])

# Define a data referência
data_referencia = pd.Timestamp("1905-01-22")

# Calculando a diferença de dias entre os eventos
df["Diferença (dias)"] = (df["Data"] - data_referencia).dt.days

# Formatando coluna data
df["Data"] = df["Data"].dt.strftime("%d/%m/%Y")

# Exibindo os resultados
print(df)
