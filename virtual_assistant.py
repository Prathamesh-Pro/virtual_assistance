#Description : This is a virtual assistance program that get current time ,date,responds back with a random greeting , and returns information on a person.

#pip install pyaudio
#pip install speech_Recognition
#pip install gTTS
#pip install wikipedia
#import the libraries

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

#Ignore any warning messages
warnings.filterwarnings('Ignore')

#Record audio and return it as a string
def recordAudio ():

    #Record the audio
    r = sr.Recognizer()     #creating a recognizer object
    #open the microphone and start recording
    with sr.Microphone() as source:
        print('Hello I am cloak How can I help you!')
        audio = r.listen(source)
    #Use google speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('Ok sir: '+data)
    except sr.UnknownValueError: #chech for unknown value error
        print('I couldnt understand your words please say it again, unknown Error')
    except sr.RequestError as e:
        print('Request result from GSR speech error ',+e)

        return data
    recordAudio()
#A function to get the virtual assistance response
def assistantResponse(text):
    print(text)

    #convert the text int speech
    myobj =  gTTS(text = text,lang='en' , slow = False)

    #save the converted audio into a file
    myobj.save('assistant_response.mp3')

    #play the converted file
    os.system('start assistant_response.mp3')

#A function for wake word(s) or phrase
def wakeWord(text):
    WAKE_WORDS = ['hey cloak','ok cloak','cloak'] #A list of wake words
    text = text.lower() #converting the text to all lower case words

    #Check if the user command / text contain a wake words or phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    #If the wake word isn't found in the text from the loop and so it return false
    return False
# A function to get the current date
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    #A list of month
    month_name = ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December']

    #A list of ordinal number
    ordinalNumber = ['1st' , '2nd' , '3rd' ,'4th' , '5th' , '6th' , '7th' , '8th' , '9th' , '10th' , '11th' ,'12th' ,
                  '13th' , '14th' , '15th' , '16th' , '17th' , '17th' , '19th' , '20th' , '21th' , '22th' , '23th' ,
                   '24th' , '25th' , '26th' , '27th' , '28th' , '29th' , '30th' , '31th']
    return  'Today is' +weekday+ ' ' + month_name[monthNum  - 1]+ ' the' + ordinalNumber[dayNum - 1]+'. '
print(getDate())
#A function to return a random greeting as a response
def greeting(text):

    #Greeting inputs
    GREETING_INPUTS = ['hi' , 'hey' , 'hola' ,'wassup' , 'hello']

    #Greeting response
    GREETING_RESPONSES = ['hey there']

    #If the user input is a greeting, then return a random choosen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    #If no greeting was detected then return as empty string
    return ''

# A function to get a person first and last name from the text
def getPerson(text):
    wordList = text.split() #Splittng the text into list of words
    for i in range (0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList [i+2] + ' ' + wordList[i+3]
while True:
    #Record the Audio
    text = RecordAudio()
    response = ''

    #check for the wake word/phrases
    if(wakeWord(text) == True):
        #Check for greeting for the user
        response = response + greeting(text)

        #check to see if the user said anythning having to do with the date
        if ('date' in text):
            get_date = get_date()
            response = response + ' ' + get_date

        #check to see if the user said anything having to do with the time
        if (time in text):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >=12:
                meridiem = 'p.m' #post meridiem (PM) after midday
                hour = now.hour - 12
            else:
                meridiem = 'a.m' #  Ante meridiem (AM) before midday
                hour = now.hour

            #Convert minute into a proper string
            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)
            response = response + ' ' + 'It is' + str(hour) + ':' + minute + ' ' + meridiem + ' .'

        #check to see if the user said 'who is'
        if ('who is' in text):
            person = getPerson(Text)
            wiki = wikipedia.summary(person, sentences = 2)
            response = response + ' ' + wiki

        #Have the assistant respond back using audio and the text from response
        assistantResponse(response)