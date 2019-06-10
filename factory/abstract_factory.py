# =============================================================================
# Ingridients
class Dough(object):
    pass


class ThinCrusDough(Dough):
    pass


class Sauce(object):
    pass


class MarinaraSauce(Sauce):
    pass


class Veggie(object):
    pass


class Garlic(Veggie):
    pass


class Onion(Veggie):
    pass


class Mushrrom(Veggie):
    pass


class RedPepper(Veggie):
    pass


class Cheese(object):
    pass


class BlueCheese(Cheese):
    pass


class Pepperoni(object):
    pass


class SlicedPepperoni(Pepperoni):
    pass


class Clam(object):
    pass


class FreshClam(Clam):
    pass


# =============================================================================
# Ingridients factories
class PizzaIngridientFactory(object):

    def create_dough(self):
        raise NotImplementedError

    def create_sauce(self):
        raise NotImplementedError

    def create_cheese(self):
        raise NotImplementedError

    def create_veggies(self):
        raise NotImplementedError

    def create_pepperoni(self):
        raise NotImplementedError

    def create_clam(self):
        raise NotImplementedError


class NYPizzaIngridientFactory(PizzaIngridientFactory):

    def create_dough(self):
        return ThinCrusDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return BlueCheese()

    def create_veggies(self):
        return [
            Garlic(), Onion(), Mushroom(), RedPepper()
        ]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClam()


# =============================================================================
# Pizza
class Pizza(object):

    def __init__(self, name):
        self._name = name
        self._dough = None
        self._sauce = None
        self._veggies = None
        self._cheese = None
        self._pepperoni = None
        self._clam = None

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cuttings the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self._name

    def __str__(self):
        return 'Pizza[%s]' % self._name


class CheesePizza(Pizza):

    def __init__(self, pizza_ingridient_factory):
        Pizza.__init__(self, 'Cheese pizza')
        self._pizza_ingridient_factory = pizza_ingridient_factory

    def prepare(self):
        print('Preparing %s' % self._name)
        self._dough = self._pizza_ingridient_factory.create_dough()
        self._sauce = self._pizza_ingridient_factory.create_sauce()
        self._cheese = self._pizza_ingridient_factory.create_cheese()


class ClamPizza(Pizza):

    def __init__(self, pizza_ingridient_factory):
        Pizza.__init__(self, 'Clam pizza')
        self._pizza_ingridient_factory = pizza_ingridient_factory

    def prepare(self):
        print('Preparing %s' % self._name)
        self._dough = self._pizza_ingridient_factory.create_dough()
        self._sauce = self._pizza_ingridient_factory.create_sauce()
        self._cheese = self._pizza_ingridient_factory.create_cheese()
        self._clam = self._pizza_ingridient_factory.create_clam()


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
        pizza_ingridient_factory = NYPizzaIngridientFactory()

        if 'cheese' == type:
            pizza = CheesePizza(pizza_ingridient_factory)
        elif 'veggie' == type:
            pizza = VeggiePizza(pizza_ingridient_factory)
        elif 'pepperoni' == type:
            pizza = PepperoniPizza(pizza_ingridient_factory)

        return pizza


if __name__ == '__main__':
    ny_store = NYStylePizzaStore()

    pizza = ny_store.order_pizza('cheese')
    print('Ordered pizza is %s' % pizza.get_name())
