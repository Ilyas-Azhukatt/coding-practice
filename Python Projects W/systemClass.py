class system:
    'common base class for all systems'
    sysCount = 0

    def __init__(self,name,location,ip):
        self.name = name
        self.location=location
        self.ip=ip
        system.sysCount+=1
    
    def displayCount(self):
        print ("Total Number of  Systems %d" % system.sysCount)

    def displaySystem(self):
        print ("Name:",self.name,"Location:",self.location,"IP Address:",self.ip)

sys1=system("MADM Manjeri","Manjeri TE","192.168.10.111")
sys2=system("MADM Anakkayam","Anakkayam TE","192.168.10.162")

sys1.displaySystem()
sys2.displaySystem()

print ("Total number of systems is : %d" %system.sysCount)
    