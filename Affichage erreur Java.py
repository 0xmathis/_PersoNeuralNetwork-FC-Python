from matplotlib.pyplot import plot, show

with open('Z:\\Mega\\Programmation\\Java\\TIPE\\errors.txt') as f:
    lines = f.read()

Y = list(map(lambda x: float(x), lines.strip().split('\n')))
X = [i for i in range(1, len(Y) + 1)]

plot(X, Y)
show()
