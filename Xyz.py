import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/SHIN-DATA')
except:pass
try:os.system('mkdir /sdcard/SHIN-DATA/OK')
except:pass
try:os.system('mkdir /sdcard/SHIN-DATA/CP')
except:pass
try:os.system('mkdir /sdcard/SHIN-DATA/TAP-A2F')
except:pass
if __name__ == "__main__":
        try:
                __import__("Xyz").login()
        except Exception as e:
                exit(str(e))
