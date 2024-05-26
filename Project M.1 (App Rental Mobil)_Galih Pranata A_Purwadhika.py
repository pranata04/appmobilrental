# Project Modul 1 (PURWADHIKA)
# CASE STUDY : 
# Membuat aplikasi sederhana terdiri dari 5 field dengan 1 field unik (id) pada aplikasi rental mobil

# Program
data_app_rent = []  # Fungsi data collection

def create_data_pelanggan(Id_card, Nama, Alamat, Jenis_Kendaraan, Jumlah_Hari):  # Deklarasi fungsi, menambahkan fungsi pada function
    global data_app_rent  # Deklarasi variabel global
    if ID_UNIK(Id_card):  # Fungsi ID unik, tampilan jika terdapat id yang sama
        print(f"ID Card {Id_card} sudah digunakan. Silakan gunakan ID Card yang berbeda.")
        return
    
    data_pelanggan = {
        'Id_Card': Id_card,  # id unik
        'Nama': Nama,
        'Alamat': Alamat,
        'Jenis_Kendaraan': Jenis_Kendaraan,
        'Jumlah_Hari': Jumlah_Hari  # bersifat int (angka saja)
    }
    data_app_rent.append(data_pelanggan)
    print("Selamat, data anda masuk dalam database ARI Rental Mobil")

def ID_UNIK(Id_card):  # Deklarasi ID unik, menghindari identitas ganda
    global data_app_rent  # Deklarasi variabel global
    for data_pelanggan in data_app_rent:
        if data_pelanggan['Id_Card'] == Id_card:
            return True
    return False

def display_data():  # Fungsi untuk menampilkan database
    global data_app_rent  # Deklarasi variabel global
    if not data_app_rent:  # Fungsi apabila belum ada database yang di input
        print("Database ARI Rental Mobil kosong.")
    else:
        print("Data Pelanggan di Database ARI Rental Mobil:")  # Hasil tampilkan apabila sudah ada data yang masuk dalam databases
        for data_pelanggan in data_app_rent:
            print(f"ID Card: {data_pelanggan['Id_Card']}")
            print(f"Nama: {data_pelanggan['Nama']}")
            print(f"Alamat: {data_pelanggan['Alamat']}")
            print(f"Jenis Kendaraan: {data_pelanggan['Jenis_Kendaraan']}")
            print(f"Jumlah Hari: {data_pelanggan['Jumlah_Hari']}")
            print()  # Menambahkan baris kosong untuk pemisah antar data

def display_data_by_id(Id_card):  # Fungsi menampilkan pencarian databases berdasarkan id
    global data_app_rent  # Deklarasi variabel global
    found = False
    for data_pelanggan in data_app_rent:
        if data_pelanggan['Id_Card'] == Id_card:
            found = True
            print(f"Data pelanggan dengan ID Card {Id_card}:")
            print(f"Nama: {data_pelanggan['Nama']}")
            print(f"Alamat: {data_pelanggan['Alamat']}")
            print(f"Jenis Kendaraan: {data_pelanggan['Jenis_Kendaraan']}")
            print(f"Jumlah Hari: {data_pelanggan['Jumlah_Hari']}")
            break
    if not found:  # Jika data tidak ditemukan
        print(f"Tidak ada data pelanggan dengan ID Card {Id_card}.")

def delete_data_by_id(Id_card):  # Fungsi untuk menghapus data berdasarkan ID
    global data_app_rent  # Deklarasi variabel global
    found = False
    for i, data_pelanggan in enumerate(data_app_rent):
        if data_pelanggan['Id_Card'] == Id_card:
            found = True
            del data_app_rent[i]
            print(f"Data pelanggan dengan ID Card {Id_card} telah dihapus.")
            break
    if not found:  # Jika data tidak ditemukan
        print(f"Tidak ada data pelanggan dengan ID Card {Id_card}.")

def main():
    while True:  # Pengulangan/looping apabila data benar
        print('\nMenu ARI Rental Mobil:')
        print('1. Input Data ke Database')
        print('2. Tampil Semua Data Database ARI Rental Mobil')
        print('3. Tampil Data Berdasarkan ID Pelanggan')
        print('4. Hapus Data Berdasarkan ID Pelanggan')
        print('5. Keluar dari Program')

        Menu = input('Masukan nomor yang ingin dituju: ').strip()
        if Menu == '1':
            Id_card = input('Masukan ID Card Pelanggan: ').strip()
            while ID_UNIK(Id_card):  # Looping apabila ada data yang sudah diinputkan sebelumnya
                print(f"ID Card {Id_card} sudah digunakan. Silakan gunakan ID Card yang berbeda.")
                Id_card = input('Masukan ID Card Pelanggan: ').strip()
            
            Nama = input('Masukan Nama Pelanggan: ').strip()
            Alamat = input('Masukan Alamat Pelanggan: ').strip()
            Jenis_Kendaraan = input('Masukan Jenis Kendaraan Sewa: ').strip()
            Jumlah_Hari = input('Masukan Jumlah Hari Sewa: ').strip()
            try:
                Jumlah_Hari = int(Jumlah_Hari)
                create_data_pelanggan(Id_card, Nama, Alamat, Jenis_Kendaraan, Jumlah_Hari)
            except ValueError:
                print('Data Jumlah Hari harus berupa angka, silahkan input data kembali. Terima kasih.')
        elif Menu == "2":  # Display data berdasarkan databases yang sudah diinput
            display_data()
        elif Menu == '3':  # Fungsi pencarian pelanggan berdasarkan Id dalam databases
            Id_card = input('Masukan ID Pelanggan yang ingin ditampilkan: ')
            display_data_by_id(Id_card)
        elif Menu == '4':  # Fungsi menghapus pelanggan berdasarkan Id dalam databases
            Id_card = input('Masukan ID Pelanggan yang ingin dihapus: ')
            delete_data_by_id(Id_card)
        elif Menu == '5':  # Fungsi keluar program
            print("Terima Kasih Telah Menggunakan App ARI Rental Mobil")
            break
        else:  # Fungsi yang akan berjalan apabila karakter yang dimasukan selain (1,2,3,4)
            print("Data Menu Tidak Sesuai! Silahkan Masukan Data Berdasarkan Menu yang tersedia")

if __name__ == "__main__":
    print("\nSELAMAT DATANG DI APP ARI RENTAL MOBIL")
    print('Kami melayani rental mobil sebagaimana kebutuhan anda sehari-hari')
    print('Silahkan masukan data diri anda sebagaimana pada tampilan menu yang tersedia')
    print('------ KEPUASAN ANDA ADALAH HARAPAN KAMI ------')
    main()
