marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

'''
simple input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''
