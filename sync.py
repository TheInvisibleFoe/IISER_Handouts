import os
import datetime
loc = ["~/Welearn/*"]
for i in loc:
    os.system("cp -r "+i+" ../IISER_Handouts")
os.system("git add . ")
x = datetime.datetime.now()
os.system("git commit -m "+"\""+str(x.strftime("%c"))+"\"")
os.system("git push origin main")

