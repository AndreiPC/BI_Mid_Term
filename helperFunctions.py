from proteinDictionary import Proteins

def getLongestProteinSequence(sequence):
    startCDN = ['AUG']
    stopCDN = ['UAA', 'UAG', 'UGA']
    proteinList = []
    temp = []
    counter = 0
    increment = 1
    startEncountered = False

    for nucleotide in sequence:
        try:
            codon = sequence[counter] + sequence[counter + 1] + sequence[counter + 2]   

            if codon  in startCDN and startEncountered == False:
                startEncountered = True
                increment = 3

            elif codon in stopCDN and startEncountered == True:
                increment = 1
                startEncountered = False
                proteinList.append(temp)
                temp = []

            if startEncountered == True:
                temp.append(Proteins[codon])
    
            counter += increment
        except Exception:
            pass

    return max(proteinList,key=len)
