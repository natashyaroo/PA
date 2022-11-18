import os, time, sys

admin = ("admin", "123")

os.system("cls")

user = {
    "tequila": {"password": "samarinda", "saldo": 200000},
    "asteakin": {"password": "bontang", "saldo": 100000},
}

#================================================================================================================== 
def menabung(username):
    print ('')
    print ('==========[MENU MENABUNG]==========')
    print ('Silahkan Menabung.')
    print ('')
    dana_setoran = int(input("Masukan jumlah setoran = "))
    saldo = user[username]["saldo"]
    user[username].update({"saldo": saldo + dana_setoran})
    print ('Anda Berhasil Menabung.')
    

#================================================================================================================== 
def transfer(username):
    print ('')
    print ('==========[MENU TRANSFER]==========')
    print ('Silahkan TRANSFER.')
    print ('')
    tujuan = input("Masukan username tujuan = ")
    saldo_lama = user[username]["saldo"]
    for usertujuan, data in user.items():
        if tujuan == usertujuan:
            if user[username]["saldo"] > 0:
                saldo_lama_tujuan = data["saldo"]
                saldo_tf = int(input("Masukan saldo yang ingin di transfer = "))
                if user[username]["saldo"] > saldo_tf:
                    user[usertujuan].update({"saldo": saldo_lama_tujuan + saldo_tf})
                    user[username].update({"saldo": saldo_lama - saldo_tf})
                    print ('Anda Berhasil Transfer.')


   
           
            

#================================================================================================================== 
def kalkulator_investasi():
    print ('')
    print ('==========[MENU KALKULATOR INVESTASI]==========')
    print ('Silahkan Mulai Perhitungan.')
    print ('')
    setoran = int(input("Masukan dana yang ingin dihitung (Rp.) = "))
    jangka_waktu = int(input("Masukan jangka waktu investasi (bulan) = "))
    return_rate = int(input("Masukan return rate perbulan (%) = "))

    return_bulan = (setoran * return_rate) / 100
    perkiraan_investasi = round(return_bulan * jangka_waktu)
    os.system("cls")

    print("")
    print(f"Dana yang dihitung = Rp.{setoran}")
    print(f"Jangka waktu investasi = {jangka_waktu} bulan")
    print(f"Return rate (%) = {return_rate}%")
    print("")
    print(f"Perkiraan hasil investasi = {perkiraan_investasi}")
  

#================================================================================================================== 
def pengaturan(username):
    print ('Menu ini untuk mengedit username dan password anda.')
    print ('')
    newuser = input("Masukan username baru = ")
    newpwd = input("masukan password baru = ")

    user[username].update({"password": newpwd})
    print ('Anda Berhasil Mengedit Akun anda.')
    

#================================================================================================================== 
def readUser():
    print ("Menampilkan Data Pengguna.")
    for username, data in user.items():
        print(f"Username: {username}")
        print(f"Saldo: {data['saldo']}")
        print()

#==================================================================================================================
def hapusPengguna():
    print ("Menampilkan Data Pengguna.")
    for i in user:
        print(f"{i}")
    hapus = input("Ingin Hapus Data Pengguna Siapa: ")
    del user[hapus]
    print ("Pengguna Berhasil Dihapus.")
    menuAdmin()

#==================================================================================================================
def edit():
    print("Berikut Adalah Akun Admin Yang Terdaftar :")
    for i in admin:
        print(f"{i['Nama']}")

    nama=input("\nNama yang ingin diubah: ")
    for i in admin:
        if nama == i['Nama']:
            i['nama']=input("Masukan nama baru: ")
            i['password']=input("Masukan password baru: ")
            print()

#==================================================================================================================
def login():
    print ('')
    print ('==========[LOGIN SEBAGAI USER]==========')
    print ('Masukkan Username dan Password')
    retry = 0
    while retry < 3:
        log_user = input("masukan username : ")
        log_pwd = input("masukan password : ")
        for username, pwd in user.items():
            if log_user == username and log_pwd == pwd["password"]:
                return username
        retry+=1  
        print("Username atau password salah, pastikan username dan password yang anda masukan benar!")
        print(65*"=")
    print("Kesempatan anda untuk login telah habis\nsilahkan kembali ke menu login")
    time.sleep(5)
    os,system("cls")
    menuUtama()



#=================================================================================================================
def register():
    print ("Masukkan Username, Password, dan Saldo Pengguna Baru ")
    while True:
        try:
            user_register = {}

            username = str(input("Masukkan Username : "))
            if username in user:
                os.system("cls")
                print("username telah terdaftar")
                print("")
                print("Silahkan coba masukan username lagi.")
                
                continue
            else:
                user_register["password"] = str(input("Masukkan Password : "))
                user_register["saldo"] = int(input("Masukkan Saldo    : "))

                user[username] = user_register
        except ValueError:
            print("Username atau Password Yang Tidak Sesuai.")
        else:
            print("Akun anda telah terdaftar")
        kembali = input("Kembali ke menu awal? (y/t) = ")
        if kembali == "y":
            L="/-'\\|"
            for q in range(20):
                time.sleep(0.1)
                sys.stdout.write("\rWaiting"  +L[q % len(L)]+"")
                sys.stdout.flush()
            os.system("cls")
            menuUtama()
        else:
            register()
        print(65*"=")

