# coding=utf-8
import time
import argparse
import platform




class UserManager:

    def __init__(self):
        self.running = True

        self.BLUE = '\033[94m'
        self.GREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.NOCOLOR = '\033[0m'

        self.parser = argparse.ArgumentParser(description=self.GREEN + 'Simple bot'
                                                                       'prototyping' + self.NOCOLOR)
        self.parser.add_argument('--directory', '-d', help='path to directory')

        # TODO: implement ticks and a good event loop
        # self.TICKS_PER_SECOND = 25
        # self.SKIP_TICKS = 1000 / self.TICKS_PER_SECOND
        # self.MAX_FRAMESKIP = 5
        # self.startTime = 0
        # self.next_tick = 0

    def main(self):
        # self.startTime = self.getStartTime()
        # self.next_tick = self.startTime


        print platform.system()
        args = self.parser.parse_args()
        print args

        self.setup()

    def getStartTime(self):
        return int(round(time.time() * 1000))

    # ------------------------------------------------------------------------

    def getTickCount(self):
        return self.startTime

    # ------------------------------------------------------------------------

    def setup(self):
        print "In Setup"
        self.eventLoop()

    # ------------------------------------------------------------------------

    def eventLoop(self):
        while self.running:
            self.update()
            time.sleep(1)
        # print "Before loop"
        # loops = 0
        # while self.getTickCount() > self.next_tick and loops < self.MAX_FRAMESKIP:
        #     # self.update()
        #     self.next_tick += self.SKIP_TICKS
        #     print next_tick
        #     loops = loops + 1
        #     print loops

            # If needed render here. Interpolation is not set. If needed add

    # ------------------------------------------------------------------------

    def sendTweet(self, message):
        print "A random tweet"
    # THIS IS THE UPDATE LOOP - DO WHATEVER STUFF NEEDS TO BE DONE HERE
    # ------------------------------------------------------------------------

    def update(self):
        print "Update"

    # ------------------------------------------------------------------------

    def closeProgram(self):
        print "Program closed"


# ----------------------------------------------------------------------------

if __name__ == '__main__':
    prog = UserManager()
    prog.main()
