from paramiko import SSHClient
from scp import SCPClient
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('rboddu495@dsclagnt-ch2-a1s.sys.comcast.net:/home/rboddu495')
with SCPClient(ssh.get_transport()) as scp:
    scp.put('README.md', 'README.md') 