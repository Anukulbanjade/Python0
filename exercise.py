def getdatafromuser():
    D = {}
    while True:
        studentId = input("Enter student id: ")
        marklist = input("Enter Marks By comma-separated Value: ")
        morestudents = input("Enter 'no' to quit: ")
        if studentId in D:
            print(studentId, "is already inserted")
        else:
            D[studentId] = marklist.split(",")
        if morestudents.lower() == "no":
            return D

studentdata = getdatafromuser()

def getavgmarks(D):
    avgmarks = {}
    for x in D:
        l = D[x]
        s = 0
        for marks in l:
            s += float(marks)
        avgmarks[x] = s / len(l)
    return avgmarks

avgm = getavgmarks(studentdata)

for x in avgm:
    print("student:", x, "got avg marks as:", avgm[x])
