from collections import defaultdict


Set=defaultdict(int)
Set2=defaultdict(int)

# part 1
for line in open('data.in'):
	begin,end=line.split('->')
	x1,y1=begin.split(',')
	x2,y2=end.split(',')
	x1=int(x1)
	y1=int(y1)
	x2=int(x2)
	y2=int(y2)

	x1,x2=min(x1,x2),max(x1,x2)
	y1,y2=min(y1,y2),max(y1,y2)

	if x1==x2 or y1==y2:
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				if (x,y) not in Set:
					Set[(x,y)]=0
				Set[(x,y)]+=1

	

# part 2
for line in open('data.in'):
	begin,end=line.split('->')
	x1,y1=begin.split(',')
	x2,y2=end.split(',')
	x1=int(x1)
	y1=int(y1)
	x2=int(x2)
	y2=int(y2)

	xdiff=x2-x1
	ydiff=y2-y1


	for i in range(1+max(abs(xdiff),abs(ydiff))):
		if xdiff>0:
			x=x1+1*i
		else:
			if xdiff<0:
				x=x1-1*i
			else:
				x=x1
		if ydiff>0:
			y=y1+1*i
		else:
			if ydiff<0:
				y=y1-1*i
			else:
				y=y1
		Set2[(x,y)]+=1



ans=0
for a in Set:
	if Set[a] > 1:
		ans+=1
print(ans)
ans=0
for a in Set2:
	if Set2[a]>1:
		ans+=1
print(ans)

