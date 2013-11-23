## Welcome to Diogo's personal blog

My poor attempt of writing a small static blog generator (à la [Jekyll][1]). This time the main weapons of choice were [Python][2] and [Flask][3].

During this first (quick) iteration, the blog entries are being loaded and parsed from the hard-drive when a request comes in. In the near future, the objective is to have this proccess automatized, whenever a blog entry is edited/added (add a watch operation).

I had three main objectives in mind, developing this: 

* To remove the MongoDB dependency that the previous blog version had 
* To add a simpler, content centered, responsive design
* To be able to write the entries using Markdown

The three of them were achieved. There are a lot of nice-to-have's that I'd like to add, but one just has so many off-days per week. :)


## Used software

* [Python 2.7][2]
* [Flask Microframework][3]
* [Ink Interface Kit][4]
* [HighlightJS][5]
* [Flask-Ink][6]
* [Flask-Cache][7]
* [Flask-Paginate][8]
* [html2text][9]
* [Pymongo][10]
* [Misaka][11]
* [BeautifulSoup][12]


[1]: http://jekyllrb.com/
[2]: http://www.python.org/
[3]: http://flask.pocoo.org/
[4]: http://ink.sapo.pt/
[5]: http://highlightjs.org/
[6]: https://pypi.python.org/pypi/Flask-Ink/2.2.1
[7]: http://pythonhosted.org/Flask-Cache/
[8]: http://pythonhosted.org/Flask-paginate/
[9]: https://github.com/aaronsw/html2text
[10]: http://api.mongodb.org/python/current/
[11]: http://misaka.61924.nl/
[12]: http://www.crummy.com/software/BeautifulSoup/
