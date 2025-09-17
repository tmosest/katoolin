#!/usr/bin/python



import os
import sys, traceback

import six
six.moves.reload_module(six)

from six.moves import input

from messages import NEED_SUDO
from menu import INFO_GATHERING, MENU_TITLE, MAIN_MENU_OPTIONS, FIRST_SUB_MENU, OPTION_1, WHAT_TO_DO, INVALID_COMMAD, CLASSIC_MENU, TO_INSTALL_CLASS, TO_INSTALL_KALI, LIST_COMMANDS, CATEGORIES
from cmd_utils import is_sudo, run_eval, run_cmd, get_kali_linux_certs, update_apps, remove_kali, read_sources, add_classic, add_kali_menu
from tools import handle_options, TOOL_CAT_MAP, install_all

if is_sudo() == False:
	print(NEED_SUDO)
	sys.exit()


def main():
	try:
		print (MENU_TITLE)
		def inicio1():
			while True:
				print (MAIN_MENU_OPTIONS)

				opcion0 = run_eval(OPTION_1)
				
				
				while opcion0 == "1":
					print(FIRST_SUB_MENU)
					repo = run_eval(WHAT_TO_DO)
					if repo == "1":
						get_kali_linux_certs()
					elif repo == "2":
						update_apps()
					elif repo == "3":
						remove_kali()
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						read_sources()
					else:
						print (INVALID_COMMAD) 					
						

				if opcion0 == "3":
					print (CLASSIC_MENU)
					repo = run_eval
					if repo == "y":
						add_classic()

				elif opcion0 == "4"	:
					repo = run_eval(TO_INSTALL_KALI)
					if repo == "y":
						add_kali_menu()
				elif opcion0 == "5":
					print (LIST_COMMANDS)


				def inicio():
					while opcion0 == "2":
						print (CATEGORIES)
						print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

						opcion1 = run_eval(OPTION_1)
					
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							print("TODO fix")
							install_all()
						while opcion1 in TOOL_CAT_MAP:

							result = handle_options(opcion1)

							if result == True:
								inicio()
							elif result is None:
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
