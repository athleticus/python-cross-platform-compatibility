"""
Requirements:
    sox:

        OS X (tested):
            - `brew install sox`
        Linux:
            - Install sox using distro's package manager.
"""

try:
    import winsound
except ImportError:
    import subprocess
    import os
    import signal
    class winsound:
        SND_FILENAME    = 0b00000001
        SND_ASYNC       = 0b00000010
        SND_LOOP        = 0b00000100
        SND_PURGE       = 0b00001000

        _sounds = []
        _sox_exec = '/usr/local/bin/play'

        @classmethod
        def Beep(cls, frequency, duration):
            subprocess.run([cls._sox_exec,
                            '--no-show-progress',
                            '--null',
                            '--channels', '1',
                            'synth', '{:f}'.format(duration/1000.0),
                            'sine', str(frequency)])

        @classmethod
        def PlaySound(cls, sound, flags):
            if sound is None or sound is "NULL":
                return cls._clear()

            if flags & cls.SND_PURGE:
                print("winsound.SND_PURGE flag is ignored.")

            if not(flags & cls.SND_FILENAME | flags & cls.SND_ASYNC):
                raise NotImplementedError("PlaySound wrapper only supports playing sound files.")

            method = subprocess.Popen if flags & cls.SND_ASYNC else subprocess.run
            
            args = [cls._sox_exec, sound, '--no-show-progress',
                            '--null',
                            '--channels', '1']

            if flags & cls.SND_LOOP:
                if not(flags & cls.SND_ASYNC):
                    raise RuntimeError("SND_LOOP requires SND_ASYNC.")
                args.extend(('repeat', '9999999'))

            p = method(args)

            if flags & cls.SND_ASYNC:
                cls._sounds.append(p)

        @classmethod
        def _clear(cls):
            for sound in cls._sounds:
                sound.kill()

            cls.sounds = []

    import atexit
    atexit.register(winsound._clear)




if __name__ == '__main__':
    winsound.Beep(2500, 10)
