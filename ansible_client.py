import sys, os

class AnsibleClient:
    """
    initializing the class TODO!!!
    name - name of the connection, "connection" by default
    user - name of user, default root NOT RECOMMENDED!
    """
    def __init__(self, name="connection", user="root"):
        print("Welcome to Ansible Client! What do you want to setup?")
        self.connection_file = name + ".yml"
        self.user = user
        self.initialize_file(self.parse_hosts())

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
        cmd = "ansible " + hosts[0] + "-m ping -u " + self.user
        os.system(cmd)

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
        cmd = ("ansible-playbook " + self.connection_file + " -u " + self.user +
              " --ask-become-pass")
        os.system(cmd)

    """
    This method is used to initialize the yaml file, meaning that it only adds
    the hosts/groups to the file without any other action
    """
    def initialize_file(self, hosts):
        f = open(self.connection_file, "w")
        for h in hosts:
            f.write("- hosts: " + h)
        f.close()

    """
    adds package name to be installed for a host, leave host blank to
    have the all group as default
    """
    def install(self, host, package):
        with open(self.connection_file, "r") as in_file:
            buf = in_file.readlines()

        with open(self.connection_file, "w") as out_file:
            for line in buf:
                l = len(line)
                if line[9:l].rstrip() == host:
                    line += ("\n  remote_user: " +  self.user +
                             "\n  become: yes" +
                             "\n  become_method: su")
                    line += ("\n  tasks:\n    - name: Installing "
                            + package + "\n      apt:\n        name: "
                            + package + "\n")
                out_file.write(line)


#p = AnsibleClient()
#p.show_my_hosts()
#p.connect_with_hosts()

# AnsibleClient.
# p.show_my_hosts()
