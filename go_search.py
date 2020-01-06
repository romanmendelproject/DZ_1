import sys
import logging
from search.google_search import pars_google


def main(url, rec):
    if len(url) > 20:
        print("Искомое слово должно быть не более 20 символов")
        sys.exit(1)
    elif int(rec) > 10:
        print("Глубина рекурсии не более 10")
        sys.exit(1)
    else:
        try:
            if int(rec) > 10:
                print("Глубина рекурсии не более 10")
                sys.exit(1)
            else:
                pars_google(url, int(rec))
        except ValueError:
            logging.error('value is not int')
            print("Ошибка. Укажите целое число!")
            sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        logging.error('sys.argv < 2')
        print("Ошибка. Слишком мало параметров!")
        sys.exit(1)
    elif len(sys.argv) == 2:
        main(sys.argv[1], 0)
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        logging.error('sys.argv > 3')
        print("Ошибка. Слишком много параметров!")
        sys.exit(1)
