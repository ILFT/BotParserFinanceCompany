
from unicodedata import name
import requests


if __name__ == "__main__":

    r = requests.get("https://smart-lab.ru/q/aas/f")
    print(r.status_code)