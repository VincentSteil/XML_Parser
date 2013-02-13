# --------------------------
# XML.py
# Mateusz Dubaniowski, mid325
# Vincent Steil, vjs432
# --------------------------

# --------------
# imports
# --------------

import sys

# --------------
# XML_parseline
# --------------

def XML_parseline(reader, value_indent_array, indent):
    """
    reads and parses current line of tags and appends the tags to value_indent_array
    reader is a reader
    value_index_array is the list of 2 element lists of tag, indent with the index being it's occurrence
    value_index_array[n] element 1 == tag
    value_index_array[n] element 2 == indent
    indent is a list with one element! Used in order to pass a pointer, not a copy
    returns True if succeeded and False if not
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
    if(indent[0] == 1): 
        assert indent[0] == 1                                        #check if you've reached the closing root tag
        return False
    else:
        assert indent[0] != 1
        return True

# ---------------------
# XML_find_occurrences
# ---------------------

def XML_find_occurrences(doc_array, search_array):
    """
    returns the indices of each occurence of pattern, defined by search_array, in doc_array
    doc_array is a list of 2-element lists containing all tags and their indents in the document to be searched
    search_array is a list 2-element lists containing pattern's tags and their indents
    return list of indices where the pattern(search_array) searched for occurs in the document(doc_array)
    """
    assert len(doc_array) > 0
    assert len(search_array) > 0
    i = 0
    temp=0    #keeps track of how far the subtree and search_array are equal
    res=[]    #stores the results
    indent_keep=0   #indent of last element in the subtree
    tt=0      #the beginning point of current subtree
    last_indent=0
    
    for x in range(0, len(doc_array)):
        if(temp==len(search_array)):            #add another occurence and reset if the current subtree is same as search_array
            res.append(tt)
            indent_keep=0
            tt=0
            last_indent=0
            temp=0                      #or (indent_keep>=doc_array[x][1] and search_array[temp][1]<search_array[temp-1][1])
        if(indent_keep>=doc_array[x][1]): #if subtree finished but not the same as search_array or wrong sibling present then reset
            indent_keep=0
            tt=0
            temp=0
            last_indent=0
        if(doc_array[x][0]==search_array[temp][0] and indent_keep<doc_array[x][1] and(indent_keep==0 or last_indent>=doc_array[x][1]-1)): #subtree started or expanded if it is consistent with search_array
            last_indent=doc_array[x][1]
            if(temp==0):
                indent_keep=doc_array[x][1]
                tt=x+1
            temp+=1
    if(temp==len(search_array)): #result appended in case last iteration completes the subtree to search_array
            res.append(tt)
    return res #return the result


# -----------
# XML_parser
# -----------

def XML_parser(reader, writer):
    """
    parses the given xml doc line by line into doc_array
    then parses the xml search parameter into search_array
    then gets the indices of where the pattern(search_array) searched for occurs in the document(doc_array)
    reader is a reader
    writer is a writer
    """
    doc_array = []
    search_array = []
    indent = [1]
    res = []
    
    while(XML_parseline(reader, doc_array, indent)):            #parse the entire xml document
        continue
    while(XML_parseline(reader, search_array, indent)):         #parse the entire xml doc given as search parameter
        continue
    res=XML_find_occurrences( doc_array, search_array)
    #writes the result to the output
    writer.write(str(len(res)) + "\n")
    for i in xrange(0, len(res)):
        writer.write(str(res[i]) + "\n")
# ------
# END
# ------
