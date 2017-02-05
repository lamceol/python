inp = raw_input("Enter Hours: ")
hours = float(inp)
inp = raw_input("Enter Rate: ")
rate = float(inp)


def computepay(a, b):
    if hours <= 40 : 
        pay = rate * hours
    else :
        pay = rate * 40 + ( rate * 1.5 * ( hours - 40) )
    return pay

print computepay(hours, rate)