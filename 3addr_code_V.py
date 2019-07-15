operation="x=a*(b+c)"

operand=['a','b','c','x']
operator=['*','+','=']

three_addr=[]

ind1=operation.find('(')
ind2=operation.find(')')

count=1
exp=''
exp='t'+str(count)+' = '
count=count+1
for i in range(ind1+1,ind2,1):
	exp=exp+operation[i]
three_addr.append(exp)

exp_t=exp[0:2:1]
ind=operation.find('=')
char=operation[ind+1]
opr=operation[ind+2]
exp=char+opr+exp_t
n_exp='t'+str(count)+' = '
exp=n_exp+exp
three_addr.append(exp)

char=operation[0]
ind=n_exp.find('=')
n_exp=n_exp[:ind-1]
exp=char+"="+n_exp
three_addr.append(exp)

print("Operation is : ")
print(operation)
print()
print("Three Address Code is : ")
print(three_addr)
print()

print("Quadruple Representation : ")
quadruples=[['No.','OP','ARG1','ARG2','RESULT']]
count=1
for entry in three_addr:
	temp=[]
	temp.append(count)
	ind_opr=-1
	for ch in entry:
		if ch in operator and ch!='=':
			temp.append(ch)
			ind_opr=entry.find(ch)
	ind_eq=entry.find("=")
	arg1=''
	if ind_opr==-1:
		temp.append('=')
		for i in range(ind_eq+1,len(entry),1):
			arg1=arg1+entry[i]
	else:
		for i in range(ind_eq+1,ind_opr,1):
			arg1=arg1+entry[i]
	temp.append(arg1)
	arg2=''
	if ind_opr==-1:
		arg2='N.A.'
	else:
		for i in range(ind_opr+1,len(entry),1):
			arg2=arg2+entry[i]
	temp.append(arg2)
	res=''
	for i in range(0,ind_eq,1):
		res=res+entry[i]
	temp.append(res)
	quadruples.append(temp)
	count=count+1

#print(quadruples)

for i in quadruples:
	print(i)

print()
print("Triples Representation : ")

triples=[]

for entrylist in quadruples:
	temp=[]
	temp.append(entrylist[0])
	temp.append(entrylist[1])
	opr1=entrylist[2]
	if opr1=='t1' or opr1=='t2' or opr1=='t3':
		temp.append(str(opr1[len(opr1)-1]))
	else:
		temp.append(opr1)
	opr2=entrylist[3]
	if opr2=='t1' or opr2=='t2' or opr2=='t3':
		temp.append(str(opr2[len(opr2)-1]))
	else:
		if opr2=='N.A.':
			res=entrylist[4]
			temp.append(res)
		else:
			temp.append(opr2)
	triples.append(temp)

for i in triples:
	print(i)

print()
print("Indirect Triples Representation : ")

indirect_triples=[]

for i in range(len(triples)-1):
	temp=[]
	temp.append(i+1)
	temp.append('('+str(i+1)+')')
	indirect_triples.append(temp)

for i in indirect_triples:
	print(i)
