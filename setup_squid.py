import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

ip_file = "ip_addresses.txt" #put your ip addresses in this file
output = "output_squid.txt" #completed commands are in this file
file_read = open(ip_file,"r")
file_write = open(output,"w")
count = 1
file_write.write("http_port 80\n") #port for squid
#file_write.write("acl localnet src 1.1.1.1\n") #ip address from where the proxies are used, comment out if needed
file_write.write("http_access allow localhost\n")
file_write.write("http_access allow localnet\n\n")
for line in file_read:
    ip = line.strip()
    ip_replaced = ip.replace(".","_")
    file_write.write("acl my_ip_{:1} myip {:2}\n".format(ip_replaced, ip))
    file_write.write("tcp_outgoing_address {:1} my_ip_{:2}\n\n".format(ip, ip_replaced))
    count += 1
file_read.close()
file_write.close()