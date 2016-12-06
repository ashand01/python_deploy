import os

def install_apache():
    print("installing apache server")
    os.system('yum -y install httpd')


    print("enabling apache server")
    os.system('systemctl enable httpd.service')

    print("starting apache server")
    os.system('systemctl start httpd.service')


    print("If you open the security settings for port 80 on your server, you should see the apache start page")
install_apache()

def install_dirty_cow():
    os.system('yum clean all')
    os.system('yum update kernel') 
    os.system('reboot')

def verify_dirty_cow():
    os.system('rpm -q --changelog kernel | grep CVE-2016-5195')
verify_dirty_cow()

def install(package):
    os.system('yum -y install ' + package)

def install_git():
    os.system('yum -y install git; git clone https://github.com/nic-instruction/NTI-300/')
