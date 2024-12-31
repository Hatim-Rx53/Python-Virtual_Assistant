import time
import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import wikipedia
import pywhatkit
import requests
from AppOpener import open, close
from bs4 import BeautifulSoup
from pygooglenews import GoogleNews


def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and 
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[0].id)
	engine.setProperty('rate', 160)
	
	# Method for the speaking of the assistant
	engine.say(audio) 
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()


# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module 
	# we will use the Microphone module
	# for listening the command
	with sr.Microphone() as source:
		print("")
		print('Listening...')
		
		# seconds of non-speaking audio before 
		# a phrase is considered complete
		r.pause_threshold = 0.35
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized 
		# it is good else we will have exception 
		# handling
		try:
			print("< Recognizing >")
			print("")
			
			# for Listening the command in indian
			# english we can also use 'hi-In' 
			# for hindi recognizing
			Query = r.recognize_google(audio, language='en-in')
			print("Given Command : ", Query)
			print("")
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			speak("Say that again sir")
			time.sleep(0.25)
			print("")
			return "None"
		
		return Query

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number 
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday', 
				3: 'Wednesday', 4: 'Thursday', 
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	
	# This method will give the time
	present_time = time.localtime()
	Timehour = time.strftime("%I:%M %p", present_time)
	print(Timehour)
	speak("The current time is " + Timehour)

def Hello():
	
	# This function is for when the assistant 
	# is called it will say hello and then 
	# take query
	speak("hello sir I am DOODLE your desktop assistant. Tell me how may I help you")

def get_news():
	gn = GoogleNews(lang='en', country='IN')
	top = gn.geo_headlines('India')

	entries = top["entries"]
	count = 0
	for entry in entries:
		count = count + 1
		if count <= 10:
			print(
				str(count) + ". " + entry["title"])
			speak(entry["title"])
			time.sleep(0.25)

def get_random_joke():
    headers = {
        'Accept': 'application/json'}

    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def get_random_fact():
    url = 'https://uselessfacts.jsph.pl/random.json?language=en'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we raise an exception for bad status codes
        fact_data = response.json()
        return fact_data['text']
    except requests.exceptions.RequestException as e:
        return f"Error fetching fact: {e}"


# Driver Code

def Take_query():

	# calling the Hello function for 
	# making it more interactive
	print("\n\n\n\t\t\t\tHello sir I am DOODLE your desktop assistant. Tell me how may I help you\t\t\t\t\n\n\n")
	Hello()
	
	# This loop is infinite as it will take
	# our queries continuously until and unless
	# we do not say bye to exit or terminate 
	# the program
	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times 
		# query matches and we get the perfect 
		# output
		query = takeCommand().lower()

		if "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue

		elif "today's day" in query:
			tellDay()
			continue

		elif "time" in query:
			tellTime()
			continue

		# this will exit and terminate the program
		elif "turn off" in query:
			speak("Initialising self Destruct sequence in 3...2...1... Justkidding byee seeya")
			exit()

		elif "bye" in query:
			speak("Initialising self Destruct sequence in 3...2...1... Justkidding byee seeya")
			exit()

		elif "who is" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			query = query.replace("who is", "")
			
			# it will give the summary of 4 lines from 
			# wikipedia we can increase and decrease 
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			print(result)
			speak(result)
			continue

		elif "who are" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			query = query.replace("who is", "")
			
			# it will give the summary of 4 lines from 
			# wikipedia we can increase and decrease 
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			print(result)
			speak(result)
			continue

		elif "what is" in query:
			
			# if any one wants to have information
			# from wikipedia
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			query = query.replace("what is", "")
			query = query.replace("a", "")
			query = query.replace("an", "")
			
			# it will give the summary of 4 lines from 
			# wikipedia we can increase and decrease 
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			print(result)
			speak(result)
			continue

		elif "tell me about" in query:
			
			# if any one wants to have information
			# from wikipedia
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			query = query.replace("tell me about", "")
			query = query.replace("a", "")
			query = query.replace("an", "")
			
			# it will give the summary of 4 lines from 
			# wikipedia we can increase and decrease 
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			print(result)
			speak(result)
			continue

		elif ".com" in query:
			query = query.replace('ok doodle', '')
			query = query.replace('hey doodle', '')
			query = query.replace('open', '')
			speak("Opening")
			webbrowser.open(query)
			continue

		elif "search on google" in query:
			query = query.replace('search on google', '')
			speak("Searching on google")
			pywhatkit.search(query)
			continue

		elif "tell me your name" in query:
			speak("I am Doodle. Your desktop Assistant")
			continue

		elif "who made you" in query:
			speak("If you are speaking with me you might have met him or maybe you are sitting with him right now.")
			speak("but then too its my duty to introduce him to you")
			speak("Hatim aka HR made me, He is a student currently persuing BCA, HE created me as a school project on 01-09-22 that was all the information that i am allowed to give to you")
			continue

		elif "joke" in query:
			print(get_random_joke())
			speak(get_random_joke())
			continue

# for opening and closing Apps
		elif "open" in query:
			query = query.replace('open', '')
			speak('opening' + query)
			open(query, match_closest=True)
			continue

		elif "close" in query:
			query = query.replace('close', '')
			speak('closing' + query)
			close(query, match_closest=True)
			continue

# for playing songs on youtube
		elif 'youtube' in query:
			query = query.replace('the', '')
			query = query.replace('on', '')
			query = query.replace('youtube', '')
			query = query.replace('video', '')
			query = query.replace('play', '')
			query = query.replace('search', '')

			speak('playing'+query)
			pywhatkit.playonyt(query)
			continue

		elif "news headlines" in query:
			news = get_news()
			print(news)
			speak(news)
			continue

		elif "give an advice" in query:
			advice = get_random_advice()
			print(advice)
			speak(advice)
			continue

		elif "tell me a fact" in query:
			fact = get_random_fact()
			print(fact)
			speak(fact)
			continue


if __name__ == '__main__':
	
	# main method for executing
	# the functions
	Take_query()
