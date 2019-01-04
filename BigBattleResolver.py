import random as r

attackers = 10
defenders = 10

def rollDice():
        attackResults = []
        #Attackers roll first
        for i in range(0, min(3, attackers)):
            attackResults.append(r.randint(1, 6))
            

        defendResults = []
        for i in range(0, min(2, defenders)):
            defendResults.append(r.randint(1, 6))
            
        print("Attacker dicerols are ", attaclResults)
        print("Defenders dicerolls are ", defendResults)

    
        return attackResults, defendResults
        

def computeResult():
        result = rollDice()
        
        #Attackerdie, sort the results, simple n^2 sorting will do, as only 3 elements need to be sorted    
        aSize = len(result[0])
        numbersSmaller = [0]*aSize
        aFirst = 0
        aSecond = 0

        for i in range(0, aSize):
            cNumb = result[0][i]
            for j in range(0, aSize):
                if i==j:
                    continue
                nNumb = result[0][j]
                if cNumb>=nNumb:
                    numbersSmaller[i] += 1
       
       for i in range(0, aSize):
           cVal = numbersSmaller[i] 
            if cVal == aSize-1:
                afirst = result[0][i]
                continue
            if cVal == aSize-2:
                aSecond = result[0][i]
          
        #Handle the special case of 1 attacker
        if aSize == 1:
            aFirst = result[0][0]
        
        #Handle special case if dices show same result
        if aSecond == 0 and aSize>1:
            aSecond = aFirst


        #Defenderdie, max 2 defenders, classic risk style
        dFirst = 0
        dSecond = 0
        dSize = len(result[1])

        if dSize == 2:
            if result[1][0]<result[1][1]:
                dFirst = result[1][1]
                dSecond = result[1][0]
            else:
                dFirst = result[1][0]
                dSecond = result[1][1]
        else:
            dFirst= result[1][0]


       #Ready to compare and kill soldiers
       defendersSort = [dFirst, dSecond]
       attackersSort = [dFirst, dSecond]
       defenderLosses = 0
       attackerLosses = 0
       for i in range(0, min(aSize, dSize)):
           if defendersSort[i]>=attackersSort[i]:
               attackerLosses += 1
           else:
               defenderLosses += 1

       print("Attacker lost ", attackerLosses)
       print("Defender lost ", defenderLosses)
       defenders -= defenderLosses
       attackers -= attackerLosses
    
def runSim():
    while attackers != 0 and defenders != 0:
        computeResult()



