nota = float(input("Digite a nota (entre 0 e 20): "))

if 0 <= nota <= 20:
    if nota > 10:
        print("Validada")
    else:
        print("Não validada")
else:
    print("Nota fora do intervalo permitido.")
