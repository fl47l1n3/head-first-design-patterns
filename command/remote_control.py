class CeilingFan(object):

    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self):
        self._speed = self.OFF

    def high(self):
        self._speed = self.HIGH
        print('Set speed HIGH')

    def medium(self):
        self._speed = self.MEDIUM
        print('Set speed MEDIUM')

    def low(self):
        self._speed = self.LOW
        print('Set speed LOW')

    def off(self):
        self._speed = self.OFF
        print('Set speed OFF')

    def get_speed(self):
        return self._speed


class Light(object):

    def on(self):
        print('Light ON')

    def off(self):
        print('Light OFF')


class Stereo(object):

    def on(self):
        print('Stereo ON')

    def off(self):
        print('Stereo OFF')

    def set_cd(self, name):
        print('Set CD %s' % name)

    def set_volume(self, level):
        print('Volume level is %s' % level)


class Command(object):

    def execute(self):
        raise NotImplementedError()

    def undo(self):
        raise NotImplementedError()


class NoCommand(Command):

    def execute(self):
        print('NO_COMMAND')

    def undo(self):
        print('NO_UNDO')


class MacroCommand(Command):

    def __init__(self, commands):
        self._commands = commands

    def execute(self):
        for command in self._commands:
            command.execute()

    def undo(self):
        pass


class LightOffCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()


class LightOnCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class StereoOnWithCDCommand(Command):

    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.set_cd('Beatles - Help!')
        self._stereo.set_volume(11)

    def undo(self):
        self._stereo.off()


class StereoOffCommand(Command):

    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.off()

    def undo(self):
        self._stereo.on()


class CeilingFanOffCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan
        self._prev_speed = None

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.off()

    def undo(self):
        if CeilingFan.HIGH == self._prev_speed:
            self._ceiling_fan.high()
        elif CeilingFan.MEDIUM == self._prev_speed:
            self._ceiling_fan.medium()
        elif CeilingFan.LOW == self._prev_speed:
            self._ceiling_fan.low()
        elif CeilingFan.OFF == self._prev_speed:
            self._ceiling_fan.off()


class CeilingFanMediumCommand(CeilingFanOffCommand):

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.medium()


class CeilingFanHighCommand(CeilingFanOffCommand):

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.high()


class RemoteControl(object):

    MAX_COMMANDS = 7

    def __init__(self):
        self._on_commands = [NoCommand() for i in range(self.MAX_COMMANDS)]
        self._off_commands = [NoCommand() for i in range(self.MAX_COMMANDS)]
        self._undo_command = NoCommand()

    def set_command(self, slot, on_command, off_command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self._on_commands[slot].execute()
        self._undo_command = self._on_commands[slot]

    def off_button_was_pushed(self, slot):
        self._off_commands[slot].execute()
        self._undo_command = self._off_commands[slot]

    def undo_button_was_pushed(self):
        self._undo_command.undo()

    def __str__(self):
        result = '------ Remote Control ------\n'
        for cmd_index in range(self.MAX_COMMANDS):
            result += '[slot %s ] %s %s\n' % (
                cmd_index,
                self._on_commands[cmd_index].__class__.__name__,
                self._off_commands[cmd_index].__class__.__name__
            )
        return result


if __name__ == '__main__':
    remote_control = RemoteControl()

    light = Light()
    stereo = Stereo()
    ceiling_fan = CeilingFan()

    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)
    stereo_on_command = StereoOnWithCDCommand(stereo)
    stereo_off_command = StereoOffCommand(stereo)
    ceiling_fan_high_command = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_medium_command = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_off_command = CeilingFanOffCommand(ceiling_fan)

    party_macro_on = MacroCommand([
        light_on_command, stereo_on_command, ceiling_fan_high_command
    ])
    party_macro_off = MacroCommand([
        light_off_command, stereo_off_command, ceiling_fan_off_command
    ])

    remote_control.set_command(0, light_on_command, light_off_command)
    remote_control.set_command(1, stereo_on_command, stereo_off_command)
    remote_control.set_command(
        2, ceiling_fan_medium_command, ceiling_fan_off_command
    )
    remote_control.set_command(
        3, ceiling_fan_high_command, ceiling_fan_off_command
    )
    remote_control.set_command(4, party_macro_on, party_macro_off)

    print(remote_control)

    print('"""""""" Simple on/off """""""""')
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)

    print('\n"""""""" Undo """""""""')
    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.undo_button_was_pushed()

    print('\n"""""""" State Undo """""""""')
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.undo_button_was_pushed()

    remote_control.on_button_was_pushed(3)
    remote_control.undo_button_was_pushed()

    print('\n"""""""" Macro """""""""')
    remote_control.on_button_was_pushed(4)
    remote_control.off_button_was_pushed(4)




