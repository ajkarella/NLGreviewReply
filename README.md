# NLGreviewReply
Generates review replies using NLG. We utilized tensorflow for the creation and training of our model. Comments in the **NLGmodel.ipynb** explain some of the steps we took to get our generated responses and their evaluation metrics.

Other code files in this repository include **yelp_scraper.ipynb** which was our development process on collecting review and reply pairs, and **threadedYelpScraper.py** which uses multithreading to collect data rapidly(this didn't work because Yelp employs captchas after too many requests in a given timeframe). 
