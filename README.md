# PlantNet

DB:
sudo apt-get install sqlite3 libsqlite3-dev

Python lib for grove:
https://github.com/Seeed-Studio/grove.py
https://www.dexterindustries.com/GrovePi/programming/python-library-documentation/
https://www.dexterindustries.com/grovepi-tutorials-documentation/

https://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/
mkdir ~/Dexter
cd /home/pi/Dexter
git clone https://github.com/DexterInd/GrovePi

cd /home/pi/Dexter/GrovePi/Script
Installation script:
bash ./update_grovepi.sh



#Python installation

https://phoenixnap.com/kb/how-to-install-pip-on-ubuntu

sudo apt install python3-pip
sudo pip3 install --upgrade pip
sudo apt install python-pip
sudo pip install -r requirements.txt
sudo pip install --upgrade pip

#/var/lib/systemd/system/plantdata.service example
[Unit]
Description=plantdata
After=network.target network-online.target

[Service]
Type=simple
User=pi
Group=pi
Restart=always
ExecStartPre=+/bin/mkdir -p /var/run/plantdata
PIDFile=/var/run/plantdata/service.pid
ExecStart=python /home/pi/projects/PlantNet/plant_monitor.py

[Install]
WantedBy=multi-user.target
