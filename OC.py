import requests
import pandas as pd
from bs4 import BeautifulSoup
import json 


def page_stats(url):
	#input a url and this returns the odds table with the odds broker
	r = requests.get(url = url)
	soup = BeautifulSoup(r.text, "html.parser")


	table = soup.find( "table", {"class":"eventTable "} )

	df = pd.read_html(str(table))
	df = df[0].dropna(axis=0, thresh=0)
	cols = ["winner", "bet365" , "skybet", "betstars", "william hill", "betfred", "sportingbet", "betvictor", "paddypower", "stanjames.com", "ladbrokes", "coral", "Boyle Sports", "Winner", "Betfair", "Betway", "BetBright", "Netbet", "BWin", "32Win", "10Bet", "Marathon Bet", "188Bet", "888sport", "Blacktype", "unibet", "betfair exchange", "betdaq", "Matchbook"]
	while len(cols) != len(df.columns):
		if len(cols) > len(df.columns):
			cols = cols[:-1]
		if len(cols) < len(df.columns):
			cols.append("dummy")

	try:
		df.columns = cols
	except: 
		print "problem adding usual columns... because fuck them."
	return {"title": soup.title.text, "df": df}

def search(query):
	#input a search query and this returns the first responce from the Oddschecker search
	url = "https://www.oddschecker.com/search/process?from=1&limit=10&query={0}".format(query.replace(" ", "+"))
	r = requests.get(url = url)
	j = json.loads(r.text)
	base_url = "https://www.oddschecker.com/"
	return base_url+j["search_results"]["search_results"][0]["market_map"]






# url = "https://www.oddschecker.com/politics/british-politics/next-uk-general-election/overall-majority"
# # print url
# print page_stats(url)