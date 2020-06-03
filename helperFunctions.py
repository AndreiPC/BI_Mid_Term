from proteinDictionary import Proteins

#To find the ORF:
    #Find start codon
    #Translate to proteins until a stop codon is encountered

#Maybe keep in mind the index ? idk yet
#Not sure if multiple start codons can be encountered.


startCDN = ['AUG']
stopCDN = ['UAA', 'UAG', 'UGA']
proteinList = []

shortSequence = ['AUG','AAA', 'CUG', 'CUC', 'UUC', 'UUC', 'CUG', 'CUG','UGA','AUG']

startEncountered = False
stopTranscribing = False

for codon in shortSequence:
    if codon in startCDN:
        startEncountered = True
    elif codon in stopCDN and startEncountered == True:
        stopTranscribing = True

    if startEncountered == True and stopTranscribing != True:
        proteinList.append(Proteins[codon])
    

print(proteinList)


#BEFORE FULLY IMPLEMENTING THIS ! CHECK IF MULTIPLE START CODONS CAN EXIST IN A SEQUENCE.