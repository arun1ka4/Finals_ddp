#library yang digunakan
from datetime import datetime

data_akun = (
    {
        "username":"nela124",
        "password":"12345",
        "gems":10,
        "saldo":1000000,
        "akun":"VIP"
    },
    {
        "username":"anggur_muda",
        "password":"yntkts",
        "saldo":300000,
        "gems":10000000,
        "akun":"Biasa"
    }
    )

item_normal = (
    {
        "opsi":"1",
        "item":"Bandage",
        "gems":10
    },
    {   "opsi":"2",
        "item":"Healing potion",
        "gems":7
    },
    {
        "opsi":"3",
        "item":"Two assassin swords",
        "gems":35
    },
    {
        "opsi":"4",
        "item":"Heavy axe",
        "gems":35
    }
    )

item_pass = (
    {
        "opsi":"1",
        "item":"Fire chain blade",
        "gems":100
    },
    {
        "opsi":"2",
        "item":"Ambalabu giant spear",
        "gems":70
    },
    {
        "opsi":"3",
        "item":"Crimson Chainblade",
        "gems":120
    },
    {
        "opsi":"4",
        "item":"Eclipse barrier",
        "gems":150
    },
    {
        "opsi":"5",
        "item":"Hellsing two assassin swords",
        "gems":70
    },
    {
        "opsi":"6",
        "item":"Ultimate Love Heavy axe",
        "gems":100
    }
    )

item_pagi = (
    {
        "opsi":"1",
        "item":"5 Bandages",
        "gems":45
    },
    {
        "opsi":"2",
        "item":"3 Healing potions",
        "gems":20
    },
    {
        "opsi":"3",
        "item":"Purifer gloves",
        "gems":40
    }
)

item_siang = (
    {
        "opsi":"1",
        "item":"Chocolatos",
        "gems":15
    },
    {
        "opsi":"2",
        "item":"3 Healing potions",
        "gems":20
    },
    {
        "opsi":"3",
        "item":"Purifer gloves",
        "gems":40
    }
)

item_malam = (
    {
        "opsi":"1",
        "item":"Chocolatos",
        "gems":15
    },
    {
        "opsi":"2",
        "item":"Wavebreaker sword",
        "gems":20
    },
    {
        "opsi":"3",
        "item":"Shield of shadow",
        "gems":40
    }
)

#maksudnya diskon di sini adalah jumlah gems yang berkurang jika menggunakan voucher ini
voucher = (
    {
        "nama":"2024SukseskanPilkada",
        "diskon":10,
        "syarat":50,
        "dipakai":0,
        "batas":2
    },
    {
        "nama":"Nov11Sebelas",
        "diskon":5,
        "syarat":45,
        "dipakai":0,
        "batas":3
    },
    {
        "nama":"AnnivElKing",
        "diskon":35,
        "syarat":100,
        "dipakai":0,
        "batas":1
    }
)

top_up = (
    {
        "opsi":"1",
        "gems":10,
        "saldo":15000
    },
    {
        "opsi":"2",
        "gems":45,
        "saldo":50000
    },
    {
        "opsi":"3",
        "gems":60,
        "saldo":70000
    },
    {
        "opsi":"4",
        "gems":100,
        "saldo":125000
    }
)

def login():
    print("\n                     ┍━━━━━━━━━━━━━━━☽【❖】☾━━━━━━━━━━━━━━━┑")
    print("                                 ECLIPSE KINGDOM ")
    print("                     ┕━━━━━━━━━━━━━━━☽【❖】☾━━━━━━━━━━━━━━━┙ ")
    print("\n                                    ▐██▄██▄█▌")
    print("                            █▄█▄█▄█▄█▐█████▌█▄█▄█▄█▄█")
    print("                            ███┼█████▐█████▌█████┼███")
    print("                            █████████▐██┼██▌█████████")
    print("\nDengan kekuatan yang mengalir dalam setiap jiwa, masuklah dan mulai petualanganmu")
    
    kesempatan = 3
    while kesempatan > 0:
        username_saya = input("\nUsername: ")
        password = input("Password: ")

        berhasil = False 
        
        for data in data_akun:
            if data["username"] == username_saya and data["password"] == password:
                berhasil = True
                menu_utama(username_saya)
                break 
        
        if berhasil:
            break 
        else:
            kesempatan -= 1
            if kesempatan > 0:
                print(f"Username atau password anda salah. Kesempatan login tersisa {kesempatan}")
            else:
                print("Kesempatan login anda telah habis, silahkan ulang programnya...")
                exit()

