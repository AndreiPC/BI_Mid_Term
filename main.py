from objectLb import sourceData as SD
from biEnum import transcriptionEquivalent
import helperFunctions



def main(sourceSequence):          
    dataObj = SD()
    dataObj.setRawData(sourceSequence)
    dataObj.transcriptToRNA()
    dataObj.setListOfCodons() 

    print(dataObj.Codons.count("AUG"))
    print(dataObj.Codons)


if __name__ == "__main__":
    #file = input("Which file is the source ? ") 
    #main(file + ".txt")
    main("source.txt")
