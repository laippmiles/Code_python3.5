e2f = {'dog':'chien','cat':'chat','walrus':'morse'};
print('e2f:',e2f);
print('what is \'walrus\':',e2f.get('walrus'));
f2e = {};
for name,contenrs in e2f.items():
    f2e[contenrs]=name;
print('f2e:',f2e);
print('what is \'chien\':',f2e.get('chien'));
eset = set(e2f.keys());
print('eset:',eset);

