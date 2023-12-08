
try :
	inp = raw_input("Enter Hours: ")
	hours = float(inp)
	inp = raw_input("Enter Rate: ")
	rate = float(inp)

except:
	print "ah here, thats not a float.. "
	quit()

	print rate, hours
	if hours <= 40 : 
		pay = rate * hours
	else :
		pay = rate * 40 + ( rate * 1.5 * ( hours - 40) )
	print pay



largest = None
smallest = None

mylist = [0]

while True:
    try:
        p = raw_input("Enter a number: ")
        num = float(p)
    except:
        print "Please enter a number"
    
    if num == "done" : 
        break
    mylist.extend(num)
    for i in mylist:
        if i > largest:
            largest = i
        if smallest is None:
            smallest = i
        elif i < smallest:
            smallest = i
    
print mylist
print num

print "Maximum", largest
print "Minimum", smallest









