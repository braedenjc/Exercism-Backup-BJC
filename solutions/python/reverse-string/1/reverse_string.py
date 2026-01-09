def reverse(text):
    text_length = len(text)
    text_index = text_length - 1
    reversed = ""
    print(text_length)
    while text_index >= 0:
        reversed += text[text_index]
        text_index -= 1
    return reversed