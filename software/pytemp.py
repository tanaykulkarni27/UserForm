import sys
def debug(*a):
	print(a,file = sys.stderr,flush = True)
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
