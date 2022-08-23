num1 = int(input("Digite valor para num1:"))
num2 = int(input("Digite valor para num2:"))

sum = 0

if(num1 == num2): print('Os números são iguais')

while num1 != num2:

    if(num1 > num2):
        num1 -= 1
    elif(num1 < num2):
        num1 += 1
    elif(num1 == num2):
        exit()

    if(num1 % 2 == 0 and num1 != num2):
        sum += num1    

print('A soma é :', sum)
print('FIM!')