import sys, os

class AnsibleClient:
    """
    initializing the class TODO!!!
    name - name of the connection, "connection" by default
    """
    def __init__(self, name="connection"):
        print("Welcome to Ansible Client! What do you want to setup?")
        self.initialize_file(name, self.parse_hosts())

    def parse_hosts(self):
        res = []
        self.show_my_hosts("tmp")
        file = open("tmp.txt", "r")
        for line in file:
            if line[0] == "[":
                # group!!!
                pass
            elif line[0] != "#" and line[0] != "\n":
                res.append(line)
        file.close()
        os.system("rm tmp.txt")
        return res


    def connect_with_hosts(self):
        hosts = self.parse_hosts()
        os.spawnlp(os.P_WAIT, "ansible", "ansible", hosts, "-m", "ping", "-u", "test")

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
        os.system("ansible-playbook connection.yml")

    def initialize_file(self, name, hosts):
        name += ".yml"
        f = open(name, "w")
        for h in hosts:
            f.write("- hosts: " + h)
        cmd = "cat " + name
        os.system(cmd)

#p = AnsibleClient()
#p.show_my_hosts()
#p.connect_with_hosts()

# AnsibleClient.
# p.show_my_hosts()
