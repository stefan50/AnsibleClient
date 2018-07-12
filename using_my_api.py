import ansible_client as ac
import sys

answer = input("Do you want a VM? [N/y]:")
if answer.lower() == 'y' or answer.lower() == 'yes':
    iso = input("Give me a path to the iso file:")
    name = input("Give me a name for the VM, leave blank for default:")
    if name is None:
        name = "generic_test"
    ac.AnsibleClient.create_vm(iso, 1024, name)

del answer

while(True):
    print("You can do something with your VMs:")
    name = input("Name?:")
    print(name)
    print("1 - Start a machine")
    print("2 - Stop a machine")
    print("3 - Shut a machine down")
    print("4 - Install")
    answer = input("Now you can choose:")
    if(answer == "1"):
        ac.AnsibleClient.vm_start(name)
    elif(answer == "2"):
        ac.AnsibleClient.vm_stop(name)
    elif(answer == "3"):
        ac.AnsibleClient.vm_shutdown(name)
    elif(answer == "4"):
        p = ac.AnsibleClient(user="test")
        apps = ["apache2", "nginx", "htop"]
        for a in apps:
            answer = input(("Do you want " + a + " [N/y]:"))
            if answer.lower() == 'y' or answer.lower() == 'yes':
                p.install("192.168.122.148", a)
    elif(answer == "quit"):
        sys.exit()
