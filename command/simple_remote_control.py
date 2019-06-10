class Command(object):

    def execute(self):
        raise NotImplementedError()


class Light(object):

    def on(self):
        print('Light ON')


class LightOnCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()


class SimpleRemoteControl(object):

    def __init__(self):
        self._slot = None

    def set_command(self, command):
        self._slot = command

    def button_was_pressed(self):
        self._slot.execute()


if __name__ == '__main__':
    remote = SimpleRemoteControl()
    light = Light()
    light_on = LightOnCommand(light)

    remote.set_command(light_on)
    remote.button_was_pressed()
