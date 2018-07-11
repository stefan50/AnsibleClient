import ansible_client as ac

p = ac.AnsibleClient(user="test")

apps = ["apache2", "nginx", "htop"]
for a in apps:
    answer = input(("Do you want " + a + " [N/y]"))
    if answer.lower() == 'y' or answer.lower() == 'yes':
        p.install("192.168.122.148", a)
