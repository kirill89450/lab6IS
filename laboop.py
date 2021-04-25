class BigBell:  # 1 базовый синтаксис
    f = 0

    def sound(arg1):
        if not arg1.f:
            arg1.f = 1
            print("ding")
        else:
            arg1.f = 0
            print("dong")


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
print('\n')


class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, num):
        self.right += num

    def add_left(self, num):
        self.left += num

    def result(self):
        if self.left == self.right:
            return '='
        if self.left > self.right:
            return 'L'
        if self.left < self.right:
            return 'R'


Balance = Balance()
Balance.add_right(5)
Balance.add_left(3)
print(Balance.result())
print('\n')


class Point:  # 4 специальные методы (Pycharm говорит первый параметр должен называться self,но в документации нашел что arg1,2,3.. как правильно?
    def __init__(arg1, x, y):
        arg1.x = x
        arg1.y = y

    def __str__(arg1):
        return '[{} and {}]'.format(arg1.x, arg1.y)

    def __eq__(arg1, other):
        return (arg1.x == other.x
                and
                arg1.y == other.y)

    def __ne__(arg1, other):
        return (arg1.x != other.x
                and
                arg1.y != other.y)


p1 = Point(1, 2)
p2 = Point(5, 6)

if p1 == p2:
    print(p1, p2, " Eual True")
else:
    print(p1, p2, "Eual False")
if p1 != p2:
    print(p1, p2, "Not eual True")
else:
    print(p1, p2, 'Not eual False')
print('\n')


class Triangle:  # 9 наследование
    def __init__(arg1, a, b, c):
        arg1.a = a
        arg1.b = b
        arg1.c = c

    def P(arg1):
        per = arg1.a + arg1.b + arg1.c
        return per


class EquilateralTriangle(Triangle):
    def __init__(arg2, a):
        arg2.a = a
        arg2.b = a
        arg2.c = a

    def P(arg2):
        return Triangle.P(arg2)


VersatileTriangle = Triangle(1, 3, 4)
print(VersatileTriangle.P())

EquilateralTriangle = EquilateralTriangle(5)
print(EquilateralTriangle.P())
print('\n')



class A:  # 12 наследование

    def __str__(arg1): return 'A.__str__ method'

    def hello(arg1): print('Hello')


class B:
    def __str__(arg1): return 'B.__str__ method'

    def good_evening(arg1): print('Good evening')


class C(A, B): pass


class D(B, A): pass


c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(c)
print(d)
print('\n')



