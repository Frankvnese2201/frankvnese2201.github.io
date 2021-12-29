a=[5,3,5,6,7,2,1,10,12]
for i in range(0,len(a)):
	key=a[i]
	j=i-1
	while j>=0 and key<a[j]:
	
		a[j+1]=a[j]
		j=j-1

	
	a[j+1]=key

for i in range(0,len(a)):
	print(a[i])

