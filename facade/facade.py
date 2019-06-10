class Dvd:

    def on(self):
        print('Dvd ON')

    def off(self):
        print('Dvd OFF')

    def eject(self):
        print('Dvd eject')

    def stop(self):
        print('Movie stop')

    def play(self, movie):
        print('Play movie %s' % movie)


class Amplifier:

    def on(self):
        print('Amplifier ON')

    def off(self):
        print('Amplifier OFF')

    def set_dvd(self, dvd):
        print('Set dvd %s' % dvd)

    def set_surround_sound(self):
        print('Surround sound is enabled')

    def set_volume(self, level):
        print('Volume is set to %s' % level)


class Lights:

    def dim(self, dim):
        print('Lights dimersion %s' % dim)

    def on(self):
        print('Lights ON')

    def off(self):
        print('Lights OFF')


class Screen:

    def down(self):
        print('Move screen down')

    def up(self):
        print('Move screen up')


class Popper:

    def on(self):
        print('Popper ON')

    def off(self):
        print('Popper OFF')

    def pop(self):
        print('Popper pop')


class Projector:

    def on(self):
        print('Projector ON')

    def off(self):
        print('Projector OFF')

    def wide_screen_mode(self):
        print('Projector set to wide screen mode')


class HomeTheaterFacade:

    def __init__(self, amp, dvd, projector, screen, lights, popper):
        self._amp = amp
        self._dvd = dvd
        self._projector = projector
        self._screen = screen
        self._lights = lights
        self._popper = popper

    def watch_movie(self, movie):
        print('Get ready to watch a movie...')
        self._popper.on()
        self._popper.pop()
        self._lights.dim(10)
        self._screen.down()
        self._projector.on()
        self._projector.wide_screen_mode()
        self._amp.on()
        self._amp.set_dvd(self._dvd)
        self._amp.set_surround_sound()
        self._amp.set_volume(5)
        self._dvd.on()
        self._dvd.play(movie)

    def end_movie(self):
        print('Shuttong movie theater down...')
        self._popper.off()
        self._lights.on()
        self._screen.up()
        self._projector.off()
        self._amp.off()
        self._dvd.stop()
        self._dvd.eject()
        self._dvd.off()


if __name__ == '__main__':
    home_theater = HomeTheaterFacade(
        Amplifier(), Dvd(), Projector(), Screen(), Lights(), Popper()
    )
    home_theater.watch_movie('Raiders of the Lost Ark')
    home_theater.end_movie()
