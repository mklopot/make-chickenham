import subprocess


class Splitter:
    def __init__(self, threshold, number, hex=True, bits=256):
        self.threshold = threshold
        self.number = number
        self.bits = bits
        self.hex = hex

    def __call__(self, secret):
        cmd = ['ssss-split', '-t{}'.format(self.threshold), '-n{}'.format(self.number), '-s{}'.format(self.bits)]
        if self.hex:
            cmd.append('-x')
        process = subprocess.Popen(cmd,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True)
        stdout, _ = process.communicate(input=secret+"\n")
        output_list = stdout.split("\n")
        return output_list[-self.number-1:-1]
