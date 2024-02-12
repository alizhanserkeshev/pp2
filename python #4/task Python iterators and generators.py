#first task
def square_generator(N):
    for i in range(N):
        yield i**2

N = int(input())
squares = square_generator(N)
print(list(squares))

print("--------")

#second task
def even_generator(N):
    for i in range(N+1):
        if i % 2 == 0:
            yield i

n = int(input())
evens = even_generator(n)
print("Even numbers between 0 and", n, ":", ', '.join(map(str, evens)))

print("--------")
#third task
def divisible_by_3_and_4_generator(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
divisible_nums = divisible_by_3_and_4_generator(n)
print("Numbers divisible by 3 and 4 between 0 and", n, ":", list(divisible_nums))


print("--------")
#fourth task
def squares_generator(a, b):
    for i in range(a, b+1):
        yield i**2

a, b = 2, 5
for square in squares_generator(a, b):
    print(square)

print("--------")
#fifth task
def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
countdown = countdown_generator(n)
print(list(countdown))
