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


github file describe

###### http_server,py ######
need install flask package.
listen ip address can set 0.0.0.0 or self-defind ip address

curl http://151.1.11.101/ztp.py can get web page

if you does not use http_server.py
you can install apache2 service, 


###### ZTP_File ######

when use http_server.py ,this directory will auto generate ztp.py file



