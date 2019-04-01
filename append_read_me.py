import glob
import os,sys


pwd=os.getcwd()+r"/"

list_of_files = glob.glob(pwd+'*.py') 
latest_file = max(list_of_files, key=os.path.getctime)

last_updated_python_file_name=latest_file.split(r"/")[-1]

data=[]
with open('README.md') as f:
    data=f.readlines()
last_date=None
is_already_added=False
for c in reversed(data):
    if "## Day " in c:
        if not last_date:
            last_date=c.strip()
        if last_updated_python_file_name in c:
            is_already_added=True
            break
if is_already_added:
    print("Last updated file "+last_updated_python_file_name+" is already added")
    sys.exit(0)

try:
    today_number=int(last_date[7])+1
except:
    pass

new_data="\n\n## Day "+str(today_number)+": "+last_updated_python_file_name+"\n"

desc=input("Please Enter description for "+last_updated_python_file_name+"\n")

new_data=new_data+"- "+desc.strip()

with open('README.md',"a+") as file:
    file.write(new_data)
