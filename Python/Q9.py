# 1 - 가능
a['name'] = 'python'
print(a)
a.clear()

# 2 - 가능
a[('a',)] = 'python'
print(a)
a.clear()

# 3 - error 발생
try:
    a[[1]] = 'python' # 리스트는 key값으로 올 수 없다.
except TypeError:
    print('error')
    pass

# 4 - 가능
a[250] = 'python'
print(a)
a.clear()