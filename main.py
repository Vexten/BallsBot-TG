#BallsBot

from BallsBot import BallsBot
import sys

def main():
    if (len(sys.argv) < 2):
        BallsBot.set_locale('en-US')
    else:
        BallsBot.set_locale(sys.argv[1])
    BallsBot.create()
    print('succ')
    BallsBot.start()

if __name__=='__main__':
    main()