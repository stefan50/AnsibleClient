import sys, os

class AnsibleClient:
    """
    initializing the class TODO!!!
    """
    def __init__(self):
        print("Welcome to Ansible Client! What do you want to setup?")

    def parse_hosts(self):
        res = ""
        self.show_my_hosts("tmp")
        file = open("tmp.txt", "r")
        for line in file:
            if line[0] == "[":
                # group!!!
            elif line[0] != "#":
                res += line
        file.close()
        res = res.strip()
        os.system("rm tmp.txt")
        return res


    def connect_with_hosts(self):
        hosts = self.parse_hosts()
        os.spawnlp(os.P_WAIT, "ansible", "ansible", hosts, "-m", "ping")

    """
    a method which shows every host - for now a simple cat
    """
    def show_my_hosts(self, output="standard"):
        sys_call = "cat /etc/ansible/hosts"
        if output != "standard":
            sys_call += " > tmp.txt"
        os.system(sys_call)

    """
    Starts the connection
    """
    def start_connection(self):
        pass


#p = AnsibleClient()
#p.show_my_hosts()
#p.connect_with_hosts()

# AnsibleClient.
# p.show_my_hosts()
