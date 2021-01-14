# search_web



![pypi](data:image/jpeg;base64,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Z0f90rhT4FUTG7WWHd7z+6OA9p9isuB7NCneJHyZnAHQCzdRbqfgqrxLfbfT0L6U3jzTWYx94+nSZtNtq21K3ivETE5WBTeC+oep+xQim8F9Q9T9gXIeD4/Mcek/0v8AdZ8iE2hP/EcO/wAb7q6sAiaa3FCWtJzMFyATYsNx0VtdG0kEgEjgbajoeSNiaCSGgE8TYa9fFdSrmXhhOFQOsXRsqi6QD/pCQ3uPDgpquxOnqK/DzTva8NMgJaNBdmjb+PlyV2bC0DKGtA10sLa8dFxjpo22DWMFrkWaBYnjbwQZ3TPMU1dFPWR0hfK91pYA7eROHdLXOcLgDSy9eK0rfRqCjp376YlskMou0xxtObe8y0WIFvLyV5mpo32L2MdbhmaDbpdchE298rb2tewvbwv4IK9sHNGaYRhuSSNzmzNJu7fZiXOPjm4/DkrIuDYmgkhoBPEganqea5oCIiAiIgIiICIiAiIg8b4iPPoup2tv55Fc94eeqSPBty159DzWB8BI4H3rKe0aMOrXd9rXZItHaA908HcPfbqtWWR9pPy537kX3VI2vx/sj7n4EFSwOZIzM0jUa8j0PArujp3kXAsPEkAe86LowyZzZGBriASLgHQ9RzXY+RztXEuPiSSfirKucq+2MJ7AMFjqQ4GU2aQTkHG44AuHl4K20OD08PqRi/0jq73lQOwX9d/c/NW1cT47vdxG6to1vPljHEfWIn5dr/w7Q0p0YvNeefcRF30UYc9oOoP8FSaelNtWK9ZlYzbFculrSdACVO4TE5rCHCxvf4L0xwtaLNAHQLk3ifZ9i6TZeGxt7eebZn+FfrbidSMY4ckRFaI4iIgIiICIiAiIgIiICIiAiIgIiIPAvjuX88ivS6nHI2XQ+Jwtp7uhWGXDL4aKlbYbGy1cpnikZms1uR1wO6OThfxV3XFvP+eQXql5pOYeL0i8Ylib8FqaaVm+iewXHetdv+oaL24VszV1NjHEQ36T+633nj7FsDhfivepUbu2OuUedpXPfCi4Ps26hac72vc+1w0Gwy+Z48VIKVxz9j2/kotrSdACei4rxa977u3rOOvtC72lK00YiOnKC2ZubhcX6XUg18ZmZuwLDmOBXVBhb3cbNHnx9ykKbDmM11J8Sf4LfstnuInmsRHmicz3x8njV1aevOHrLkbzX0BfV0aCIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIOD4weIXS6m8D716UQeF7COIXszeA/Jcksg881K2Qgv1ty5Ltjia3RoA6Bc0XiKVi02iOZ+bOZxgREXtgREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERB//Z)



## This module will Help You to Search on Different Websites like Google,Youtube,etc.


### You can search on more than 25 websites very easily by just 2 lines of code. 



` So First Install the module `

```python 

pip install search-web

```


### Websites Supported:-


	1.Google - `google_search("Python")`
	
	2.Youtube - ` youtube_search("Python")`
	
	3.Bing - `bing_search("Python")`
	
	4.Quora - `quora_search("5 Python Projects")`
	
	5.Python - `python_search("Input in Python")`
	
	6.Twitter - `twitter_search("Python")`
	
	7.Facebook - `facebook_search("Python")`
	
	8.Pinterest - `pinterest_search("Python images")`
	
	9.Wikipedia - `wikipedia_search("Python_(programming_language)")`
	
	10.Amazon - `amazon_search("Python Books")`
	
	11.Reddit - `reddit_search("Python")`
	
	12.Imdb - `imdb_search("python")`
	
	13.TripAdvisor - `tripadvisor_search("London")`
	
	14.Walmart - `walmart_search("python Books")`
	
	15.Craigslist - `craigslist_search("Python")`
	
	16.Ebay - `ebay_search("Python books")`
	
	17.LinkedIn- Job Search, People Search, Learning
	
	18.Playstore -`playstore_search("python")`
	
	19.Headline -`headline_search("python")`
	
	20.Esty - `esty_search("python")`
	
	21.Indeed - `indeed_search("Python Developer","USA")`
	
	22.Apple - `apple_search("Mac Book Pro")`
	
	23.ESPN - `espn_search("Cricket")`
	
	24.Webmd - `webmd_search("Python")`
	
	25.New York Times -`nytimes_search("Covid-19")`
	
	26CNN - `cnn_search("Us elections 2020")`



`Code` is so simple Just 2 lines of `Code`.

```python
from search_web import *
pysearch.google_search("How to Search via search_web module Python")
```


FUNCTIONS

+ `amazon_search(text) `

   [Amazon](https://www.amazon.com)



       Parameters
       ----------

       text:- The query which you want to search about (str)


+ `apple_search(text)`

   [Apple](https://www.apple.com/us)


        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+  `bing_search(text)`
    
   [Bing](www.bing.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `cnn_search(text)`

  [CNN](https://edition.cnn.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `craigslist_search(text)`

   [Craigslist](https://kolkata.craigslist.org)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `ebay_search(text)`

   [Ebay](https://www.ebay.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

 + `espn_search(text)`
    
   [ESPN](https://www.espn.in)

        Parameters
        -----------

        text:- The query which you want to search about (str)


  + `esty_search(text)`
    
    [Esty](https://www.etsy.c:om/in-en)

        Parameters
        -----------

        text:- The query which you want to search about (str)


+ `facebook_search(text)`

   [Facebook](https://facebook.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

 + ` google_search(text)`
    
      [Google](https://www.google.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

 +  ` headline_search(text) `


    [Headline](https://www.healthline.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `imdb_search(text)`

    [IMDB](https://www.imdb.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

 +  `indeed_search(job_title, location)`

    [Indeed](https://in.indeed.com/m/jobs)

        Parameters
        -----------

        job_title:- Name of the Job (str)

        location:- Location (str)
        

+ `linkedin_job_search(text)`

    [Linkedin](https://www.linkedin.com/jobs)

        Parameters
        -----------

        text:- The query which you want to search about (str)


 +  `linkedin_learning_search(text)`

     [Linkedin](https://www.linkedin.com/learning)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `linkedin_people__search(first_name, last_name)`

    [Linkedin](https://www.linkedin.com/people-guest/pub)

        Parameters
        -----------

        first_name:- First Name of the person (str)

        last_name:- Last Name of the person (str)
        

+ `nytimes_search(text)`

    [New York Times](https://www.nytimes.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `pinterest_search(text)`

     [Pinterest](https://in.pinterest.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `play_store_search(text)`

    [Play Store](https://play.google.com/store)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `python_search(text)`

     [Python.org](www.python.org)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `quora_search(text)`

    [Quora](www.quora.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `reddit_search(text)`

   [Reddit](https://www.reddit.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `tripadvisor_search(text)`

   [Tripadvisor](https://www.tripadvisor.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `twitter_search(text`)

    [Twiiter](https://twitter.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `walmart_search(text)`

    [Walmart](https://www.walmart.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `webmd_search(text)`

    [Webmd](https://www.webmd.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)


+ `wikipedia_search(text)`

   [Wikipedia](https://en.m.wikipedia.org)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        

+ `youtube_search(text)`

    [Youtube](https://www.youtube.com)

        Parameters
        -----------

        text:- The query which you want to search about (str)
        
        
        
        
**Version-(0.0.1)-First Release**


**License-MIT**



