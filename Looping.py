#!/usr/bin/env python
# coding: utf-8

# In[2]:


#mencetak angka 1-10

for i in range(1,11):
    print(i, end=" ")


# In[4]:


#mencetak angka 10 20 30 --- 100

for i in range(10,101,10):
    print(i, end=" ")


# In[5]:


for i in range(1,11):
    print(i * 10, end=" ")


# In[6]:


#mencetak angka 10 9 8 7 .... 1

for i in range(1,11):
    print(11 - i, end= " ")


# In[13]:


for i in range(10,0,-1):
    print(i, end= " ")


# In[26]:


#mencetak angka 1 -2 3 -4 5 -6 ...10
sign = -1
for i in range(1,11):
    sign = sign * -1
    print(i * sign, end = " ")


# In[27]:


sign = 1
for i in range(1,11):
    print(i * sign, end = " ")
    sign = sign * -1


# In[46]:


#mencari bilangan faktorial
# input = 3, output= 3 * 2 * 1 * =6
# input = 4, output= 4 * 3 * 2 * 1 =24

bil = int(input('isikan bilangan:'))

hasil = 1 

for i in range(1, bil+1):
    hasil = hasil * i

print(f"{bil}! adalah {hasil}")


# In[64]:


bil = int(input('isikan bilangan:'))

hasil = 1 
label =""
for i in range(1, bil+1):
    hasil = hasil * i
    if i < bil: 
        label = label + str((bil+1) - i) + " * "
    else:
        label = label + str((bil+1) - i)
print(f"{bil}! adalah {hasil}")
print(f"{label} = {hasil}")


# In[68]:


#menghitung pangkat

bil = int(input("isikan bilangan:"))
pangkat = int(input("isikan bilangan:"))
hasil = 1
for i in range (1, pangkat+1):
    hasil *= bil
    
print(f"{bil} pangkat {pangkat} adalah {hasil}")


# In[96]:


## mencetak bilangan prima atau bukan
#bil. prima adalah bilangan yang hanya bisa dibagi dengan 1 dan bilangan itu sendiri=> 2 faktor

bil = int(input("isikan bilangan:"))
jumlah = 0
for i in range(1, bil + 1):
    sisa = bil % i
    if sisa == 0:
        jumlah = jumlah + 1
    
if jumlah == 2 :
    print(f"{bil} adalah bilangan prima {jumlah}")
else :
    print(f"{bil} adalah bukan bilangan prima {jumlah}")
    


# In[97]:


bil = int(input("isikan bilangan:"))
keterangan = "bilangan prima"

for i in range(2, bil):
    sisa = bil % i
    if sisa == 0:
        keterangan = "bukan bilangan PRIMA" 
        break 
        

print(f"{bil} adalah {keterangan}")


# In[95]:


#break dan continue

for i in range(1,100):
    print(i, end = " ")
    if  i == 5:
        break
print()

for j in range(1,10):
    if j == 5:
        continue
    print(j, end = " ")


# In[118]:


#looping untuk string, menghitung huruf vokal a=?, i=?, u=?, e=?, o=?
kalimat = input("isikan kalimat:") 

vokal_a = 0
vokal_i = 0
vokal_u = 0
vokal_e = 0
vokal_o = 0
for i in kalimat:
    if i == 'a':
        vokal_a += 1
    elif i == 'i':  
        vokal_i += 1
    elif i == 'u':  
        vokal_u += 1  
    elif i == 'e':  
        vokal_e += 1
    elif i == 'o':  
        vokal_o += 1
        
print(f"jumlah huruf a:{vokal_a}\n jumlah huruf i:{vokal_i}\n jumlah huruf u:{vokal_u}\n \n jumlah huruf e:{vokal_e}\n \n jumlah huruf o:{vokal_o}") 
total = vokal_a+vokal_i+vokal_u+vokal_e+vokal_o
print("total huruf :",total)


# In[117]:


#kalimat palindrome atau bukan
#palindrome adalah kalimat yang dibaca dari kiri ke kanan == kanan ke kiri
#katak =>palindrome
#kasur => rusak

kalimat = input ("isikan kalimat")
panjang = len(kalimat)

for i in range(0,panjang):
    kika = kalimat[i]
    kaki = kalimat [panjang - i-1]
    print(kika,kaki)


# In[131]:


ulang = "Y"
while(ulang== "Y"):
    kalimat = input ("isikan kalimat:")
    panjang = len(kalimat)
    keterangan = "PALINDOREME"
    for i in range(0,panjang):
        kika = kalimat[i].lower()
        kaki = kalimat [panjang - i-1].lower()
        if kika != kaki:
            keterangan = "BUKAN PALINDROME"
            break 
    print(f"{keterangan}")
    jawab =""
    while(jawab!="Y" and jawab !="T"):
        jawab = input("apakah mau mengulang program(Y/T)?:")
    ulang = jawab


# In[134]:


#NEsted FOR

for i in range(1,5):
    for j in range(1,5):
        print(f'i:(i) dan j:{j}')

