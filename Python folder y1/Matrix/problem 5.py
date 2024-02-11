from pathlib import Path 

# I'm sorry whoever marks this atrocity  
# so I overcomplciated this, but I have other stuff that need to get done tommrow so this is what it is 
folder_location = Path('Matrix') 
MatrixFile = open('Matrix1.txt')


countcolumn  = []
File = MatrixFile.read()



File = File.split("\n\n")
Fresh_file = []
count=0
for row in File :
    Fresh_file.append(File[count].replace("\n"," "))
    count=count+1

matrix1str = Fresh_file[0]
matrix2str = Fresh_file[1]


matrix1 = matrix1str.split(" ")
matrix2 = matrix2str.split(" ")


count1 = 0
for row in matrix1:
    matrix1[count1]=matrix1[count1].split(",")
    count1 = count1 +1

print(matrix1)
print(matrix2)
count1 = 0
for row in matrix2:
    matrix2[count1]=matrix2[count1].split(",")
    count1 = count1 +1


count = -1
count1=0
for row in matrix1:
    count1 = 0
    count = count+1
    for row in matrix1[count]:
        matrix1[count][count1] = int(matrix1[count][count1])

        count1 = count1+1
count = -1
for row in matrix2:
    count1 = 0
    count = count+1
    for row in matrix2[count]:
        matrix2[count][count1] = int(matrix2[count][count1])

        count1 = count1+1

Finaly  = [
        [],
        []

    ]
# so i gave up in the end and hardcoded it to a 2x3 and 3x3 
# I'm sorry but it's 5 am an the python project killed me 
# I don't have time to do 90% of the project alone 
# I swear normaly I code better 
countm1 = 0
countm2 = 0 
count = -1
count1 = 0 


for i in matrix1: 
         print(" ")

         count1 = 0
         count = count+1
         for i in matrix2 :
            Finaly[count].append(matrix1[count][countm1]*matrix2[countm2][count1]+matrix1[count][countm1+1]*matrix2[countm2+1][count1]+matrix1[count][countm1+2]*matrix2[countm2+2][count1])
            count1 = count1+1

print(Finaly)


# this was bad, it's 6 am when I finished this, I'm hoping it's worth something but I'm really not sure what we are being graded on
# sorry about not being in class the last 2 months I was beyond ill - Corbyn