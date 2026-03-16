print("Calculadora de Consumo de Energia")

aparelho = input("Nome do aparelho: ")
potencia = float(input("Potência em watts (W): "))
horas = float(input("Horas de uso por dia: "))

consumo = (potencia * horas * 30) / 1000
custo = consumo * 0.75

print("\nAparelho:", aparelho)
print("Consumo estimado:", round(consumo,2), "kWh/mês")
print("Custo estimado: R$", round(custo,2))
