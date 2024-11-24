import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
from twilio.rest import Client
import os
import wikipedia
import pyautogui
import keyboard
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import subprocess
import ctypes
import datetime
import pyjokes
from PyDictionary import  PyDictionary as Diction
from googletrans import Translator
import MyAlarm
import time 
from tkinter import*
from PIL import ImageTk,Image
from playsound import playsound
from gtts import gTTS
import PyPDF2
import random

Assistant =pyttsx3.init('sapi5')
voices= Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)

Assistant.setProperty('rate',170)

#Speak Mode
def speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f":{audio} ")
    print(" ")
    Assistant.runAndWait()

def clr():
    label4.config(text=" ")
    label3.config(text=" ")
    window.update()
    executeTask()

def voicesaid(tx):
    label4.config(text=tx)
    window.update()
    
def takeCommand():
    label3.config(text="listening...")
    window.update()
    command =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold=1
        #command.adjust_for_ambient_noise(source)
        audio=command.listen(source)

        try:
            print("Recognizing....")
            label3.config(text="recognizing...")
            window.update()
            query= command.recognize_google(audio, language='en-in')
            print(f"User said\n: {query}" )
            label3.config(text='user said :-\n'+ query)
            window.update

        except Exception as Error:
            print("Unable to Recognizing")
            return "none"
        return query



