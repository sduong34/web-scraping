Include a markdown file in the repo which includes instructions (e.g., what are the required python packages to run this, your approach for scrapping the data - the div/classes/css tags you found to extract the information)

BeautifulSoup from bs4, requests, and pandas packages are needed to run the code. 

weather.py extracts the titles and captions from the news page of weather.com, and they were extracted with the div tag, class='CollectionMediaList--title--2ELr1' (for titles) and class='CollectionMediaList--caption--3Md1w' (for captions).

I inserted the information extracted into a dataframe within the python file and then saved it to a csv file within the data folder. 