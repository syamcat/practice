str = ''
a = ['Life', 'is', 'too', 'short']

a.reverse()
while a:
    str += a.pop()
    str += ' '

print(str)