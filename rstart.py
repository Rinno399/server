import os

os.system("apachectl -k restart")
print("--[+] Server is running on 127.0.0.1:8080/ ")
os.system("xdg-open http://127.0.0.1:8080/index.php")