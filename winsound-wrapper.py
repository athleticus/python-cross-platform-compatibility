"""
OS X requires sox => `brew install sox`

Linux requires similar command (none tested)
"""

try:
    import winsound
except ImportError:
    import subprocess
    class winsound:
        @staticmethod
        def Beep(frequency, duration):
            subprocess.run(['/usr/local/bin/play',
                            '--no-show-progress',
                            '--null',
                            '--channels', '1',
                            'synth', '{:f}'.format(duration/1000.0),
                            'sine', str(frequency)])

if __name__ == '__main__':
    winsound.Beep(2500, 10)
