"""
Requirements:
    Beep uses `play` command.
    PlaySound uses `afplay` command to play files.

    OS X (tested):  
        - sox => `brew install sox`
        - afplay => included with OS X
    Linux
        - sox (or equivalent)
        - afplay equivalent
"""

try:
    import winsound
except ImportError:
    import subprocess
    class winsound:
        SND_FILENAME = 0b00000001
        SND_ASYNC = 0b00000010

        @staticmethod
        def Beep(frequency, duration):
            subprocess.run(['play',
                            '--no-show-progress',
                            '--null',
                            '--channels', '1',
                            'synth', '{:f}'.format(duration/1000.0),
                            'sine', str(frequency)])

        @classmethod
        def PlaySound(cls, sound, flags):
            if not(flags & cls.SND_FILENAME):
                raise NotImplementedError("PlaySound wrapper only supports playing sound files.")

            cmd = subprocess.Popen if flags & cls.SND_ASYNC else subprocess.run
            cmd(['afplay', sound])



if __name__ == '__main__':
    winsound.Beep(2500, 10)
