import os
os.system("cls")
from tabulate import tabulate
from datetime import datetime

def mulai():
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

mulai()
    

a = int(input("=> "))


os.system("cls")
def tahap2(ltr, nutri):
    os.system("cls")
    while True :
        os.system("cls")
        lubang = int(input("Masukkan jumlah lubang tanam pada hydroponic yang telah kamu buat\n=> "))
        air = int(lubang*ltr)
        ntr = int(air*nutri)
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
            os.system("cls")
            break
        elif nt3.lower() == 'n':
            pass
            os.system("cls")

if a == 1:
    while True :
        print("""
===================
|   PILIH SAYUR   |
===================
[A] SELADA
[B] KANGKUNG
[C] PAKCOY
[D] SELEDRI

[Z] KEMBALI
""")
        sayur = (input("=> "))
        if sayur.lower() == "a" :
            jdl = """
==========================
|   Kamu telah memilih   |
|      SAYUR SELADA      |                            
==========================
"""
            baw = 0
            bak = 28
            ltr = 1.5
            nutri = 5

        elif sayur.lower() == "b":
            jdl = """
==========================
|   Kamu telah memilih   |
|     SAYUR KANGKUNG     |                            
==========================
"""
            baw = 33
            bak = 48
            ltr = 1.5
            nutri = 5

        elif sayur.lower() == "c" :
            jdl = """
==========================
|   Kamu telah memilih   |
|      SAYUR PAKCOY      |                            
==========================
"""
            baw = 53
            bak = 76
            ltr = 1.5
            nutri = 5

        elif sayur.lower() == "d" :
            jdl = """
==========================
|   Kamu telah memilih   |
|     SAYUR SELEDRI      |                            
==========================
"""
            baw = 80
            bak = 109
            ltr = 1.5
            nutri = 5
        elif sayur.lower() == "z" :
            os.system("cls")
            mulai()
            continue
        else :
            os.system("cls")
            print("\n!!! Tolong masukkan kode dengan benar !!!")
            continue
        os.system("cls")

        pass

        while True :
            print(jdl)
            print("\nSEBELUM MELAKUKAN PENANAMAN SAYUR SELADA PADA HYDROPONIC, YUK SIMAK DULU TUTORIAL DI BAWAH INI YA\n")
            rd = open("tutorial.txt", "r")
            var = rd.readlines()[baw:bak]
            for o in var:
                print(o, end="")

            nt2 = input("\nApakah sudah paham?\n[Y/N]\n=> ")
            if nt2.lower() == "y":
                break
            elif nt2.lower() == "n":
                pass
            os.system("cls")


        tahap2(ltr, nutri)

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

            while True :
                inp3 = input("\nApakah sudah panen?\n[Y/N]\n=> ")
                if inp3.lower() == "n" :
                    pass    
                elif inp3.lower() == "y" :
                    print("Apakah kamu yakin dengan pilihanmu? Jika benar-benar sudah panen maka data penjadwalan akan terhapus")

                    finish= input("\nApakah betul sudah panen? \n[Y/N]\n=> ")
                    if finish.lower() == 'n':
                        pass
                    elif finish.lower() == "y":
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
                break
            break
        

    # elif sayur.lower() == "b" :
    #     print("\nKamu telah memilih sayur Kangkung\n")
    # elif sayur.lower() == "c" :
    #     print("\nKamu telah memilih sayur Pokcoy\n")
    # elif sayur.lower() == "d" :
    #     print("\nKamu telah memilih sayur Seledri\n")
    # break

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
