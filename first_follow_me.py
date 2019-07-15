n=int(input("Enter number of productions : "))

productions=[]
for i in range(n):
        temp=str(input("Enter production (use = instead of =>) (Enter production in ' ') ('epselon' as 'e'): "))
        temp=temp.strip("'")
        productions.append(temp)

non_terminals=[]
for prod in productions:
        if prod[0] not in non_terminals:
                non_terminals.append(prod[0])

terminals=[]
for prod in productions:
        tempind=prod.find("=")
        for c in range(tempind+1,len(prod),1):
                if prod[c] not in non_terminals and prod[c]!='e':
                        terminals.append(prod[c])

print("Terminals : ")
print(terminals)
print("Non-Terminals : ")
print(non_terminals)

first_set=[]
for prod in productions:
        temp=[]
        temp.append(prod[0])
        n_t=prod[0]
        if prod[2] in terminals:
                temp.append(prod[2])
        elif prod[2]=='e':
                if len(prod)>3:
                        temp.append("F_"+prod[3])
                else:
                        temp.append(prod[2])
        else:
                temp.append("F_"+prod[2])
        first_set.append(temp)

for i in range(10):
        entry1=first_set[i]
        entry2=first_set[i+1]
        if entry1[0]==entry2[0]:
                temp=[]
                temp.append(entry1[0])
                t=[]
                t.append(entry1[1])
                t.append(entry2[1])
                temp.append(t)
                first_set.append(temp)
        i=i+1

first_set.reverse()
first_set2=first_set[:]
first_set=[]
for entry2 in first_set2:
        flag=0
        for entry1 in first_set:
                if entry2[0]==entry1[0]:
                        flag=1
        if flag==0:
                first_set.append(entry2)

for i in range(5):
        for set_f in first_set:
                if isinstance(set_f[1],str):
                        if set_f[1].find("F_")!=(-1):
                                ind=set_f[1].find("F_")
                                n_t=set_f[1][ind+2]
                                for set_f1 in first_set:
                                        if n_t==set_f1[0]:
                                                set_f[1]=set_f1[1]
first_set.reverse()
print("First Set : ")
print(first_set)

follow_set=[]
for n_t in non_terminals:
        if non_terminals.index(n_t)==0:
                temp=[]
                temp.append(n_t)
                temp.append('$')
                follow_set.append(temp)
        temp=[]
        temp.append(n_t)
        for prod in productions:
                for i in range(2,len(prod),1):
                        ch=prod[i]
                        if ch==n_t:
                                if i==len(prod)-1:
                                        if prod[0]!=n_t:
                                                temp.append("F_"+prod[0])
                                else:
                                        ch2=prod[i+1]
                                        if ch2 in terminals:
                                                temp.append(ch2)
                                        else:
                                                for entry in first_set:
                                                        if entry[0]==ch2 and entry[1] not in temp:
                                                                if entry[1].index("e")!=(-1):
                                                                        if i+1==len(prod)-1:
                                                                                ch3=prod[0]
                                                                                entry[1].append("F_"+ch3)
                                                                        else:
                                                                                ch3=prod[i+2]
                                                                                entry[1].append("F_"+ch3)
                                                                        entry[1].remove("e")
                                                                temp.append(entry[1])
        follow_set.append(temp)

for i in range(5):
        entry1=follow_set[i]
        entry2=follow_set[i+1]
        if entry1[0]==entry2[0]:
                temp=[]
                temp.append(entry1[0])
                t=[]
                t.append(entry1[1])
                t.append(entry2[1])
                temp.append(t)
                follow_set.append(temp)
        i=i+1

follow_set.reverse()
follow_set2=follow_set[:]
follow_set=[]
for entry2 in follow_set2:
        flag=0
        for entry1 in follow_set:
                if entry2[0]==entry1[0]:
                        flag=1
        if flag==0:
                follow_set.append(entry2)
print()
print(follow_set)

for entry in follow_set:
        print(entry)
        if isinstance(entry[1],str):
                if entry[1].find("F_")!=(-1):
                        ind=entry[1].find("F_")
                        n_t=entry[1][ind+2]
                        for f_set in follow_set:
                                if f_set[0]==n_t:
                                        entry[1]=f_set[1]
        if isinstance(entry[1],list):
                for ent in entry[1]:
                        if ent.find("F_")!=(-1):
                                ind=ent.find("F_")
                                n_t=ent[ind+2]
                                for f_set in follow_set:
                                        if f_set[0]==n_t:
                                                for ch in f_set[1]:
                                                        entry[1].append(ch)
                                                entry[1].remove(ent)

print("Follow Set : ")
print(follow_set)

