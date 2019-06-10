

class Observable(object):

    def register_observer(self, observer):
        raise NotImplementedError

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError


class Observer(object):

    def update(self, temperature, humidity, pressure):
        raise NotImplementedError


class DisplayElement(object):

    def display(self):
        raise NotImplementedError


class WeatherData(Observable):

    def __init__(self):
        Observable.__init__(self)
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def rmeove_observer(self, observer):
        if observer in self._observers:
            del self._observers[observer]

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        Observer.__init__(self)
        DisplayElement.__init__(self)
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self):
        print('Current conditions: %s F degrees and %s humidity' % (
            self._temperature, self._humidity)
        )


if __name__ == '__main__':
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
