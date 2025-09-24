"""A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!"""


import random 

gep = random.randint(1, 2)
fej = 1 
iras = 2 

felhasznalo = input("Fej vagy írás?")

if felhasznalo == "fej" and gep == fej :  print("Eltaláltad!")
if felhasznalo == "írás" and gep == fej :  print("Nem találtad el!")
if felhasznalo == "fej" and gep == fej :  print("Eltaláltad!!")
if felhasznalo == "fej" and gep == fej :  print("Eltaláltad!!")

