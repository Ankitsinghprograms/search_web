"""
This module will Help You to Search on Different Websites like Google,Youtube,etc.


You can search on more than 25 websites very easily by just 2 lines of code.


Websites Supported:-

	1.Google -google_search("Python")
	2.Youtube -youtube_search("Python")
	3.Bing -bing_search("Python")
	4.Quora -quora_search("5 Python Projects")
	5.Python -python_search("Input in Python")
	6.Twitter -twitter_search("Python")
	7.Facebook -facebook_search("Python")
	8.Pinterest -pinterest_search("Python images")
	9.Wikipedia -wikipedia_search("Python_(programming_language)")
	10.Amazon -amazon_search("Python Books")
	11.Reddit -reddit_search("Python")
	12.Imdb -imdb_search("python")
	13.TripAdvisor -tripadvisor_search("London")
	14.Walmart -walmart_search("python Books")
	15.Craigslist -craigslist_search("Python")
	16.Ebay -ebay_search("Python books")
	17.LinkedIn-Job Search, People Search, Learning
	18.Playstore -playstore_search("python")
	19.Headline -headline_search("python")
	20.Esty -esty_search("python")
	21.Indeed -indeed_search("Python Developer","USA")
	22.Apple -apple_search("Mac Book Pro")
	23.ESPN -espn_search("Cricket")
	24.Webmd -webmd_search("Python")
	25.New York Times -nytimes_search("Covid-19")
	26CNN -cnn_search("Us elections 2020")


========== Example ===========

Code is to simple Just 2 lines of Code.

------------------------------------
from pysearch import *
google_search("How to Search via pysearch module Python")
------------------------------------

=============================


=========== Version ===========

+++++++++++(0.0.1)+++++++++++
~~First Relese
++++++++++++++++++++++++++++

=============================


======== Getting Errors??========

    If You get error then contact me at ankitsingh300307@gmail.com

    =============================


=========== Author ==========

Name-Ankit Singh
Email-ankitsingh300307@gmail.com
Github-https://github.com/Ankitsinghprograms
Country-India

============================



"""




import webbrowser




def open(link):
	
	"""
	Opening Webpage Through webbrowser module
	"""
	
	try:
		
		webbrowser.open(link)
		
	except:
		
		 print("EROOR UNABLE TO OPEN WEBSITE")
		 print("Common Errors:-\n\
		 ~ webbrowser module error \
		 ~ Your system doesn't have Any Webrowser \
		 	-Try Installing modules liks Chrome,Firefox,etc.\
		 ~ Contact to Author via email 'ankitsingh300307@gmail.com'")





