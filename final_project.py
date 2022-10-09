
#sonu Yadav
#C0844501
# C# Final Poject

import numpy as np
import csv  
import matplotlib.pyplot as plt
from numpy import random
from matplotlib.animation import FuncAnimation


limit = 30
x_axis_data = []
y_axis_data = []
x = []
y = []

#loop to generate the random number
for i in range(1900,2023):
    x.append(i)
    y.append(str(round(random.uniform(0,30),1)))

#csv file to write the data
with open('inflation_data.csv', 'w', encoding='UTF8',newline='') as input_file:
    writer = csv.writer(input_file)
   
    for i in range(len(y)):
        data = x[i],y[i] 
        writer.writerow(data) 

x.clear()
y.clear()

#open the csv file to read the data
with open('inflation_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader:

        x.append(int(row[0]))
        y.append(float(row[1]))

fig,ax = plt.subplots()

ax.set_xlim(1900,1930)
ax.set_ylim(0,40)

ax.set_title('Inflation Rate Year 1900 to 2022')
#X_label for the graph
plt.xlabel("Years 1900 to 1930")
#Y_label for the graph
plt.ylabel("INFLATION RATE \nMaximum Value:- "+str(max(y))+" & Minimum Value:- "+str(min(y)))

line, = ax.plot(0,0)


#method to display the graph 
def line_graph(i):
    global limit 


    if(i == len(x)-1) :
        
        limit=30 
        ax.set_xlim(1900,1930) 
        #X_label for the graph
        plt.xlabel("Years 1900 to 1930") 
        # Data is appended to list
        x_axis_data.append(x[i])
        y_axis_data.append(float(y[i]))
        #passing the data to the graph and display 
        line.set_xdata(x_axis_data)
        line.set_ydata(y_axis_data)
        # Clear the data
        x_axis_data.clear()
        y_axis_data.clear()
  
    elif(i == limit):
        # Data is appended to list
        x_axis_data.append(x[i])
        y_axis_data.append(float(y[i]))
        #passing the data to the graph and display 
        line.set_xdata(x_axis_data)
        line.set_ydata(y_axis_data)
      
        ax.set_xlim(x[i],x[i]+30)
        #X_label for the graph
        plt.xlabel("Years "+str(x[i])+" to "+str(x[i]+30))
     
        limit = limit+30
        # Clear the data
        x_axis_data.clear()
        y_axis_data.clear()
       # Data is appended to list
        x_axis_data.append(x[i])
        y_axis_data.append(float(y[i]))
        #passing the data to the graph and display 
        line.set_xdata(x_axis_data)
        line.set_ydata(y_axis_data)
    
    else :
      
        x_axis_data.append(x[i])
        y_axis_data.append(float(y[i]))
        #passing the data to the graph and display 
        line.set_xdata(x_axis_data)
        line.set_ydata(y_axis_data)
     
    return line,


animation = FuncAnimation(fig, func=line_graph,frames=np.arange(0,123,1), interval=300)

plt.show()