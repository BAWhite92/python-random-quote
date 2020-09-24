
import random

def main():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = len(quotes) - 1
    rnd = random.randint(0, last)

    print(quotes[rnd], end = "")

    rnd = random.randint(0, last)
    print(quotes[rnd])

    f = open("quotes.txt", "a")
    value = input("Now add your own quote!\n")

    f.write(value)
    f.close()


if __name__== "__main__":
  main()
