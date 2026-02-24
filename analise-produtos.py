# %%import pandas as pd

dados = {
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor", "Headset", "Cadeira Gamer"],
    "preco": [3500, 80, 150, 900, 250, 1200]
}

df = pd.DataFrame(dados)

media_preco = df["preco"].mean()
maior_preco = df["preco"].max()

print("Média de preços:", media_preco)
print("Produto mais caro:", maior_preco)

display(df)
