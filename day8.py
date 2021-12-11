#part 1
total=0
for line in open('data.txt'):
	_,end=line.split('|')
	end=end.split()

	for words in end:
		if len(words)==2 or len(words)==3 or len(words)==4 or len(words)==7:
			total+=1
print(total)

# part 2


digits = {0: 'abcefg',1: 'cf',2: 'acdeg',3: 'acdfg',4: 'bcdf',5: 'abdfg',6: 'abdefg',7: 'acf',8: 'abcdefg',9: 'abcdfg'}

total=0

for line in open('data.txt'):
	start,end=line.split('|')
	start=start.split()
	end=end.split()
	number=''
	A={}
	for word in start:
		if len(word)==2:
			cf=word
	for word in start:
		if len(word)==6 and ((cf[0] in word) != (cf[1] in word)):
			if cf[0] in word:
				A[cf[0]] = 'f'
				A[cf[1]] = 'c'
			else:
				A[cf[1]] = 'f'
				A[cf[0]] = 'c'
	for word in start:
		if len(word)==3:
			for c in word:
				if c not in cf:
					A[c] = 'a'
	for word in start:
		if len(word)==4:
			bd = ''
			for c in word:
				if c not in cf:
					bd += c
	for word in start:
		if len(word)==6 and ((bd[0] in word)!=(bd[1] in word)):
			if bd[0] in word:
				A[bd[0]] = 'b'
				A[bd[1]] = 'd'
			else:
				A[bd[1]] = 'b'
				A[bd[0]] = 'd'
	eg = ''
	for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
		if c not in A:
			eg += c


	for word in start:
		if len(word) == 6 and (eg[0] in word)!=(eg[1] in word):
			if eg[0] in word:
				A[eg[0]] = 'g'
				A[eg[1]] = 'e'
			else:
				A[eg[1]] = 'g'
				A[eg[0]] = 'e'
	

	for word in end:
		temp=''
		for i in word:
			temp+=A[i]
		temp=''.join(sorted(temp))

		for k,v in digits.items():
			if v==temp:
				number+=str(k)



	total+=int(number)

print(total)
	