from collections import defaultdict

Data=[5,1,2,1,5,3,1,1,1,1,1,2,5,4,1,1,1,1,2,1,2,1,1,1,1,1,2,1,5,1,1,1,3,1,1,1,3,1,1,3,1,1,4,3,1,1,4,1,1,1,1,2,1,1,1,5,1,1,5,1,1,1,4,4,2,5,1,1,5,1,1,2,2,1,2,1,1,5,3,1,2,1,1,3,1,4,3,3,1,1,3,1,5,1,1,3,1,1,4,4,1,1,1,5,1,1,1,4,4,1,3,1,4,1,1,4,5,1,1,1,4,3,1,4,1,1,4,4,3,5,1,2,2,1,2,2,1,1,1,2,1,1,1,4,1,1,3,1,1,2,1,4,1,1,1,1,1,1,1,1,2,2,1,1,5,5,1,1,1,5,1,1,1,1,5,1,3,2,1,1,5,2,3,1,2,2,2,5,1,1,3,1,1,1,5,1,4,1,1,1,3,2,1,3,3,1,3,1,1,1,1,1,1,1,2,3,1,5,1,4,1,3,5,1,1,1,2,2,1,1,1,1,5,4,1,1,3,1,2,4,2,1,1,3,5,1,1,1,3,1,1,1,5,1,1,1,1,1,3,1,1,1,4,1,1,1,1,2,2,1,1,1,1,5,3,1,2,3,4,1,1,5,1,2,4,2,1,1,1,2,1,1,1,1,1,1,1,4,1,5]


# # part 1

# for i in range(80):
# 	Temp=[]
# 	for d in Data:
# 		if d==0:
# 			Temp.append(8)
# 			Temp.append(6)
# 		else:
# 			Temp.append(d-1)
# 	Data=Temp

# print(len(Data))


# # part 2

def Totalfish(days):
	A= defaultdict(int)
	for d in Data:
		if d not in A:
			A[d]=0
		A[d]+=1
	
	for i in range(days):
		Temp=defaultdict(int)
		for key,val in A.items():
			if key==0:
				Temp[6]+=val
				Temp[8]+=val
			else:
				Temp[key-1]+=val
		A=Temp
	
	ans=0
	for _,val in A.items():
		ans+=val
	return ans
print("80 days : ",Totalfish(80))
print("256 days : ",Totalfish(256))
