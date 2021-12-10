# Example usage: `python script.py 10`                                                                                                        

import sys
# This is how you load modules (i.e., packages) into your python session                                                                            
# Python is probably the most active community language community around                                                                            
# Whatever you're doing, odds are there's a python package to help you do it                                                                        
import binary_string
# That's because it's very easy to package up code and use it as a module 

# The `sys` module let's us grab command line arguments as a list of strings                                                                        
i = int(sys.argv[1])
# Python is "0"-indexed, so the first element, `sys.argv[0]`, is not used:                                                                          
# the first command line argument is the python script name, here "script.py"                                                                       
# Arguments will initially be strings, so their type may need to be converted 
print(binary_string.binary_string(i))
# Just as the `argv` function (i.e., method) is called
#   from the imported `sys` module object as `sys.argv`
# so too do is the `binary_string` function (i.e., method) called from
#   the imported `binary_string` module object as `binary_string.binary_string`
