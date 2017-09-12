#!/usr/bin/python
from DType import *
import dt_zip
def main():
    print("Beginning tests...")
    a=DDataFile("../tests/zip1.zip")
    for i in dt_zip.pk.tests:
        print i.name, ", priority:",i.priority
        check=True
        for j in i.requirements:
            willPass=a.checkReq(j)
            print "\t\tChecking requirement:",j,"....",willPass
            if not willPass: break
        else:
            print "\tPasses? ",i.fn(a)
if __name__ == '__main__':
    main()

