import sys, os, string

def reducer (filename_resultmappersorted, filename_resultreducer):

    # Ouverture en lecture du fichier
    fileIn = open(filename_resultmappersorted, 'r')
    # Ouverture en Ã©criture du fichier contenant le resultat du reducer
    fileOut = open(filename_resultreducer, 'w')
    current_word = None
    current_count = 0
    word = None

    for line in fileIn:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        word, count = line.split('\t', 1)
        
        # convert count (currently a string) to int
        try:
            count = float(count)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue
        
        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_word == word:
            current_count += count
        else:
            if current_word != None:
                fileOut.write(current_word+'\t'+str(current_count)+'\n')
            current_count = count
            current_word = word

    # do not forget to output the last word if needed!
    if current_word == word :
        fileOut.write(current_word + '\t'+str(current_count)+'\n')


    fileOut.close() # fermeture du fichier resultat
    fileIn.close() # fermeture du fichier original


def mapper(filename_original, filename_resultmapper):
    # Open the input and output files using context managers
    with open(filename_original, 'r') as fileIn, open(filename_resultmapper, 'w') as fileOut:
        
        for line in fileIn:
            # Remove leading and trailing whitespace
            line = line.strip()
            # Split the line into words/items
            items = line.split('\t')
            
            # Check if the line contains at least 7 items (since indexing starts at 0)
            if items[2]=="San Francisco":
                # Get the 6th and 7th items (indexing starts from 0, so use 5 and 6)
                item6 = items[-1]
                item7 = items[-2]
                
                # Write the 6th and 7th items to the output file
                fileOut.write(f"{item6}\t{item7}\n")

    
    fileOut.close() # fermeture du fichier resultat
    fileIn.close() # fermeture du fichier original

if __name__ == '__main__':
    
    filename_original           = 'purchases10000.txt'
    filename_resultmapper       = 'resultmapper_ventes.txt'
    filename_resultmappersorted = 'resultmappersorted_ventes.txt'
    filename_resultreducer      = 'resultreducer_ventes.txt'

    # Appel au mapper
    mapper(filename_original, filename_resultmapper)
    
    # Tri du rÃ©sultat prÃ©cÃ©dent
    with open(filename_resultmapper,"r") as f:
        with open(filename_resultmappersorted, "w") as g:
            lines = f.readlines()
            g.writelines(sorted(lines))
    
    # Appel au reducer
    reducer(filename_resultmappersorted, filename_resultreducer)