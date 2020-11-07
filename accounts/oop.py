# class Point:
#     "Класс для представления координат точек на плоскости"
#     x = 1
#     y = 1
#
#
# print(Point.__doc__)


class Point:
    x = 1;
    y = 1

    def setPoint(self):
        print(self.__dict__)


pt = Point()
pt.x = 5
pt.y = 10
pt.setPoint()
