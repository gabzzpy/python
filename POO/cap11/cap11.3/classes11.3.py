class Ponto:

    def __init__(self,x,y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x},{self._y})"

    def __repr__(self):
        return f"Ponto({self._x+1}, {self._y+1})"


if __name__ == '__main__':
    p1 = Ponto(1,2)
    p2 = eval(repr(p1)) # Mesma coisa que executar p2 = Ponto(2,3)

    print(p1)
    print(p2)