def menu_utama(username_saya):
    while True:
        print("\n┍━━━━━━━━━━━━━━━☽【❖】☾━━━━━━━━━━━━━━━┑")
        print("        Selamat Datang Pejuang ")
        print("┕━━━━━━━━━━━━━━━☽【❖】☾━━━━━━━━━━━━━━━┙ ")
        print(f"Pejuang {username_saya} telah kembali...")
        print("1. Item normal")
        print("2. Item pass")
        print("3. Item event")
        print("4. Top up gems")
        print("5. Lihat gems")
        print("6. Kembali")
        choose = input("Opsi: ")
        if choose == "1":
            pembelian_normal(username_saya)
        elif choose == "2":
            pembelian_pass(username_saya)
        elif choose == "3":
            pembelian_event(username_saya)
        elif choose == "4":
            proses_top_up(username_saya)
        elif choose == "5":
            print("╭──── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ────╮")
            print("       Lihat Gems")
            print("╰──── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ────╯")
            for gems in data_akun:
                if gems["username"] == username_saya:
                    print(f"Gems yang anda miliki: {gems['gems']} gems")
                    break
            return menu_utama(username_saya)
        elif choose == "6":
            login()
            break
        else:
            print("Tidak ada opsi yang anda pilih, silahkan sesuaikan pilihan anda...")
            continue

def pembelian_normal(username_saya):
    print("╭──── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ────╮")
    print("       Item Normal")
    print("╰──── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ────╯")
    
    for data_item in item_normal:
        print(f"{data_item['opsi']}. {data_item['item']} - Harga: {data_item['gems']} gems")
    print("0. Kembali ke menu utama")
    
    while True:
        try:
            opsi = input("\nPilih item (masukkan nomor opsi): ")
            if opsi == "0":
                return menu_utama(username_saya)
            jumlah = int(input("Jumlah item: "))
            break
        except ValueError:
            print("Jumlah yang Anda masukkan tidak valid. Harap masukkan angka.")
            continue
    print("Masukkan kode hadiah untuk mendapatkan bonus spesial...")
    kode_hadiah = input("Kode: ")

    item_terpilih = None
    kode_benar = None
    
    for data_item in item_normal:
        if data_item["opsi"] == opsi:
            item_terpilih = data_item
            break

    if kode_hadiah:
        for kode in voucher:
            if kode["nama"] == kode_hadiah:
                kode_benar = kode
                break

    if item_terpilih:
        for status in data_akun:
            if status["username"] == username_saya:
                total_harga = item_terpilih["gems"] * jumlah
                diskon = 0
                harga_diskon = total_harga
                if status["gems"] >= total_harga:

                    if kode_benar:
                        if kode_benar["dipakai"] < kode_benar["batas"]:
                            if total_harga >= kode_benar["syarat"]:
                                kode_benar["dipakai"] += 1
                                diskon = kode_benar["diskon"]
                                harga_diskon = total_harga - diskon
                            else:
                                print(f"\nVoucher {kode_hadiah} tidak berlaku karena total harga Anda kurang dari {kode_benar['syarat']} gems..")
                        else:
                            print(f"\nVoucher {kode_hadiah} telah mencapai batas penggunaan sehingga tidak dapat digunakan...")
                    elif kode_hadiah:
                        print(f"\nKode {kode_hadiah} yang Anda masukkan tidak valid...")

                    print(f"\nItem yang Anda beli: {item_terpilih['item']}")
                    print(f"Jumlah item: {jumlah}")
                    print(f"Harga awal: {total_harga} gems")
                    print(f"Diskon: {diskon} gems")
                    print(f"Harga setelah diskon: {harga_diskon} gems")
                    print(f"\nHarga yang harus dibayar: {harga_diskon} gems")
                    pilih = input("Apakah Anda ingin membeli? (ya/tidak): ").lower()

                    if pilih == "ya":
                        if status["gems"] >= harga_diskon:
                            status["gems"] -= harga_diskon
                            print(f"Pembelian berhasil! {jumlah} {item_terpilih['item']} telah dibeli...")
                            print(f"Gems Anda sekarang: {status['gems']} gems")
                            return menu_utama(username_saya)
                        else:
                            print("\nGems Anda tidak cukup untuk membeli item ini...")
                            return menu_utama(username_saya)
                    elif pilih == "tidak":
                        print("\nPembelian dibatalkan...")
                        return menu_utama(username_saya)
                    else:
                        print("\nPilihan tidak valid, pembelian dibatalkan...")
                        return menu_utama(username_saya)
                else:
                    print("\nGems Anda tidak cukup untuk membeli item ini...")
                    return menu_utama(username_saya)
    else:
        print("\nOpsi yang Anda pilih tidak ada, silakan sesuaikan pilihan Anda...")
        return menu_utama(username_saya)

