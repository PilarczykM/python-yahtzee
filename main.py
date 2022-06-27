import sys

from yahtzee import YahtzeeGame


def main():
    game = YahtzeeGame()
    game.play()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
