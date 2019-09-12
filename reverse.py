# Author   = Satria Andhika Adi Saputra
# Codename = ./ExGeneralTz
# Lang = Python2
# Mau Nge-Recode? Apa Ga Malu:)

# Meng-Import Modul Yang Digunakan Di Program Inu
import os
import time
import sys
import random
import time

#WARNA
B='\033[34;1m'
G='\033[32;1m'
P='\033[35;1m'
C='\033[36;1m'
R='\033[31;1m'
W='\033[37;1m'
Y='\033[33;1m'

os.system('clear')

#Banner-Program
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

os.system('clear')
mengetik('#####################################')
mengetik('#### <\> \033[31;1mProgram Information \033[37;1m</> ####')
mengetik('#####################################')
mengetik('- Author       : ./ExGeneralTz')
mengetik('- Name Program : Reverse IP Lookup')
mengetik('- Created Date : 12-09-2019')
print('')

# Meng-Input Data Api
data = raw_input('Name Domain --> ')

# Menghapus Banner Sebelumnya
os.system('clear')

# Execute / Mengambil Data Api
def cek():
    os.system ('curl -s https://api.hackertarget.com/reverseiplookup/?q={}'.format(data))

# Output Data Api
print (G+'--------------------------------------------')
print (R+'     Hasil Reverse IP Web {}        ').format(data)
print (G+'--------------------------------------------')
cek()
print ('')

# Fungsi Def Ini Sebagai Menampilkan Waktu
def waktu():
    a=time.localtime()
    hr=a.tm_hour
    mn=a.tm_min
    sc=a.tm_sec
    return ('{}:{}:{}'.format(hr,mn,sc))

# Akhir Dari Program Ini :'(
print('')
print ('Selesai Pada Jam'), waktu()
os.system('exit')
print ('')
