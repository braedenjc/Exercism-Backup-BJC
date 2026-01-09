import re

BOLD_REGEX_PATTERN = '(.*)__(.*)__(.*)'
ITALIC_REGEX_PATTERN = '(.*)_(.*)_(.*)'
LIST_ITEM_REGEX_PATTERN = r'\* (.*)'
SPECIAL_ELEMENT_PATTERN = '<h|<ul|<p|<li'

def parse(markdown):
    lines = markdown.split('\n') #Split the markdown whenever there is a new line and make a list out of them.
    res = '' # the HTML response
    number_of_lines = len(lines)
    ul_closed = True

    for i in range(number_of_lines):
        current_line = lines[i]
        #For each line, we parse any text that contains the header, bold, italic, and markdown.
        current_line = translate_any_header_markdown(current_line)
        current_line = translate_any_bold_markdown(current_line)
        current_line = translate_any_italic_markdown(current_line)
        #next step. Unordered lists.
        #Here are our cases:
        #We have a list item, but have not created an open <ul> element yet.
        #We have a list item, and have created an open <ul>
        #We do not have a list item, and the <ul> is open.
        #We have finished our parse, but our <ul> is still open.
        #We do not have a list item, and the <ul> is open.
        confirmed_line_item = is_list_item(current_line)
        if confirmed_line_item:
            list_item = "<li>" + confirmed_line_item.group(1) + "</li>"
            if ul_closed:
                current_line = "<ul>" + list_item
                ul_closed = False
            elif not ul_closed:
                current_line = list_item
            if not ul_closed and (i == number_of_lines - 1):
                current_line = list_item + "</ul>"
                ul_closed = True
        if not confirmed_line_item and not ul_closed:
            res += "</ul>"
            print("Current Line after UL close: " + current_line)
        #If we are no longer in a list, we make the item into a paragraph.
        in_special_text = re.match(SPECIAL_ELEMENT_PATTERN, current_line) 
        if not in_special_text:
            current_line = '<p>' + current_line + '</p>'
        res = res + current_line #Add to response.
    return res

#A helper method for checking for the proper header size, down to h6.
#If there is no header, return an unmodified line.
def translate_any_header_markdown(linetocheck):
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
        
#check to see if we are in list mode by confirming we have a '* ' pairing with nothing to the left of the '* '
def is_list_item(linetocheck):
    return re.match(LIST_ITEM_REGEX_PATTERN, linetocheck)

def translate_any_list_markdown(linetocheck):
    list_match = get_list_item_regular_expression(linetocheck)
    if list_match:
        linetocheck = '<li>' + list_match.group(1) + '</li>'
    return linetocheck

def translate_any_bold_markdown(linetocheck):
    bold_match = re.match(BOLD_REGEX_PATTERN, linetocheck)
    if bold_match:
        linetocheck = bold_match.group(1) + '<strong>' + bold_match.group(2) + '</strong>' + bold_match.group(3)
    return linetocheck

def translate_any_italic_markdown(linetocheck):
    italic_match = re.match(ITALIC_REGEX_PATTERN, linetocheck)
    if italic_match:
        linetocheck = italic_match.group(1) + '<em>' + italic_match.group(2) + '</em>' + italic_match.group(3)
    return linetocheck