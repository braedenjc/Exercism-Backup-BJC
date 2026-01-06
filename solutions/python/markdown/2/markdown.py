import re


def parse(markdown):
    lines = markdown.split('\n') #Split the markdown whenever there is a new line.
    res = '' # the HTML response
    in_list = False
    in_list_append = False
    #This is header work. When someone gives x #s, it gives us a header element, and then contents.
    #We check each line for the header tokens(?)
    #First, let's make methods off each of these. It'll make the code easier to focus on and work.
    
    for i in lines:
        #For each line, we look for header tokens first to generate the proper header size elements.
        #The contents of the line will then be contained between header tags.
        i = check_for_headers(i)
        #m is the place holder variable for seeing if we have a match for list syntax, marked with a *
        m = re.match(r'\* (.*)', i) 
        #ugh, some duplicated code.
        #TODO, split the in_list, is_bold, and is_italic into their own methods.
        if m: #
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res

#A helper method for checking for the proper header size, down to h6.
#If there is no header, return an unmodified line.
def check_for_headers(linetocheck):
    #I don't want to destruct the linetocheck for debugging reasons.
    #It's a small enough memory cost to hold a modified copy with the header token removed.
    
    #We will split it on the first space char, giving us the header token in the first list and the string in the second.
    #Then, we will use fstrings in python to create the proper header element for HTML.
    
    splitline = linetocheck.split(" ", maxsplit=1)
    headertokencount = splitline[0].count("#")
    textcontents = splitline[1] 
    if(0 < headertokencount < 7): 
        outputstring = f'<h{headertokencount}>{textcontents}</h{headertokencount}>'
        return outputstring
    else:
        return linetocheck