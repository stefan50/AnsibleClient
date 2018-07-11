import ansible_client as ac

p = ac.AnsibleClient(user="test")
p.install("192.168.122.148", "apache2")
p.install("192.168.122.148", "htop")
