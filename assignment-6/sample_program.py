from sklearn import tree

with open("diabetes.csv", "r") as f:
    data = f.readlines()
feats = data[0]
feats = feats.replace("\n", "")
feats = feats.split(",")

feats = feats[0 : (len(feats) - 1)]
dat = []
labs = []
for i in range(1, len(data)):
    line = data[i]
    line = line.replace("\n", "")
    csvline = line.split(",")
    labs = labs + [int(csvline[len(csvline) - 1])]
    csvline = [float(csvline[i]) for i in range(len(csvline) - 1)]
    dat = dat + [csvline]

print(len(dat))

print(labs)

clf = tree.DecisionTreeClassifier(max_leaf_nodes=3)
clf = clf.fit(dat, labs)

correct = 0
for i in range(len(dat)):
    if clf.predict([dat[i]]) == labs[i]:
        correct = correct + 1

print(f"Accuracy: {100.0* correct / len(dat)}")
