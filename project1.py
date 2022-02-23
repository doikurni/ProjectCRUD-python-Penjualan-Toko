snack = [{'INV':'CT01','Rasa':'Barbeque', 'Harga':'7000', 'Kuantitas':'10pc', 'Total':'70.000'},
{'INV':'CT02','Rasa':'Seaweed', 'Harga':'8000', 'Kuantitas':'10pc', 'Total':'80.000'},
{'INV':'CT03','Rasa':'Saltegg', 'Harga':'9000', 'Kuantitas':'10pc', 'Total':'90.000'}]

def Read_Data():
    read = True
    while read != '3':
        print("\n~~~~~~~Snack Sales Report~~~~~~~\n")
        print("1. All Sales data report")
        print("2. Parsial Sales data report")
        print("3. Back to main menu")
        read = input("Silahkan pilih sub menu Read Data [1-3]:  ")
        if read == '1':
            if len(snack) != 0 :
                print('Daftar Penjualan Snack: ')
                for j, i in enumerate(snack) :
                    print(f"{j+1}. INV : {i['INV']}, 'Rasa': {i['Rasa']}, Harga : {i['Harga']}, Kuantitas : {i['Kuantitas']}, Total : {i['Total']}")
            else :
                print('\n~~~~Maaf Produk Yang dimaksud tidak ada~~~~')
            continue
        elif read == '2' :
            if len(snack) != 0 :
                pdct = input('Masukkan Nomor Invoice yang mau dicari: ').upper()
                print(f'List produk yang dicari : {pdct}')
                for j, i in enumerate(snack):
                    if i['INV'] == pdct:
                        print(f"\n{j+1}, INV : {i['INV']},'Rasa': {i['Rasa']}, Harga : {i['Harga']}, Kuantitas : {i['Kuantitas']}, Total : {i['Total']}")
                        break
                else:
                    print('\n~~~~Maaf Produk Yang dimaksud tidak ada~~~~')
            else:
                print('\n~~~~Maaf Produk Yang dimaksud tidak tidak terdaftar~~~~')
        elif read == '3' :
            break
        else:
            print("\n~~~~Pilihan Menu Tidak Ada~~~~")    

def create_data():
    create = True
    while create != '2':
        print("\n~~~~~~~Menambahkan Penjualan~~~~~~~\n")
        print("1. Menambahkan penjualan masuk")
        print("2. Back to main menu")
        create = input("Silahkan pilih sub menu Tambah Data [1-2] : ")
        if create == '1':
                input_numb = input('Masukkan number: ')
                for j, i in enumerate(snack):
                    if len(snack) != 0 :
                        if input_numb == i['INV']:
                            print('\nData yang ingin dicreate sudah ada sebelumnya')
                            break
                else:    
                    inv_product= input('Masukkan INV baru: ')
                    rasa_product= input('Masukan rasa snack: ')
                    harga_product= input('Input harga: ')
                    kuantitas_product= input('Input jumlah pembelian: ')
                    total_product= input('Total: ')

                    print("\n====Simpan Data====\n")
                    print("1. Simpan [YES]")
                    print("2. Batal [NO]")
                    while True:
                        konfirmasi = input('\nApakah data yang ditambahkan mau disimpan? [YES/NO] ').upper()
                        if konfirmasi == 'YES' :
                            snack.append(
                            {'INV' : inv_product,
                            'Rasa' : rasa_product,
                            'Harga' : harga_product,
                            'Kuantitas' : kuantitas_product,
                            'Total': total_product}
                            )
                            print('\nData Terbaru Tersimpan\n')
                            if len(snack) != 0 :
                                for j, i in enumerate(snack) :
                                    print(f"{j+1}. INV : {i['INV']}, 'Rasa': {i['Rasa']}, Harga : {i['Harga']}, Kuantitas : {i['Kuantitas']}, Total : {i['Total']}")
                            break
                        else:
                            if konfirmasi == 'NO' :
                                print("Data batal input")
                                break
                        
        elif create_data == '2':
            break
        else:
            print("\nPilihan menu tidak ada")

