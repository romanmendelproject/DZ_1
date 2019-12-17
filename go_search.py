import sys
from search.google_search import pars_google

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Ошибка. Слишком мало параметров!")
        sys.exit(1)
    elif len(sys.argv) == 2:
        pars_google(sys.argv[1], 0)
    elif len(sys.argv) == 3:
        try:
            pars_google(sys.argv[1], int(sys.argv[2]))
        except ValueError:
            print("Ошибка. Укажите целое число!")
            sys.exit(1)
    else:
        print("Ошибка. Слишком много параметров!")
        sys.exit(1)
