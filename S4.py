banyak_data=int(input("Masukkan banyak data :"))
i=1
jumlah_nilai=0
jumlah_data=0
while i<=banyak_data:
    nilai=int(input("Masukkan nilai :"))
    jumlah_nilai+=nilai
    jumlah_data+=1
    rata_rata=jumlah_nilai/jumlah_data
    i+=1
print("rata-rata yang diperoleh :",rata_rata)
    
    

