# cisco-ztp

ubuntu server as dhcp server

#######  isc-dhcp-server  example ########

cat /etc/dhcp/dhcpd.conf 

subnet 151.1.11.0 netmask 255.255.255.0 {
range 151.1.11.150 151.1.11.200;
option routers 151.1.11.101;
option subnet-mask 255.255.255.0;
option domain-name "donewin.com";
option bootfile-name "http://151.1.11.101/ztp.py";
}


###### http_server,py ######
python http_server.py 

curl http://151.1.11.101/ztp.py can get web page
