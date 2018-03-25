from bs4 import BeautifulSoup
import requests
from string import ascii_lowercase


def iterate(soup):
	
	terms 		= []
	definitions = []

	for term in soup.find( 'div', "view-content clearfix" ).find_all( 'h2' ):
		terms.append(term.text.encode( "utf8" ))

	for definition in soup.find( 'div', "view-content clearfix" ).find_all( 'div', 'content clearfix' ):
		s 		= ""
		for x in definition.find_all('p'):
			s += ( x.text.encode( "utf8" ) )
		definitions.append(s)
	return terms, definitions

def print_contents(terms, definitions):
	for term, definition in zip(terms, definitions):
	    print term
	    print definition
	    print "_______________________________________________________________________________________"


for c in ascii_lowercase:
	url	 					= 'https://www.economist.com/economics-a-to-z/'+c
	r 						= requests.get( url )
	data 					= r.text
	soup 					= BeautifulSoup(data, "lxml")
	terms, definitions		= iterate(soup)
	print_contents(terms, definitions)
	print '\n\n'