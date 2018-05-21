import os,os.path,shutil,fnmatch

root_directory = os.getcwd()
directory_files = os.listdir(root_directory) # ambil semua file dan folder di direktori tersebut

#direktori ekstensi - berisi nama folder dan ekstensi yang termasuk di dalamnya
exts = {
"Applications": ['.exe'],
"Codes": ['.py','.java','.c','.cpp','.rb','.asm','.php','.html','.css','.js','.lua','.jar','.o','.obj'],
"Musics": ['.mp3','.ogg','.wav'],
"Videos": ['.mp4','.3gp','.avi'],
"Pictures": ['.jpg','.jpeg','.png','.bmp','.gif'],
"Archives": ['.zip','.rar','.7zip','.tar','.iso','.tar.gz'],
"Documents": ['.docx','.doc','.pdf','.txt','.ppt','.pptx','.ppsx','.pptm',
             '.docm','.dotx','.dotm','.docb','.xlsx','.xlsm','.xltx',
             '.xltm','.xlsb','.xla','.xlam','.xll','.xlw',
             '.ACCDB','.ACCDE','.ACCDT','.ACCDR','.pub',
             '.potx','.potm','.ppam','.ppsm','.sldx','.sldm']
}


def organize_files_by_extension():
    for File in directory_files:
        #typ = nama folder, lis = ekstensi yang termasuk
        for typ,lis in exts.iteritems():
            for ex in lis:
                if File.endswith(ex) or File.endswith(ex.upper()):
                    if os.path.isfile(File):
                        try:
                            #buat direktori dengan nama sesuai typ
                            os.makedirs(typ);
                        except:
                            None
                        #pindahkan file tersebut ke typ
                        shutil.move(File,typ);
 
organize_files_by_extension()
