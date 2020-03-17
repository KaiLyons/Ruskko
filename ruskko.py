import sys, re
#---------------------------------------------------------#
#  CLI Options for User                                   #
#---------------------------------------------------------#
def help():
    print("Here is a list of options:")
    print("--------------------------")
    print("")
    print("    -o  | output (sets output name)")
    print("        | Usage: ruskko file.rsko -o index")
    print("        | Will set to a .html file automatically")
    print("========|=======================================")
    print("   -of  | output file (sets exact file name)")
    print("        | Usage: ruskko file.rsko -o index.html")
    print("        | Has no automatic file extension set")
    print("        |\n")

#---------------------------------------------------------#
#  Export files                                           #
#---------------------------------------------------------#



#---------------------------------------------------------#
#  Define Ruskko built tags                               #
#---------------------------------------------------------#



#---------------------------------------------------------#
#  Get/Set arguments such as file and CLI for future use  #
#---------------------------------------------------------#
def incorrectUsage(err):
    print("Error Detected: ", err, " - Incorrect command usage")
    print("Usage: ruskko <filename> [OPTIONS] [COMMAND]")
    print("do 'ruskko -help' for a list of options.")

def incorrectFile(file):
    print("got file: ", file)
    print("expected a \".rsko\" file!")

# this is where the program starts:
arguments = sys.argv
del arguments[0] # Remove the python file name
args_len = len(arguments)
print("Total Arguments: ", args_len)
print("Arguments Seen: ", arguments)

if (arguments[0] == "-help"):
    help()
else:
    if (not arguments[0].endswith(".rsko")):
        incorrectFile(arguments[0])
    else:
        pass

if (args_len == 1):
    pass
elif (args_len == 2):
    incorrectUsage("Unused Option")
elif (args_len == 3):
    pass
elif (args_len == 0):
    incorrectUsage("No File Specified")
else:
    incorrectUsage("Too many arguments! Limit = 3")
