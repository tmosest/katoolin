

import os
import sys, traceback

import six
six.moves.reload_module(six)

from six.moves import input

def add_classic():
    cmd1 = run_cmd("add-apt-repository ppa:diesch/testing && apt-get update")
    cmd = run_cmd("sudo apt-get install classicmenu-indicator")
    return [cmd1, cmd]

def add_kali_menu():
    return os.system("apt-get install kali-menu")

def is_sudo():
    return os.getuid() == 0

def run_eval(val):
    opcion0 = eval(input(val))
    opcion0 = f"{opcion0}"
    return opcion0

def run_cmd(cmd):
    return os.system(cmd)

def get_kali_linux_certs():
    cmd1 = run_cmd("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
    cmd2 = run_cmd("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
    return [cmd1, cmd2]

def update_apps():
    return run_cmd("apt-get update -m")

def read_sources():
    file = open('/etc/apt/sources.list', 'r')
    print((file.read()))

def remove_kali():
    infile = "/etc/apt/sources.list"
    outfile = "/etc/apt/sources.list"
    delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
    fin = open(infile)
    os.remove("/etc/apt/sources.list")
    fout = open(outfile, "w+")
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
            fout.write(line)
    fin.close()
    fout.close()
    print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")

def install_tool(name):
    run_cmd(f"apt-get -f -y install {name}")