import os
os.system("cls")
from tabulate import tabulate
from datetime import datetime

print("""
==================================
|   SELAMAT DATANG DI APLIKASI   |
|           HY! PONIC            |                            
==================================
""")

print("Aplikasi ini membantu kamu untuk budidaya tanaman dalam hydroponic\n\n")
print("-"*65)
print("""\n\nPilih jenis tanaman yang ingin kamu budidaya

----------------           ----------------
|  [1]  SAYUR  |           |  [2]  BUAH   |
----------------           ----------------
""")


a = int(input("=> "))
os.system("cls")
if a == 1:
    print("""
===================
|   PILIH SAYUR   |
===================
[A] SELADA
[B] KANGKUNG
[C] POKCOY
[D] SELEDRI
""")
    while True :
        sayur = (input("=> "))
        if sayur.lower() == "a" :
            os.system("cls")
            print("""
==========================
|   Kamu telah memilih   |
|      SAYUR SELADA      |                            
==========================
""")
            pass

            while True :
                print("\nSEBELUM MELAKUKAN PENANAMAN SAYUR SELADA PADA HYDROPONIC, YUK SIMAK DULU TUTORIAL DI BAWAH INI YA\n")
                rd = open("tutorial.txt", "r")
                var = rd.readlines()[0:7]
                for o in var:
                    print(o, end="")

                nt2 = input("\nApakah sudah paham?\n[Y/N]\n=> ")
                if nt2.lower() == "y":
                    break
                elif nt2.lower() == "n":
                    pass
                os.system("cls")


            os.system("cls")
            while True :
                os.system("cls")
                lubang = int(input("Masukkan jumlah lubang tanam pada hydroponic yang telah kamu buat\n=> "))
                air = int(lubang*1.5)
                ntr = int(air*5)
                print(f"""\nJumlah lubang pada hydroponic kamu adalah {lubang}\n\nMAKA KAMU MEMBUTHKAN SEKITAR
=======================
|   {air} LITER AIR   |                                
=======================
Dalam proses penanamanan sayur Selada\n
""")
                print("-"*65)
                print(f"""\n\nMaka dengan {air} liter air\n\nKAMU MEMBUTUHKAN 
========================
|   {ntr} ML NUTRISI   |                                
========================
Dalam setiap kali penjadwalan\n(!!! 3 HARI SEKALI !!!)\n
""")
                print("-"*65)

                nt3 = input("\n\nApakah kamu mau lanjut ke tahap penjadwalan?\n[Y/N]\n=> ")
                if nt3.lower() == "y":
                    break
                    os.system("cls")
                elif nt3.lower() == 'n':
                    pass
                    os.system("cls")


            import pandas as pd
            tgl = datetime.now().strftime("%d/%m/%y")
            while True:
                os.system("cls")
                inp1 = int(input("Penjadwalan pemberian nutrisi ke => "))
                inp2 = float(input("PH air saat ini-> "))
                print("\n")
                if inp2 < 6:
                    lar = "PH UP"
                elif inp2 > 7:
                    lar = "PH DOWN"
                else:
                    lar = "NETRAL"

                opn= open("data.txt","a")
                opn.write(f"{tgl},{inp1},{inp2},{lar}\n")
                opn.close()

                note = pd.read_csv("data.txt")
                port = note.to_csv("data.csv", index = None)
                list = pd.read_csv("data.csv")
                print(tabulate(list.iloc[0:20], headers="keys", tablefmt="fancy_grid", showindex=False))
                print("""
!!! NB !!!
[1] JIKA KETERANGAN LARUTAN "PH DOWN" PERLU DIBERIKAN LARUTAN PH DOWN
[2] JIKA KETERANGAN LARUTAN "PH UP" PERLU DIBERIKAN LARUTAN PH UP
[3] JIKA KETERANGAN LARUTAN "NETRAL" PH AIR SUDAH STABIL
""")
                inp3= input("\nApakah sudah panen [Y/N]\n=> ")
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
            break

        elif sayur.lower() == "b" :
            print("\nKamu telah memilih sayur Kangkung\n")
        elif sayur.lower() == "c" :
            print("\nKamu telah memilih sayur Pokcoy\n")
        elif sayur.lower() == "d" :
            print("\nKamu telah memilih sayur Seledri\n")


elif a == 2 :
    print("""
==================
|   PILIH BUAH   |
==================
[A] ANGGUR
[B] STOBERI
[C] TOMAT
[D] PAPRIKA
    """)
    buah = (input("=> "))
    if buah.lower() == "a" :
        print("\nKamu telah memilih buah Anggur\n")
    elif buah.lower() == "b" :
        print("\nKamu telah memilih buah Stoberi\n")
    elif buah.lower() == "c" :
        print("\nKamu telah memilih buah Tomat\n")
    elif buah.lower() == "d" :
        print("\nKamu telah memilih buah Paprika\n")
    else :
        print("\nPilih A/B/C/D")
