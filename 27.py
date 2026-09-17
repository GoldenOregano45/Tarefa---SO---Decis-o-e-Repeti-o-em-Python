voltas = int(input("Digite o número de voltas: "))
extensao = float(input("Digite a extensão da pista em metros: "))
tempo_min = float(input("Digite o tempo em minutos: "))

distancia_km = (voltas * extensao) / 1000
tempo_horas = tempo_min / 60

velocidade_media = distancia_km / tempo_horas
print(f"A velocidade média é de {velocidade_media:.2f} km/h")