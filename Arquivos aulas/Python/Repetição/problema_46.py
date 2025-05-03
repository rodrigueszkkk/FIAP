num = int(input('Digite um numero: '))

divisor = 1
while divisor <= num:
    if num % divisor == 0:
        print(divisor)
    divisor = divisor + 1

print(divisor)