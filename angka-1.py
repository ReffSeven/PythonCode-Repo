"""
#####  #   #  #####  
    #  #   #  #      
#####  #####  #####  
    #      #      #  
#####      #  #####  
"""

n_data = input("Angka : ")
n_size = int(input("Tinggi : "))
s_size = int(n_size/2)
n_len = len(n_data)
n_angka = []

for i in range(n_len):
	xy_data = []
	if(n_data[i]=='0'):
		xy_data = [''.join(['#' if(y==0) or(y==n_size-1) or(x==0) or(x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	elif(n_data[i]=='1'):
		xy_data = [''.join(['#' if(y==0 and x>=s_size) or(x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	elif(n_data[i]=='2'):
		xy_data = [''.join(['#' if(y==0) or(y==s_size) or(y==n_size-1) or(y>=s_size and x==0) or(y<=s_size and x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	elif(n_data[i]=='3'):
		xy_data = [''.join(['#' if(y==0) or(y==s_size) or(y==n_size-1) or(x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	elif(n_data[i]=='4'):
		xy_data = [''.join(['#' if(y==s_size) or(y<=s_size and x==0) or(x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	elif(n_data[i]=='5'):
		xy_data = [''.join(['#' if(y==0) or(y==s_size) or(y==n_size-1) or(y<=s_size and x==0) or(y>=s_size and x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	elif(n_data[i]=='6'):
		xy_data = [''.join(['#' if(y==0) or(y==s_size) or(y==n_size-1) or(x==0) or(y>=s_size and x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	elif(n_data[i]=='7'):
		xy_data = [''.join(['#' if(y==0) or(x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	elif(n_data[i]=='8'):
		xy_data = [''.join(['#' if(y==0) or(y==s_size) or(y==n_size-1) or(x==0) or(x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	elif(n_data[i]=='9'):
		xy_data = [''.join(['#' if(y==0) or(y==s_size) or(y==n_size-1) or(y<=s_size and x==0) or(x==n_size-1) else ' ' for x in range(n_size)]) for y in range(n_size)]
	
	n_angka.append(xy_data)

print('')
for i in range(len(n_angka[0])):
	for j in range(len(n_angka)):
		print(n_angka[j][i] + '  ', end='')
	print('')
