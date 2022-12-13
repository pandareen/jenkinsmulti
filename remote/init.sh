apt update
apt install openssh-server -y
systemctl enable ssh
service ssh start
echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
adduser --home /home/jenkins --shell /bin/sh jenkins
echo -n 'jenkins:1234' | chpasswd
tail -f /dev/null