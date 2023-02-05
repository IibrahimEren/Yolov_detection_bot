import os#dosyaların uzantısını değiştirir

path_folder = r'D:\\Projeler\\train\\labels'#yolu belirledik.dosya olabilir

print()#bosluk
print('path: {}'.format(path_folder))#yolu emin olmak için dizi haline aldı
print()#bosluk
 



#eski  uzantıyı yazmak için'.' kullanıldı
#enter the old extension(webp) : webp'deki resimleri uzantısıyla ekledi
old_extension = '.' + input('enter the old extension(txt) --> ')
#yeni uzantıyı yazmak için '.' kullanıldı
#enter the new extension(jpg):eski uzantı artık jpg formatında oldu
new_extension = '.' + input('enter the new extension(jpg) --> ')
print()#bosluk

files_counter = 0#uzantısı değişen dosyaların sayını sayacak 


#klasör ve dosyaların adlarını scandir ile döndürdük 
#scandir: yol,ad,dosya olup olmadığını hakkında bilgi verir. 
#files_and_folders:yineliyici 
with os.scandir(path_folder) as files_and_folders:
    #for döngüsüne alarak yeniliyicinin üzerinden geçtik 
    for element in files_and_folders:
        #if ile dosya olup olmadığına baktık 
        #element.is_file:öge dosya ise 
        if element.is_file():
            #splitext:yolu ve uzantısını ayrır
            #root:dosyanın yolunu tutar
            #ext: dosyanın uzantısını tutar
            
            #tuple_root_ext = os.path.splitext(element.path)
            #root = tuple_root_ext[0]
            #ext = tuple_root_ext[1]

#asağıdaki kod yukarıyla aynı işlemi yapar.
            root, ext = os.path.splitext(element.path)
            #ext == old_extension: eski uzantının yeni uzantıya eşit olup oolmadığına bakıyor
            if ext == old_extension:
                #yeni uzantı
                new_path = root + new_extension
                #os.rename : yeniden adlandır
                os.rename(element.path, new_path)
                #uzantısı değişen dosyları artırdı   
                files_counter +=1

# path = os.chdir("C:\\Users\\bkerimoglu201\\Desktop\\teknofest\\kod\\images")
# i = 0
# for file in os.listdir(path):
#     new_file_name = "kalp{}.jpg".format(i)
#     os.rename(file,new_file_name)
#     i = i+1
    
print('**RECAP **')
print()
print('Number of files processed: {}' .format(files_counter))
print('extension: from {} to {}' .format(old_extension, new_extension))

