import hashlib
import time
import multiprocessing

def passwordsCrack(characterBase, tempTry, passwords, length):
    #if the initialized trying characters less than the length it is calculating now and no corressponds password add a new character space
    if len(tempTry) < length:
        tempResult = ""
        for x in characterBase:
            tempResult = passwordsCrack(characterBase, (tempTry + x), passwords,length)
    #if there is the result then just return the value        
            if tempResult != None:
                return tempResult
        return None
    
    elif length == len(tempTry):
        #if the passwords match then return the password and move to the next passwords in the inputList
        trying=hashlib.md5((tempTry).encode('utf-8')).hexdigest()
        if trying == passwords :
            return tempTry
def multiprocessing_func(passwords):
    
    passwords=passwords.rstrip()
    #start timing
    startTime = time.time()
    solved = False;
    #intialize the variables, the results set to empty and the maximum length of the password would be 8
    result=""
    length=8 
    for i in range(length):
        if not solved:
            tempcompare = ""
            result = passwordsCrack(characterBase,tempcompare, passwords, i)
  


            if result != "NULL" and result != None:
                solved = True;
                #After get out the result print all of the data to the output file
                elastingT=time.time()-startTime
                print("The hashed password is:" +passwords+"\n")
                print( "The cracked password is:" + result+"\n")
                print( "And the time to solve it lasts (in seconds):"+str(elastingT)+"\n")
                outputFile.write("\n")
                print("I have finished a password")


#open the files to read and write
inputFile=open("hashes.txt","r")
inputList=inputFile.readlines()
outputFile=open("result.txt","w")
processes=[]

#Construct the character base for the passwords cracking function to search
characterBase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@','!']

#Read the hash one by one
for passwords in inputList:
    #multiprocessing_func(passwords)
    result=multiprocessing.Process(target=multiprocessing_func,args=(passwords,))
    processes.append(result)
    result.start()
    for result in processes:
        result.join() 
inputFile.close()
