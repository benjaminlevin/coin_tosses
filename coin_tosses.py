import random
def coin_toss(i):
    heads_count = 0
    tails_count = 0
    for z in range(1,i+1):
        x = round(1*random.random(),0)
        if x == 0:
            heads_count = heads_count + 1
            print "Attempt #" + str(z) + ": Throwing a coin... it's heads... got " + str(heads_count) + " head(s) so far and " + str(tails_count) + " tail(s) so far"
        elif x == 1:
            tails_count = tails_count + 1
            print "Attempt #" + str(z) + ": Throwing a coin... it's tails... got " + str(tails_count) + " tail(s) so far and " + str(heads_count) + " head(s) so far"
coin_toss(5000)
