""" 
Rumus Volume Gas Ideal 
V = nRT / P

Volume Gas Ideal    : V
Tekanan             : P
Mol Gas             : n
Temperatur          : T
Konstanta Gas Ideal : R
"""
print('Kondisi:\n1. Mencari STP\n2. Mencari RTP\n3. Tekanan(atm), Jumlah Mol(mol), Suhu(kelvin)\n4. Tekanan(kilopascal), Jumlah Mol(mol), Suhu(celcius)\n5. Tekanan(atm), Jumlah Mol(mol), Suhu(celcius)\n6. Tekanan(kilopascal), Jumlah Mol(mol), Suhu(kelvin)\n7. Convert\n\n')
print('NB: Jika bilangan bulat dan angka beribu-ribu atau ratusan tidak boleh menggunakan titik(.) ataupun koma(,)\nJika bilangan desimal jangan menggunakan koma(,) tetapi menggunakan titik(.)\n\n')
pilih = int(input('Pilih kondisi: '))
print()

""" Rumus """
def rumus(P,n,T,R):
  return (float(n) * float(R) * float(T)) / float(P)

def rumus2(n,Vm):
  return float(n) * float(Vm)

""" Kondisi """
def STP(n):
  Vm = 22.4
  volume = rumus2(n,Vm)
  print('Keadaan Standar :',volume,'liter')

def RTP(n):
  Vm = 24.4
  volume = rumus2(n,Vm)
  print('Keadaan Kamar :',volume,'liter')

def kondisi1(P,n,T):
  R = 0.082
  volume = rumus(P,n,T,R)
  print('Volume Gas :',volume,'liter')

def kondisi2(P,n,T):
  S = float(T) + 273.15
  R = 8.314
  volume = rumus(P,n,S,R)
  print('Volume Gas :',volume,'liter')

def kondisi3(P,n,T):
  R = 0.082
  S = float(T) + 273.15
  volume =  rumus(P,n,S,R)
  print('Volume Gas :',volume,'liter')

def kondisi4(P,n,T):
  R = 8.314
  volume = rumus(P,n,T,R)
  print('Volume Gas :',volume,'liter')

""" Menu """
if pilih == 1:
  mol = input('Jumlah Mol: ')
  STP(mol)
elif pilih == 2:
  mol = input('Jumlah Mol: ')
  RTP(mol)
elif pilih == 3:
  tekanan = input('Tekanan (atm): ')
  mol = input('Jumlah Zat (mol): ')
  suhu = input('Suhu (kelvin): ')
  kondisi1(tekanan,mol,suhu)
elif pilih == 4:
  tekanan = input('Tekanan (kilopascal): ')
  mol = input('Jumlah Zat (mol): ')
  suhu = input('Suhu (celcius): ')
  kondisi2(tekanan,mol,suhu)
elif pilih == 5:
  tekanan = input('Tekanan (atm): ')
  mol = input('Jumlah Zat (mol): ')
  suhu = input('Suhu (celcius): ')
  kondisi3(tekanan,mol,suhu)
elif pilih == 6:
  tekanan = input('Tekanan (kilopascal): ')
  mol = input('Jumlah Zat (mol): ')
  suhu = input('Suhu (kelvin): ')
  kondisi3(tekanan,mol,suhu)
elif pilih == 7:
  print('Menu:\n1. Convert Suhu Celcius ke Kelvin\n2. Convert Suhu Kelvin ke Celcius\n3. Convert Atm(Atmosfer) ke Kpa(KiloPascal)\n4. Convert Kpa(KiloPascal) ke ATM(Atmosfer)')
  cpilih = int(input('Pilih Menu: '))
  print()

  if cpilih == 1:
    suhu = input('Masukkan Suhu Celcius: ')
    convert = float(suhu) + 273.15
    print('Suhu Celcius:',suhu,'\nSuhu Kelvin:',convert)
  elif cpilih == 2:
    suhu = input('Masukkan Suhu Kelvin: ')
    convert = float(suhu) - 273.15
    print('Suhu Kelvin:',suhu,'\nSuhu Celcius:',convert)
  elif cpilih == 3:
    atm = input('Masukkan Atm(Atmosfer): ')
    convert = float(atm) * 101,325
    print('Atm(Atmosfer):',atm,'\nKpa(KiloPascal):',convert)
  elif cpilih == 4:
    kpa = input('Masukkan Kpa(KiloPascal): ')
    convert = float(kpa) / 101,325
    print('Kpa(KiloPascal):',kpa,'\nAtm(Atmosfer):',convert)
  else:
    print('Tidak ada menu')
else:
  print('Tidak ada kondisi')
