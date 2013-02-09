"""
XML.py
Mateusz Dubaniowski
Vincent Steil
"""
import sys

def XML_parseline(value_indent_array, indent):
    """
    a is the list of 2 element lists of tag, indent with the index being it's occurrance
    index is a list with one element! Used in order to pass a pointer, not a copy
    indent is also a list with one element!
    """
    line = sys.stdin.readline()
    line = line.lstrip();
    line = line.lstrip('<')
    line = line.rstrip('>')
    line = line.split('><')                         #line is now a list of strings
    for i in xrange(0, len(line)):                  
        if(line[i].find('/') == -1):                #dereference the string in line to check for opening tag
            value_indent_array.append([line[i], indent[0]])     #opening tag
            indent[0] += 1
        else:
            indent[0] -= 1                          #closing bracket
    if(indent[0] == 0):                             #check if you've reached the closing root tag
        return False
    else:
        return True

   
def XML_parser():
    """
    parses the given xml doc line by line into doc_array
    then parses the xml search parameter into search_array
    indent is the number of indents that the next tag is at
    """
    doc_array = []
    search_array = []
    indent = [0]
    
    while(XML_parseline(doc_array, indent)):        #parse the xml document
        continue
    while(XML_parseline(search_array, indent)):     #parse the xml doc given as search parameter
        continue
    
       
    
            