def google_search(text):
	
	"""
	Search on Google (https://www.google.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""

	google=f"https://www.google.com/search?q={text}&oq={text}"
	
	open(google)
	
	
	
	
	
def youtube_search(text):
	
	"""
	Search on Youtube (https://www.youtube.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""

	youtube=f"https://www.youtube.com/results?search_query={text}"
	
	open(youtube)



def bing_search(text):
	
	"""
	Search on Bing (www.bing.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""

	bing=f"https://www.bing.com/search?q={text}"
	
	open(bing)


def quora_search(text):
	
	"""
	Search on Quora (www.quora.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""

	quora=f"https://www.quora.com/search?q={text}"
	
	open(quora)
	
	

def python_search(text):
	
	"""
	Search on Python.org (www.python.org)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	python_org=f"https://www.python.org/search/?q={text}"
	
	open(python_org)
	
	
	

def twitter_search(text):
	
	"""
	Search on twitter (https://twitter.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	twitter=f"https://twitter.com/search?q={text}"
	
	open(twitter)
	
	
	

def facebook_search(text):
	
	"""
	Search on Facebook (https://facebook.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	facebook=f"https://facebook.com/search/top/?q={text}"
	
	open(facebook)
	
	
	

def pinterest_search(text):
	
	
	"""
	Search on Pinterest (https://in.pinterest.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	pinterest=f"https://in.pinterest.com/search/pins/?q={text}"
	
	open(pinterest)
	
	
	

def wikipedia_search(text):
	
	
	"""
	Search on Wikipedia (https://en.m.wikipedia.org)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	wikipedia=f"https://en.m.wikipedia.org/wiki/{text}"
	
	open(wikipedia)



def amazon_search(text):
	
	
	"""
	Search on amazon (https://www.amazon.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	amazon=f"https://www.amazon.com/s?k={text}"
	
	open(amazon)
	
	
	
	
	
def reddit_search(text):
	
	
	"""
	Search on Reddit (https://www.reddit.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	reddit=f"https://www.reddit.com/search?q={text}"
	
	open(reddit)




def imdb_search(text):
	
	
	"""
	Search on imdb (https://www.imdb.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	imdb=f"https://www.imdb.com/find?q={text}"
	
	open(imdb)




def tripadvisor_search(text):
	
	
	"""
	Search on Tripadvisor (https://www.tripadvisor.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	tripadvisor=f"https://www.tripadvisor.com/Search?q={text}"
	
	open(tripadvisor)





def walmart_search(text):
	
	
	"""
	Search on Walmart (https://www.walmart.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	walmart=f'https://www.walmart.com/search/?query={text}'
	
	open(walmart)





def craigslist_search(text):
	
	
	"""
	Search on craigslist (https://kolkata.craigslist.org)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	craigslist=f'https://kolkata.craigslist.org/d/services/search/bbb?query={text}'
	
	open(craigslist)





def ebay_search(text):
	
	
	"""
	Search on Ebay (https://www.ebay.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	ebay=f"https://www.ebay.com/sch/i.html?_nkw={text}"
	
	open(ebay)





def linkedin_job_search(text):
	
	
	"""
	Search on Linkedin (https://www.linkedin.com/jobs)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	linkedin_job=f"https://www.linkedin.com/jobs/search?keywords={text}"
	
	open(linkedin_job)





def linkedin_people_search(first_name,last_name):
	
	
	"""
	Search on Linkedin (https://www.linkedin.com/people-guest/pub)
	
	Parameters
	-----------
	
	first_name:- First Name of the person (str)
	
	last_name:- Last Name of the person (str)
	
	"""
	
	linkedin_people=f"https://www.linkedin.com/people-guest/pub/dir?firstName={first_name}&lastName={last_name}"
	
	open(linkedin_people)





def linkedin_learning_search(text):
	
	
	"""
	Search on Linkedin (https://www.linkedin.com/learning)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	linkedin_learning=f"https://www.linkedin.com/learning/search?keywords={text}"
	
	open(linkedin_learning)





def playstore_search(text):
	
	
	"""
	Search on Play Store (https://play.google.com/store)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	play_store=f"https://play.google.com/store/search?q={text}"
	
	open(play_store)





def headline_search(text):
	
	
	"""
	Search on Headline (https://www.healthline.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	headline=f'https://www.healthline.com/search?q1={text}'
	
	open(headline)





def esty_search(text):
	
	
	"""
	Search on Esty (https://www.etsy.c:om/in-en)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	esty=f'https://www.etsy.com/in-en/search?q={text}'
	
	open(esty)





def indeed_search(job_title,location):
	
	
	"""
	Search on Indeed (https://in.indeed.com/m/jobs)
	
	Parameters
	-----------
	
	job_title:- Name of the Job (str)
	
	location:- Location (str)
	
	"""
	
	indeed=f'https://in.indeed.com/m/jobs?q={job_title}&l={location}'
	
	open(indeed)





def apple_search(text):
	
	
	"""
	Search on Apple (https://www.apple.com/us)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	apple=f"https://www.apple.com/us/search/{text}"
	
	open(apple)





def espn_search(text):
	
	
	"""
	Search on Espn (https://www.espn.in)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	espn=f'https://www.espn.in/search/_/q/{text}'
	
	open(espn)





def webmd_search(text):
	
	
	"""
	Search on Webmd (https://www.webmd.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	webmd=f'https://www.webmd.com/search/search_results/default.aspx?query={text}'
	
	open(webmd)





def nytimes_search(text):
	
	
	"""
	Search on New York Times (https://www.nytimes.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	nytimes=f'https://www.nytimes.com/search?query={text}'
	
	open(nytimes)





def cnn_search(text):
	
	
	"""
	Search on CNN (https://edition.cnn.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	cnn=f'https://edition.cnn.com/search?q={text}'
	
	open(cnn)



