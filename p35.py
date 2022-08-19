#p35.py
#Ryan Yee
#7/24/19
#Python Version: 3.7.3
#Description: a program which reads the data from sunspots.txt
#and computes the average for each year, writing them to a file averages.txt

myFile = open('sunspots.txt','r')
fileAsListOfLines = myFile.read().splitlines()
myFile.close()

otherFile = open('averages.txt','w')
otherFile.write("year average\n")
for j in range(0,len(fileAsListOfLines),1):
    aLine = fileAsListOfLines[j]
    #print(aLine)
    lineData = aLine.split()
    #print(lineData)
    year = lineData[0]
    #print('year =', year)
    sumData = 0
    for i in range(1,len(lineData),1):
        sumData += float(lineData[i])
    avg = sumData/(len(lineData)-1)
    #print('year', year,'avg %.2f' %avg)
    otherFile.write("%s   %.2f \n" %(year,avg))
otherFile.close()

'''
see file for result
'''
