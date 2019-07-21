# THIS IS HVD'S OR HARSH VARDHAN DUBEY'S HANGMAN#
import random
import turtle as t
def filler(b,p):                                                               # THIS IS USED TO FILLUP PARTICULAR LETTER FOR A TRIAL#
                m=''
                for j in range(len(p)):
                                if p[j]==b:
                                                m=m+p[j]
                                else:
                                                m=m+'_'
                                
                                
                return m
def compiler(q):                                                            #THIS ACTS AS A COMPILER TO CONVERT STORED DATA TO FILLED OUTPUT#
                s=''
                for i in range(len(q)):
                                s=s+q[i]
                return s

def graphic_control(f):                                                 #THIS IS USED TO CONTROL GRAPHIC FLOW OF THE PROGRAM#
                if f==1:
                                t.home()
                                t.clear()
                                t.hideturtle()
                                t.pendown()
                                t.up()
                                t.right(90)
                                t.forward(200)
                                t.right(90)
                                t.forward(100)
                                t.down()
                                t.forward(200)
                                t.up()
                                t.backward(100)
                                t.left(270)
                                t.pendown()
                                t.forward(400)
                                t.right(90)
                                t.forward(250)
                                t.right(90)
                                t.forward(120)
                elif f==2:
                                t.right(90)
                                t.circle(35)
                                t.up()
                                t.left(90)
                                t.forward(70)
                elif f==3:
                                t.pendown()
                                t.forward(20)
                                t.right(100)
                                t.forward(100)
                                t.right(180)
                                t.up()
                                t.forward(100)
                                
                elif f==4:
                                t.down()
                                t.left(20)
                                t.forward(100)
                                t.left(180)
                                t.forward(100)
                                t.left(80)

                elif f==5:
                                t.forward(90)
                elif f==6:
                                t.right(60)
                                t.forward(100)
                                t.right(180)
                                t.up()
                                t.forward(100)
                elif f==7:
                                t.right(60)
                                t.down()
                                t.forward(100)
                                t.right(180)
                                t.up()
                                t.forward(100)
                                t.up()
                                t.home()
                                  
                
def hangman():
                m=['apple','banana','lumbini','croatia','alexandria','market','refugee','hanger','blossom','cauliflower','baggage','carrot','envelope','python','gorilla','roadrunner','modesty', 'nostradamus','forest','india','botswana','avogadro','ferrari','millionaire','molassus','simulation','procrastinate','assyria','albania','antigua','aphelion','playstation','chromatography','cincinnati','nebraska','carpenter','blacksmith','doraemon','dichlorodiphenyltrichloroethane','livermonium','claustrophobia','pyromaniac','kleptomaniac','computer','grignard','awkward','bagpipes','banjo','bungler','croquet','crypt','dwarves','fervid','fishhook','fjord','gazebo','gypsy','haiku','haphazard','hyphen','ivory','jazzy','jiffy','jinx','jukebox','kayak','kiosk','klutz','memento','mystify','numbskull','ostracize','oxygen','pajama','phlegm','pixel','polka','quad','quip','rhythmic','rogue','sphinx','squawk','swivel','toady','twelfth','unzip','waxy','wildebeest','yacht','zealous','zigzag','zippy','zombie','bereft','rhythm','spine','walrus','tesseract','dab','nigger','bigger','winder','legion','algorithm','window','raft','tinder','render','binder','blinder','panzer']
                print 'ok wanna play hangman'
                b=raw_input("press any key to begin y/n:-")
                t=raw_input("do you like graphics:-")
                if b=='y':
                                sa=random.randint(0,len(m)/3)
                                sb=random.randint((len(m)/3)+1,2*(len(m)/3))
                                sc=random.randint((2*(len(m)/3))+1,len(m)-1)
                                i=random.randint(0,2)
                                if i==0:
                                                s=m[sa]
                                elif i==1:
                                                s=m[sb]
                                elif i==2:
                                                s=m[sc]
                print "the word is"
                print "_ "*len(s)
                print "it is a ",len(s),"letter word"
                c=0
                f=0
                d=''
                g=''
                q=[]
                storage=[]
                while True:                                        #FROM THIS LINE 109 TILL LINE 148 IS THE HEART AND SOUL OF THE PROGRAM
                                a=raw_input("guess a letter:-")
                                if a not in storage:
                                                storage.append(a)
                                elif a in storage:
                                                print "you already have guessed this letter previously"
                                if a in s:
                                                d=filler(a,s)
                                                f=f+1
                                                e=d
                                                w=''
                                                if f==1:
                                                                for i in range(len(d)):
                                                                               q.append(d[i])
                                                                print d
                                                elif f!=1:
                                                                for j in range(len(q)):
                                                                                if q[j]=='_' and s[j]==a:
                                                                                                q[j]=s[j]
                                                                                                w=compiler(q)
                                                                print w
                                                                if w==s:
                                                                                print "congratulations you have won the game"
                                                                                break
                                                                                
                                if a not in s:
                                                c=c+1
                                                print "wrong guess"
                                                if 7-c!=1:
                                                                print 7-c,"tries left"
                                                elif 7-c==1:
                                                                print 7-c,"try left"
                                                if t=='y':
                                                                graphic_control(c)
                                                elif t=='n':
                                                                g=1
                                if c==7:
                                                print "game over ,the man is hanged"
                                                print "the word is",s
                                                break
                                                                               
hangman()                                                                                                 # PRETTY LONG HUH
                                
while True:
                n=raw_input("do you want to continue playing y/n")
                if n=='y':
                                hangman()
                elif n=='n':
                                print "ok bye bye"
                                break
