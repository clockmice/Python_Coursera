def computepay(h,r):
    if h <= 40 :
        pay = h * r
    
    else :
        pay = 40 * r + (h - 40) * (r * 1.5)
    
    return pay


hrs = raw_input('Enter Hours: ')
a = float(hrs)

rate = raw_input('Enter Rate: ')
b = float(rate)

print computepay(a,b)
