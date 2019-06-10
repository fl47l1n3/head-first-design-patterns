
class Beverage(object):

    def __init__(self):
        self._description = None

    def get_description(self):
        return self._description

    def cost(self):
        raise NotImplementedError


class CondimentDecorator(Beverage):

    def get_description(self):
        raise NotImplementedError


class Espresso(Beverage):

    def __init__(self):
        super(Espresso, self).__init__()
        self._description = 'Espresso'

    def cost(self):
        return 1.99


class HouseBlend(Beverage):

    def __init__(self):
        super(HouseBlend, self).__init__()
        self._description = 'House Blend Coffee'

    def cost(self):
        return 0.89


class DarkRost(Beverage):

    def __init__(self):
        super(DarkRost, self).__init__()
        self._description = 'Dark Rost Coffee'

    def cost(self):
        return 0.70


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        super(Mocha, self).__init__()
        self._beverage = beverage

    def get_description(self):
        return '%s, Mocha' % self._beverage.get_description()

    def cost(self):
        return 20.0 + self._beverage.cost()


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        super(Whip, self).__init__()
        self._beverage = beverage

    def get_description(self):
        return '%s, Whip' % self._beverage.get_description()

    def cost(self):
        return 12.1 + self._beverage.cost()


if __name__ == '__main__':
    beverage = Espresso()
    print('%s $%s' % (beverage.get_description(), beverage.cost()))

    beverage2 = DarkRost()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print('%s $%s' % (beverage2.get_description(), beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3 = Mocha(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print('%s $%s' % (beverage3.get_description(), beverage3.cost()))
