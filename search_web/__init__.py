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
	26.CNN -cnn_search("Us elections 2020")
	27.Best Buy- `bestbuy_search("Python")`
	28.Britanica-`britannica_search("Anything")`
	29.Bussiness Insider- `businessinsider__search("News")`
	30.Dictionary- `dictionary_search("graphics")`
	31.Gamepedia- `gamepedia_search("Minecraft")`
	32.Github- `github_search("ankitsinghprograms")`
	33.Home depot- `homedepot_search("News")`
	34.MapQuest- `mapquest_search("California,USA")`
	35.Mayo clinic- `mayoclinic_search("What to do during Fever")`
	36.Medical News Today- `medicalnewstoday_search("COVID-19")`
	37.Merriam Webster- `merriam_webster_search("News")`
	38.Microsoft- `microsoft_search("Mac Book Pro")`
	39.NIH- `nih_search("Usa News")`
	40.Quizlet- `quizlet_search("Std 8")`
	41.Rotten Tomatoes- `rottentomatoes_search("Water Bottle")`
	42.Target- `target_search("Anything")`
	43.Urban Dictionary- `urban_dictionary_search("LOL meaing in urban dictionary")`
	44.USA Today- `usatoday_search("USA election")`
	45.Yahoo- `yahoo_search("C++")`
	46.Zillow- `zillow_search("News")`




========== Example ===========

Code is to simple Just 2 lines of Code.

------------------------------------
from pysearch import *
google_search("How to Search via pysearch module Python")
------------------------------------

=============================


=========== Version ===========

++ 0.1.3 (19/01/2021)+++++++++

~~ Bug Fixes

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
	
	


# Functions Added in Version- 0.1.2 (19/01/2021) are below:-


def github_search(text):
	
	
	"""
	Search on github (https://github.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	github="https://github.com/search?q={text}"
	
	open(github)





def merriam_webster_search(text):
	
	
	"""
	Search on merriam_webster (https://www.merriam-webster.com/dictionary/)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	merriam_webster=f"https://www.merriam-webster.com/dictionary/{text}"
	
	open(merriam_webster)





def gamepedia_search(text):
	
	
	"""
	Search on gamepedia (https://www.gamepedia.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	gamepedia=f'https://www.gamepedia.com/search?search={text}'
	
	open(gamepedia)





def microsoft_search(text):
	
	
	"""
	Search on Microsoft (https://www.microsoft.com/en-in/)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	microsoft=f"https://www.microsoft.com/en-in/search/result.aspx?{text}"
	
	open(microsoft)





def target_search(text):
	
	
	"""
	Search on target (https://www.target.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	target=f'https://www.target.com/s?searchTerm={text}'
	
	open(target)





def homedepot_search(text):
	
	
	"""
	Search on homedepot (https://www.homedepot.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	homedepot=f"https://www.homedepot.com/s/{text}"
	
	open(homedepot)





def nih_search(text):
	
	
	"""
	Search on NIH (https://search.nih.gov)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	nih=f"https://search.nih.gov/search?utf8=%E2%9C%93&affiliate=nih&query={text}&commit=Search"
	
	open(nih)





def rottentomatoes_search(text):
	
	
	"""
	Search on Rotten Tomatoes (https://www.rottentomatoes.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	rottentomatoes=f"https://www.rottentomatoes.com/search?search={text}"
	
	open(rottentomatoes)





def quizlet_search(text):
	
	
	"""
	Search on Quizlet (https://quizlet.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	quizlet=f"https://quizlet.com/subject/{text}/"
	
	open(quizlet)





def mapquest_search(text):
	
	
	"""
	Search on Mapquest (https://www.mapquest.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	mapquest=f"https://www.mapquest.com/search/results?query={text}"
	
	open(mapquest)





def britannica_search(text):
	
	
	"""
	Search on Britannica (https://www.britannica.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	britannica=f"https://www.britannica.com/search?query={text}"
	
	open(britannica)





def businessinsider_search(text):
	
	
	"""
	Search on Business Insider (https://www.businessinsider.in)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	businessinsider=f"https://www.businessinsider.in/searchresult.cms?query={text}"
	
	open(businessinsider)





def dictionary_search(text):
	
	
	"""
	Search on Dictionary (https://www.dictionary.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	dictionary=f"https://www.dictionary.com/browse/{text}/s=t"
	
	open(dictionary)





def zillow_search(text):
	
	
	"""
	Search on Zillow (https://www.zillow.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	zillow=f"https://www.zillow.com/homes/{text}/"
	
	open(zillow)





def mayoclinic_search(text):
	
	
	"""
	Search on Mayoclinic (https://www.mayoclinic.org)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	mayoclinic=f'https://www.mayoclinic.org/search/search-results?q={text}'
	
	open(mayoclinic)





def bestbuy_search(text):
	
	
	"""
	Search on Bestbuy (https://www.bestbuy.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	bestbuy=f"https://www.bestbuy.com/site/searchpage.jsp?st={text}"
	
	open(bestbuy)





def yahoo_search(text):
	
	
	"""
	Search on Yahoo (https://in.search.yahoo.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	yahoo=f"https://in.search.yahoo.com/search?p={text}"
	
	open(yahoo)





def usatoday_search(text):
	
	
	"""
	Search on USA Today (https://www.usatoday.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	usatoday=f"https://www.usatoday.com/search/?q={text}"
	
	open(usatoday)





def medicalnewstoday_search(text):
	
	
	"""
	Search on Medical News Today (https://www.medicalnewstoday.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	medicalnewstoday=f"https://www.medicalnewstoday.com/search?q={text}"
	
	open(medicalnewstoday)





def urban_dictionary_search(text):
	
	
	"""
	Search on Urban Dictionary (https://www.urbandictionary.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	urban_dictionary="https://www.urbandictionary.com/define.php?term={text}"
	
	open(urban_dictionary)





def usatoday_search(text):
	
	
	"""
	Search on USA Today (https://www.usnews.com)
	
	Parameters
	-----------
	
	text:- The query which you want to search about (str)
	
	"""
	
	usanews=f"https://www.usnews.com/search?q={text}"
	
	open(usanews)








