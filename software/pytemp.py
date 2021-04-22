def debug(*args):
		try:
			print(*args)
		except:
				print(args)
def solve():
		pass
t = int(input())
for i in range(1,t+1):
		print("Case #{}:".format(i),end=' ')
		solve()
