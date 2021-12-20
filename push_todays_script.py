import os,subprocess
#from constants import WORKING_DIR

os.chdir("../automated-python-scripts")

cmd = "git add ."
subprocess.check_output(cmd, shell=True)  

status= "git status -s"
returned_value = subprocess.check_output(status, shell=True) 

print('updated files:', returned_value)

if not returned_value==b'':
    commit_message='"Done Changed in the following files '
    if len(str(returned_value).split(r'\n'))>0:        
        for file_name in str(returned_value).split(r'\n'):
                    commit_message=commit_message+file_name[5:]+" "
        cmd= "git commit -m "+commit_message+r'"'
        print("Commit message ",subprocess.check_output(cmd, shell=True))
        try:
            cmd= "git push origin master"
            result = subprocess.check_output(cmd, shell=True)
            print(result) 
        except:
            cmd = "git pull"
            returned_value = subprocess.check_output(cmd, shell=True)  
            cmd = "git push origin master"
            result = subprocess.check_output(cmd, shell=True)
            print(result)
