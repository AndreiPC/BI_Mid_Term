from objectLb import sourceData as SD
from biEnum import transcriptionEquivalent
import helperFunctions



def main(sourceSequence):          
    dataObj = SD()
    dataObj.setRawData(sourceSequence)
    dataObj.transcriptToRNA()
    dataObj.setListOfCodons() 
    #print(dataObj.Codons)
    print(helperFunctions.getProteinSequence(dataObj.RNAsequence))



if __name__ == "__main__":
    main("source.txt")



#To Do ?

#Find aug from the start so you dont have to do it 3 times.
#Itterate over one nucleotide at a time, and get groups of 3 untill an end codon is reached
#After finding an end codon, start looking for another start codon and keep doing step one until the end of the sequence.
#The 2nd and 3rd itterations do the same things but starting at index 1 and 2 rather than 0.
#End result should be the longest protein sequence out of the 3 itterations


#Write it to another result file.
#Maybe ask the user to give the name of the file
#Add extra steps to make sure the file is in the format I want it too.
#Add checks in all methods to guard against bad input
#Initialize the object directly with all the information (name, rawSequence, RNAsequence, ProteinSequence - maybe remove the codons since I only need them for 1 operation)

#Bonus check the longest sequences so far against the length of the rest of the sequence.

#Question:

#What happens if the sequence is not divisible by 3 ?   -> handle the error prior to translating
#Should the source of the text be the user's input ?    -> Nice To Have file/ sequence itelf.
#Should we invest in guarding the code against different inputs ? -> 
#Should we write tests for the code ?
#How many open reading frames can one sequence have ?
#Depending on the anwser how many protein sequences should we save at the end.




#- Spike in difficulty for Basic Python projects (for non-devs)
#follow up by leo and sorin

#- Galaxy course is not updated, deprecated tools are used and cannot follow the workflow

#- Some Galaxy jobs are not executed and cannot follow the workflow

#- Coursera Plus is required for Galaxy course, but the free tutorial on Galaxy's help platform is more detailed and updated than the Coursera presentation  

#Understand the theory and how galaxy does what it does. Real life work will most likely involve other similar tools.
#Leo to follow up with a short introduction into what is used in the field.