nomeHeroi = input(("Qual o seu nome?\n"))
xp = float (input(("Quanto de XP você possui?\n")))

match xp:
    

    case _ if xp >= 1001 and xp <= 2000:
        categoria = "Bronze"
        
    case _ if xp >= 2001 and xp <= 5000:
        categoria = "Prata"
        
    case _ if xp >= 6001 and xp <= 7000:
        categoria = "Ouro"
        
    case _ if xp >= 7001 and xp <= 8000:
        categoria = "Platina"
        
    case _ if xp >= 8001 and xp <= 9000:
        categoria = "Ascendente"

    case _ if xp >= 9001 and xp <= 10000:
        categoria = "Imortal"
        
    case _ if xp >= 10001:
        categoria = "Radiante"

    case _:
        categoria = "Ferro"
        
print(f"O herói de nome {nomeHeroi} está no nivel: {categoria}!")        

