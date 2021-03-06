######################################################################################
#
#	Putlocker.is - v0.01
#
######################################################################################

TITLE = "Putlocker"
PREFIX = "/video/putlocker"
ART = "art-default.jpg"
ICON = "icon-default.png"
ICON_LIST = "icon-list.png"
ICON_COVER = "icon-cover.png"
ICON_SEARCH = "icon-search.png"
ICON_NEXT = "icon-next.png"
ICON_MOVIES = "icon-movies.png"
ICON_SERIES = "icon-series.png"
ICON_QUEUE = "icon-queue.png"
BASE_URL = "http://putlocker.is"
MOVIES_URL = "http://putlocker.is/genre"

######################################################################################
# Set global variables

def Start():

	ObjectContainer.title1 = TITLE
	ObjectContainer.art = R(ART)
	DirectoryObject.thumb = R(ICON_LIST)
	DirectoryObject.art = R(ART)
	VideoClipObject.thumb = R(ICON_MOVIES)
	VideoClipObject.art = R(ART)
	
	HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0'
	HTTP.Headers['Referer'] = 'putlocker.is'
	
######################################################################################
# Menu hierarchy

@handler(PREFIX, TITLE, art=ART, thumb=ICON)
def MainMenu():

	oc = ObjectContainer()
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2014", category="year/2014", page_count = 1), title = "2014", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2013", category="year/2013", page_count = 1), title = "2013", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2012", category="year/2012", page_count = 1), title = "2012", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2011", category="year/2011", page_count = 1), title = "2011", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2010", category="year/2010", page_count = 1), title = "2010", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2009", category="year/2009", page_count = 1), title = "2009", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2008", category="year/2008", page_count = 1), title = "2008", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2007", category="year/2007", page_count = 1), title = "2007", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2006", category="year/2006", page_count = 1), title = "2006", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2005", category="year/2005", page_count = 1), title = "2005", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2004", category="year/2004", page_count = 1), title = "2004", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2003", category="year/2003", page_count = 1), title = "2003", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2002", category="year/2002", page_count = 1), title = "2002", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2001", category="year/2001", page_count = 1), title = "2001", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="2000", category="year/2000", page_count = 1), title = "2000", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="1999", category="year/1999", page_count = 1), title = "1999", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="1998", category="year/1998", page_count = 1), title = "1998", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="1997", category="year/1997", page_count = 1), title = "1997", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="1996", category="year/1996", page_count = 1), title = "1996", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="1995", category="year/1995", page_count = 1), title = "1995", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="1994", category="year/1994", page_count = 1), title = "1994", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Action", category="genre/action", page_count = 1), title = "Action", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Adventure", category="genre/adventure", page_count = 1), title = "Adventure", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Animation", category="genre/animation", page_count = 1), title = "Animation", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Biography", category="genre/biography", page_count = 1), title = "Biography", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Comedy", category="genre/comedy", page_count = 1), title = "Comedy", thumb = R(ICON_MOVIES)))	
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Crime", category="genre/crime", page_count = 1), title = "Crime", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Documentary", category="genre/documentary", page_count = 1), title = "Documentary", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Drama", category="genre/drama", page_count = 1), title = "Drama", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Family", category="genre/family", page_count = 1), title = "Family", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Fantasy", category="genre/fantasy", page_count = 1), title = "Fantasy", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="History", category="genre/history", page_count = 1), title = "History", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Horror", category="genre/horror", page_count = 1), title = "Horror", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Music", category="genre/music", page_count = 1), title = "Music", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Mystery", category="genre/mystery", page_count = 1), title = "Mystery", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Romance", category="genre/romance", page_count = 1), title = "Romance", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Sci-Fi", category="genre/sci-fi", page_count = 1), title = "Sci-Fi", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Short", category="genre/short", page_count = 1), title = "Short", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Sport", category="genre/sport", page_count = 1), title = "Sport", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Talk Show", category="genre/talk-show", page_count = 1), title = "Talk Show", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Thriller", category="genre/thriller", page_count = 1), title = "Thriller", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="War", category="genre/war", page_count = 1), title = "War", thumb = R(ICON_MOVIES)))
	oc.add(DirectoryObject(key = Callback(ShowCategory, title="Western", category="genre/western", page_count = 1), title = "Western", thumb = R(ICON_MOVIES)))
	return oc

######################################################################################
# Creates page url from category and creates objects from that page

@route(PREFIX + "/showcategory")	
def ShowCategory(title, category, page_count):

	oc = ObjectContainer(title1 = title)
	page_data = HTML.ElementFromURL(BASE_URL + '/' + str(category) + '/' + str(page_count))
	
	for each in page_data.xpath("//td[contains(@style, 'padding-top: 5px; padding-left: 5px; padding-right: 5px;padding-bottom: 10px;')]"):
		url = each.xpath("./a/@href")[0]
		title = each.xpath("./a/@title")[0]
		thumb = each.xpath("./a/img/@src")[0]

		oc.add(DirectoryObject(
			key = Callback(EpisodeDetail, title = title, url = url),
			title = title,
			thumb = Resource.ContentsOfURLWithFallback(url = thumb, fallback=R(ICON_MOVIES))
			)
		)

	oc.add(NextPageObject(
		key = Callback(ShowCategory, title = category, category = category, page_count = int(page_count) + 1),
		title = "More...",
		thumb = R(ICON_NEXT)
			)
		)
	
	return oc

######################################################################################
# Gets metadata and google docs link from episode page. Checks for trailer availablity.

@route(PREFIX + "/episodedetail")
def EpisodeDetail(title, url):
	
	oc = ObjectContainer(title1 = title)
	page_data = HTML.ElementFromURL(url)
	title = page_data.xpath("//h2[contains(@style,'padding:0px;margin:0px;display:inline;font-weight:normal;border:0px;font-size:12px;')]/a/text()")[0]
	description = page_data.xpath("//td[@align='justify']/text()")[0]
	thumb = page_data.xpath("//img[contains(@style,'solid silver')]/@src")[0]
	
	oc.add(VideoClipObject(
		url = url,
		title = title,
		thumb = Resource.ContentsOfURLWithFallback(url = thumb, fallback='icon-cover.png'),
		summary = description
		)
	)	
	
	return oc
