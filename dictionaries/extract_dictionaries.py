import pickle

f = open("babyanimal.txt", 'r')
babyanimal_dict = {}
for line in f:
	print line.split("	")
	babyanimal_dict[line.split("	")[0]] = line.split("	")[1:]

print babyanimal_dict

pickle.dump(babyanimal_dict, open("babyanimal.dat", "wb"))

dict2 = pickle.load( open( "babyanimal.dat", "rb" ) )
print 'dict2', dict2