TestCases = int(input()) # Convert number of test cases to an integer

#Initialize variables
counter = 0 #this is the number of IO advertisements AKA the output number
I = 0
i = 0

for index in range(TestCases): #Loop through the test cases
    S = input() # S is the string containing the data I need to search
    case = index + 1 #I need the "case number" for the output; since index starts at 0, I add a 1 to it
    for j in S: #Loop through the advertisements
        if j == 'I': #I am counting how many capital I's there are in this data set
            I+=1
        elif j == 'i': #I counted the number of lowercase I's in the data set
            i+=1
        elif j == 'o': #If there is a lowercase o, I tested it against the lowercase i first
            if i == 0: #if there is NOT a lowercase i already, then this o must be paired with an uppercase I
                I -=1
            else: #if there is a lowercase i already, then I want to pair that off to the lowercase o first, since I'm seeing how many IO pairs there are
                i -=1
        elif j == 'O': #if there is an uppercase O, I prefer to pair it with an uppercase I so I test that first
            if I == 0: #if there is no uppercase I before this capital O, I must 'pair' it with a lowercase i
                i -=1
            else: #if there IS a capital I, I'll pair it with this capital O and increment the counter
                counter+=1
                I -=1
        else: #I think this is unneeded because it HAS to be one of four things, but I put this in anyways just in case
            pass
    print("Case #"+str(case)+": "+str(counter)) #output the answer
    #ready the variables for the next case
    counter = 0
    I=0
    i=0
            
