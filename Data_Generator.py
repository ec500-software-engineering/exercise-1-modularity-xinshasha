import random

f=open('./bo.txt','w')
for i in range(10):
	f.write("2018 ")
	f.write(str(random.random()))
	f.write('\n')
f.close()

f=open('./bp.txt','w')
for i in range(10):
	f.write("2018 ")
	f.write(str(random.random()*30+90))
	f.write('\n')
f.close()

f=open('./pulse.txt','w')
for i in range(10):
	f.write("2018 ")
	f.write(str(random.random()*30+60))
	f.write('\n')
f.close()