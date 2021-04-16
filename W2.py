##test01 算錢
#w=50*int(input("How many 50?"))
#x=10*int(input("How many 10?"))
#y=5*int(input("How many 5?"))
#z=1*int(input('How many 1?'))
#print(w+x+y+z)


#test02 找錢
#int(input("How much do you spend?"))
cons=500
back=1000-cons
fiveh=(back//500)
oneh=(back-500*fiveh)//100
fifd=(back-500*fiveh-100*oneh)//50
tend=(back-500*fiveh-100*oneh-50*fifd)//10
fivd=(back-500*fiveh-100*oneh-50*fifd-10*tend)//5
oned=(back-500*fiveh-100*oneh-50*fifd-10*tend)%5
print(fiveh, oneh, fifd, tend, fivd, oned)