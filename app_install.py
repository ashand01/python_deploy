import os

def install_apache():
   print('installing pache')
   os.system('yum -y install httpd')
  
   print('enabling apache server')
   os.system('systemctl enable httpd.service')

   print('statring apache server')
   os.system('systemctl start httpd.service')

   print('please open a security setting for port 80 on your server')
 
install_apache()
