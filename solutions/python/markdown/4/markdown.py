import re


def parse(markdown):
    lines = markdown.split('\n') #Split the markdown whenever there is a new line.
    res = '' # the HTML response
    in_list = False #a control boolean that checks if we are making <li></li> or <ul></ul> elements
    in_list_append = False #For when we need to close the list in the final </ul> tags.
    
    #This is <h(x)></h(x)> work. When someone gives x #s, it gives us a header element, and then contents.
    #We check each line for the header tokens.
    #First, let's make methods off each of these. It'll make the code easier to focus on and work.
    
    for i in lines:
        #For each line, we look for header tokens first to generate the proper header size elements.
        #The contents of the line will then be contained between header tags.
        i = check_for_headers(i)
        #m is the place holder variable for seeing if we have a match for list syntax, marked with a *
        m = re.match(r'\* (.*)', i)  #check for a star, a space, then followed by characters. A raw string is used for the regular    expression parser
        in_list_mode = are_we_in_list(i)
        if(in_list_mode):
            print("LIST MODE BABY!\n")

        '''TODO, split the in_list, is_bold, and is_italic into their own methods.
            De-duplicate code
            correct logic flow to prevent need for that emergency in list mode catch.
            reduce regex dependency as much as possible.
        '''

        #Current task! Split is_bold and is_italic into their own methods.
        if m: # If there is a match from the <li> detecting regex, we are now appending the either a <ul> or <li> element.
            #check to see if we have bold or italics
            if not in_list: #Since we are not exactly in <li> mode yet, we will check to see if we need to bold/italicize text.
                in_list = True
                is_bold = is_text_bold(i)
                is_italic = is_text_italic(i)
                curr = m.group(1) #take the parsed groups, and select the first one as the current item we are checking.
                if is_bold:
                    split_bold_text = split_bold_markdown(curr)
                    curr = split_bold_text[0] + "<strong>" + split_bold_text[1] + "</strong>" + split_bold_text[2]
                '''
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                '''
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>' #add the root <ul> tag, and the accompanying <li></li> element.
            else: #since we are now in li mode, we now append <li></li> elements, and encase text in it.
                is_bold = is_text_bold(i)
                is_italic = is_text_italic(i)
                curr = m.group(1)
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
        else: #once we have no more matches, we leave list mode, and set the flag for appending the closing </ul> tag.
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i) #Check to see if we are already in an element.
        if not m:
            i = '<p>' + i + '</p>' #if we aren't in any kind of special element, we just encapsulate our text in <p></p> elements.
        #again, check to see if our text contains the bold or italicize markdown, and properly encapsulate.
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i #if we are in list append mode, place text AFTER the closing text. (why?)
            in_list_append = False
        res += i #Add to response.
    if in_list:
        res += '</ul>' #?! Why do we have an in_list check here? Are we not catching all cases?
        print("Oops, we got here!\n")
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

#A helper method that uses the built in string method count(). We use a modulo to see if we have 2 '_'s, marking an italic.
def is_text_italic(linetocheck):
    return linetocheck.count("_") == 2
#I don't think I can use the split method here!
def split_italic_markdown(linetocheck):
    pass

#A helper method using the built in string method count(), we use this to see if we have a bold element.
def is_text_bold(linetocheck):
    return linetocheck.count("__") > 1 #this MUST come in pairs.

#A helper method using the built in string method split(), we are going to split text into a list of 3 elements.
def split_bold_markdown(linetocheck):
    return linetocheck.split('__')

def are_we_in_list(linetocheck):
    return linetocheck.count("* ") 