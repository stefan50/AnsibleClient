import ansible_client as ac

#p = ac.AnsibleClient(user="test")
#ac.AnsibleClient.create_vm("../../../Downloads/debian-9.4.0-i386-netinst.iso", 1024)
ac.AnsibleClient.vm_shutdown("generic")
