


'''run in python 2.7'''


import zipfile #to extract the downloaded zip files
import re #regExp
#import urlparse
import urllib
import urllib2
import argparse
import os,sys
from urllib2 import urlopen
from urllib import urlretrieve
from BeautifulSoup import BeautifulSoup as bs #parsing the url
from string import maketrans 

#no error/exception handling has been performed; code is unstructured and very noob-ish

def subs(st):

	x=st.split()
	for i in range(len(x)-1):
		x[i]=x[i][0].upper()+x[i][1:]+' '
	st=''.join(x)

	u='http://subscene.com' #downloading from this website

	url=u+'/subtitles/title?q='

	#st=raw_input("Enter the movie name: ")
	print 'You entered: '+st
	cnt=-1
	if not st.endswith(')'):
		for i in st:
			cnt+=1
			if i=='[':
				#print 'not ok'
				st=st[:cnt-1]	#if movie name has Batman The Dark Knight (2008) [1080p], removes the "[1080p]"
	
	st1=re.sub(' ','+',st)
	st1=re.sub('\(','%28',st1)
	st1=re.sub('\)','%29',st1)
	
	print 'st1= '+st1
	
	url+=st1+'&l='
	
	print 'url= '+url #url format
	
	opener=urllib2.build_opener()
	opener.addheaders=[('user-agent','Mozilla/4.0')]
	
	
	soup=str(bs(urlopen(url)))
	
	st2=re.sub('\(','\(',st)
	st2=re.sub('\)','\)',st2)
	st2+='<\/a>'
	
	print 'st2='+st2
	
	x=st2.split()
	for i in range(len(x)-1):
		x[i]+='(.?) '
	
	x=''.join(x) #if movie name misses ":" or any other char
	
	print 'x='+x
	
	f='\/(.+)'+x
	li={}
	l=re.compile(f)
	for m in l.finditer(soup):
		li[m.group()]=m.start()
	
	sam=li.keys()[-1] #the title

	print 'sam='+sam

	c=re.sub('>(.+)','',sam)
	c=c[:-1]
	url2=u+c+'/english'

	print 'url2='+url2

	soup2=str(bs(urlopen(url2)))
	ds=urlopen(url2)
	ss=ds.read()
	ss=ss.translate(maketrans("\n\t\r","   ")) #removes the white spaces

	po=re.sub('\/','\/',c)
	po=re.sub('\-','\-',po)

	fer='<a href=\"'+po+'\/english\/[0-9]{6}\">\s*<div class=\"visited\">\s*<span class=\"l r positive\-icon\">'
	#will download only "rated good" subtitles
	newstr=re.search(fer,ss).group()
	newstr=re.search('\/(.+?)>',newstr).group()
	newstr=newstr[:-2]

	print 'newstr='+newstr

	url3=u+newstr

	soup3=str(bs(urlopen(url3)))

	n=re.search('<a href=(.+)>Download English Subtitle',soup3).group()

	n=re.search('"(.+?)"',n).group()

	n=n[1:-1]

	urlret=u+n
	urlretrieve(urlret,'C:\Python27\omg2.zip') #need to better this code to save the downloaded file to the movie folder. (NOTE: check os.chdir and os module)

	with zipfile.ZipFile('omg2.zip','r') as z:
		z.extractall('C:\\') #needs to be appropriately extracted to appropriate folders


if __name__ == "__main__":
	parser=argparse.ArgumentParser(prog='subtitles',description='Subtitle downloader; Currently downloads by taking user input(keyboard input)')
	parser.add_argument('-m',metavar='movie name',type=str,nargs='+',help="usage: Movie Name (YYYY)",required=True)
	
	args=parser.parse_args()
	ur1=''
	for i in range(len(args.m)):
	
		ur1 += args.m[i] + ' '
	
	ur1=ur1[:-1]
	print ur1[-1]
	if not ur1.endswith(')'):
		print 'please type in again with the year'
		parser.print_help()
		sys.exit(-1)
		
	subs(ur1)