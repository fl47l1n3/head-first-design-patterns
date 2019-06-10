
class ChocolateBoiler(object):

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(ChocolateBoiler, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._empty = True
        self._boiled = False

    def fill(self):
        if self.is_empty():
            self._empty = True
            self._boiled = False

    def drain(self):
        if self.is_empty() and self.is_boiled():
            empty = True

    def boil(self):
        if not self.is_empty() and not self.is_boiled():
            self._boiled = True

    def is_empty(self):
        return self._empty

    def is_boiled(self):
        return self._boiled


if __name__ == '__main__':
    print(ChocolateBoiler() == ChocolateBoiler())
