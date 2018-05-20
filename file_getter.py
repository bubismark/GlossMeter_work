import os
import paramiko
print "6"
paramiko.util.log_to_file('paramiko.log')
paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
print"a"

host='169.254.187.92'
port=22
username='pi'
password='a1bAcde!'

remote_images_path = 'Adafruit-Motor-HAT-Python-Library/Adafruit_MotorHAT/pic/'
local_path = 'pic/'
print "b"
ssh = paramiko.SSHClient()
print "d"
ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
print "e"

print "9"
def get_files():
    ssh.connect(hostname=host, port=port, username=username, password=password)
    print "c"
    sftp = ssh.open_sftp()

    files = sftp.listdir(remote_images_path)
    while(files != []):
        files = sftp.listdir(remote_images_path)
        for file in files:
            file_remote = remote_images_path + file
            file_local = local_path + file
            print file_remote + '>>>' + file_local
            sftp.get(file_remote, file_local)
            sftp.remove(file_remote)


    sftp.close()
    ssh.close()
print "7"