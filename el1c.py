
# use command "python el1c.py <inputname> <outputname>" to work

from _el1c_f import el1c

from sys import argv
from pickle import load,dump

assert __name__ == "__main__"

if len(argv) < 3:
    print('use command "python lc.py <inputname> <outputname>" to work')
else:
    with open(argv[1],'rb') as fileobj:
        input_obj = load(fileobj)
        output_obj = el1c(input_obj)
    with open(argv[2],'wb') as fileobj:
        dump(output_obj,fileobj)
        
    
