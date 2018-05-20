import paramiko

ip='169.254.187.92'
port=22
username='pi'
password='a1bAcde!'

client = paramiko.SSHClient()
client.load_system_host_keys()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def send_ssh_go():
    client.connect(ip, port="22", username=username, password = password)

    stdin, stdout, stderr = client.exec_command("python Adafruit-Motor-HAT-Python-Library/Adafruit_MotorHAT/slave.py")
    print stdout.read(), stderr.read()

    client.close()