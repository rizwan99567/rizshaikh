#task1:To check whether number is prime or not
def prime(num):
    if num<=1:
        print(f'{num} is not prime number')
    else:
        for i in range(2,num):
            if num%2==0:
                print(f'{num} is not a prime number')
                break
        else:
            print(f'{num} is prime number')

prime(12)
prime(101)
prime(3)

#task2:check whethe number is palindrome or not
def palindrome(name):
    if name==name[::-1]:
        print(f'{name} is palindrome')
    else:
        print(f'{name} is not palindrome')

palindrome("Rizwan")
palindrome("markram")

#task3: create a table of given number.
def table(num):
    print(f'Your entered number is {num}')
    for i in range(1,11):
        print(f'{num} * {i} = ',num * i)
table(7)
