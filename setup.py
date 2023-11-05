import subprocess,os

try:
    subprocess.check_output("php -h",shell=True)
except:
    subprocess.check_output("pkg install php -y && pkg install apache2 -y")
    subprocess.check_output("pkg install php-apache -y")
    
try:
    os.system("mkdir /sdcard/www")
    os.system("mkdir /sdcard/www/htdocs")
    os.system("mv index.php /sdcard/www/htdocs/index.php")
    # os.system("ln -s /data/data/com.termux/files/usr/share/apache2/default-site/htdocs/ /sdcard/www/htdocs")
    
    os.system("echo 'alias apacheStart=\"python /data/data/com.termux/files/home/server/start.py\"' >> /data/data/com.termux/files/usr/etc/bash.bashrc")
    os.system("echo 'alias apacheStop=\"python /data/data/com.termux/files/home/server/stop.py\"' >> /data/data/com.termux/files/usr/etc/bash.bashrc")
    os.system("echo 'alias apacheRestart=\"python /data/data/com.termux/files/home/server/rstart.py\"' >> /data/data/com.termux/files/usr/etc/bash.bashrc")
    os.system("mv /data/data/com.termux/files/usr/etc/apache2/httpd.conf /data/data/com.termux/files/usr/etc/apache2/httpd.conf.back")
    os.system("cp /data/data/com.termux/files/home/server/httpd.conf /data/data/com.termux/files/usr/etc/apache2/httpd.conf")
    print("--[+]You can start by typing cmd --> apacheStart")
    print("--[+]You can stop by typing cmd --> apacheStop")
    print("--[+]You can restart by typing cmd --> apacheRestart")
    gg=input("Press enter to exit when you read above warnings-->")
    os.system("exit")
    
    
except:
    print("Something wrong")
