#Mahyar Gorji 8135109 Year 1 ITI1120



def read_initial_info():
    ''' None->(float, 2D-list)
    Reads the file a4-input.txt and returns a tuple. The first element of that tuple is the limit,
    the second is a 2D list called banks of a format as follows (for this particular file a4-input.txt_:
    [[25.0, 1, 100.5, 4, 320.5], [125.0, 2, 40.0, 3, 85.0], [175.0, 0, 125.0, 3, 75.0], [75.0, 0, 125.0], [181.0, 2, 125.0]]

    Before returning the tuple the function should also print the 2D list banks by calling print(banks) 
    '''

    # YOUR CODE GOES HERE
    #Opening method taken straight from Prof. Vida's lecture.
    infoinput = open("a4-input.txt",encoding="utf-8").read().splitlines()
    limit = infoinput[0]
    alist = []
    floatlist = []
    #Code below transforms the cash values into floats, as is necessary.
    for i in range(1,len(infoinput)):
        alist.append(infoinput[i].split(" "))
    #Code below goes into the 2D list and turns every second entry for
    #the lists within the main list into a float, keeping bank numbers
    #as strings.
    for i in range(len(alist)):
        for j in range(0, len(alist[i]),2):
            alist[i][j] = float(alist[i][j])
        #Code below goes into the 2D list and turns every second entry starting
        #at the second entry into an int, as the IDs for the banks should be as such.
    for i in range(len(alist)):
        for j in range(1, len(alist[i]),2):
            alist[i][j] = int(alist[i][j])
            
    banks = alist
    print(banks)
    return (limit,banks)

    
def current_Assets(banks):
    ''' (2D-list)->list
    given the 2D list banks, returns a (1D) list with the current_assets of all banks
    Precondition: the format of the 2D list banks is as explained in the assignment
    and as produced in read_initial_info()
    '''
    # YOUR CODE GOES HERE TOO
    bankassets=[]
    for i in range(len(banks)):
        assets = 0
        for j in range(0,len(banks[i]),2):
            assets = assets + banks[i][j]
        bankassets.append(assets)
    return(bankassets)

    
    
def find_unsafe():
    '''None->None

    Your solution goes here. This function should start off by calling read_initial_info()
    and then work with the data read_initial_info() returns, i.e. with limit and 2D list banks
    It should call other helper functions
    '''
    pair=read_initial_info()
    limit=pair[0]
    print("Safe limit is:", limit,"million dollars\n\n")
    banks=pair[1]
    bankassets = current_Assets(banks)
    # YOUR CODE GOES HERE TOO

    unsafelist = []
    for i in range(len(bankassets)):
        if bankassets[i] < 201:
            unsafelist.append(i)
    unsafeliststring = " ".join(str(x) for x in unsafelist)
    print("The unsafe banks are:", unsafeliststring)
    #Ran out of time. This is as far as I got.

 

# main
# main can only have this function call and nothing else. Do not modify after this line
find_unsafe()
    
