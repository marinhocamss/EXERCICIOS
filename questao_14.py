peso_peixes = float(input("\nDigite o peso de peixes em quilos: "))

limite = 50

if limite<peso_peixes:
    excesso = peso_peixes - limite
    multa = excesso*4
    print("O peso dos peixes execedeu o limite em kg:", excesso)
    print("A multa pelo excesso de peso é de (em reais)!", multa)

else:
    excesso = 0
    multa = 0
    print("O peso dos peixes não foi excedido! Não se têm multa a ser paga!")
