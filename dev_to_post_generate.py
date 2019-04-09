import constants,os
import pyperclip
with open('README.md') as f:
    data=f.readlines()
last_updated_date=None

desc=""
for c in reversed(data):
    if "## Day " in c:
        last_updated_date=c.strip()
        break
    desc=c+desc

day,file_name=last_updated_date=last_updated_date[3:].split(":")

user_title=input("Please enter title for "+file_name.strip()+"\n")

title=day.title()+" - "+user_title
desc=desc[2:]

print(desc)
with open(os.path.join(constants.WORKING_DIR,file_name.strip())) as f:
    code= f.read()

with open("data/devto_post_template") as f:
    template=f.read()

template=template.replace("###code###", code)
template=template.replace("###desc###", desc)
template=template.replace("###title###", title)
template=template.replace("###day###", day.title())
template=template.replace("###file_name###", file_name.strip().replace(".py", ""))

pyperclip.copy(template)