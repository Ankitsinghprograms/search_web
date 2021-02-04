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


search_list = [
	('google_search', 'text', 'https://www.google.com/search?q={text}&oq={text}', 'Search on Google (https://www.google.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('youtube_search', 'text', 'https://www.youtube.com/results?search_query={text}', 'Search on Youtube (https://www.youtube.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('bing_search', 'text', 'https://www.bing.com/search?q={text}', 'Search on Bing (www.bing.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('quora_search', 'text', 'https://www.quora.com/search?q={text}', 'Search on Quora (www.quora.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('python_search', 'text', 'https://www.python.org/search/?q={text}', 'Search on Python.org (www.python.org)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('twitter_search', 'text', 'https://twitter.com/search?q={text}', 'Search on twitter (https://twitter.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('facebook_search', 'text', 'https://facebook.com/search/top/?q={text}', 'Search on Facebook (https://facebook.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('pinterest_search', 'text', 'https://in.pinterest.com/search/pins/?q={text}', 'Search on Pinterest (https://in.pinterest.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('wikipedia_search', 'text', 'https://en.m.wikipedia.org/wiki/{text}', 'Search on Wikipedia (https://en.m.wikipedia.org)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('amazon_search', 'text', 'https://www.amazon.com/s?k={text}', 'Search on amazon (https://www.amazon.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('reddit_search', 'text', 'https://www.reddit.com/search?q={text}', 'Search on Reddit (https://www.reddit.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('imdb_search', 'text', 'https://www.imdb.com/find?q={text}', 'Search on imdb (https://www.imdb.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('tripadvisor_search', 'text', 'https://www.tripadvisor.com/Search?q={text}', 'Search on Tripadvisor (https://www.tripadvisor.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('walmart_search', 'text', 'https://www.walmart.com/search/?query={text}', 'Search on Walmart (https://www.walmart.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('craigslist_search', 'text', 'https://kolkata.craigslist.org/d/services/search/bbb?query={text}', 'Search on craigslist (https://kolkata.craigslist.org)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('ebay_search', 'text', 'https://www.ebay.com/sch/i.html?_nkw={text}', 'Search on Ebay (https://www.ebay.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('linkedin_job_search', 'text', 'https://www.linkedin.com/jobs/search?keywords={text}', 'Search on Linkedin (https://www.linkedin.com/jobs)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('linkedin_learning_search', 'text', 'https://www.linkedin.com/learning/search?keywords={text}', 'Search on Linkedin (https://www.linkedin.com/learning)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('playstore_search', 'text', 'https://play.google.com/store/search?q={text}', 'Search on Play Store (https://play.google.com/store)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('headline_search', 'text', 'https://www.healthline.com/search?q1={text}', 'Search on Headline (https://www.healthline.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('esty_search', 'text', 'https://www.etsy.com/in-en/search?q={text}', 'Search on Esty (https://www.etsy.c:om/in-en)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('apple_search', 'text', 'https://www.apple.com/us/search/{text}', 'Search on Apple (https://www.apple.com/us)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('espn_search', 'text', 'https://www.espn.in/search/_/q/{text}', 'Search on Espn (https://www.espn.in)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('webmd_search', 'text', 'https://www.webmd.com/search/search_results/default.aspx?query={text}', 'Search on Webmd (https://www.webmd.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('nytimes_search', 'text', 'https://www.nytimes.com/search?query={text}', 'Search on New York Times (https://www.nytimes.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('cnn_search', 'text', 'https://edition.cnn.com/search?q={text}', 'Search on CNN (https://edition.cnn.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('github_search', 'text', 'https://github.com/search?q={text}', 'Search on github (https://github.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('merriam_webster_search', 'text', 'https://www.merriam-webster.com/dictionary/{text}', 'Search on merriam_webster (https://www.merriam-webster.com/dictionary/)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('gamepedia_search', 'text', 'https://www.gamepedia.com/search?search={text}', 'Search on gamepedia (https://www.gamepedia.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('microsoft_search', 'text', 'https://www.microsoft.com/en-in/search/result.aspx?{text}', 'Search on Microsoft (https://www.microsoft.com/en-in/)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('target_search', 'text', 'https://www.target.com/s?searchTerm={text}', 'Search on target (https://www.target.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('homedepot_search', 'text', 'https://www.homedepot.com/s/{text}', 'Search on homedepot (https://www.homedepot.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('nih_search', 'text', 'https://search.nih.gov/search?utf8=%E2%9C%93&affiliate=nih&query={text}&commit=Search', 'Search on NIH (https://search.nih.gov)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('rottentomatoes_search', 'text', 'https://www.rottentomatoes.com/search?search={text}', 'Search on Rotten Tomatoes (https://www.rottentomatoes.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('quizlet_search', 'text', 'https://quizlet.com/subject/{text}/', 'Search on Quizlet (https://quizlet.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('mapquest_search', 'text', 'https://www.mapquest.com/search/results?query={text}', 'Search on Mapquest (https://www.mapquest.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('britannica_search', 'text', 'https://www.britannica.com/search?query={text}', 'Search on Britannica (https://www.britannica.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('businessinsider_search', 'text', 'https://www.businessinsider.in/searchresult.cms?query={text}', 'Search on Business Insider (https://www.businessinsider.in)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('dictionary_search', 'text', 'https://www.dictionary.com/browse/{text}/s=t', 'Search on Dictionary (https://www.dictionary.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('zillow_search', 'text', 'https://www.zillow.com/homes/{text}/', 'Search on Zillow (https://www.zillow.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('mayoclinic_search', 'text', 'https://www.mayoclinic.org/search/search-results?q={text}', 'Search on Mayoclinic (https://www.mayoclinic.org)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('bestbuy_search', 'text', 'https://www.bestbuy.com/site/searchpage.jsp?st={text}', 'Search on Bestbuy (https://www.bestbuy.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('yahoo_search', 'text', 'https://in.search.yahoo.com/search?p={text}', 'Search on Yahoo (https://in.search.yahoo.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('usatoday_search', 'text', 'https://www.usatoday.com/search/?q={text}', 'Search on USA Today (https://www.usatoday.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('medicalnewstoday_search', 'text', 'https://www.medicalnewstoday.com/search?q={text}', 'Search on Medical News Today (https://www.medicalnewstoday.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('urban_dictionary_search', 'text', 'https://www.urbandictionary.com/define.php?term={text}', 'Search on Urban Dictionary (https://www.urbandictionary.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('usatoday_search', 'text', 'https://www.usnews.com/search?q={text}', 'Search on USA Today (https://www.usnews.com)\n\tParameters\n\t-----------\n\ttext:- The query which you want to search about (str)\n\t'),
	('linkedin_people_search', 'first_name, last_name', 'https://www.linkedin.com/people-guest/pub/dir?firstName={first_name}&lastName={last_name}', 'Search on Linkedin (https://www.linkedin.com/people-guest/pub)\n\n\tParameters\n\t-----------\n\tfirst_name:- First Name of the person (str)\n\n\tlast_name:- Last Name of the person (str)'),
	('indeed_search', 'job_title, location', 'https://in.indeed.com/m/jobs?q={job_title}&l={location}', 'Search on Indeed (https://in.indeed.com/m/jobs)\n\n\tParameters\n\t-----------\n\n\tjob_title:- Name of the Job (str)\n\n\tlocation:- Location (str)\n\n	')
]

FUNC_TEMPLATE = '''
def {0}({1}): 
	"""
	{3}
	"""
	
	openurl=f"{2}" 
	open(openurl)
'''

for search in search_list:
	exec(FUNC_TEMPLATE.format(*search))

