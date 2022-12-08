import os
import time
import csv
from tabulate import tabulate
from datetime import datetime
import pandas as pd


def login():
    os.system("cls")
    print("=====LOGIN=====")
    username = input("Username  :")
    password = input("password  :")
    loginn = False
    with open("userslog.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == username and row[1] == password:
                loginn = True
                break

    if loginn:
        mulai()
    else:
        os.system("cls")
        print("Username dan password tidak sesuai program akan diulang dalam...3")
        time.sleep(2)
        os.system("cls")
        for i in range(3):
            print(f"Username dan password tidak sesuai program akan diulang dalam...{3-i}")
            time.sleep(1)
            os.system("cls")
        os.system("cls")
        login()


def register():
    os.system("cls")
    print("=====REGISTRASI=====")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    with open("userslog.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                # print(row)
                if row[0] == username:
                    os.system("cls")
                    print("Username telah dipakai\nSilahkan buat username yang baru\nprogram akan diulang dalam...3")
                    time.sleep(2)
                    os.system("cls")
                    for i in range(3):
                        print(f"Username telah dipakai\nSilahkan buat username yang baru\nprogram akan diulang dalam...{3-i}")
                        time.sleep(1)
                        os.system("cls")
                    os.system("cls")
                    register()
                    break
    with open("userslog.csv", "a",newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([username, password])


def utama():
    while True:
        print("1. REGISTER")
        print("2. LOGIN")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            register()
            os.system('cls')
            print('Sedang membuat akunmu....')
            time.sleep(2)
            print('REGISTER BERHASIL\nSILAHKAN LOGIN\n\n')
            login()
            break
        elif pilihan == '2':
            login()
            break
        else:
            os.system("cls")
            print("input tidak sesuai masukkan 1 atau 2")
            

def header():
    print("""
==================================
|   SELAMAT DATANG DI APLIKASI   |
|           HY! PONIC            |                            
==================================
""")
    print("Aplikasi ini membantu kamu untuk budidaya tanaman dalam hydroponic\n\n")
    print("-"*65)
    utama()


#MEMULAI PROGRAM
def mulai():
    os.system("cls")
    print("""\n\nPilih jenis tanaman yang ingin kamu budidaya
----------------           ----------------
|  [1]  SAYUR  |           |  [2]  BUAH   |
----------------           ----------------
""")
    main(mulai, tahap2, pilih_syr, pilih_buah, tutorSyrBh, penjadwalan)




#PENGISIAN LUBANG HYDROPONIC
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



#MEMILIH SAYUR
def pilih_syr(mulai):
    print("""
===================
|   PILIH SAYUR   |
===================
[A] SELADA
[B] KANGKUNG
[C] PAKCOY
[D] SELEDRI
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
        bak = 30
        ltr = 1.5
        nutri = 5

    elif sayur.lower() == "b":
        jdl = """
==========================
|   Kamu telah memilih   |
|     SAYUR KANGKUNG     |                            
==========================
"""
        baw = 35
        bak = 53
        ltr = 1.5
        nutri = 5

    elif sayur.lower() == "c" :
        jdl = """
==========================
|   Kamu telah memilih   |
|      SAYUR PAKCOY      |                            
==========================
"""
        baw = 58
        bak = 84
        ltr = 1.5
        nutri = 5

    elif sayur.lower() == "d" :
        jdl = """
==========================
|   Kamu telah memilih   |
|     SAYUR SELEDRI      |                            
==========================
"""
        baw = 88
        bak = 120
        ltr = 1.5
        nutri = 5
            
    else :
            os.system("cls")
            print("\n!!! Tolong masukkan kode dengan benar !!!")
            pilih_syr(mulai)
            return jdl,baw,bak,ltr,nutri

    os.system("cls")
    return jdl,baw,bak,ltr,nutri




#MEMILIH BUAH
def pilih_buah(mulai):
    print("""
===================
|    PILIH BUAH   |
===================
[A] ANGGUR
[B] STOBERI
[C] TOMAT
[D] PAPRIKA

""")
    buah = (input("=> "))
    if buah.lower() == "a" :
        jdl = """
==========================
|   Kamu telah memilih   |
|      BUAH ANGGUR       |                            
==========================
"""
        baw = 0
        bak = 28
        ltr = 1.5
        nutri = 5

    elif buah.lower() == "b":
        jdl = """
==========================
|   Kamu telah memilih   |
|      BUAH STOBERI      |                            
==========================
"""
        baw = 33
        bak = 48
        ltr = 1.5
        nutri = 5

    elif buah.lower() == "c" :
        jdl = """
==========================
|   Kamu telah memilih   |
|       BUAH TOMAT       |                            
==========================
"""
        baw = 53
        bak = 76
        ltr = 1.5
        nutri = 5

    elif pilih_buah.lower() == "d" :
        jdl = """
==========================
|   Kamu telah memilih   |
|      BUAH PAPRIKA      |                            
==========================
"""
        baw = 80
        bak = 109
        ltr = 1.5
        nutri = 5

    else :
        os.system("cls")
        print("\n!!! Tolong masukkan kode dengan benar !!!")
    os.system("cls")
    return jdl,baw,bak,ltr,nutri



#TUTOR SAYUR DAN BUAH
def tutorSyrBh(jdl, baw, bak):
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

#PENJADWALAN DAN CEK PH
def penjadwalan():
    os.system("cls")
    tgl = datetime.now().strftime("%d/%m/%y")
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
    print(tabulate(list.iloc[0:30], headers="keys", tablefmt="fancy_grid", showindex=False))
    print("""
!!! NB !!!
[1] JIKA KETERANGAN LARUTAN "PH DOWN" PERLU DIBERIKAN LARUTAN PH DOWN
[2] JIKA KETERANGAN LARUTAN "PH UP" PERLU DIBERIKAN LARUTAN PH UP
[3] JIKA KETERANGAN LARUTAN "NETRAL" PH AIR SUDAH STABIL
""")


def main(mulai, tahap2, pilih_syr, pilih_buah, tutorSyrBh, penjadwalan):
    pick = int(input("=> "))
    os.system("cls")
    if pick == 1:
            jdl, baw, bak, ltr, nutri = pilih_syr(mulai)
            tutorSyrBh(jdl, baw, bak)
            tahap2(ltr, nutri)
            penjadwalan()

            while True :
                inp3 = input("\nApakah sudah panen?\n[Y/N]\n=> ")
                if inp3.lower() == "n" :
                    penjadwalan()
                    continue    
                elif inp3.lower() == "y" :
                    print("Apakah kamu yakin dengan pilihanmu? Jika benar-benar sudah panen maka data penjadwalan akan terhapus")

                    finish= input("\nApakah betul sudah panen? \n[Y/N]\n=> ")
                    if finish.lower() == 'n':
                        penjadwalan()
                        continue
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
 
    elif pick == 2:
            jdl, baw, bak, ltr, nutri = pilih_buah(mulai)
            tutorSyrBh(jdl, baw, bak)
            tahap2(ltr, nutri)
            penjadwalan()

            while True :
                inp3 = input("\nApakah sudah panen?\n[Y/N]\n=> ")
                if inp3.lower() == "n" :
                    penjadwalan()
                    continue    
                elif inp3.lower() == "y" :
                    print("/nApakah kamu yakin dengan pilihanmu? Jika benar-benar sudah panen maka data penjadwalan akan terhapus")

                    finish= input("\nApakah betul sudah panen? \n[Y/N]\n=> ")
                    if finish.lower() == 'n':
                        penjadwalan()
                        continue
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

    else :
        os.system("cls")
        print("\n!!! Tolong masukkan kode dengan benar !!!")
        mulai()
        main(mulai, tahap2, pilih_syr, pilih_buah, tutorSyrBh, penjadwalan)



header()


# utama()
# mulai()
# start()
# main(mulai, tahap2, pilih_syr, pilih_buah, tutorSyrBh, penjadwalan)

 
# login()
