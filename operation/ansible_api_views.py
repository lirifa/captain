#!/usr/bin/python
#coding=utf-8
import ansible.runner
import ansible.inventory
import json
import sys
class AnsibleWork():
    def __init__(self, ipAddress, remotePort, remoteUser, moduleName, moduleArgs):
        self.ipAddress = [ ipAddress ]
        self.webInventory = ansible.inventory.Inventory(self.ipAddress)
        self.remotePort = remotePort
        self.remoteUser = remoteUser
        self.moduleName = moduleName
        self.moduleArgs = moduleArgs
        self.timeOut = 20

    def printscriptLog(self, output):
        if len(output["dark"]) != 0 and len(output["contacted"]) == 0:
            for (hostname, result) in output["dark"].items():
                cmdresult = "\033[1;31m%s \033[0m"%result['msg']
        elif len(output["dark"]) == 0 and len(output["contacted"]) != 0:
            for (hostname, result) in output["contacted"].items():
                if 'failed' in result:
                    cmdresult = "\033[1;31m%s \033[0m"%result['msg']
                elif result['changed'] == True or result['changed'] == False:
                    cmdresult = "%s"%result['stdout']
                else:
                    cmdresult = "\033[1;31mAnsible output error\033[0m"
        else:
            cmdresult = "\033[1;31mOutput Error...\033[0m"
        return hostname,cmdresult

    def printcopyLog(self, output):
        if len(output["dark"]) != 0 and len(output["contacted"]) == 0:
            for (hostname, result) in output["dark"].items():
                cmdresult = "\033[1;31m%s \033[0m"%result['msg']
        elif len(output["dark"]) == 0 and len(output["contacted"]) != 0:
            for (hostname, result) in output["contacted"].items():
                if 'failed' in result:
                    cmdresult = "\033[1;31m%s \033[0m"%result['msg']
                elif result['changed'] == True or result['changed'] == False:
                    cmdresult = "\033[1;32mFile sync succeed. \033[0m"
                else:
                    cmdresult = "\033[1;31mAnsible output error\033[0m"
        else:
            cmdresult = "\033[1;31mOutput Error...\033[0m"
        return hostname,cmdresult

    def printcmdLog(self, output):
        if len(output["dark"]) != 0 and len(output["contacted"]) == 0: 
            for (hostname, result) in output["dark"].items():
                cmdresult = "\033[1;31m%s \033[0m"%result['msg']
        elif len(output["dark"]) == 0 and len(output["contacted"]) != 0:
            for (hostname, result) in output["contacted"].items():
                if 'failed' in result:
                    cmdresult = "\033[1;31m%s \033[0m"%result['msg']
                elif result['stdout'] != '':
                    cmdresult = "\033[1;32m%s \033[0m"%result['stdout']
                elif result['stderr'] != '':
                    cmdresult = "\033[1;31m%s \033[0m"%result['stderr']
                else:
                    #cmdresult = "\033[1;31mAnsible output error\033[0m"
                    cmdresult = "\033[1;31m\033[0m"
        else:
            cmdresult = "\033[1;31mOutput Error...\033[0m"
        return hostname,cmdresult

    def workrun(self):
        checkrunner = ansible.runner.Runner(
            module_name = self.moduleName,
            module_args = self.moduleArgs,
            timeout = self.timeOut,
            remote_port = self.remotePort,
            remote_user = self.remoteUser,
            inventory = self.webInventory
        )
        if self.moduleName == "shell" or self.moduleName == "command":
            self.output = checkrunner.run()
            return self.printcmdLog(self.output)
        elif self.moduleName == "copy":
            self.output = checkrunner.run()
            return self.printcopyLog(self.output)
        elif self.moduleName == "script":
            self.output = checkrunner.run()
            return self.printscriptLog(self.output)
        else:
            pass


#theUser = AnsibleWork('172.27.13.179', 22, 'pmops', 'script', './check_services_srvzx001.py')
#print theUser.workrun()
