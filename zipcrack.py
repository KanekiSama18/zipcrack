import zipfile
from colorama import Fore

print(Fore.BLUE, "[+] Welcome to ZIPCRACK [+] ")

idesc = "Enter the name of the zip file(with .zip): "
fname = input(idesc)
pdesc = "Enter the name of wordlist file(with .txt): "
pname = input(pdesc)

print(Fore.YELLOW , "[+] Starting Attack: \n")

count = 1

with open(pname,'rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile(fname,'r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print(Fore.GREEN , '''******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print(Fore.RED , '[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
            count += 1
            pass
