import sys, re
#---------------------------------------------------------#
#  CLI Options for User                                   #
#---------------------------------------------------------#



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
    print("Usage: ruskko <filename> [OPTIONS]")
    print("do 'ruskko -help' for a list of options.")

# this is where the program starts:
arguments = sys.argv
del arguments[0] # Remove the python file name
args_len = len(arguments)
print("Total Arguments: ", args_len)
print("Arguments Seen: ", arguments)
