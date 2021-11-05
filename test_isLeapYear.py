from isLeapYear import isLeapYear



def testleapyear():
    assert isLeapYear(1922) == False
                    # 1922 % 4 != 0
    assert isLeapYear(2004) == True
                    # 2004 % 4 == 0
                    # 2004 % 100 != 0
    assert isLeapYear(2009) == False
                    # 2009 % 4 != 0
    assert isLeapYear(2000) == True
                    # 2000 % 4 == 0
                    # 2000 % 100 == 0
                    # 2000 % 400 == 0



    #skal feile

    assert isLeapYear(1922) == True
                    
    assert isLeapYear(2004) == False
                  
    assert isLeapYear(2009) == True
                    
    assert isLeapYear(2000) == False
