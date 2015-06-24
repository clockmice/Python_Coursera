hrs = raw_input ('Enter Hours: ')
try:
    h = float (hrs)
except:
    print ('Numeric numbers only')
    quit ()
    
rate = raw_input ('Enter Rate: ')
try:
    r = float (rate)
except:
    print ('Numeric numbers only')
    quit ()
    
if h <= 40 :
    pay = h * r
    print pay
else :
    pay = 40 * r + (h - 40) * (r * 1.5)
    print pay
        