def executeTask():
    speak("Hello Sir, How may I help you")

    def WhatsApp():
        speak("Tell me the name of the person")
        name=takeCommand().lower()

        if 'aakruti' in name:
            speak("Tell me the message!")
            msg=takeCommand()
            speak("tell me the time")
            speak("Time in hour")
            hour=int (takeCommand())
            speak("Time in minutes!")
            min=int(takeCommand())
            pywhatkit.sendwhatmsg("+919993666602",msg,hour,min,5)
            speak("Ok sir, Sending whatsapp Message!")

        elif'aadarsh' in name:
            speak("Tell me the message!")
            msg=takeCommand()
            speak("tell me the time")
            speak("Time in hour")
            hour=int (takeCommand())
            speak("Time in minutes!")
            min=int(takeCommand())
            pywhatkit.sendwhatmsg("+918319458082",msg,hour,min,5)
            speak("Ok sir, Sending whatsapp Message!")

        elif 'nikita' in name:
            speak("Tell me the message!")
            msg=takeCommand()
            speak("tell me the time")
            speak("Time in hour")
            hour=int (takeCommand())
            speak("Time in minutes!")
            min=int(takeCommand())
            pywhatkit.sendwhatmsg("+919522758625",msg,hour,min,5)
            speak("Ok sir, Sending whatsapp Message!")

        elif 'rahul sir' in name:
            speak("Tell me the message!")
            msg=takeCommand()
            speak("tell me the time")
            speak("Time in hour")
            hour=int (takeCommand())
            speak("Time in minutes!")
            min=int(takeCommand())
            pywhatkit.sendwhatmsg("+919584748443",msg,hour,min,5)
            speak("Ok sir, Sending whatsapp Message!")
        
        else:
            speak("Tell me the phone number!")
            phone=int(takeCommand())
            ph = '+91' + phone
            speak("Tell me the message!")
            msg=takeCommand()
            speak("tell me the time")
            speak("Time in hour")
            hour=int (takeCommand())
            speak("Time in minutes!")
            min=int(takeCommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,5)
            speak("Ok sir, Sending whatsapp Message!") 

    def Music():
        speak("Tell me the name of music")
        voicesaid("Tell me the name of music")
        MusicName= takeCommand().lower()

        if 'leja re' in MusicName:
            os.startfile('E:\\music\\lejaRe.mp3')

        elif 'makhna' in MusicName:
            os.startfile('E:\\music\\makhna.mp3')

        elif 'jab Koi Baat' in MusicName:
            os.startfile('E:\\music\\jabKoiBaat.mp3')
        
        else:
            pywhatkit.playonyt(MusicName)
        
        speak("Your song has been started!, Enjoy sir!")
        voicesaid("Your song has been started!, Enjoy sir!")


    def openApps():
        speak("Ok Wait a second Executing the Task...")
        voicesaid("Ok Wait a second Executing the Task...")

        if 'code' in query:
            os.startfile("C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'telegram' in query:
            os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")

        elif 'notepad' in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk")
        
        elif 'word pad' in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\wordPad.lnk")
        
        elif 'zoom' in query:
            os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

        elif 'paint' in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")

        elif 'google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'chorme' in query:
            webbrowser.open("https://www.google.com/")

        
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        
        elif 'twitter' in query:
            webbrowser.open("https://www.twitter.com/")
        
        elif 'map' in query:
            webbrowser.open("https://www.google.com/maps?authuser=0")
        
        elif 'drive' in query:
            webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
        
        elif 'leet code' in query:
            webbrowser.open("https://leetcode.com/")

        elif 'geeks for geeks' in query:
            webbrowser.open("https://practice.geeksforgeeks.org/")
        
        elif 'meet' in query:
            webbrowser.open("https://meet.google.com/")
        
        elif 'classroom' in query:
            webbrowser.open("https://classroom.google.com/")
        
        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        
        else:
            speak("Can you say Again?")

    
    def closeApps():
        speak("Ok Wait a second Executing the Task...")
        voicesaid("Ok Wait a second Executing the Task...")

        if 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im telegram.exe")

        elif 'notepad' in query:
            os.system("TASKKILL /F /im Notepad.lnk")

        elif 'word pad' in query:
            os.system("TASKKILL /F /im wordPad.lnk")
        
        elif 'zoom' in query:
            os.system("TASKKILL /F /im Zoom.exe")

        elif 'paint' in query:
            os.system("TASKKILL /F /im Paint.lnk")

        elif 'google' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")
          
        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'twitter' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'map' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'drive' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'leet code' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'geeks for geeks' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'meet' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'classroom' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'whatsapp' in query:
            os.system("TASKKILL /F /im chrome.exe")
        else:
            speak("Can you say Again?")
            voicesaid("Can you say again?")

        #speak("Done sir")

    def Dict(): 
        speak("Activated Dictionary!")
        voicesaid("Activated Dictionary!")
        speak("tell me your problem")
        voicesaid("tell me your problem")
        prob =takeCommand().lower()

        if 'meaning' in prob:
            prob=prob.replace("what is the","")            
            #prob=prob.replace("of","")
            prob=prob.replace("meaning of","")
            result= Diction.meaning(prob)
            speak(f"The meaning for {prob} is {result}")
        
        elif 'synonym' in prob:
            prob=prob.replace("what is the","")
            #prob=prob.replace("of","")
            prob=prob.replace("synonym of","")
            result= Diction.synonym(prob)
            speak(f"The synonym for {prob} is {result}")
        
        elif 'antonym' in prob:
            prob=prob.replace("what is the","")
            #prob=prob.replace("of","")
            prob=prob.replace("antonym of","")
            result= Diction.antonym(prob)
            speak(f"The antonym for {prob} is {result}")
        
        speak("Exit Dictionary")
    
    def takeHindi():
        command =sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            command.pause_threshold=1
            audio=command.listen(source)
            try:
                print("Recognizing....")
                query= command.recognize_google(audio, language='hi')
                print(f"User said: {query}")

            except Exception as Error:
                print("Unable to Recognizing")
                return "none"
        return query

    def trans():
        speak("Speak...")
        line=takeHindi()
        tr =Translator(service_urls=['translate.googleapis.com'])
        result= tr.translate(line,dest='en')
        text=result.text
        speak(f"The translation of this line is :"+ text)
        voicesaid(f"Translation is: "+text)

    def Reader():
        speak("Tell me the name of the book")
        name=takeCommand()
        if 'wise' in name:
            os.startfile('C:\\Users\\HP\\Downloads\\voice assitant\\Wise and Otherwise.pdf')
            book=open('C:\\Users\\HP\\Downloads\\voice assitant\\Wise and Otherwise.pdf','rb')
            pdfreader=PyPDF2.PdfReader(book)
            pages=len(pdfreader.pages)
            speak("Number of pages in this book is "+ str(pages))
            speak("from which page start to read")
            numPage=int(takeCommand())
            page=pdfreader.pages[numPage]
            text=page.extract_text()
            speak("In which language , i have to read ?")
            lang=takeCommand()

            if 'hindi' in lang:
                trans1=Translator()
                textHin=trans1.translate(text,'hi')
                textm=textHin.text
                speech=gTTS(text=textm)
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')
                except:
                    playsound('book.mp3')
            else:
                speak(text)

        elif 'rich' in name:
            os.startfile('C:\\Users\\HP\\Downloads\\voice assitant\Rich Dad Poor Dad.pdf')
            book=open('C:\\Users\\HP\\Downloads\\voice assitant\Rich Dad Poor Dad.pdf','rb')
            pdfreader=PyPDF2.PdfReader(book)
            pages=len(pdfreader.pages)
            speak("Number of pages in this book is"+ str(pages))
            speak("from which page start to read")
            numPage=int(takeCommand())
            page=pdfreader.pages[numPage]
            text=page.extract_text()
            speak("In which language , i have to read ?")
            lang=takeCommand()

            if 'hindi' in lang:
                trans1=Translator()
                textHin=trans1.translate(text,'hi')
                textm=textHin.text
                speech=gTTS(text=textm)
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')
                except:
                    playsound('book.mp3')
            else:
                speak(text)
        else:
            speak("you don't have any book of this name")

    def game():
            speak("It's a 3 round game")
            i=1
            me=0
            com=0

            while (i<3):
                speak("your turn")
                user_action = takeCommand().lower()
                possible_actions = ["rock", "paper", "scissors"]
                if user_action!= "rock" and user_action!= "paper" and user_action!= "scissor":
                    speak("choose again")
                    continue
                computer_action = random.choice(possible_actions)
                speak(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

                if user_action == computer_action:
                    speak(f"Both players selected {user_action}. It's a tie!")
                elif user_action == "rock":
                    if computer_action == "scissors":
                        me +=1
                        speak("Rock smashes scissors! You win!")
                    else:
                        com+=1
                        speak("Paper covers rock! You lose.")
                elif user_action == "paper":
                    if computer_action == "rock":
                        me+=1
                        speak("Paper covers rock! You win!")
                    else:
                        com+=1
                        speak("Scissors cuts paper! You lose.")
                elif user_action == "scissors":
                    if computer_action == "paper":
                        me+=1
                        speak("Scissors cuts paper! You win!")
                    else:
                        com+=1
                        speak("Rock smashes scissors! You lose.")
                i+=1

            speak("Final score")   
            if me==com :
                    speak("It's a Tie")
            elif me>com:
                    speak("you win")
            elif com > me:
                    speak("computer win")


            speak("Do you want to play again?")
            play_again = takeCommand().lower()
            if play_again.lower() != "yes":
                    speak("Ok sir, Exiting the game mode")
            else:
                    game()

    if 1:
    
        
        query=takeCommand().lower()
        
        if 'hello' in query:
             speak("Hello Sir, I am your assistant how may I help you")
             voicesaid("Hello Sir, I am your assistant how may I help you")

        elif 'how are you' in query:
            speak("I'm fine sir, How are you?")
            voicesaid("I'm fine sir, How are you?")

        elif 'fine' in query:
            speak("It's good to know sir, how may I help you")
        elif 'bye' in query:
            speak("ok sir,you can call me anytime, just say Wakeup jeannie ")
        
        elif 'youtube search' in query:
            query=query.replace("youtube search","")
            speak("Searching "+query+" for you")
            web="https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
            speak("Done sir") 

        elif 'google search' in query:
            import wikipedia as googleScrap
            query=query.replace("google search","")
            query=query.replace("google","")
            speak("This is what I found")
            pywhatkit.search(query)
            
            try:
                result=googleScrap.summary(query,3)
                speak(result)
                
            except:
                speak("No speakable data available")
            

            

            pywhatkit.search(query)
            speak("Done sir")
        
        elif 'website' in query:
            speak("ok sir")
            query=query.replace("website","")
            query=query.replace(" ","")
            web1 =query.replace("open","")
            web2 = "https://www."+web1+".com/"
            webbrowser.open(web2)
            speak("launched")
        
        elif 'launch' in query:
            speak("Tell me the name of website ")
            voicesaid("Tell me the name of website ")
            name=takeCommand()
            label3.config(text=name)
            window.update()
            name=name.replace(" ","")
            web2 = "https://www."+name+".com/"
            webbrowser.open(web2)
            speak("launched")
        
        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            query=query.replace("search","")
            wiki=wikipedia.summary(query,2)
            speak("According to Wikipedia:"+wiki)
        
        elif 'whatsapp' in query:
           WhatsApp()
        
        elif 'screenshot' in query:
            speak("Ok sir, What should I name thate file?")
            path =takeCommand()
            pathName = path +".png"
            path1= "E:\\"+pathName
            kk= pyautogui.screenshot()
            kk.save(path1)
            os.startfile("E:\\")
            speak("Here is your screenshot")

        elif 'call' in query:
            speak("Calling on your number")
            account_sid = 'AC8cd7dc89de3301d721472057af432503'
            auth_token = 'dc915a2ab6f6216e3123d139dfff68bd'
            client = Client(account_sid, auth_token)
            
            call = client.calls.create(
             to='+919993666602',  # The phone number to call
            from_='+16205429296',  # Your Twilio phone number
            url='http://demo.twilio.com/docs/voice.xml'  # The URL of the TwiML document that controls the call
            )

            # Print the call SID
            print(call.sid)
            speak("Done sir")

        elif 'send message' in query:
            speak("Sir what should I say")
            msz=takeCommand()
            account_sid = 'AC8cd7dc89de3301d721472057af432503'
            auth_token = 'dc915a2ab6f6216e3123d139dfff68bd'
            client = Client(account_sid, auth_token)
            
            message = client.messages.create(
                     
                     to='+919993666602',
                     from_='+16205429296',
                     body=msz
                     
                     )

            print(message.sid)
            speak("Done sir")
        
        elif 'game' in query:
            speak("Lets play stone paper scissor")
            game()
        #youtube automation
        elif 'pause youtube' in query:
            pyautogui.press('spacebar')
            time.sleep(1)
        elif 'restart youtube' in query:
            keyboard.press('0')
        elif 'mute youtube' in query:
            keyboard.press('m')
        elif 'skip youtube' in query:
            keyboard.press('l')
        elif 'back youtube' in query:
            keyboard.press('j')
        elif 'full screen youtube' in query:
            keyboard.press('f')
        elif 'film mode youtube' in query:
            keyboard.press('t')
        
        #chrome automation
        elif 'close tab' in query:
            keyboard.press_and_release('cntrl + w')
        elif 'open new tab' in query:
            keyboard.press_and_release('cntrl + t')
        elif 'open new window' in query:
            keyboard.press_and_release('cntrl + n')
        elif 'history' in query:
            keyboard.press_and_release('cntrl + h')
        elif 'close window' in query:
            keyboard.press_and_release('ctrl + shift + w')
        
        elif 'joke' in query:
            get=pyjokes.get_joke()
            speak(get)
        
        elif 'repeat my words' in query:
            speak("Speak sir")
            jj=takeCommand()
            speak(f"you said: {jj}")

        elif 'my location' in query:
            speak("Ok sir")
            webbrowser.open('https://www.google.com/maps/@23.1928597,75.7625081,16z?authuser=0')
        
        elif "dictionary" in query:
            Dict()

        elif 'translator' in query:
            trans()
        
        elif "temperature" in query:
            speak("of which location")
            
            temp=takeCommand()
            newtemp="temperature of " + temp
            url="https://www.google.com/search?q=" + newtemp
            r = requests.get(url) 
            data=BeautifulSoup(r.text,"html.parser")
            tem=data.find("div",class_="BNeawe").text   
            speak(f"the temperature outside is {tem} celcius")
            voicesaid(f"the temperature outside is {tem} celcius")

        elif "how to" in query:
            speak("getting data...please wait!")
            tex=query
            max_result=1
            how_to_funv =search_wikihow(tex,max_result)
            assert len(how_to_funv)==1
            how_to_funv[0].print()  
            speak(how_to_funv[0].summary)
        
        elif 'note' in query:
                speak("what you want to write")
                voicesaid("what you want to write")
                text=takeCommand()
                date = datetime.datetime.now()
                file_name = str(date).replace(":", "-") + "-note.txt"
                with open(file_name, "w") as f:
                    f.write(text)

        elif 'alarm' in query:
                speak("please tell me the time to set the alarm, for exmple set alarm to 5:30 am")
                tt=takeCommand()   # set alarm to 4:20 p.m.
                tt=tt.replace("set alarm to ","")
                tt=tt.replace(".","")
                tt=tt.upper()
                speak("Setting the alarm")
                voicesaid("alarm set to "+tt)
                MyAlarm.alarm(tt)
        
        elif 'shutdown system' in query or 'shut down system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system('shutdown /s /t 1')

        elif "will you be my gf" in query or "will you be my bf" in query:
                speak("I'm not sure about, may be you should give me some time")
        
        elif  'i love you' in query:
                speak("love you too dear") 
        
        elif 'who created you' in query:
             speak("I am created by, Aakruti , Adarsh and Nikita , as major project for their bachelor of Engineering in Computer Science")

        elif 'who are you' in query:
             speak("hello , i am jeannie .I can perform the task coammanded by you and can make your life easy")
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()  
        
        elif 'volume up' in query:
                pyautogui.press("volumeup")

        elif 'volume down' in query:
                pyautogui.press("volumedown")
        
        elif 'open' in query:
            openApps()
        
        elif 'close' in query:
            closeApps()
        
        elif "remember that" in query:
            remembermsg=query.replace("remember that","")
            speak("you tell me to remember that"+remembermsg)
            rember=open('data.txt','w')
            rember.write(remembermsg)
            rember.close()

        elif "what do you remember" in query:
            rember=open('data.txt','r')
            text=""
            text += rember.read()
            speak("you told me that " + text)
            voicesaid("That " + text)
            rember.close()
        
        elif 'book' in query:
            Reader()


        else:
            speak("Unable to recognize")




    
if __name__=="__main__":
    window=Tk()
    window.title('VOICE-ASSITANT')
    window.geometry("800x600")

    label1=Label(window)
    label1.config(bg='black',fg='white',font=('yu gothic ui',10,'bold'))
    label1.pack(fill='both',expand='yes')
    gifImage11="Bb.gif"
    OpenImage1=Image.open(gifImage11)
    frames1=OpenImage1.n_frames
    imageObject1=[PhotoImage(file=gifImage11,format=f"gif -index {i}") for i in range(frames1)]
    count=0
    showAnimation=None
    def animationnn(count):
        global showAnimation
        newImage1=imageObject1[count]
        gif_label2.configure(image=newImage1)
        count +=1
        if count == frames1:
            count=0
        showAnimation=window.after(50,lambda:animationnn(count))
    gif_label2=Label(window,image="",bg="black")
    gif_label2.place(x=50,y=-100,height=300,width=700)
    animationnn(count)
    label2=Label(window)
    label2.config(text='Design and Developed by : Aakruti joshi ,Adarsh satnami and Nikita vyas',bg='black',fg='white',font=('yu gothic ui',10,'bold'))
    label2.place(x=200,y=550)
    gifImage="Aa.gif"
    OpenImage=Image.open(gifImage)
    frames=OpenImage.n_frames
    imageObject=[PhotoImage(file=gifImage,format=f"gif -index {i}") for i in range(frames)]
    count=0
    showAnimation=None
    def animation(count):
        global showAnimation
        newImage=imageObject[count]
        gif_label.configure(image=newImage)
        count +=1
        if count == frames:
            count=0
        showAnimation=window.after(50,lambda:animation(count))
    gif_label=Label(window,image="",bg="black")
    gif_label.place(x=20,y=200,height=300,width=200)
    animation(count)
    label3=Label(window,borderwidth=0,relief="raised")
    label3.config(bg='black',fg='White',font=('Perpetua Titling MT',13,'bold'))
    label3.place(x=240,y=90,width='350',height='80')
    label4=Label(window,borderwidth=0,relief="raised")
    label4.config(bg='black',fg='White',font=('Perpetua Titling MT',10,'bold'))
    label4.place(x=240,y=200,width='350',height='50')
    bg2 = ImageTk.PhotoImage(Image.open("zz.jpeg"))
    bgg2=Button(image=bg2,bg='black',border=0)
    bgg2.config(command=clr)
    bgg2.place(x=330,y=250,width='180',height='250')

    

    def animationn(count):
        global showAnimation
        newImage=imageObject[count]
        gif_label1.configure(image=newImage)
        count +=1
        if count == frames:
            count=0
        showAnimation=window.after(50,lambda:animationn(count))
    gif_label1=Label(window,image="",bg="black")
    gif_label1.place(x=580,y=200,height=300,width=200)
    animationn(count)

    window.mainloop()