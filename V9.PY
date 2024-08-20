# Solicita ao usuário a quantidade de fotocópias realizadas
quantidade_fotocopias = int(input("Digite a quantidade de fotocópias realizadas: "))

# Inicializa o valor da fatura
fatura = 0.0

# Calcula o valor da fatura com base na quantidade de fotocópias
if quantidade_fotocopias <= 10:
    fatura = quantidade_fotocopias * 0.25
elif quantidade_fotocopias <= 30:
    fatura = (10 * 0.25) + ((quantidade_fotocopias - 10) * 0.20)
else:
    fatura = (10 * 0.25) + (20 * 0.20) + ((quantidade_fotocopias - 30) * 0.10)

# Exibe a fatura
print(f"A fatura correspondente é R$ {fatura:.2f}.")
