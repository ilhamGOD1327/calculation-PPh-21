import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# navigasi  sidebar
with st.sidebar:
    selected = option_menu("Pajak Penghasilan", ["Orang Pribadi ber NPWP", 'Orang Pribadi Tidak ber NPWP', "Wajib Pajak Badan"], 
        icons=['cursor', 'cursor','cursor'], default_index=0)
    st.write ("PPh pasal 21 mengatur tentang penghasilan wajib kena pajak Orang pribadi dan Badan Usaha")

# halaman hitung luas persegi panjang
if (selected == 'Orang Pribadi ber NPWP') :
    st.title('Pajak Penghasilan Orang Pribadi ber NPWP')

    pendapatan = st.number_input ("Masukan Nominal Gaji per Bulan ", 0)
    tunjangan = st.number_input ("Masukan Nominal Tunjangan", 0)
    bonus = st.number_input ("Masukan Nominal Penghasilan Tidak Rutin", 0)
    hitung = st.button ("Penghasilan Bruto")


    if hitung:
        hasil = pendapatan + tunjangan + bonus
        st.success (f"Penghasilan Bruto = {hasil}")

        biayajab= 0.05 * (pendapatan + tunjangan + bonus)
        st.success (f"Biaya Jabatan = {biayajab}")
        st.write ("Copy hasil Biaya Jabatan ini untuk mengisi data selanjutnya!")

    biayajabatan = st.number_input ("Masukan Nominal Biaya Jabatan ", .0)
    st.write ("*Biaya jabatan bisa diketahui di button atas*")
    biayapensiun = st.number_input ("Masukan Nominal Biaya Pensiun ", 0)
    iuran = st.number_input ("Masukan Nominal Iuran Lainya", 0)
    totbiy = st.button ("Penghasilan NETTO")

    if totbiy:
        totalbiaya= pendapatan + tunjangan + bonus - biayapensiun - iuran - biayajabatan
        st.success (f"Penghasilan NETTO = {totalbiaya}")

        nettotahun = totalbiaya * 12
        st.success (f"Penghasilan NETTO per Tahun = {nettotahun}")

    pengtahun = st.number_input ("Penghasilan Netto per Tahun")
    wabjak = st.number_input ("Untuk Diri Wajib Pajak", 0)
    st.write ("*Untuk Diri Wajib pajak = 54000000*")
    kawin = st.number_input ("Tambahan karena menikah", 0)
    st.write ("*Bila, Belum menikah = 0 (Tidak Dikenai Pajak)*")
    st.write ("*Sudah menikah = 4500000*")
    tangg =st.number_input ("Pajak Tanggungan", 0)
    st.write ("*Tanggungan 1 = 4500000, Tanggungan 2 = 9000000, Tanggungan 3 = 13500000*")
    st.write ("*Silahkan copy nominal keterangan ini untuk melengkapi data di atas*")
    ptkp = st.button ("Penghasilan Tidak Kena Pajak")

    if ptkp:
        totptkp = wabjak + kawin + tangg
        st.success (f"Total Penghasilan Tidak Kena Pajak = {totptkp}")

        pkp= pengtahun - totptkp
        st.success (f"Penghasilan  Kena Pajak = {pkp}")

    ptkptahun = st.number_input ("Penghasilan Kena Pajak")
    pkptahun = st.button ("Penghasilan Netto < Rp. 60.000.000 ")


    if pkptahun:
        dasar= 0.05 * ptkptahun
       
        st.success (f"PPH Pasal 21 Terhutang = {dasar}")

        dasar1 = dasar / 12
        
        st.success (f"PPh pasal 21 per Bulan = {dasar1}")


    pkp1tahun = st.button ("Penghasilan Netto Rp. 60.000.000 sd. Rp. 250.000.000 ")
    if  pkp1tahun:
        tk1= 0.05 * ptkptahun
        
        st.success (f"PPH Pasal 21 Terhutang = {tk1}")

        tk2= 0.15 * (ptkptahun - tk1)
        
        st.success (f"PPH Pasal 21 Terhutang = {tk2}")

        tk3 = ptkptahun - tk1 - tk2
        
        st.success (f"PPh pasal 21 per Tahun = {tk3}")

        tk4 = tk3 / 12
        
        st.success (f"PPh pasal 21 per Bulan = {tk4}")


    pkp2tahun = st.button ("Penghasilan Netto Rp. 250.000.000 sd. Rp. 500.000.000 ")
    if  pkp2tahun:
        lk1= 0.05 * ptkptahun
        
        st.success (f"PPH Pasal 21 Terhutang = {lk1}")

        lk2= 0.15 * (ptkptahun - lk1)
        
        st.success (f"PPH Pasal 21 Terhutang = {lk2}")

        lk3 = 0.25 * (ptkptahun - lk1 - lk2)
        
        st.success (f"PPH Pasal 21 Terhutang = {lk3}")

        lk4 = ptkptahun - lk1 - lk2 - lk3
        
        st.success (f"PPh pasal 21 per Tahun = {lk4}")   

        lk5 = lk4 / 12
        
        st.success (f"PPh pasal 21 per Bulan = {lk5}")

