tokens=['#','include','<','>','stdio.h','printf','(',')',';','int','scanf',',','&','number']
identifier=[]
keyword=[]

f=open("text.txt")
code=f.read()

tok=''
index=0
token=0
flag=0
flag1=0
spaces=0
for ch in code:
	tok=tok+ch
	index=index+1
	if flag==1 and ch=="/":
		flag=0	
		tok=''
	elif flag1==1 and ch=='"':
		flag1=0
		token=token+1
		tok=''
	elif ch==" ":
		token=token+0
		tok=''
		spaces=spaces+1
	elif ch=="\n":
		token=token+0
		tok=''	
	elif ch=='"' and flag1==0:
		flag1=1
		tok=''	
	elif ch=="/" and flag==0:
		ind=code.find(ch,index-1)
		ch2=code[ind+1]
		if ch2=="*":
			flag=1
		tok=''
	elif tok in tokens:
		token=token+1
		tok=''
	else:
		token=token+0
print("TOKENS : ",token)
print("WHITE SPACES : ",spaces)

print("--------------------------------------------")
for word in tokens:
	if 
print("--------------------------------------------")
