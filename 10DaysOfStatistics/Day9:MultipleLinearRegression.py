# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model


m, n = map(int, input().split())
X, Y = [], []

for i in range(n):
    x = [0]
    a = list(map(float, input().split()))
    for j in range(len(a)):
        if j < m:
            x.append(a[j])
        else:
            Y.append(a[j])
    X.append(x)

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

q = int(input())
new_X = []
for i in range(q):
    x = [0]
    a = list(map(float, input().split()))
    for j in range(len(a)):
        x.append(a[j])
    new_X.append(x)

res = lm.predict(new_X)
for i in range(len(res)):
    print(round(res[i],2))
