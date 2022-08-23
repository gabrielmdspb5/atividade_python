num1 = 38
num2 = 37

count = 1
sum = 0

while count <= 37:
    sum += (num2 * num1) / count

    num1 -= 1
    num2 -= 1
    count += 1

print('A soma é :', sum)