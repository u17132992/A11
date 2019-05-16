import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
data = pd.read_csv("C:/Users/Public/Desktop/Projects/Python/Assignment11/mpg.csv")

data["Power_To_Weight"] = data["horsepower"] / data["weight"] 

print(data)


eightcylinders = data[data.cylinders == 8]

print(eightcylinders)

correlation = eightcylinders["horsepower"].corr(eightcylinders["weight"])


print(correlation)



fourcylinders = data[data.cylinders == 4]
sixcylinders = data[data.cylinders == 6]
threecylinders = data[data.cylinders == 3]
fivecylinders = data[data.cylinders == 5]


plt.scatter(threecylinders.cylinders, threecylinders.mpg)
plt.scatter(fourcylinders.cylinders, fourcylinders.mpg)
plt.scatter(fivecylinders.cylinders, fivecylinders.mpg)
plt.scatter(sixcylinders.cylinders, sixcylinders.mpg)
plt.scatter(eightcylinders.cylinders, eightcylinders.mpg)
plt.legend(['3 cylinders','4 cylinders', '5 cylinders', '6 cylinders', '8 cylinders' ])
plt.xlabel('Cylinder Amount')
plt.ylabel('Mpg attained')
plt.title('How the amounts of cylinders impact the mpg of a vehicle')
plt.show()