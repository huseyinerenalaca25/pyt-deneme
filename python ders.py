'''
nick= huso
'''
if __name__ == '__main__':
    baslik='Ogrenci Bilgi Sistemi(v1)'
    print (baslik) 

    print('-'*90)
    print(f'| {baslik:^84} |x|')
    
    print('-'*90)

    öğrenci_adları=[]
    öğrenci_soyadları=[]
    öğrenci_numaraları=[]
    try:
     öğrenci_sayısı=int(input("öğrenci sayısını giriniz"))
    except:
       print("lütfen sayısal değer giriniz")
       exit
    for index in range(öğrenci_sayısı):

     öğrenci_adları.append(input(f'{index+1}. Öğrenci Adini Giriniz:'))
     öğrenci_soyadları.append(input(f'{index+1}. Öğrenci Soydini Giriniz:'))
     öğrenci_numaraları.append(input(f'{index+1}. Ogrenci Numarasini Giriniz:'))
    

    '''
    ------------------------------------------------------------------------------------------
    | Isim                 | Soyisim                  | Numara                               |
    ------------------------------------------------------------------------------------------
    |                      |                          |                                      |
    |                      |                          |                                      |
    
    '''
    print('-'*90)
    print(f'|{" "*8} | {"Isim":<30} | {"Soyisim":<25} | {"Numara":<15} |')
    print('-'*90)
    for index in range(öğrenci_sayısı):
      
     print(f'| {index+1:>7} | {öğrenci_adları[index]:<30} | {öğrenci_soyadları[index]:<25} | {öğrenci_numaraları[index]:<15} |')
     
     

    

    
    
    
    
    
    
    