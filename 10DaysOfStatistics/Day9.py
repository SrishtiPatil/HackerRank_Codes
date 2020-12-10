# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model


m, n = map(int, input().split())
X, Y = [], []

for i in range(n):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < m:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

q = int(input())
new_X = []
for i in range(q):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

result = lm.predict(new_X)
for i in range(len(result)):
    print(round(result[i],2))
