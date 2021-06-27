__author__ = 'hafid'

import sys
import  time


class ProgressBar:
    def __init__(self, max):
        self.max = max
        self.maxBar = 50;
        self.timeStart = time.time()
        self.timeElapsed = 0
        self.tempElapsedSeconds = time.time()
        self.start()


    def update(self, progress):
        if progress <=0 or self.max <=0 :
            return

        status = ""
        self.timeElapsed = self.timer(self.timeStart, time.time())
        progress = float(progress) / float(self.max)
        block = int(round(self.max * progress)) / (self.max / self.maxBar)

        elapsedSeconds = time.time() - self.tempElapsedSeconds
        if (elapsedSeconds > 1) or (progress == 1):
            self.tempElapsedSeconds = time.time()

            text = "\rPercent: [{0} {1}] [{2}% {3}]{4}"\
                .format( "#"*int(block),
                 "-" * (self.maxBar - int(block)),
                round(progress*100, 1), self.timeElapsed, status)
            sys.stdout.write(text)
            sys.stdout.flush()
    def end(self):
        self.update(self.max)
        print("")
    def start(self):
        try :
            self.update(0)
        except :
            pass
    def timer(self, start, end):
         hours, rem = divmod(end-start, 3600)
         minutes, seconds = divmod(rem, 60)
         return ("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))