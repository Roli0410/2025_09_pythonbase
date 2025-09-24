"""Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!
 Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""
import random

random_szam = random.randint(1, 3)
guess_number = int(input("Adj meg egy számot 1 és 3 között!"))

if random_szam == guess_number: print("Helyes a találatod!")
else: print("Helytelen a találat")