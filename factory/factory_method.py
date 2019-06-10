# =============================================================================
# Pizza
class Pizza(object):

    def __init__(self, name, dough, sauce, toppings):
        self._name = name
        self._dough = dough
        self._sauce = sauce
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
        return '%s pizza on %s douhg with %s' % (
            self._name, self._dough, self._sauce
        )


class NYCheesePizza(Pizza):

    def __init__(self):
        Pizza.__init__(self,
            'cheese', 'thin', 'mayonase',
            ['masdam cheese', 'blue cheese']
        )


class NYGreekPizza(Pizza):

    def __init__(self):
        Pizza.__init__(self,
            'greek', 'thin', 'greek sause',
            ['olive', ]
        )


class NYPepperoniPizza(Pizza):

    def __init__(self):
        Pizza.__init__(self,
            'cheese', 'thin', 'tomato sause',
            ['pepperoni', 'blue cheese']
        )


class ChicagoCheesePizza(Pizza):

    def __init__(self):
        Pizza.__init__(self,
            'cheese', 'thick', 'mayonase',
            ['masdam cheese', 'blue cheese']
        )


class ChicagoGreekPizza(Pizza):

    def __init__(self):
        Pizza.__init__(self,
            'greek', 'thick', 'greek sause',
            ['olive', ]
        )


class ChicagoPepperoniPizza(Pizza):

    def __init__(self):
        Pizza.__init__(self,
            'cheese', 'thick', 'tomato sause',
            ['pepperoni', 'blue cheese']
        )


# =============================================================================
# Pizza stores
class PizzaStore(object):

    def order_pizza(self, type):
        pizza = self._create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def _create_pizza(self, type):
        raise NotImplementedError


class NYStylePizzaStore(PizzaStore):

    def _create_pizza(self, type):
        pizza = None

        if 'cheese' == type:
            pizza = NYCheesePizza()
        elif 'greek' == type:
            pizza = NYGreekPizza()
        elif 'pepperoni' == type:
            pizza = NYPepperoniPizza()

        return pizza


class ChicagoStylePizzaStore(PizzaStore):

    def _create_pizza(self, type):
        pizza = None

        if 'cheese' == type:
            pizza = ChicagoCheesePizza()
        elif 'greek' == type:
            pizza = ChacagoGreekPizza()
        elif 'pepperoni' == type:
            pizza = ChicagoPepperoniPizza()

        return pizza


if __name__ == '__main__':
    ny_store = NYStylePizzaStore()
    chicago_store = ChicagoStylePizzaStore()

    pizza = ny_store.order_pizza('cheese')
    print('Ordered pizza is %s' % pizza.get_name())

    pizza = chicago_store.order_pizza('cheese')
    print('Ordered pizza is %s' % pizza.get_name())
