import os
import csv
import time
import pandas as pd
from datetime import datetime
from tabulate import tabulate



#LOGIN
def login():
    os.system("cls")
    print("======= LOGIN =======\n")
    username = input("Username  : ")
    password = input("Password  : ")
    kali = 1
    loginn = False
    with open("userslog.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == username and row[1] == password:
                loginn = True
                break

    if loginn:
        os.system("cls")
        print("LOGIN BERHASIL\n\nAkan memasuki aplikasi dalam...3")
        time.sleep(1)
        os.system("cls")
        for i in range(3):
            print(f"LOGIN BERHASIL\n\nAkan memasuki aplikasi dalam...{3-i}")
            time.sleep(1)
            os.system("cls")
        mulai()

    else:
        os.system("cls")
        print("Username atau Password tidak sesuai")
        time.sleep(2)
        os.system("cls")
        login()
        
        kali = 1
        while kali < 3 :
            if row[0] == username and row[1] == password :
                print(f"Kamu telah gagal login sebanyak {kali} kali")
                print("Sistem akan kembali ke menu utama dalam...3")
                time.sleep(1)
                os.system("cls")
                for i in range(3):
                    print(f"Sistem akan kembali ke menu utama dalam...{3-i}")
                    time.sleep(1)
                    os.system("cls")
                utama()
            kali += 1



#REGISTRASI
def register():
    os.system("cls")
    print("====== REGISTRASI ======\n")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    with open("userslog.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[0] == username:
                    os.system("cls")
                    print("Username telah dipakai, silahkan buat username baru")
                    time.sleep(2)
                    os.system("cls")
                    register()
                    break
    with open("userslog.csv", "a",newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([username, password])



#PERMULAAN MELAKUKAN LOGIN ATAU REGISTER
def utama():
    while True:
        print("Tekan 1 atau 2\n")
        print("[1] REGISTER")
        print("[2] LOGIN")

        pilihan = input("=> ")
        if pilihan == "1":
            register()
            os.system('cls')
            print('Sedang membuat akunmu....\n')
            time.sleep(2)
            os.system("cls")
            print("REGISTER BERHASIL, akan menuju login dalam...3")
            time.sleep(1)
            os.system("cls")
            for i in range(3):
                print(f"REGISTER BERHASIL, akan menuju login dalam...{3-i}")
                time.sleep(1)
                os.system("cls")
            login()
            break
        elif pilihan == '2':
            login()
            break
        else:
            os.system("cls")
            print("!!! Ketikkan sesuai dengan kode !!!")
            


#PEMBUKAAN APLIKASI
def header():
    print("""
==================================
|   SELAMAT DATANG DI APLIKASI   |
|           HY! PONIC            |                            
==================================
""")
    print("Aplikasi ini membantu kamu untuk budidaya tanaman dalam hydroponic\n\n")
    print("-"*65)
    print("-"*65)
    print("\n\n")
    utama()



#MEMULAI PROGRAM
def mulai():
    os.system("cls")
    print("""
==================================
|   SELAMAT DATANG DI APLIKASI   |
|           HY! PONIC            |                            
==================================
""")
    print("""\n\nPilih jenis tanaman yang ingin kamu budidaya
----------------           ----------------
|  [1]  SAYUR  |           |  [2]  BUAH   |
----------------           ----------------
""")
    main(mulai, tahap2, pilih_syr, pilih_buah, tutorSyrBh, penjadwalan)



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

    elif sayur.lower() == "z" :
        mulai()
            
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

[Z] KEMBALI
""")
    buah = (input("=> "))
    if buah.lower() == "a" :
        jdl = """
==========================
|   Kamu telah memilih   |
|      BUAH ANGGUR       |                            
==========================
"""
        baw = 125
        bak = 145
        ltr = 1.5
        nutri = 5

    elif buah.lower() == "b":
        jdl = """
==========================
|   Kamu telah memilih   |
|    BUAH STRAWBERRY     |                            
==========================
"""
        baw = 149
        bak = 166
        ltr = 1.5
        nutri = 5

    elif buah.lower() == "c" :
        jdl = """
==========================
|   Kamu telah memilih   |
|       BUAH TOMAT       |                            
==========================
"""
        baw = 170
        bak = 196
        ltr = 1.5
        nutri = 5

    elif buah.lower() == "d" :
        jdl = """
==========================
|   Kamu telah memilih   |
|      BUAH PAPRIKA      |                            
==========================
"""
        baw = 201
        bak = 221
        ltr = 1.5
        nutri = 5

    elif buah.lower() == "z" :
        mulai()

    else :
        os.system("cls")
        print("\n!!! Tolong masukkan kode dengan benar !!!")
        pilih_buah(mulai)
        return jdl,baw,bak,ltr,nutri

    os.system("cls")
    return jdl,baw,bak,ltr,nutri



#TUTOR SAYUR DAN BUAH
def tutorSyrBh(jdl, baw, bak):
    while True :
        print(jdl)
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
        print("-"*65)
        print(f"""\n\nMaka dengan {air} liter air\n\nKAMU MEMBUTUHKAN 
========================
|   {ntr} ML NUTRISI   |                                
========================
Dalam setiap kali penjadwalan\n(!!! 3 HARI SEKALI !!!)\n
""")
        print("-"*65)
        print("-"*65)

        nt3 = input("\n\nApakah kamu mau lanjut ke tahap penjadwalan?\n[Y/N]\n=> ")
        if nt3.lower() == "y":
            os.system("cls")
            break
        elif nt3.lower() == 'n':
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



#PENENTUAN PANEN ATAU BELUM
def panen(penjadwalan):
    while True :
        inp3 = input("\nApakah sudah panen?\n[Y/N]\n=> ")
        if inp3.lower() == "n" :
            penjadwalan()
            continue    
        elif inp3.lower() == "y" :
            print("\nApakah kamu yakin dengan pilihanmu? Jika benar-benar sudah panen maka data penjadwalan akan terhapus")

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



#TAHAP PENGUMPULAN SEMUA DEF
def main(mulai, tahap2, pilih_syr, pilih_buah, tutorSyrBh, penjadwalan):
    pick = int(input("=> "))
    os.system("cls")
    if pick == 1:
        jdl, baw, bak, ltr, nutri = pilih_syr(mulai)
        tutorSyrBh(jdl, baw, bak)
        tahap2(ltr, nutri)
        penjadwalan()
        panen(penjadwalan)
            
        exit()

    elif pick == 2:
        jdl, baw, bak, ltr, nutri = pilih_buah(mulai)
        tutorSyrBh(jdl, baw, bak)
        tahap2(ltr, nutri)
        penjadwalan()
        panen(penjadwalan)
        
        exit()

    else :
        os.system("cls")
        print("\n!!! Tolong masukkan kode dengan benar !!!")
        mulai()
        main(mulai, tahap2, pilih_syr, pilih_buah, tutorSyrBh, penjadwalan)



header()
# utama()
# main(mulai, tahap2, pilih_syr, pilih_buah, tutorSyrBh, penjadwalan)
