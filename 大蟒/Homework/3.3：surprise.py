surprise = ['Groucho','Chico','Harpo'];
a = surprise[-1].lower();
surprise[-1]= a[::-1].capitalize();
print(surprise)