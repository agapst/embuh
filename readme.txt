Fix engine 2.7 ke atas yg error file record perdetik / banyak

#wajib dimulai dgn unmount HDD agar file tidak hilang

#wajib root
kecilin-stream --stop-monitor
kecilin-stream --del-monitor
kecilin-stream --stop-api
killall binutils
killall kecilin-api
#reinstall requirement
python3.9 -m pip install --ignore-installed -r requirement.txt
#bila ada eror silahkan copas log erornya ke google pasti nemu solusinya
#bila sudah gk ada yg eror lanjut instal ulang engine
apt install --reinstall ./kecilin-stream.deb (versi 2.6.1)
kecilin-stream -k BRIC_RM.key --register
kecilin-stream -c config.json
kecilin-stream --stop-monitor
kecilin-stream --del-monitor
kecilin-stream --print
kecilin-stream -sn TID --delet
kecilin-stream -i (ADD ULANG TID)
kecilin-stream --monitor-all
#cek file recording di /mnt/sda1/TID (ini di storage OS bukan HDD)
#bila sudah normal 
kecilin-stream --stop-monitor
#hapus folder TID di mnt/sda1/
rm -rf /mnt/sda1/TID
#Mounting HDD
#copy kecilin-stream v2.7.3
cp kecilin-stream /usr/bin/
cp kecilin-api /usr/bin/
chmod +x /usr/bin/kecilin-stream
chmod +x /usr/bin/kecilin-api
rm /usr/lib/python3.9/utility/db/orm.py
kecilin-stream --monitor-all

#cek ulang file record di HDD sd sesuai/blm
pm2 save & startup

#install File-cleaner v1.0.3
cp file-cleaner /usr/bin/
chmod +x /usr/bin/file-cleaner
pm2 start /usr/bin/file-cleaner
pm2 save 
pm2 startup