# halaman hitung Pajak Penghasilan Pegawai Tidak NPWP
if (selected == 'Orang Pribadi Tidak ber NPWP') :
    st.title('Pajak Penghasilan Orang Pribadi Tidak NPWP')

    pendapata = st.number_input ("Masukan Nominal Gaji per Bulan ", 0)
    tunjanga = st.number_input ("Masukan Nominal Tunjangan", 0)
    bonu = st.number_input ("Masukan Nominal Penghasilan Tidak Rutin", 0)
    hitun = st.button ("Penghasilan Bruto")

    if hitun:
        hasil = pendapata + tunjanga + bonu
        
        st.success (f"Penghasilan Bruto = {hasil}")

        biayajab= 0.05 * (pendapata + tunjanga + bonu)
        
        st.success (f"Biaya Jabatan = {biayajab}")
        st.write ("Copy hasil Biaya Jabatan ini untuk mengisi data selanjutnya!")

    biayajabata = st.number_input ("Masukan Nominal Biaya Jabatan ", .0)
    st.write ("*Biaya jabatan bisa diketahui di button atas*")
    biayapensiu = st.number_input ("Masukan Nominal Biaya Pensiun ", 0)
    iura = st.number_input ("Masukan Nominal Iuran Lainya", 0)
    totbi = st.button ("Penghasilan NETTO")

    if totbi:
        totalbiay= pendapata + tunjanga + bonu - biayapensiu - iura - biayajabata
        st.write ("Penghasilan NETTO = ", totalbiay)
        st.success (f"Penghasilan NETTO = {totalbiay}")

        nettotahun = totalbiay * 12
        
        st.success (f"Penghasilan NETTO per Tahun = {nettotahun}")

    pengtahu = st.number_input ("Penghasilan Netto per Tahun")
    wabja = st.number_input ("Untuk Diri Wajib Pajak", 0)
    st.write ("*Untuk Diri Wajib pajak = 54000000*")
    kawi = st.number_input ("Tambahan karena menikah", 0)
    st.write ("*Bila, Belum menikah = 0 (Tidak Dikenai Pajak)*")
    st.write ("*Sudah menikah = 4500000*")
    tang =st.number_input ("Pajak Tanggungan", 0)
    st.write ("*Tanggungan 1 = 4500000, Tanggungan 2 = 9000000, Tanggungan 3 = 13500000*")
    st.write ("*Silahkan copy nominal keterangan ini untuk melengkapi data di atas*")
    ptk = st.button ("Penghasilan Tidak Kena Pajak")

    if ptk:
        totptk = wabja + kawi + tang
       
        st.success (f"Total Penghasilan Tidak Kena Pajak = {totptk}")

        pk= pengtahu - totptk
      
        st.success (f"Penghasilan  Kena Pajak = {pk}")

    ptkptahu = st.number_input ("Penghasilan Kena Pajak")
    pkptahu = st.button ("Penghasilan Netto < Rp. 60.000.000 ")


    if pkptahu:
        dasa= 0.05 * 1.2 * ptkptahu
        
        st.success (f"PPH Pasal 21 Terhutang = {dasa}")

        dasr1 = dasa / 12
       
        st.success (f"PPh pasal 21 per Bulan = {dasr1}")


    pkp1tahu = st.button ("Penghasilan Netto Rp. 60.000.000 sd. Rp. 250.000.000 ")
    if  pkp1tahu:
        t1= 0.05 * 1.2 *ptkptahu
        
        st.success (f"PPH Pasal 21 Terhutang = {t1}")

        t2= 0.15 * 1.2 *(ptkptahu - tk1)
       
        st.success (f"PPH Pasal 21 Terhutang = {t2}")

        t3 = ptkptahu - t1 - t2
        
        st.success (f"PPh pasal 21 per Tahun = {t3}")

        t4 = t3 / 12
        
        st.success (f"PPh pasal 21 per Bulan = {t4}")


    pkp2tahu = st.button ("Penghasilan Netto Rp. 250.000.000 sd. Rp. 500.000.000 ")
    if  pkp2tahu:
        l1= 0.05 * 1.2 * ptkptahu
        
        st.success (f"PPH Pasal 21 Terhutang = {l1}")

        l2= 0.15 * 1.2 * (ptkptahu - l1)
        
        st.success (f"PPH Pasal 21 Terhutang = {l2}")

        l3 = 0.25 * 1.2 *(ptkptahu - l1 - l2)
        
        st.success (f"PPH Pasal 21 Terhutang = {l3}")

        l4 = ptkptahu - l1 - l2 - l3
        
        st.success (f"PPh pasal 21 per Tahun = {l4}")   

        l5 = l4 / 12
        
        st.success (f"PPh pasal 21 per Bulan = {l5}")

