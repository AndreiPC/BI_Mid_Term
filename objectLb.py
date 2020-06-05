from biEnum import transcriptionEquivalent

class sourceData():

    def __init__(self):
        self.rawSequence = ""
        self.RNAsequence = ""

    # Sets data from the file given as input
    def setRawData(self, sourceFile):
        rawText = open(sourceFile, "r")
        self.rawSequence = rawText.read().upper()

    #Currently only transforms the T-> U 
    #Can be extended to convert the whole sequence.
    def transcriptToRNA(self):
        for basePair in self.rawSequence:
            if basePair == "T":
                self.RNAsequence += str(transcriptionEquivalent.T)
            else:
                self.RNAsequence += basePair
