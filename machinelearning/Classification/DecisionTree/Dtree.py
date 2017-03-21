from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

allElectronicsData = open(r'example.csv','rb')
reader = csv.reader(allElectronicsData)
headers = reader.next()
#print headers

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row)-1])
    rowDic = {}
    for i in range(1,len(row)-1):
        rowDic[headers[i]] = row[i]
    featureList.append(rowDic)

print featureList
print labelList

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()


lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(dummyX,dummyY)


with open("all.dot","w") as f:
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)

'''
dot_data = StringIO()
tree.export_graphviz(clf,out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph.write_pdf("tree.pdf")
'''

oneRowX = dummyX[0,:]

newRowX = oneRowX
newRowX[0]=1
newRowX[1]=0
print "newRowX:"+str(newRowX)

predictY = clf.predict(newRowX)
print "predictY:"+str(predictY)


'''dot -Tpdf all.dot -o all.pdf'''