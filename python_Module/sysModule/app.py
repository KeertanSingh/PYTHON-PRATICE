"""
>> sys - System-specific parameters and functions
>> It provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
"""


import sys





# exit() = this function is used to terminate a program when needed. it can also be used to exit from python terminal.

# print("Hello world")  # print 'hello world'
# sys.exit()  # Terminate the program here
# print("Bye world!") # It will not run




# Path: This vaiable shows the value of python path environment variable which is set in the current system.

# for i in sys.path:
#     print(i)



# Platform : This variable is useed to identify the host operating system which we are using.
# print(sys.platform)

# Executable: This specifies the path of python executable path 
# to find the python.exe file on the system 
# print(sys.executable)

# modules : Return the list of available modules.
# for module in sys.modules:
#     print(module)


# copyright: This shows the copyright info
# print(sys.copyright)


# argv: This is actually a list which stores the command line arguments. the command line arguments or CLA are the parameters which are passed from command prompt while excuting a python program. The are similar to command line arguments of C/C++/JAVA. 
# for x in sys.argv:
#     print(x)

# sys._clear_type_cache() = Clear the internal type lookup cache.
# print(sys._clear_type_cache())



# print(sys.flags) # The named tuple flags exposes the status of command lines flags. 

# print(sys.float_info)  # A tuple holding information about the float type.

# print(sys.getwindowsversion())   # return window version 


# print(sys.maxsize)  # return the largest integer a variable can take

# print(sys.version) # Return the version number of the current python interpreter.


# stdin: It can be used to get input from the command line directly. It is used for standard input. It internally calls the input() method. It, also, automatically adds ‘\n’ after each sentence.

# for line in sys.stdin:
# 	if 'q' == line.rstrip():
# 		break
# 	print(f'Input : {line}')

# print("Exit")



# stdout 

# sys.stdout.write("joker")










