from biEnum import transcriptionEquivalent

class sourceData():

    def __init__(self):
        self.rawSequence = ""
        self.RNAsequence = ""
        self.proteinSequence = []
        self.Codons = []

    # Sets data from the file given as input
    def setRawData(self, sourceFile):
        rawText = open(sourceFile, "r")
        self.rawSequence = rawText.read()

    #Currently only transforms the T-> U 
    #Can be extended to convert the whole sequence.
    def transcriptToRNA(self):
        for basePair in self.rawSequence:
            if basePair == "T":
                self.RNAsequence += str(transcriptionEquivalent.T)
            else:
                self.RNAsequence += basePair

    def setListOfCodons(self):
        counter = 0

        #I divide by 3 to iterate over the maximum number of codons of length 3 that can exist inside a string.
        #Try catch is here because the given raw sequence might end up not being divisible by 3 -> need to ask what should I do with the reminder nucleotides.
        
        for index in range(int(len(self.RNAsequence) / 3)):
            try:
                self.Codons.append(self.RNAsequence[counter]+self.RNAsequence[counter+1]+self.RNAsequence[counter+2])
            except Exception:
                print("Implementation for sequences that cant be devided into an exact number of codons is not in place yet.")
        
            counter += 3