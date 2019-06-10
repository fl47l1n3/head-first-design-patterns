

class Observable(object):

    def __init__(self):
        self._observers = []
        self._changed = False

    def set_changed(self):
        self._changed = True

    def register_observer(self, observer):
        self._observers.append(observer)

    def rmeove_observer(self, observer):
        if observer in self._observers:
            del self._observers[observer]

    def notify_observers(self, **kwargs):
        if self._changed:
            for observer in self._observers:
                observer.update(self, **kwargs)
            self._changed = False


class Observer(object):

    def update(self, observable, **kwargs):
        raise NotImplementedError


class DisplayElement(object):

    def display(self):
        raise NotImplementedError


class WeatherData(Observable):

    def __init__(self):
        Observable.__init__(self)
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def get_temperature(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity

    def get_pressure(self):
        return self._pressure

    def measurements_changed(self):
        self.set_changed()
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

    def update(self, observable):
        if isinstance(observable, WeatherData):
            self._temperature = observable.get_temperature()
            self._humidity = observable.get_humidity()
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