def pembelian_pass(username_saya):
    print("╭──── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ────╮")
    print("        Item Pass")
    print("╰──── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ────╯")

    for data_item in item_pass:
        print(f"{data_item['opsi']}. {data_item['item']} - Harga: {data_item['gems']} gems")
    print("0. Kembali ke menu utama")
    
    while True:
        try:
            opsi = input("\nPilih item (masukkan nomor opsi): ")
            if opsi == "0":
                menu_utama(username_saya)
                return
            jumlah = int(input("Jumlah item: "))
            break
        except ValueError:
            print("Jumlah yang Anda masukkan tidak valid. Harap masukkan angka.")
            continue
    print("Masukkan kode hadiah untuk mendapatkan bonus spesial...")
    kode_hadiah = input("Kode: ")

    item_terpilih = None
    kode_benar = None

    for data_item in item_pass:
        if data_item["opsi"] == opsi:
            item_terpilih = data_item
            break

    if kode_hadiah:
        for kode in voucher:
            if kode["nama"] == kode_hadiah:
                kode_benar = kode
                break

    if item_terpilih:

        for status in data_akun:
            if status["username"] == username_saya:
                if status["akun"] == "VIP":  
                    total_harga = item_terpilih["gems"] * jumlah
                    diskon = 0
                    harga_diskon = total_harga
                    if status["gems"] >= total_harga:

                        if kode_benar:
                            if kode_benar["dipakai"] < kode_benar["batas"]:
                                if total_harga >= kode_benar["syarat"]:
                                    diskon = kode_benar["diskon"]
                                    harga_diskon = total_harga - diskon
                                    kode_benar["dipakai"] += 1
                                else:
                                    print(f"\nVoucher {kode_hadiah} tidak berlaku karena total harga Anda kurang dari {kode_benar['syarat']} gems.")
                            else:
                                print(f"\nVoucher {kode_hadiah} telah mencapai batas penggunaan sehingga tidak dapat digunakan")
                        else:
                            print(f"\nKode {kode_hadiah} yang Anda masukkan tidak valid...")

                        print(f"\nItem yang Anda beli: {item_terpilih['item']}")
                        print(f"Jumlah item: {jumlah}")
                        print(f"Harga awal: {total_harga} gems")
                        print(f"Diskon: {diskon} gems")
                        print(f"Harga setelah diskon: {harga_diskon} gems")
                        print(f"\nHarga yang harus dibayar: {harga_diskon} gems")
                        pilih = input("Apakah Anda ingin membeli? (ya/tidak): ").lower()

                        if pilih == "ya":
                            if status["gems"] >= harga_diskon:
                                status["gems"] -= harga_diskon
                                print(f"Pembelian berhasil! {jumlah} {item_terpilih['item']} telah dibeli.")
                                print(f"Gems Anda sekarang: {status['gems']} gems")
                                return menu_utama(username_saya)
                            else:
                                print("\nGems Anda tidak cukup untuk membeli item ini...")
                                return menu_utama(username_saya)
                        elif pilih == "tidak":
                            print("\nPembelian dibatalkan...")
                            return menu_utama(username_saya)
                        else:
                            print("\nPilihan tidak valid, pembelian dibatalkan...")
                            return menu_utama(username_saya)
                    else:
                        print("\nGems Anda tidak cukup untuk membeli item ini...")
                        return menu_utama(username_saya)
                else:
                    print("\nAkun Anda belum VIP. Item pass hanya dapat dibeli untuk akun VIP...")
                    return menu_utama(username_saya)
    else:
        print("Opsi yang Anda pilih tidak ada, silakan sesuaikan pilihan Anda...")
        return menu_utama(username_saya)

