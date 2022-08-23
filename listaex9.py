count = 0

maior = 0

while count < 20:
    count += 1
    
    num = int(input("Digite valor para o numero:"))

    if(num > maior): maior = num

print('O maior numero é', maior)