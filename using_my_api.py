import ansible_client as ac

p = ac.AnsibleClient(user="test")
#print("Do you want apache2? [N/y]:", end="")
answer = input("Do you want apache2? [N/y]: ")
if(answer == 'y'):
    p.install("192.168.122.148", "apache2")
answer = input("Do you want nginx? [N/y]: ")
if(answer == 'y'):
    p.install("192.168.122.148", "nginx")

#p.install("192.168.122.148", "htop")
#p.install("192.168.122.148", "apache2")
