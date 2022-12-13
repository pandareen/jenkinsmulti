import paramiko
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip_addr", help="remote ip address")
    parser.add_argument("--root_dir", help="The root directory where we should start scan from")

    args = parser.parse_args()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(f'{args.ip_addr}', username='jenkins', password='1234')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f'ls {args.root_dir}**')
    print(ssh_stdout.read())
    ssh_stdin.close()

if __name__ == "__main__":
    main()
