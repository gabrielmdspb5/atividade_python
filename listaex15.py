current = 1
next = 1

count = 1

while count <= 15:
    print(current)

    current = next
    next = current + next

    count += 1