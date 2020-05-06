# Title: Monty Hall Shenanigans
# Author: Doug Hart
# Date Created: 5/5/2020
# Last Updated: 5/5/2020


#prior probability of any door having a goat, or a prize
goatdoor = (.25)*(0/3) + (.25)*(1/3) + (.25)*(2/3) + (.25)*(3/3) # = 0.5

#posterior probability of first choice of door having prize
(1/3)*(0/3) + (3/8)*(1/3) + (1/4)*(3/3) # = 0.375

#posterior probability of switching doors ang receiving prize a prize
(.25)*(0/3) + (3/8)*(2/3) + (1/4)*(3/3) + (.25)*(3/3)*0 = 0.5

'''alternatively, solving the problem, and checking our work via simulation'''

def sneakymonty(n):
    '''
    this simulates the scenario in its entirety from the begining, 
    assuming nothing about whether or not Monty can open a door.

    n: the number of times to run simulation
    '''
    icount = 0
    ocount = 0
    for i in range(n):
        selection = np.array([1,2,3])
        n_prizes = np.random.randint(0,4)
        if n_prizes == 0:
            continue
        if n_prizes == 1:
            prize = np.random.choice(selection)
            mypick = np.random.choice(selection)
            if prize == mypick:
                icount += 1
            else:
                ocount += 1
        if n_prizes == 2:
            ocount += 1
            goat = np.random.choice(selection)
            mypick = np.random.choice(selection)
            if mypick != goat:
                icount +=1
        if n_prizes == 3:
            icount +=1
            ocount +=1
    return icount/n, ocount/n


def sneakymonty_V2(n):
    '''
    V2 assumes that Monty can, and has opened a door as outlined in the problem.

    n: the number of times to run simulation
    '''
    icount = 0
    ocount = 0
    m = n
    for i in range(n):
        selection = np.array([1,2,3])
        n_prizes = np.random.randint(0,4)
        if n_prizes == 0:
            continue
        if n_prizes == 1:
            prize = np.random.choice(selection)
            mypick = np.random.choice(selection)
            if prize == mypick:
                icount += 1
            else:
                ocount += 1
        if n_prizes == 2:
            goat = np.random.choice(selection)
            mypick = np.random.choice(selection)
            if mypick == goat:
                m -= 1
            else:
                ocount += 1
                icount += 1
        if n_prizes == 3:
            m -= 1
    return icount/m, ocount/m

sneakymonty2(1000000)