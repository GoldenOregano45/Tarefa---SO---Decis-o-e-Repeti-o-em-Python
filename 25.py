h_ini = int(input("digite a hora inicial:"))
m_ini = int(input("digite o minuto inicial:"))  
h_fim = int(input("digite a hora DE TERMINO:"))
m_fim = int(input("digite o minuto DE TERMINO:"))

minutos_ini = h_ini * 60 + m_ini
minutos_fim = h_fim * 60 + m_fim

if minutos_fim < minutos_ini:
    minutos_fim += 24 * 60

duracao = minutos_fim - minutos_ini
horas = duracao // 60
minutos = duracao % 60

print(f"duracao: {horas} horas e {minutos:02d} minutos")