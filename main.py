from objectLb import sourceData as SD
from biEnum import transcriptionEquivalent
import helperFunctions



def main(sourceSequence):          
    dataObj = SD()
    dataObj.setRawData(sourceSequence)
    dataObj.transcriptToRNA()
    dataObj.setListOfCodons() 
    print(helperFunctions.getProteinSequence(dataObj.Codons))



if __name__ == "__main__":
    main("source.txt")



#To Do ?

#Maybe ask the user to give the name of the file
#Add extra steps to make sure the file is in the format I want it too.
#Add checks in all methods to guard against bad input
#Initialize the object directly with all the information (name, rawSequence, RNAsequence, ProteinSequence - maybe remove the codons since I only need them for 1 operation)