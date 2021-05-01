def debug_helper(x,ok = True):
	
	try:
		n = len(x)
		print('{',end = '')
		for i in range(n):
			if i != n-1:
				debug_helper(x[i],False)
			else:
				debug_helper(x[i],True)
		if not ok:
			print('}',end=',')
		else:
			print('}',end = '')
	except:
		if ok:
			print(x,end='')
		else:
			print(x,end=',')
			
	#	print('}')
def debug(*a):
	for i in range(len(a)):
		if i < len(a)-1:
			debug_helper(a[i],False)
		else:
			debug_helper(a[i],True)
def read(typ = str):
	return typ(input())
def read_arr(typ):
	return list(map(typ,input().split()))

def solve():
	print()
t = int(input())
for i in range(1,t+1):
		print("Case #{}:".format(i),end=' ')
		solve()
