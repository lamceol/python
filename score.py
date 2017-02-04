#
# Script for checking the score of a grade
# Robert Lambe
#

# Get input
inp = raw_input("Enter Score: ")
score = float(inp)

# Calculate score
if score < 0 :
    print "Error1"
    quit()

elif score > 1 :
    print "Error2"
    quit()

elif score >= 0.9 :
    print "A"

elif score >= 0.8 :
    print "B"

elif score >= 0.7 :
    print "C"

elif score >= 0.6 :
    print "D"

elif score < 0.6 :
    print "F"