#==================================================================================================================
def loginAdmin():
    print ('')
    print ('==========[LOGIN SEBAGAI ADMIN]==========')
    ulang = False
    coba = 1
    while ulang == False and coba <= 3:
        print("Masukkan Username dan Password Admin")
        username = str(input("Masukkan Username : "))
        password = str(input("Masukkan Password : "))
   
        if username == admin[0] and password == admin[1]:
            L="/-'\\|"
            for q in range(20):
                time.sleep(0.1)
                sys.stdout.write("\rMemeriksa Username/Password"  +L[q % len(L)]+"")
                sys.stdout.flush()
            os.system("cls")
            print ('Berhasil Login!')
            print("Selamat Bekerja, ", admin[0], " ")
            menuAdmin()
        else:
            print("Username atau Password salah,Pastikan Username atau Password yang anda masukkan benar !")
            # print("Pastikan bahwa akun anda sudah ter-registrasi terlebih dahulu")
            print(65*"=")
            coba += 1
    if coba >=3 :
        print("Kesempatan Anda untuk Login Telah Habis\nSilahkan Kembali Ke Menu Login")
        time.sleep(2)
        os.system("cls")
        menuUtama()

################################################### MENU USER ####################################################
def menuUser(username):
    while True:
        print("===============[SELAMAT DATANG DI TABUNGAN INVESTASI]===============")
        print('Tabungan Investasi Dapat Mempermudah Anda Mengelola Keuangan Anda.')
        print('Anda Dapat Menabung, Cek Saldo, Transfer, Serta Membantu Anda Mengkalkulasikan Investasi Anda.')
        print('Ingin Melakukan Apa Hari Ini?')
        print()
        print(username) 
        print(user[username]["saldo"])
        print()
        print("""
=============================
| [1.] Menabung             |
| [2.] Transfer Saldo       |   
| [3.] Kalkulator Investasi |
| [4.] Pengaturan Akun      |
| [5.] Kembali Ke Menu Utama|
=============================
"""
      )
        pilihan = input("Pilih Menu Yang Ingin Dituju = ")
        if pilihan == "1" or pilihan == "Menabung" or pilihan == "menabung":
            menabung(username)
        elif (
            pilihan == "2"
            or pilihan.lower() == "transfer saldo"
            or pilihan.lower() == "transfer"
            or pilihan.lower() == "tf"
        ):
            transfer(username)
        elif (
            pilihan == "3"
            or pilihan.lower() == "kalkulator investasi"
            or pilihan.lower() == "kalkulator"
        ):
            kalkulator_investasi()
        elif (
            pilihan == "4"
            or pilihan.lower() == "pengaturan akun"
            or pilihan.lower() == "pengaturan"
        ):
            pengaturan(username)
        elif (
            pilihan == "5"
            or pilihan.lower() == "kembali ke menu utama"
            or pilihan.lower() == "kembali"
        ):
            menuUtama()
        else:
            print("Menu tidak terdaftar")
            continue
 
################################################### MENU ADMIN ####################################################
def menuAdmin():
    while True:
        print()
        print("===============[SELAMAT DATANG ADMIN]===============")
        print("""
================================     
| [1.] Lihat Data Pengguna     |
| [2.] Edit Akun Admin         |
| [3.] Menghapus Akun          |
| [4.] Kembali ke Menu         |
================================""")
        try :
            mnuad = int(input('Silahkan Pilih (1/2/3/4): '))
            if mnuad == 1 or mnuad == "Lihat Data Pengguna":
                readUser()
                input("Tekan Enter Untuk Kembali ke Menu Admin.")
            elif mnuad == 2 or mnuad == "Edit Akun Admin":
                edit()
            elif mnuad == 3 or mnuad == "Menghapus Akun":
                hapusPengguna()            
            elif mnuad == 4 or mnuad == "Kembali ke Menu":
                os.system ("cls")
                menuUtama()
            else:
                print('Mohon Input Dengan Benar!')
        except ValueError:
            os.system('cls')
            print("ERORR")
            # continu

################################################### MENU UTAMA #################################################### 
def menuUtama():
    while True:
        os.system("cls")
        print()           
        print("""✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿
SELAMAT DATANG DI TABUNGAN INVESTASI
✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿
========================
| [1.] Login Admin     |
| [2.] Login Pengguna  |
| [3.] Register        |
| [4.] Keluar          |
========================""")
        try:
            x = input('Silahkan Pilih (1/2/3/4): ')
            if x == '1' or x == "Login Admin" :
                loginAdmin()
            elif x == '2'or x == "Login Pengguna" :
                username_login = login()
                if username_login:
                    menuUser(username_login)
            elif x == '3' or x == "Register" :
                register()
            elif x == '4' or x == "Keluar" :
                exit()
            else:
                print('Mohon Input Dengan Benar!')
        except KeyboardInterrupt: #ctrl+c
            print("Tidak terdeteksi diprogram.")
       
menuUtama()

