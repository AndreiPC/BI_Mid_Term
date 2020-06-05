from proteinDictionary import Proteins

def getProteinSequence(sequence):
    startCDN = ['AUG']
    stopCDN = ['UAA', 'UAG', 'UGA']
    proteinList = []
    temp = []
    counter = 0
    increment = 1
    startEncountered = False

    

#Stop trasncribing needs to be reset to false after encountering one stop

    for nucleotide in sequence:
        try:
            codon = sequence[counter] + sequence[counter + 1] + sequence[counter + 2]   

            if codon  in startCDN and startEncountered == False:
                startEncountered = True
                increment = 3

            elif codon in stopCDN and startEncountered == True:
                startEncountered = False
                proteinList.append(temp)
                temp = []

            if startEncountered == True:
                temp.append(Proteins[codon])
    
            counter += increment
        except Exception:
            pass

    
    #daca cel mai mare array e mai mare decat restul secventei iesi


    return proteinList




def longestProteinSequence(listOfSequences):
    if(not isinstance(listOfSequences, list)): 
        return(0)
    return(max([len(listOfSequences),] + [len(subl) for subl in listOfSequences if isinstance(subl, list)] +
        [longestProteinSequence(subl) for subl in listOfSequences]))