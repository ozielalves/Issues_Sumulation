from contextlib import redirect_stdout
from functools import cmp_to_key
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

with open("rotulos.in", encoding="utf-8") as f:
    ordered = sorted([line.strip() for line in f.readlines()], key=cmp_to_key(locale.strcoll))

with open("rotulos.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        print("\n".join(ordered))