def update_data():
    update = True
    while update == True:
        print("\n======Update data penjualan======\n")
        print("1. Update data penjualan produk ")
        print("2. Back to main menu")

        update = input("\nSilahkan pilih sub menu Update Data [1-2] : ")
        if update == '1':
            input_update = input('Masukkan Invoice: ')
            for j, i in enumerate(snack):
                if len(snack) != 0 :
                    if input_update == i['INV']:
                        print(f"\nData penjualan dengan nomor invoice {input_update}")
                        print(f"{j+1}.'INV':{i['INV']}, 'Rasa':{i['Rasa']}, 'Harga':{i['Harga']}, 'Kuantitas':{i['Kuantitas']}, 'Total':{i['Total']}")
                        
                        while True:
                            ask_update = input("\nApakah anda yakin ingin update/edit data penjualan [YES/NO]: ")
                            if ask_update == 'YES' :
                                    update_kolom = input('Pilih Kolom yang ingin diupdate: ')
                                    if update_kolom == 'INV':
                                        new_update = input('\nMasukan invoice Revisi/pembenaran: ')
                                        for j, i in enumerate(snack):
                                            if new_update == i['INV']:
                                                print("\nNomor invoice {} Sudah ada".format(i['INV']))
                                                break
                                            else: 
                                                i['INV'] = new_update 
                                                print("\nData sudah berhasil diupdate")
                                                if len(snack) != 0 :
                                                    for j, i in enumerate(snack) :
                                                        print(f"{j+1}. INV : {i['INV']}, 'Rasa': {i['Rasa']}, Harga : {i['Harga']}, Kuantitas : {i['Kuantitas']}, Total : {i['Total']}\n")
                                                    break
                                    break
                            else:
                                if ask_update == "NO":
                                    print('Invoice Batal Edit')
                                    update_data()
                        break
                    else:
                        print("\nInvoice yang dimaksud tidak ada")
                        break
        elif update == '2':
            break
        else:
            print("\n~~~~~~ Pilihan menu tidak ada ~~~~~~")


def delete_data():
    delete = True
    while delete != '2':
        print("\n======Menghapus data penjualan======\n")
        print("1. Menghapus data penjualan produk ")
        print("2. Back to main menu")
        delete = input("Silahkan pilih sub menu Delete Data [1-2] : ")
        if delete == '1':
            input_inv = input('Masukkan Invoice: ')
            for j, i in enumerate(snack):
                if len(snack) != 0 :
                    if input_inv == i['INV']:
                        print("\n~~~~ Data yang ingin diDELETE tersedia ~~~~")
                        
                        while True:
                            konfirmasi = input('\nApakah data yakin akan dihapus? [YES/NO] ')
                            if konfirmasi == 'YES':
                                for i in range(len(snack)):
                                    if snack[i]['INV'] == input_inv :
                                        del snack[i]
                                        print('\nData berhasil dihapus')
                                    if len(snack) != 0 :
                                        for j, i in enumerate(snack) :
                                            print(f"{j+1}. INV : {i['INV']}, 'Rasa': {i['Rasa']}, Harga : {i['Harga']}, Kuantitas : {i['Kuantitas']}, Total : {i['Total']}")
                                        break
                                break
                            else:
                                if konfirmasi == "NO":
                                    print('Batal delete invoice')
                                    delete_data()
                break                                    
            else:
                print("\n~~~~ Data yang ingin diDELETE tidak tersedia ~~~~")
                delete_data()

        elif delete == '2':
            break
        else:
            print("\n~~~~~~ Pilihan menu tidak ada ~~~~~~")

while True:
    print("\n====Aplikasi Penjualan====\n")
    print("1. Lihat Data Penjualan")
    print("2. Menambahkan Data Penjualan")
    print("3. Edit/Update Data Penjualan")
    print("4. Hapus/Delete Data Penjualan")
    print("5. Exit")
    selected_menu = input("Silahkan Pilih Menu> [1-5] :")

    if selected_menu == '1':
        Read_Data()
    elif selected_menu == '2':
        create_data()
    elif selected_menu == '3':
        update_data()
    elif selected_menu == '4':
        delete_data()
    elif selected_menu == '5':
        print("Thank you & Goodbye !!")
        break
    else:
        print("~~~Pilihan menu yang anda masukkan salah~~~")
                     
