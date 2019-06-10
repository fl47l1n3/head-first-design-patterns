class Iterator:

    def has_next(self):
        raise NotImplementedError()

    def next(self):
        raise NotImplementedError()


class MenuIterator(Iterator):

    def __init__(self, items):
        self._items = items
        self._position = 0

    def has_next(self):
        if self._position >= len(self._items):
            return False
        else:
            return True

    def next(self):
        menu_items = self._items[self._position]
        self._position += 1
        return menu_items


class MenuItem:

    def __init__(self, name, description, vegetarian, price):
        self._name = name
        self._description = description
        self._vegetarian = vegetarian
        self._price = price

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def is_vegetarian(self):
        return self._vegetarian


class Menu:

    def create_iterator(self):
        raise NotImplementedError()


class PancakeHouseMenu(Menu):

    def __init__(self):
        self._menu_items = []
        self.add_item(
            'K&B Pancake Breakfast',
            'Pancakes with scrambled eggs, and toast',
            True, 2.99
        )
        self.add_item(
            'Regualr Pancake Breakfast',
            'Regular with fried eggs, sausage',
            False, 2.99
        )
        self.add_item(
            'Blueberry Pancakes',
            'Pancakes made with fresh blueberries',
            True, 3.49
        )
        self.add_item(
            'Waffles',
            'Waffles, with your choice if blueberries or strawberries',
            True, 3.59
        )

    def add_item(self, name, description, vegetarian, price):
        self._menu_items.append(
            MenuItem(name, description, vegetarian, price)
        )

    def create_iterator(self):
        return MenuIterator(self._menu_items)


class DinnerMenu(Menu):

    MAX_ITEMS = 6

    def __init__(self):
        self._number_of_items = 0
        self._menu_items = []
        self.add_item(
            'Vegetarian BLT',
            "(Fakin') Bacon with lettuce & tomato on whole wheat",
            True, 2.99
        )
        self.add_item(
            'BLT',
            "Bacon with lettuce & tomato on whole wheat",
            False, 2.99
        )
        self.add_item(
            'Soup of the day',
            'Soup of the day, with a side of potato slald',
            False, 2.99
        )
        self.add_item(
            'Hotdog',
            'A hot dog, with saurkraut, relish, onions. topped with cheese',
            False, 3.05
        )

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        if self._number_of_items >= self.MAX_ITEMS:
            print("Sorry, menu is full! Can't add item to menu")
        else:
            self._menu_items.append(menu_item)

    def create_iterator(self):
        return MenuIterator(self._menu_items)


class CafeMenu(Menu):

    def __init__(self):
        self._menu_items = {}
        self.add_item(
            'Veggie Burger and Air Fries',
            'Veggie burger on a whole wheat bun, lettuce, tomato and fries',
            True, 3.99
        )
        self.add_item(
            'Soup ot the day',
            'A cup of the soup of the day, with a side salad',
            False, 3.69
        )
        self.add_item(
            'Burrito',
            'A large burrito, with whole pinto beans, salsa, guacamole',
            True, 4.29
        )

    def add_item(self, name, description, vegetarian, price):
        self._menu_items[name] = MenuItem(name, description, vegetarian, price)

    def create_iterator(self):
        return MenuIterator(list(self._menu_items.values()))


class Waitress:

    def __init__(self, menus):
        self._menus = menus

    def print_menus(self):
        for menu in self._menus:
            self.print_menu(menu.create_iterator())

    def print_menu(self, iterator):
        while iterator.has_next():
            menu_item = iterator.next()
            print('%s, %s -- %s' % (
                menu_item.get_name(),
                menu_item.get_price(),
                menu_item.get_description()
            ))


if __name__ == '__main__':
    pancake_house_menu = PancakeHouseMenu()
    dinner_menu = DinnerMenu()
    cafe_menu = CafeMenu()
    waitress = Waitress([pancake_house_menu, dinner_menu, cafe_menu])
    waitress.print_menus()
