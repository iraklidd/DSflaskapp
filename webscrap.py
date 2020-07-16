from bs4 import BeautifulSoup

import requests
import re




url = 'C:/.../file.html'

page = open(url, encoding='utf8')

soup = BeautifulSoup(page.read(), "html.parser")
pattern = re.compile(r"(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?")
matches = []


elementdiv = soup.find_all('div', class_='nqmvxvec j83agx80 cbu4d94t bi6gxh9e tvfksri0 aov4n071 l9j0dhe7')

k = 0;
for elementdivn in elementdiv:
	pass
	k+=1
	elementa = elementdivn.find('a', class_='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l oo9gr5id')
	if elementa.has_attr('aria-label'):
		match = elementa['href']
	else:
		match = elementa['href']
	
	matches = matches + [match]
	print(match, k)


# 	# if elementa.has_attr('aria-label'):
# 	# 	match = pattern.finditer(element['href'])
# 	# 	# match = "aaa"
# 	# else:
# 	# 	# print(element['href'])
# 	# 	match = pattern.finditer(element['href'])
# 	# 	# match = element['href']
	
# 	# for m in match:
# 	# 	matches = matches + [m]

		
print(matches)






class getnumbers:

	wurl = ""

	def __init__(self, wurl):
		r  = requests.get(wurl)
		data = r.text;
		soup = BeautifulSoup(data, 'html.parser');

		webcontent = soup.get_text()
		self.f_allnumb = re.findall(r'[0-9]+', webcontent)


	def allnumbers(self):
		return self.f_allnumb


"""
html_doc = "<html></html>"

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
soup = BeautifulSoup(html_doc, 'html.parser') # from file
# print(soup)
# print(soup.prettify())
# print(soup.head)
# print(soup.get_text())


r  = requests.get("http://ds.a9b8c0.xyz/psql")
data = r.text;
soup = BeautifulSoup(data, 'html.parser');

webcontent = soup.get_text()


# for link in soup.find_all('a'):
#    print(link.get('href'))


# x = re.findall("[0-5][0-9]", webcontent) # orcifrianebi
x = re.findall(r'[0-9]+', webcontent)

# print(x)
"""


class getfacebook:

	wurl = "donaldtrumplikes.html"

	def __init__(self, wurl):
		r  = requests.get(wurl)
		data = r.text;
		soup = BeautifulSoup(data, 'html.parser');

		webcontent = soup.get_text()


	def getlikes(self):

		# url = "http://ds.a9b8c0.xyz"

		# headers = {
		#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
		#     }

		# response = requests.get(url, headers=headers)
		# soup = BeautifulSoup(response.content, "html.parser")
		# return soup



		url = 'static/files/donaldtrumplikes.html'

		page = open(url, encoding='utf8')

		soup = BeautifulSoup(page.read(), "html.parser")
		pattern = re.compile(r"(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?")
		matches = []

		k = 0;
		for element in soup.find_all('a', class_='_5i_s'):
			k+=1
			if element.has_attr('title'):
				match = pattern.finditer(element['href'])
				# match = "aaa"
			else:
				# print(element['href'])
				match = pattern.finditer(element['href'])
				# match = element['href']
			
			for m in match:
				matches = matches + [m]
		return matches
