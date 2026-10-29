import sys


def count_words(text):
    return len(text.split())


def main():
    path = sys.argv[1]
    with open(path) as f:
        text = f.read()
    print(count_words(text))


if __name__ == "__main__":
    main()
