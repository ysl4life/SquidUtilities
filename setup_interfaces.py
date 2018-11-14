import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

ip_file = "ip_addresses.txt" #put your ip addresses in this file
output = "output_interfaces.txt" #completed commands are in this file
file_read = open(ip_file,"r")
file_write = open(output,"w")
count = 1
for line in file_read:
    ip = line.strip()
    file_write.write("auto eth0:{:1}\n".format(count))
    file_write.write("iface eth0:{:1} inet static\n".format(count))
    file_write.write("address {:1}\n".format(ip))
    file_write.write("netmask 255.255.255.255\n")
    file_write.write("sudo ip addr add {:1}/32 dev eth0:{:2}\n".format(ip, count))
    file_write.write("ip link set eth0:{:1} up\n".format(count))
    file_write.write("\n")
    count += 1
file_read.close()
file_write.close()