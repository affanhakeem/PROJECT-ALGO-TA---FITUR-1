import os
import pandas as pd
from datetime import datetime

tgl = datetime.now().strftime("%d/%m/%y")
while True:
    os.system("cls")
    inp1 = int(input("Penjadwalan pemberian nutrisi ke-> "))
    inp2 = float(input("PH-> "))
    if inp2 < 6:
        lar = "PH UP"
    elif inp2 > 7:
        lar = "PH DOWN"
    else:
        lar = "NETRAL"

    opn= open("data.txt","a")
    opn.write(f"{tgl},{inp1},{inp2},{lar}\n")
    opn.close()

    a = pd.read_csv("data.txt")
    z = a.to_csv("data.csv", index = None)
    b = pd.read_csv("data.csv")
    print(b)
    inp3= input("\nApakah sudah panen [y/n]\n-> ")
    if inp3.lower() == "y":
        opn= open("data.txt","w")
        opn.write("Tanggal,Jadwal,PH,Larutan\n")
        opn.close()
        print("""
============================
|   SELAMAT TANAMAN KAMU   |
|       TELAH PANEN!       |                                
============================
""")
        break
    elif inp3.lower() == 'n':
        pass