def pembelian_event(username_saya):
    print("╭──── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ────╮")
    print("       Item Event")
    print("╰──── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ────╯")
    
    waktu_sekarang = datetime.now().hour

    if 5 <= waktu_sekarang < 12:
        judul = "Pagi: Awal Petualangan"
        data_item = item_pagi
    elif 12 <= waktu_sekarang < 18:
        judul = "Siang: Saatnya Beraksi"
        data_item = item_siang
    else:
        judul = "Malam: Misteri Menanti"
        data_item = item_malam

    print(f"{judul}")
    for item in data_item:
        print(f"{item['opsi']}. {item['item']} - Harga: {item['gems']} gems")
    print("0. Kembali ke menu utama")
    
    while True:
        opsi = input("\nPilih item (masukkan nomor opsi): ")
        if opsi == "0":
            menu_utama(username_saya)

        try:
            jumlah = int(input("Jumlah item: "))
            break  
        except ValueError:
            print("Jumlah yang Anda masukkan tidak valid. Harap masukkan angka.")
            continue 

    print("Masukkan kode hadiah untuk mendapatkan bonus spesial...")
    kode_hadiah = input("Kode: ")

    item_terpilih = None
    kode_benar = None
    
    for item in data_item:
        if item["opsi"] == opsi:
            item_terpilih = item
            break

    if kode_hadiah:
        for kode in voucher:
            if kode["nama"] == kode_hadiah:
                kode_benar = kode
                break

    if item_terpilih:
        for status in data_akun:
            if status["username"] == username_saya:
                total_harga = item_terpilih["gems"] * jumlah
                diskon = 0
                harga_diskon = total_harga
                if status["gems"] >= total_harga:
                    if kode_benar:
                        if kode_benar["dipakai"] < kode_benar["batas"]:
                            if total_harga >= kode_benar["syarat"]:
                                diskon = kode_benar["diskon"]
                                harga_diskon = total_harga - diskon
                                kode_benar["dipakai"] += 1
                            else:
                                print(f"\nVoucher {kode_hadiah} tidak berlaku karena total harga Anda kurang dari {kode_benar['syarat']} gems...")
                                harga_diskon = total_harga
                        else:
                            print(f"\nVoucher {kode_hadiah} telah mencapai batas penggunaan sehingga tidak dapat digunakan...")
                    else:
                        print(f"\nKode {kode_hadiah} yang Anda masukkan tidak valid...")

                    print(f"\nItem yang Anda beli: {item_terpilih['item']}")
                    print(f"Jumlah item: {jumlah}")
                    print(f"Harga awal: {total_harga} gems")
                    print(f"Diskon: {diskon} gems")
                    print(f"Harga setelah diskon: {harga_diskon} gems")
                    print(f"\nHarga yang harus dibayar: {harga_diskon} gems")
                    pilih = input("Apakah Anda ingin membeli? (ya/tidak): ").lower()

                    if pilih == "ya":
                        if status["gems"] >= harga_diskon:
                            status["gems"] -= harga_diskon
                            print(f"Pembelian berhasil! {jumlah} {item_terpilih['item']} telah dibeli...")
                            print(f"Gems Anda sekarang: {status['gems']} gems")
                            return menu_utama(username_saya)
                        else:
                            print("\nGems Anda tidak cukup untuk membeli item ini...")
                            return menu_utama(username_saya)
                    elif pilih == "tidak":
                        print("\nPembelian dibatalkan...")
                        return menu_utama(username_saya)
                    else:
                        print("\nPilihan tidak valid, pembelian dibatalkan...")
                        return menu_utama(username_saya)
                else:
                    print("\nGems Anda tidak cukup untuk membeli item ini...")
                    return menu_utama(username_saya)
    else:
        print("Opsi yang Anda pilih tidak ada, silakan sesuaikan pilihan Anda...")
        return menu_utama(username_saya)
        
def proses_top_up(username_saya):
    print("\n┏━━━━━━✦❘༻༺❘✦━━━━━━┓")
    print("    Top Up Gems")
    print("┗━━━━━━✦❘༻༺❘✦━━━━━━┛")
    
    while True:
        print("\nPilih opsi top-up:")
        for isi_gems in top_up:
            print(f"{isi_gems['opsi']}. {isi_gems['gems']} Gems - Saldo: Rp{isi_gems['saldo']}")
        print("0. Kembali ke menu utama")

        opsi = input("\nMasukkan opsi: ")
        if opsi == "0":
            break  

        gems_terpilih = None
        for gems in top_up:
            if gems["opsi"] == opsi:
                gems_terpilih = gems
                break

        if gems_terpilih:

            for data in data_akun:
                if data["username"] == username_saya:
                    if data["saldo"] >= gems_terpilih["saldo"]: 
                        data["saldo"] -= gems_terpilih["saldo"]
                        data["gems"] += gems_terpilih["gems"]
                        print(f"\nAnda berhasil top-up: {gems_terpilih['gems']} gems")
                        print(f"Gems anda sekarang: {data['gems']}")
                        print(f"Saldo anda tersisa: Rp{data['saldo']}")
                        menu_utama(username_saya)
                    else:
                        print("\nSaldo Anda tidak cukup untuk membeli gems ini.")
                    break
        else: 
            print("\nPilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    login()
