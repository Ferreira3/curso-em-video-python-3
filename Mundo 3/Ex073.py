#Exercício Python 73:
#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Vasco.

seriea = ("Flamengo", "Cruzeiro", "Palmeiras", "Mirassol",
          "Bahia", "Botafogo", "São Paulo", "Bragantino",
          "Corinthians", "Fluminense", "Ceará", "Internacional",
          "Atlético-MG", "Grêmio", "Vasco da Gama", "Santos",
          "Vitória", "Juventude", "Fortaleza", "Sport")

print("===========SÉRIE A BRASILEIRÃO===========\n")
print(f"- G5: {seriea[0]}, {seriea[1]}, {seriea[2]}, {seriea[3]} e {seriea[4]}\n")
print(f"- Z4: {seriea[-4]}, {seriea[-3]}, {seriea[-2]} e {seriea[-1]}\n")
print(f"- Times em ordem alfabética: {sorted(seriea)}\n")
print(f"- O Vasco está em {seriea.index("Vasco da Gama")+1}° lugar da tabela!")
