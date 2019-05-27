import shutil,os,zipfile

location=r""
project_name=r""
path=os.path.join(location,project_name)

if os.path.isdir(path):
    shutil.rmtree(os.path.join(path,'node_modules'))
    
    zf = zipfile.ZipFile(os.path.join(location,project_name+".zip"), "w")
    for dirname, subdirs, files in os.walk(path):
        zf.write(dirname)
        print(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
