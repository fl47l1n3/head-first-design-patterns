

####################################################################################################
# Интерфейсы
class Duck(object):

    def __init__(self, fly_behavior, quack_behavior):
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    def set_fly_behavior(self, fly_behavior):
        self._fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self._quack_behavior = quack_behavior

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

    def swim(self):
        print('Duck swim')


class FlyBehavior(object):

    def fly(self):
        raise NotImplementedError


class QuackBehavior(object):

    def quack(self):
        raise NotImplementedError


####################################################################################################
# Реализация
class FlyWithWings(FlyBehavior):

    def fly(self):
        print('Flyyyyyyyy....')


class FlyNoWay(FlyBehavior):

    def fly(self):
        print('Dont flyyyy :(')


class FlyRocketPowered(FlyBehavior):

    def fly(self):
        print('Fly as rocket!')


class Quack(QuackBehavior):

    def quack(self):
        print('Quack')


class MuteQuack(QuackBehavior):

    def quack(self):
        print('...silence...')


class Squeak(QuackBehavior):

    def quack(self):
        print('Squeak')


class MallardDuck(Duck):

    def __init__(self):
        Duck.__init__(
            self,
            fly_behavior=FlyWithWings(),
            quack_behavior=Quack(),
        )


class ModelDuck(Duck):

    def __init__(self):
        Duck.__init__(
            self,
            fly_behavior=FlyNoWay(),
            quack_behavior=Quack(),
        )


####################################################################################################
# Тестируем
if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    # Изменяем поведение
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()
