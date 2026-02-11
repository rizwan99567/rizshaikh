#decimal to binary conversion
num=int(input("Enter the decimal number: "))
res=bin(num)
print(f'Your decimal number {num} converted into binary numbrr {res}')
print("----------------------------------------------------------------")

#decimal to octal conversion
num1=int(input("Enter the decimal number: "))
res1=oct(num1)
print(f'Your decimal number {num1} converted into octal number {res1}')
print("----------------------------------------------------------------")

#decimal to hexadecimal conversion
num2=int(input("Enter the decimal number: "))
res2=hex(num2)
print(f'Your decimal number {num2} converted into hexadecimal number {res2}')


#2. Accept binary, octal or hexadecimal from user and convert it into decimal number and display it.
num3 = input("Enter the number: ")
base = int(input("Enter the base (2 for binary, 8 for octal, 16 for hexadecimal): "))

decimal = int(num3, base)

print("Decimal number is:", decimal)
