class Firearms:
    className = 'Firearms'
    objectsCount = 0

    def __init__(self, name, cartridges, speed, range):
        self._name = name
        self._cartridges = cartridges
        self._speed = speed
        self._range = range
        Firearms.objectsCount = Firearms.objectsCount + 1

    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n

    def get_cartridges(self):
        return self._cartridges

    def set_cartridges(self, cartridges):
        if cartridges > 0:
            self._cartridges = cartridges
        else:
            self._cartridges = 0.1

    def speed(self):
        return self._speed

    def range(self):
        return self._range

    def info(self):
        print(self._name)
        print(f"Количество патронов в магазине: {self._cartridges} ")
        print(f'Скорострельность: {self._speed} в/мин')
        print(f'Дальность стрельбы: {self._range} м')

    def seconds(self):
        print(f'Магазин опустеет за: {self._speed * 60} сек')

    def ratio(self):
        print(f'Соотношение скорострельности к дальности стрельбы: {self._speed / self._range} ')

class Assault_rifle(Firearms):
    className = 'Assault_rifle'

    def __init__(self, name, cartridges, speed, range, caliber):
        super().__init__(name, cartridges, speed, range)
        self.caliber = caliber

    def set_caliber(self, caliber):
        if caliber > 0:
            self.caliber = caliber
        else:
            self.caliber = 1

    def info(self):
        super().info()
        print(f'Тип: {Assault_rifle.className}')
        print(f"Калибр (мм): {self.caliber}")


b = Firearms("Объект класса " + Firearms.className, 500, 499, 765)
b.info()
b.seconds()
b.ratio()

print('\n')

f = Assault_rifle('штурмовая винтовка', 20, 800, 500, 5.56)
f2 = Assault_rifle('снайперская винтовка', 10, 30, 1200, 7.62)


f.seconds()



print(f'Objects count: {File.objectsCount}')