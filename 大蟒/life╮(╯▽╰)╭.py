people = ['Henri','Grumpy','Lucy'];
empty_dic = {};
dicanimals = {'cats':people,'octopi':empty_dic,'emus':empty_dic};
life = {'animals':dicanimals,'plants':empty_dic,'others':empty_dic};
print(list(life.keys()));
print(list(life['animals'].keys()));
print(list(life['animals']['cats']));