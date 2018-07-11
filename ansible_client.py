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

    """
    From the given tmp.txt file, take only these lines which have
    important information aka an entry
    !IMPORTANT! Doesn't support groups yet!
    """
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

    """
    Tests the connectivity between you and your host(s)
    """
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
    This method is used to initialize the yaml file, meaning that it only adds
    the hosts/groups to the file without any other action
    """
    def initialize_file(self, hosts):
        f = open(self.connection_file, "w")
        for h in hosts:
            f.write("- hosts: " + h)
            f.write("\n  remote_user: " +  self.user +
                     "\n  become: yes" +
                     "\n  become_method: su")
        f.close()

    def check(self):
        token = False
        #print(open(self.connection_file, "r").read().find('tasks'))
        f = open(self.connection_file, "r")
        for line in f.read():
            print(line)
            if line.strip() == "tasks:":
                token = True
        f.close()
        print(token)
        return token

    """
    adds package name to be installed for a host, leave host blank to
    have the all group as default
    """
    def install(self, host, package):
        token = False
        with open(self.connection_file, "r") as in_file:
            buf = in_file.readlines()

        with open(self.connection_file, "w") as out_file:
            for line in buf:
                l = len(line)
                if line[9:l].rstrip() == host:
                    #line += ("\n  remote_user: " +  self.user +
                    #         "\n  become: yes" +
                    #         "\n  become_method: su")
                    if not self.check():
                        line += ("\n  tasks:\n    ")
                    line += ("- name: Installing "
                            + package + "\n      apt:\n        name: "
                            + package + "\n")
                out_file.write(line)

    """
    Runs the file
    """
    def __del__(self):
        cmd = ("ansible-playbook " + self.connection_file + " -u " + self.user +
              " --ask-become-pass")
        os.system(cmd)

#p = AnsibleClient()
#p.show_my_hosts()
#p.connect_with_hosts()

# AnsibleClient.
# p.show_my_hosts()
