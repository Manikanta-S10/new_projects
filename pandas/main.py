'''
   dataset is in weather_data.csv

'''

#importing pandas python module 
import pandas
 
data = pandas.read_csv('weather_data.csv')    #Reading data using pandas
print(data)    # printing whole data that we have read using pandas

print(data.temp) #Feteching particular column (example: temp)

print(data[data.day == 'Tuesday'])  # Fetching partricualr row from the data

Wednesday = data[data.day == 'Wednesday']  #Fetching particular element from thye data
print(Wednesday.day)

# Converting from dict to dataFrame (pandas)
student_dict = {
    'Name' : ['Mani','Ram','Sita','Hanuman'],
    'Course' : ['CSE','ISE','ISE','EEE'],
    'Score': [96,97,100,97]
}
Df = pandas.DataFrame(student_dict)
print(Df)

#Looping through dataset in pandas
for (index,row) in Df.iterrows():    
    print(index)                      #index will print index number
    print(row)                        #row will fetch each rows
    if row.Score == 100:
        print(row.Name)