if (selected == 'Wajib Pajak Badan') :
    st.title('Wajib Pajak Badan')

    penbruto = st.number_input ("Masukan Nominal Penghasilan Bruto Perusahaan ", 0)

    totbi = st.button ("Penghasilan Bruto < Rp. 500.000.000")
    if totbi:
        st.write ("Tidak Dikenai Pajak", totbi)
        st.success (f"Tidak Dikenai Pajak = {totbi}")

    tobi = st.button ("Penghasilan Bruto Rp. 500.000.000 sd. 4.800.000.000.000")
    if tobi:
        tobi= 0.005 * penbruto
        st.write ("PPh final", tobi)
        st.success (f"PPh final = {tobi}")
    
    st.write ("Bila Pendapatan bruto badan lebih dari Rp. 4.800.000.000 isi lah data berikut ini")

    biypod = st.number_input ("Masukan Nominal Biaya Produksi ", 0)
    bung = st.number_input ("Masukan Nominal Bunga, sewa , dan royalti ", 0)
    premi = st.number_input ("Masukan Nominal Premi Asuransi ", 0)
    promosi = st.number_input ("Masukan Nominal Biaya Promosi", 0)
    administrasi = st.number_input ("Masukan Nominal Biaya Administrasi ", 0)
    biylain = st.number_input ("Masukan Nominal biaya lain-lain ", 0)
    sumbangan = st.number_input ("Masukan Nominal Sumbangan ", 0)
    piutang = st.number_input ("Masukan Nominal Piutang Tak Tertagih ", 0)
    rugi = st.number_input ("Masukan Nominal kerugian", 0)

    totbia = st.button ("Penghasilan Kena Pajak")
    if totbia:
        hitung = penbruto - biypod - bung -premi -promosi- administrasi-biylain-sumbangan-piutang-rugi
      
        st.success (f"Penghasilan Kena Pajak = {hitung}")
        st.write ("*Copy hasil PKP untuk mengisi data selanjutnya*")

    pengnet = st.number_input ("Masukan Nominal PKP Badan", 0)
    st.write ("*Data bisa anda dapatkan di button atas*")
    pph1 = st.button ("Penghasilan Bruto 4.800.000.000.000 sd. 50.000.000.000.000")
    if pph1:
        al = 4800000000
        pph1 = pengnet * al / penbruto
        
        st.success (f"Jumlah PKP dari bagian peredaran bruto yang memperoleh fasilitas =  {pph1}")

        pph2 = pengnet - pph1
        
        st.success (f"Jumlah PKP dari bagian peredaran bruto yang tidak memperoleh fasilitas =  {pph2}")

        pph6 = (0.5 * 0.22) * pph1

        pph7 = 0.22 * pph2
        
        pph8 = pph6 + pph7
        
        st.success (f"Jumlah Pajak penghasilan yang terutang tahun 2022  =  {pph8}")

    pph3 = st.button ("Penghasilan Bruto > 50.000.000.000.000")
    if pph3:
        pph3= 0.22 * pengnet
       
        st.success (f"Jumlah Pajak penghasilan yang terutang tahun 2022 =  {pph3}")
       
