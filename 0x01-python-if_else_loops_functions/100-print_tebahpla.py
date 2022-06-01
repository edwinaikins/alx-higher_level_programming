#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print(f"{i if (i % 2 == 0) else (i - 32):c}", end='')
