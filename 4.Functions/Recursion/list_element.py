#write a recursive function to print all element im a list
# .


def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
fruits =["graps","apple","kiwi","orange"]   

print_list(fruits)