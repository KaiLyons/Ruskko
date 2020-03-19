import sys, re

output = "index.html" # index.html is default
#---------------------------------------------------------#
#  Define Ruskko built tags                               #
#---------------------------------------------------------#

def parser(file):
    # Remove comments
    for i in file:
        if (i.startswith('//')):
            file.remove(i)
    
    print(file)


#---------------------------------------------------------#
#  Reading the file                                       #
#---------------------------------------------------------#
def readFile():
    file = arguments[0]
    print("File Input: ", file)
    print("File Output: ", output)
    all_lines = []

    run = open(file, 'r')
    for line in run:
        line = line.rstrip()
        line = line.lstrip()
        all_lines.append(line)
    
    all_lines = list(filter(None, all_lines))
    
    parser(all_lines)
        

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
    print("")
    exit()

def outputName(name):
    global output 
    output = name + ".html"   

def outputFile(new_file):
    global output 
    output = new_file

def fileInput(file):
    if (arguments[0] == "-help"):
        help()
    else:
        if (not arguments[0].endswith(".rsko")):
            incorrectFile(arguments[0])
        else:
            readFile()

#---------------------------------------------------------#
#  Export files                                           #
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

# Check Argument Lengths, and run code accordingly
if (args_len == 1):
    fileInput(arguments[0])
elif (args_len == 2):
    incorrectUsage("Unused Option")
elif (args_len == 3):
    fileInput(arguments[0])
    if (arguments[1] == "-o"):        
        outputName(arguments[2])
        readFile()
    elif(arguments[1] == "-of"):
        outputFile(arguments[2])
        readFile()
elif (args_len == 0):
    incorrectUsage("No File Specified")
else:
    incorrectUsage("Too many arguments! Limit = 3")
