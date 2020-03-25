import subprocess
import csv

header = ("IP","Name","Status","Remarks")

def main():
    #cwritenewIP('aapl.csv','10.10.10.1','Karan','Locked','No Issues')
    s = cgetStatusofIP('aapl.csv','192.168.6.91')
    print s
    #cupdatestatus('aapl.csv','192.168.6.91','Unlocked')

#generic API
def cwriter(header, data, filename, option):
        with open (filename, "w") as csvfile:
            if option == "write":
                movies = csv.writer(csvfile)
                movies.writerow(header)
                for x in data:
                    movies.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames = header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")

#update status
def cupdatestatus(filename,ip,status):
    with open(filename) as file:
        readData = [row for row in csv.DictReader(file)]
        print readData
        index = csearchIP(filename,ip)
        print "index"+str(index)
        readData[index]['Status'] = status
    cwriter(header, readData, filename, "update")

# add new IP data
def cwritenewIP(filename,ip,name,status,remarks):
    mylist = []
    writeData = [] 
    with open(filename) as file:
        DataListDict = [row for row in csv.DictReader(file)]
        for values in DataListDict:
            mylist.append(values['IP'])
            mylist.append(values['Name'])
            mylist.append(values['Status'])
            mylist.append(values['Remarks'])
            writeData.append(mylist)
            mylist = []
        mylist.append(ip)
        mylist.append(name)
        mylist.append(status)
        mylist.append(remarks)
        writeData.append(mylist)
        mylist = []
    cwriter(header, writeData, filename, "write")

#print table
def cprinttable(filename):
    with open(filename) as file:
        readData = csv.reader(file)
        for row in readData:
	    print(row)

#count items
def ccountItems(filename):
    count=0
    with open(filename) as file:
        readData = csv.reader(file)
        for row in readData:
            count = count + 1
    return count

# get status of particular IP
def cgetStatusofIP(filename,ip):
    with open(filename) as file:
        readData = csv.reader(file)
        for row in readData:
            if row[0]==ip:
                return row[2]
        return -1

#search IP in table and return index of IP
def csearchIP(filename,ip):
    count=0
    with open(filename) as file:
        readData = csv.reader(file)
        for row in readData:
            if row[0]==ip:
                return count-1
            count = count + 1
        return -1

def readmyIP():
    ResponseIPAddr = subprocess.check_output(["hostname","-I"])   
    AllIPAddr = ResponseIPAddr.split()
    IPAddr = AllIPAddr[0]
    print "my IP : "+IPAddr
    return IPAddr

def getName():
    name = raw_input("Enter your name : ") 
    return name

if __name__=="__main__":
    main()
