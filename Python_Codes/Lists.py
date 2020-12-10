N = int(input())
result = []
out = []
for n in range(N):
    x = input().split(" ")
    funct = x[0]
    if funct == 'append':
        result.append(int(x[1]))
    if funct == 'print':
        print(result)
    if funct == 'insert':
        result.insert(int(x[1]), int(x[2]))
    if funct == 'reverse':
        result == result.reverse()
    if funct == 'pop':
        result.pop()
    if funct == 'sort':
        result == result.sort()
    if funct == 'remove':
        result.remove(int(x[1]))
for i in out:
    print(i)
            
