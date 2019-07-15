def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

parsing_table=[
    ['E','i','TX'],['E','(','TX'],
    ['X','+','+TX'],['X',')','e'],['X','$','e'],
    ['T','i','FY'],['T','(','FY'],
    ['Y','+','e'],['Y','*','*FY'],['Y',')','e'],['Y','$','e'],
    ['F','i','i'],['F','(','(E)']
    ]

stack=''
inputstring=''
action=''

ip=str(input("Enter input string"))
stack='$E'
inputstring=ip+'$'

print("STACK              INPUT")

while(1):
    
    top=stack[len(stack)-1]
    ele=inputstring[0]
    print(stack+"                         "+inputstring)
    
    if top==ele=='$':
        print("Accepted")
        break
    elif top==ele:
        stack=stack.replace(top,'',1)
        inputstring=inputstring.replace(top,'',1)
    else:
        n_t=top
        t=ele
        for entry in parsing_table:
            if entry[0]==n_t and entry[1]==t:
                temp=entry[2]
                temp=reverse(temp)
                stack=stack.replace(n_t,'',1)
                stack=stack+temp
                action='pop('+top+')'
                if temp=='e':
                  stack=stack.replace(temp,'',1)
