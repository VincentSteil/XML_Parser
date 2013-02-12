"""
XML.py
Mateusz Dubaniowski
Vincent Steil
"""
import sys

def XML_parseline(reader, value_indent_array, indent):
    """
    value_index_array is the list of 2 element lists of tag, indent with the index being it's occurrence
    value_index_array[n] element 1 == tag
    value_index_array[n] element 2 == indent
    index is a list with one element! Used in order to pass a pointer, not a copy
    indent is also a list with one element!
    """
    line = reader.readline()
    line = line.lstrip();
    line = line.lstrip('<')
    line = line.rstrip('>\n')
    line = line.split('><')                                     #line is now a list of strings
    for i in xrange(0, len(line)):                  
        if(line[i].find('/') == -1):                            #dereference the string in line to check for opening tag
            value_indent_array.append([line[i], indent[0]])       #opening tag
            indent[0] += 1
        else:
            indent[0] -= 1                                          #closing bracket
    if(indent[0] == 1):                                          #check if you've reached the closing root tag
        return False
    else:
        return True
    

def XML_find_occurrences(doc_array, search_array):
    i = 0
    """
    while(i<len(doc_array)):
        sys.stdout.write("find occurences work\n")
        sys.stdout.write(str(i) +" ")
        occurrence = True
        indent = 0
        children = 0
        for j in xrange(0, len(search_array)):
            if(occurrence == False):
                break
            for k in xrange(i, len(doc_array)):
                children += 1
                if(search_array[j][0] == doc_array[k][0]):
                    indent = doc_array[k][1]
                    i = k + 1
                    break
                elif(doc_array[k][1] == indent):
                    occurrence = False
                    i = k 
                    break
        if(occurrence == True):
            occurrence_array.append(i -children) 
    """
    da=[]
    sa=search_array
    temp=0    
    res=[]
    indent_keep=0
    tt=0

    for x in range(0, len(doc_array)):
        if(temp==len(search_array)):
            res.append(tt)
            indent_keep=0
            tt=0
            temp=0
        if(indent_keep>doc_array[x][1] or (indent_keep>=doc_array[x][1] and search_array[temp][1]<search_array[temp-1][1])):
            indent_keep=0
            tt=0
            temp=0
        if(doc_array[x][0]==search_array[temp][0] and (indent_keep<doc_array[x][1] or (indent_keep==doc_array[x][1] and search_array[temp][1]==search_array[temp-1][1]))):
            indent_keep=doc_array[x][1]
            if(temp==0):
                tt=x+1
            temp+=1
    if(temp==len(search_array)):
            res.append(tt)

    return res
    #occurence_array=res
    

   
def XML_parser(reader, writer):
    """
    parses the given xml doc line by line into doc_array
    then parses the xml search parameter into search_array
    indent is the number of indents that the next tag is at
    """
    doc_array = []
    search_array = []
    indent = [1]
    res = []
    
    while(XML_parseline(reader, doc_array, indent)):                    #parse the entire xml document
        continue
    while(XML_parseline(reader, search_array, indent)):                 #parse the entire xml doc given as search parameter
        continue
    #print(search_array.remove(doc_array[0]))
    res=XML_find_occurrences( doc_array, search_array)

    
    
    writer.write(str(len(res)) + "\n")
    for i in xrange(0, len(res)):
        writer.write(str(res[i]) + "\n")
    
    
XML_parser(sys.stdin, sys.stdout)      
    
            
