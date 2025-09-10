"""
1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
"""

radius = int(input("Add meg a sugarat"))
PI = 3.14
print(f"Terület:{radius * radius * PI}")
print(f"Kerület:{2 * radius * PI}")