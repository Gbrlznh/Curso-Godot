nomeHeroi = input(("Qual o seu nome?\n"))
vitorias = int (input(("Quantas vitórias você teve?\n")))
derrotas = int (input(("Quantas derrotas você teve?\n")))
saldoVitorias = int

def calculadoraVD(vitorias, derrotas):
    
    return vitorias - derrotas
    

saldoVitorias = calculadoraVD(vitorias, derrotas)

match saldoVitorias:
    
    case _ if saldoVitorias >= 11 and saldoVitorias <= 20:
        categoria = "Bronze"
        
    case _ if saldoVitorias >= 21 and saldoVitorias <= 50:
        categoria = "Prata"
        
    case _ if saldoVitorias >= 51 and saldoVitorias <= 80:
        categoria = "Ouro"
        
    case _ if saldoVitorias >= 81 and saldoVitorias <= 90:
        categoria = "Diamante"

    case _ if saldoVitorias >= 91 and saldoVitorias <= 100:
        categoria = "Lendário"
        
    case _ if saldoVitorias >= 101:
        categoria = "Imortal"

    case _:
        categoria = "Ferro"
        
print(f"O herói de nome {nomeHeroi} tem o saldo de {saldoVitorias} vitórias e está no nivel: {categoria}!")        

