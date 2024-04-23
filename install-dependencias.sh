#!/bin/bash

apt update
apt -y upgrade
apt -y install python3-pip python3-tk python3-dev gnome-startup-applications ; pip3 install pyautogui
useradd -c "Click TI" clickti
passwd -d clickti
mkdir -pv /home/clickti/HorizonClick/
chown -Rv clickti:clickti /home/clickti 
echo "alias configure-password='/usr/bin/python3 /home/clickti/HorizonClick/configure-password.py'" >> /home/clickti/.bashrc
wget -P /home/clickti/Downloads/ https://download3.vmware.com/software/CART25FQ1_LIN64_DebPkg_2312.1/VMware-Horizon-Client-2312.1-8.12.1-23543969.x64.deb
sudo dpkg -i  /home/clickti/Downloads/*.deb
sudo apt -f install
sed -i 's/#WaylandEnable=false/WaylandEnable=false/' /etc/gdm3/custom.conf 
chown -Rv clickti:clickti /usr/bin/python3 /home/clickti/HorizonClick/configure-password.py
chmod -v 700 /home/clickti/HorizonClick/configure-password.py
