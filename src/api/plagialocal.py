# importation des differents modules 
from difflib import SequenceMatcher 
from pdfminer.high_level import extract_text
import glob

class Plagialocal:
    
    def plagiafichier(self,fichier,fichier2):
        with open(fichier) as first_file, open(fichier2) as second_file: 
            
            # Reading Both Text Files 
            file1 = first_file.read() 
            file2 = second_file.read() 
            
            # Comparing Both Text Files 
            ab = SequenceMatcher(None, file1, 
                                file2).ratio() 
            
            # converting decimal output in integer 
            result = int(ab*100) 
            pourcentage = int(result)
            # Display the final result
            return pourcentage
        
    
    def plagiapdf(self,fichier,fichier2): 
            #importation du fichier pdf et extraction du texte 
        string1 = extract_text(fichier)
        string2 = extract_text(fichier2)
                
        # Utilisation SequenceMatcher()
        match = SequenceMatcher(None,string1, string2) 
        # convertion du ratio 
        # multiplication par 100 pour avoir le pourcentage
        result = match.ratio() * 100
        pourcentage = int(result)
        # Display the final result
        return pourcentage 
       
        
        
        def _si_pdf(self,data):
            veri = False
            ref_file=data
            extension=ref_file.split('.')[-1]
            if extension == 'pdf':
                veri = True
            
            return veri