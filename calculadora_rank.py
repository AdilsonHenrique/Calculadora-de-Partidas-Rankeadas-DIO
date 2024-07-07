nome = input(("Qual é o seu nome?\n"))
vitorias = float(input("Quantas vitorias voce tem nas partidas rakeadas\n"))
derrotas = float(input("Quantas derrotas voce tem nas partidas rakeadas\n"))
saldo = vitorias - derrotas

def nivel_ranked(vitorias, derrotas): 
    if saldo <= 10:
        rank = "ferro"
    elif 11 <= saldo <= 20:
        rank = "bronze"
    elif 21 <= saldo <= 50:
        rank = "prata"
    elif 51 <= saldo <= 80:
        rank = "ouro"
    elif 81 <= saldo <= 90:
        rank = "diamante"
    elif 91 <= saldo <= 100:
        rank = "Lendario"
    else:
        rank = "Imortal"
    return rank

rank = nivel_ranked(vitorias, derrotas)

 
print(f"O Herói {nome} tem de saldo de {saldo} e está no nível {rank} ")  