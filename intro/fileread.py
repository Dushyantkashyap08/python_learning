import os 

dir_path = '/home/dushyant_new/ad-launch'

contents = os.listdir(dir_path)
for f in contents:
    print(f)