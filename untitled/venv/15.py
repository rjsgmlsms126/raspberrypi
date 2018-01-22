result='>>>'
def print_string(sep,*text_list):
    global result
    for s in text_list:
        result=result+sep+s
    return result

def print_string2(sep,*text_list):
    result=''
    for s in text_list:
        result=result+sep+s
    return result


print_string('-','안 ','s ','asdad')
print(print_string2('*','안 ','s ','asdad'))
print_string('','안 ','s ','asdad')
print(result)