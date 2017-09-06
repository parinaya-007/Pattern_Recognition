import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
# import math as m

##############################

def xfrange(start, stop, step):
  i = 0.0
  while start + i * step < stop:
    yield start + i * step
    i += 1.0

# Reads file contents
def readFile(file):
  X = []
  Y = []
  lineCount = 0
  for line in file:
    x = line.split()[0]
    y = line.split()[1]
    X.append(x)
    Y.append(y)
    lineCount = lineCount + 1
  return X, Y, lineCount

# gets class' plot style
def getClassPlotStyle(classNum, X, Y, rgba):
  # print "rgbaVal = ", rgba
  return go.Scatter(
    x = X,
    y = Y,
    name = 'Class ' + str(classNum),
    mode = 'markers',
    marker = dict(
      size = 7,
      color = rgba,
      line = dict(
        width = 2,
        color = 'rgb(0, 0, 0)'
        )
      )
    )

# gets mean of the vector
def getMean(X):
  Sum = 0.0
  size = float(len(X))
  for x in X:
    Sum = Sum + float(x)
  return Sum/size

# gets variance of the vector
def getVariance(X, mean):
  Sum = 0.0
  size = float(len(X))
  for x in X:
  	Sum = Sum + float((float(x)-mean))*float((float(x)-mean))
  return Sum/size

# returns trace of the object
def Trace(X, Color):
  a, b = X
  return go.Scatter(
    x = a,
    y = b,
    mode = 'markers',
    marker = dict(
      size = 5,
      color = Color
      # ,line = dict(
      #   width = 0,
      #   color = 'rgb()'
      #   )
      )
    )

# calculates discriminant function
def getDiscriminant(mean, X, var):
  meanT = mean.transpose()
  uTx = np.dot(meanT, X)
  # print(np.shape(uTx))
  uTu = np.dot(meanT, mean)
  return uTx*(1.0/var) - uTu*(1.0/(2.0*var))

##############################
##############################

# Reading files
file1 = open("LS_Group14/Class1.txt", 'r')
file2 = open("LS_Group14/Class2.txt", 'r')
file3 = open("LS_Group14/Class3.txt", 'r')
if not file1 or not file2 or not file3:
  print("file not opened")

data = []

##############################

lineCount = 0

# Reading Class 1 file
X1, Y1, lineCount = readFile(file1)
meanX1 = getMean(X1)
meanY1 = getMean(Y1)
varX1 = getVariance(X1, meanX1)
varY1 = getVariance(Y1, meanY1)

# Checking read file contents
limit = int(0.75*lineCount + 1)
x1 = X1
y1 = Y1
print(len(x1))
X1 = X1[:limit]
Y1 = Y1[:limit]
print(len(X1))
testX1 = x1[limit:]
testY1 = y1[limit:]
print(len(testX1))
print('lineCount=')
print(lineCount)
print('\nlimit=')
print(limit)
print('\n')
# print(X1)

# Specifying Scatter-plot style
Class1 = getClassPlotStyle('1', X1, Y1, 'rgba(0, 0, 150, 1)')
data.append(Class1)

##############################

lineCount = 0

# Reading Class 2 file
X2, Y2, lineCount = readFile(file2)
meanX2 = getMean(X2)
meanY2 = getMean(Y2)
varX2 = getVariance(X2, meanX2)
varY2 = getVariance(Y2, meanY2)

# Checking read file contents
limit = int(0.75*lineCount + 1)
x2 = X2
y2 = Y2
X2 = X2[:limit]
Y2 = Y2[:limit]
testX2 = x2[limit:]
testY2 = y2[limit:]
print('lineCount=')
print(lineCount)
print('\nlimit=')
print(limit)
print('\n')
# print(X2)

# Specifying Scatter-plot style 
Class2 = getClassPlotStyle('2', X2, Y2, 'rgba(0, 150, 0, 1)')
data.append(Class2)

##############################

lineCount = 0

# Reading Class 3 file
X3, Y3, lineCount = readFile(file3)
meanX3 = getMean(X3)
meanY3 = getMean(Y3)
varX3 = getVariance(X3, meanX3)
varY3 = getVariance(Y3, meanY3)

# Checking read file contents
limit = int(0.75*lineCount + 1)
x3 = X3
y3 = Y3
X3 = X3[:limit]
Y3 = Y3[:limit]
testX3 = x3[limit:]
testY3 = y3[limit:]
print('lineCount=')
print(lineCount)
print('\nlimit=')
print(limit)
print('\n')
# print(X3)

# Specifying Scatter-plot style 
Class3 = getClassPlotStyle('3', X3, Y3, 'rgba(150, 0, 0, 1)')
data.append(Class3)

