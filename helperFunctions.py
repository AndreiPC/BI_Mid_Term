from proteinDictionary import Proteins

def getProteinSequence(sequence):
    startCDN = ['AUG']
    stopCDN = ['UAA', 'UAG', 'UGA']
    proteinList = []

    startEncountered = False
    stopTranscribing = False

    for codon in sequence:
        if codon in startCDN:
            startEncountered = True
        elif codon in stopCDN and startEncountered == True:
            stopTranscribing = True

        if startEncountered == True and stopTranscribing != True:
            proteinList.append(Proteins[codon])
        
    return proteinList