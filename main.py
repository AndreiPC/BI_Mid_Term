from objectLb import sourceData as SD
from biEnum import transcriptionEquivalent
import helperFunctions



def main(sourceSequence):          
    dataObj = SD()
    dataObj.setRawData(sourceSequence)
    dataObj.transcriptToRNA()
    print(helperFunctions.getLongestProteinSequence(dataObj.RNAsequence))



if __name__ == "__main__":
    main("source.txt")

