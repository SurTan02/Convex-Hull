import convexHull as myConvexHull
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

print("Daftar Dataset")
print("1. Dataset iris")
print("2. Dataset wine")
print("3. Dataset breast cancer")

#pemilihan dataset
option = int(input("Pilih Dataset yang ingin digunakan : "))
while (option not in range(1,4)):
	option = int(input("Pilih Dataset yang ingin digunakan : "))
	
if ( option == 1 ):
	data = datasets.load_iris()
elif ( option == 2):
	data = datasets.load_wine()
elif ( option == 3):
	data = datasets.load_breast_cancer()


#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

#pemilihan atribut yang ingin digunakan
print("\nDaftar atribut:")
for i in range(len(data.feature_names)):
	print(i+1,  data.feature_names[i])
ATx = int(input("atribut-x yang ingin digunakan : "))
ATy = int(input("atribut-y yang ingin digunakan : "))


#visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
colors = ['coral','lime','blueviolet', 'magenta','blue', 'red', 'green']
plt.title(data.feature_names[ATx-1] + ' vs ' + data.feature_names[ATy-1])
plt.xlabel(data.feature_names[ATx-1])
plt.ylabel(data.feature_names[ATy-1])

for i in range(len(data.target_names)):
	bucket = df[df['Target'] == i]
	bucket = bucket.iloc[:,[ATx-1,ATy-1]].values 
	
	# Copy titik2 pada bucket ke arr
	arr=[]
	for x in bucket:
		arr +=[[x[0], x[1]]]
	hulls = myConvexHull.quickhull(arr)
	
	# Digunakan untuk keperluan plot
	x_points = []
	y_points = []
	for point in hulls:
		x_points.append(point[0])
		y_points.append(point[1])

	x_points.append(hulls[0][0])
	y_points.append(hulls[0][1])

	
	plt.plot(x_points, y_points, color = colors[i])
	plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color = colors[i])

plt.legend()
plt.show()

