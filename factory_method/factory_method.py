class CaffeineBeverage:

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customet_wants_condiments():
            self.add_condiments()

    def brew(self):
        raise NotImplementedError()

    def add_condiments(self):
        raise NotImplementedError()

    def customet_wants_condiments(self):
        return True

    def boil_water(self):
        print('Boiling water')

    def pour_in_cup(self):
        print('Pouring into cup')


class CaffeineBeverageWithHook(CaffeineBeverage):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customet_wants_condiments():
            self.add_condiments()

    def customet_wants_condiments(self):
        return True


class CoffeeWithHook(CaffeineBeverageWithHook):

    def customet_wants_condiments(self):
        yn = raw_input('Would you like milk and sugar with your coffee (y/n)?')
        return True if 'y' == yn else False

    def brew(self):
        print('Dripping Coffee through filter')

    def add_condiments(self):
        print('Adding Sugar and Milk')


class Coffee(CaffeineBeverage):

    def brew(self):
        print('Dripping Coffee through filter')

    def add_condiments(self):
        print('Adding Sugar and Milk')


class Tea(CaffeineBeverage):

    def brew(self):
        print('Steeping the tea')

    def add_condiments(self):
        print('Adding Lemon')


if __name__ == '__main__':
    tea = Tea()
    coffee_hook = CoffeeWithHook()

    print('Making tea...')
    tea.prepare_recipe()

    print('Making coffee')
    coffee_hook.prepare_recipe()
