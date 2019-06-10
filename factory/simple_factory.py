# =============================================================================
# Pizza
class Pizza(object):

    def __init__(self, name, dough, sauce, toppings):
        self._name = name
        self._dough = dough
        self._toppings = toppings

    def prepare(self):
        print('Preparing pizza')

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cuttings the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self._name


class CheesePizza(Pizza):

    def __init__(self):
        Pizza.__init__(self,
            'cheese', 'thin', 'mayonase',
            ['masdam cheese', 'blue cheese']
        )


class GreekPizza(Pizza):

    def __init__(self):
        Pizza.__init__(self,
            'greek', 'thin', 'greek sause',
            ['olive', ]
        )


class PepperoniPizza(Pizza):

    def __init__(self):
        Pizza.__init__(self,
            'cheese', 'thin', 'tomato sause',
            ['pepperoni', 'blue cheese']
        )


# =============================================================================
# Pizza factory
class PizzaFactory(object):

    def create_pizza(self, type):
        pizza = None

        if 'cheese' == type:
            pizza = CheesePizza()
        elif 'greek' == type:
            pizza = GreekPizza()
        elif 'pepperoni' == type:
            pizza = PepperoniPizza()

        return pizza


# =============================================================================
# Pizza store
class PizzaStore(object):

    def __init__(self, pizza_factory):
        self._pizza_factory = pizza_factory

    def order_pizza(self, type):
        pizza = self._pizza_factory.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


if __name__ == '__main__':
    store = PizzaStore(PizzaFactory())
    pizza = store.order_pizza('cheese')
    print('Ordered pizza is %s' % pizza.get_name())
