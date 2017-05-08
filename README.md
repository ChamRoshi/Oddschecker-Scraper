# Oddschecker scraper system

Ever wanted to programatically pull the odds offered on elections, sports and more? Just me? 

This is a simple system that allows interactions with [Oddschecker.com](https://www.oddschecker.com/) an online odds comparison site. 

## Usage

    odds_dict = page_stats("https://www.oddschecker.com/ufc-mma/joanna-jedrzejczyk-v-jessica-andrade/winner") 

page_stats will crawl a page for the odds table and return a dictionary with the title of the page under odds_dict["title"] and the pandas dataframe with the odds contained under odds_dict["df"]

    url = search("jessica andrade")

search() will return the first url returned from the on-site search system. url can then be inputted directly into page_stats()


## Todo list

 * Make batch pulling odds from one query
 * Add pandas system to add a time to the odds dataframe