from tkinter import *
import random

def letter(l):

    global letters_guessed,wordletter_array,wordlabelarray, badguess,canplay,totalscore,scorestring

    #only allow player to input if alive
    if(canplay==1):

        i=0
        while (i<len(wordletter_array)):
            if(wordletter_array[i]==l):
                wordlabelarray.pop(i)
                wordlabelarray.insert(i,l)
            i=i+1
        
        wordlabel.set(''.join(wordlabelarray))

        #if there are no letters of value l (from buttons near bottom) in the array letters_guessed
        #i.e. letter hasn't been guessed yet
        if(letters_guessed.count(l)==0):
            #and if there are no letters of value l in the array wordlabelarray
            #i.e. letter isn't in the word selected
            if(wordlabelarray.count(l)==0):
                #increase incorrect guess score by 1
                badguess=badguess+1

                #draw hangman lines to canvas
                if(badguess==1):
                    hanging.create_line(50,100,100,100)#bottomline
                if(badguess==2):
                    hanging.create_line(50,20,50,100)#verticalline 
                if(badguess==3):
                    hanging.create_line(50,20,100,20)#top
                    hanging.create_line(50,40,70,20)#cross
                    hanging.create_line(80,20,80,30)#noose
                if(badguess==4):
                    hanging.create_oval(75,30,85,40)#head
                    hanging.create_line(80,40,80,65)#body
                if(badguess==5):
                    hanging.create_line(80,41,70,51)#Larm
                    hanging.create_line(80,41,90,51)#Rarm

                #Tell player they have lost & stop letter guessing
                if(badguess==6):
                    haswon.set('You have Died! You Scored 0, to continue press \'new word\'')
                    canplay=0
                    hanging.create_line(80,65,75,82)#Leftleg
                    hanging.create_line(80,65,85,82)#Rightleg

        #add letter guessed to letters_guessed array so it can't be guessed again                   
        letters_guessed.append(l)

        #if all the letters have been discovered then tell the play that they have won and stop
        #them guessing more after winning. Find the round score(lives left) and add that to the total score of all rounds so far
        if(wordlabelarray.count('_ ')==0):
            roundscore=6-badguess
            win_message='You have survived! You Scored: '+str(roundscore)
            haswon.set(win_message)
            canplay=0
            totalscore=totalscore+roundscore
            scorestring.set('Score: '+str(totalscore))
    
def newword():

    global letters_guessed, wordletter_array,wordlabelarray,badguess,canplay,hanging

   #select a random word from the wordarray list
    selectedword=wordarray[(random.randint(0,len(wordarray)-1))]

    #reset arrays
    letters_guessed=[]
    wordletter_array=[]
    wordlabelarray=[]

    i=0
    while (i<len(selectedword)):
        #make each letter a value in an array(wordletter_array)
        wordletter_array.append(selectedword[i])
        #create dashes for each letter
        wordlabelarray.append('_ ')
        i=i+1
    #show dashes for each letter
    wordlabel.set(''.join(wordlabelarray))

    #reset variables to default values
    haswon.set('')
    badguess=0
    canplay=1
    
    #clear hangman image from screen
    hanging.delete("all")

#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

#Program starts here

Hangman = Tk()

global letters_guessed,wordletter_array, wordlabelarray, badguess, canplay, hanging, totalscore, scorestring

#Variables
wordlabel=StringVar()
haswon=StringVar()
scorestring=StringVar()
canplay=1
badguess=0
letters_guessed=[]
totalscore=0

wordarray=['bee','cow','donkey','person','horse','dog','cat','mouse','monkey','beetle','zebra','butterfly','aardvark','fly','wolf']

#Resolution
Hangman.geometry('600x338+1000+500')

#Title
Hangman.title('Hangman')

#AlphabetButtons
ButtonA=Button(Hangman,text='A',command=lambda: letter('a')).place(x=50,y=200,height=30,width=30)
ButtonB=Button(Hangman,text='B',command=lambda: letter('b')).place(x=90,y=200,height=30,width=30)
ButtonC=Button(Hangman,text='C',command=lambda: letter('c')).place(x=130,y=200,height=30,width=30)
ButtonD=Button(Hangman,text='D',command=lambda: letter('d')).place(x=170,y=200,height=30,width=30)
ButtonE=Button(Hangman,text='E',command=lambda: letter('e')).place(x=210,y=200,height=30,width=30)
ButtonF=Button(Hangman,text='F',command=lambda: letter('f')).place(x=250,y=200,height=30,width=30)
ButtonG=Button(Hangman,text='G',command=lambda: letter('g')).place(x=290,y=200,height=30,width=30)
ButtonH=Button(Hangman,text='H',command=lambda: letter('h')).place(x=330,y=200,height=30,width=30)
ButtonI=Button(Hangman,text='I',command=lambda: letter('i')).place(x=370,y=200,height=30,width=30)
ButtonJ=Button(Hangman,text='J',command=lambda: letter('j')).place(x=410,y=200,height=30,width=30)
ButtonK=Button(Hangman,text='K',command=lambda: letter('k')).place(x=450,y=200,height=30,width=30)
ButtonL=Button(Hangman,text='L',command=lambda: letter('l')).place(x=490,y=200,height=30,width=30)
ButtonM=Button(Hangman,text='M',command=lambda: letter('m')).place(x=530,y=200,height=30,width=30)
ButtonN=Button(Hangman,text='N',command=lambda: letter('n')).place(x=50,y=250,height=30,width=30)
ButtonO=Button(Hangman,text='O',command=lambda: letter('o')).place(x=90,y=250,height=30,width=30)
ButtonP=Button(Hangman,text='P',command=lambda: letter('p')).place(x=130,y=250,height=30,width=30)
ButtonQ=Button(Hangman,text='Q',command=lambda: letter('q')).place(x=170,y=250,height=30,width=30)
ButtonR=Button(Hangman,text='R',command=lambda: letter('r')).place(x=210,y=250,height=30,width=30)
ButtonS=Button(Hangman,text='S',command=lambda: letter('s')).place(x=250,y=250,height=30,width=30)
ButtonT=Button(Hangman,text='T',command=lambda: letter('t')).place(x=290,y=250,height=30,width=30)
ButtonU=Button(Hangman,text='U',command=lambda: letter('u')).place(x=330,y=250,height=30,width=30)
ButtonV=Button(Hangman,text='V',command=lambda: letter('v')).place(x=370,y=250,height=30,width=30)
ButtonW=Button(Hangman,text='W',command=lambda: letter('w')).place(x=410,y=250,height=30,width=30)
ButtonX=Button(Hangman,text='X',command=lambda: letter('x')).place(x=450,y=250,height=30,width=30)
ButtonY=Button(Hangman,text='Y',command=lambda: letter('y')).place(x=490,y=250,height=30,width=30)
ButtonZ=Button(Hangman,text='Z',command=lambda: letter('z')).place(x=530,y=250,height=30,width=30)

#Next Word Button
ButtonNextWord=Button(Hangman,text='Next Word',command=newword).place(x=50,y=150,height=30,width=100)

#Display
LetterLabel=Label(Hangman,textvariable=wordlabel).place(x=0,y=100,height=15,width=600)
Winlabel=Label(Hangman,textvariable=haswon).place(x=0,y=50,height=15,width=600)
Totalscorelabel=Label(Hangman,textvariable=scorestring).place(x=480,y=5,height=15,width=150)

#Create Canvas image
hanging = Canvas(Hangman, width=100,height=100)
hanging.place(x=0,y=0)

#Start Round Function
newword()


Hangman.mainloop()
