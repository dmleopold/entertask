def F(n):
    if n != 1:
        F(n-1)
    if n % 3 == 0:
        print(n, 'Bar')
    else:
        print(n, 'Foo')

n = int(input())
F(n)
