class Duck:

    def quack(self):
        raise NotImplementedError()

    def fly(self):
        raise NotImplementedError()


class MallardDuck(Duck):

    def quack(self):
        print('Quack')

    def fly(self):
        print('Im flying')


class Turkey:

    def gobble(self):
        raise NotImplementedError()

    def fly(self):
        raise NotImplementedError()


class WildTurkey(Turkey):

    def gobble(self):
        print('Gobble gobble')

    def fly(self):
        print('Im flying a short distance')


class TurkeyAdapter(Duck):

    def __init__(self, turkey):
        self._turkey = turkey

    def quack(self):
        self._turkey.gobble()

    def fly(self):
        for i in range(5):
            self._turkey.fly()


def test_duck(duck):
    duck.quack()
    duck.fly()


if __name__ == '__main__':
    duck = MallardDuck()

    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)

    print('The Turkey says...')
    turkey.gobble()
    turkey.fly()

    print('The Duck says...')
    test_duck(duck)

    print('The TurkeyAdapter says...')
    test_duck(turkey_adapter)