##############################

varX = (varX1 + varX2 + varX3)/3.0
varY = (varY1 + varY2 + varY3)/3.0
var = (varX + varY)/2.0
print("var = ", var)
# I = np.eye(2)
# covMatrix = I*var
# print(covMatrix)

mean1 = np.array([[meanX1], [meanY1]], dtype='float64')
print("mean1 = ", mean1)
mean2 = np.array([[meanX2], [meanY2]], dtype='float64')
print("mean2 = ", mean2)
mean3 = np.array([[meanX3], [meanY3]], dtype='float64')
print("mean3 = ", mean3)

# discriminant function for different classes
for i in xfrange(-10.0, 26.0, 0.4):
  for j in xfrange(-15.0, 20.0, 0.4):
    x = np.array([[i], [j]])
    P1 = getDiscriminant(mean1, x, var)
    print "P1 = ", P1
    P2 = getDiscriminant(mean2, x, var)
    print "P2 = ", P2
    P3 = getDiscriminant(mean3, x, var)
    print "P3 = ", P3
    P = np.amax([P3, P2, P1], axis=0)
    print(np.shape(P))
    print "P = ", P
    if P==P1:
      print "Blue", "\n"
      data.append(Trace(x, 'rgba(50, 50, 250, 1)'))
    elif P==P2:
      print "Green", "\n"
      data.append(Trace(x, 'rgba(50, 250, 50, 1)'))
    elif P==P3:
      print "Red", "\n"
      data.append(Trace(x, 'rgba(250, 50, 50, 1)'))

# i = 0
# j = 0
# while i < len(testX1) and j < len(testY1):
#   k = np.array([[testX1[i]], [testY1[j]]], dtype='float64')
#   P1 = getDiscriminant(mean1, k, var)
#   P2 = getDiscriminant(mean2, k, var)
#   P3 = getDiscriminant(mean3, k, var)
#   P = np.amax([P3, P2, P1], axis=0)
#   if P==P1:
#     data.append(Trace(k, 'rgba(0, 0, 250, 1)'))
#   elif P==P2:
#     data.append(Trace(k, 'rgba(0, 250, 0, 1)'))
#   elif P==P3:
#     data.append(Trace(k, 'rgba(250, 0, 0, 1)'))
#   i = i + 1
#   j = j + 1

# i = 0
# j = 0
# while i < len(testX2) and j < len(testY2):
#   k = np.array([[testX2[i]], [testY2[j]]], dtype='float64')
#   P1 = getDiscriminant(mean1, k, var)
#   P2 = getDiscriminant(mean2, k, var)
#   P3 = getDiscriminant(mean3, k, var)
#   P = np.amax([P3, P2, P1], axis=0)
#   if P==P1:
#     data.append(Trace(k, 'rgba(0, 0, 250, 1)'))
#   elif P==P2:
#     data.append(Trace(k, 'rgba(0, 250, 0, 1)'))
#   elif P==P3:
#     data.append(Trace(k, 'rgba(250, 0, 0, 1)'))
#   i = i + 1
#   j = j + 1

# i = 0
# j = 0
# while i < len(testX3) and j < len(testY3):
#   k = np.array([[testX3[i]], [testY3[j]]], dtype='float64')
#   P1 = getDiscriminant(mean1, k, var)
#   P2 = getDiscriminant(mean2, k, var)
#   P3 = getDiscriminant(mean3, k, var)
#   P = np.amax([P3, P2, P1], axis=0)
#   if P==P1:
#     data.append(Trace(k, 'rgba(0, 0, 250, 1)'))
#   elif P==P2:
#     data.append(Trace(k, 'rgba(0, 250, 0, 1)'))
#   elif P==P3:
#     data.append(Trace(k, 'rgba(250, 0, 0, 1)'))
#   i = i + 1
#   j = j + 1

##############################

# Creating and Showing plot
# plotly.offline.plot(data, filename='group14-LS-plot')
import plotly.offline as offline
# offline.init_notebook_mode()
# offline.iplot({'data': data, 'layout': {'title': 'Test Plot','font': dict(size=16)}},image='png')

offline.plot({'data': data, 'layout': {'title': 'Test Plot', 'font': dict(family='Comic Sans MS', size=16)}},auto_open=True, image = 'png', image_filename='plot_image' ,output_type='file', image_width=800, image_height=600, validate=False)

# offline plotting 
# layout = go.Layout(title='LS_PLot', width=1000, height=700)
# fig = go.Figure(data=data, layout=layout)
# py.image.save_as(fig, filename='group14-LS-plot.png')

# from IPython.display import Image
# Image('group14-LS-plot.png')

##############################