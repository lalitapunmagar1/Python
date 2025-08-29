from sklearn import preprocessing

weather= ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny', 'Overcast', 'Rainy']
temp= ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
humidity=['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High', 'Normal','High']
wind= ['Weak','','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','']
play= ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

le = preprocessing.LabelEncoder() #Encode target labels with value

we = le.fit_transform(weather)#weather data into number 
t = le.fit_transform(temp)
wn = le.fit_transform(wind)
h = le.fit_transform(humidity)
p = le.fit_transform(play)

features=zip(we, t, h, wn)
inp = list(features)
# print ("Input data: ")
# print(inp)
print("Actual Output: ")
print(play)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(inp,p)

predicted = model.predict([[0, 0, 1, 0 ]])
print ("Predicted value is: ", predicted)
if(predicted==1):
    print("Play Tennis: Yes")
else:
    print("Play Tennis: No")
