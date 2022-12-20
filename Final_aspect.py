import nltk
nltk.download('averaged_perceptron_tagger')
import nltk
nltk.download('punkt')
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

import os
def clear():
    os.system( 'cls' )

import spacy
nlp = spacy.load('en_core_web_sm')
pos=0
neg=0
neu=0
all=[]
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

import colorama
from colorama import Fore
from colorama import Style

def my_function_pos(dec, dec1):#positive
    with open("C:\\1---Sedraya--FEEDBACK\\1-Second paper- bothe aspect & general\\Lexicon\\opinion-lexicon-English\\positive-words.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if dec == part:
                    if (len(dec1) != 0 or dec1!=''):
                        #print(Fore.BLUE + 'Aspect:' + Style.RESET_ALL+ dec1, '          ', Fore.RED +  'Description:'+ Style.RESET_ALL+ dec, '          ',  Fore.GREEN +'Sentiment score:'+Style.RESET_ALL+ '1.0')
                        all.append({'aspect': dec1, 'description': dec, 'sentiment_score':'1.0'})
                        return 1
                        break
                    return 1
                    break

def my_function_neg(dec, dec1):#negative
    with open("C:\\1---Sedraya--FEEDBACK\\1-Second paper- bothe aspect & general\\Lexicon\\opinion-lexicon-English\\negative-words.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if dec== part:
                    if (len(dec1) != 0 or dec1 != ''):
                        #print(Fore.BLUE + 'Aspect:' + Style.RESET_ALL+ dec1, '          ', Fore.RED +  'Description:'+ Style.RESET_ALL+ dec, '          ',  Fore.GREEN +'Sentiment score:'+Style.RESET_ALL+ '- 1.0')
                        all.append({'aspect': dec1, 'description': dec, 'sentiment_score': '- 1.0'})
                        return -1
                        break
                    return -1
                    break
import cloud
cloud
print("\n")
print(Fore.RED + '                                                                            PLEASE WAITE                                '+ Style.RESET_ALL)
print("\n")
import cat
cat
print("\n")
input("Press any key to continue")
