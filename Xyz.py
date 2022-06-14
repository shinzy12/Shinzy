import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/SHIN-DATA')
except:pass

if __name__ == "__main__":
        try:
                __import__("V4.cpython-310.so").login()
        except Exception as e:
                exit(str(e))
