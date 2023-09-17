from bs4 import BeautifulSoup
import ftfy
import json

with open("website.html", "r", encoding="utf-8") as file:
	html_content = file.read()
	html_content = ftfy.fix_text(html_content)

soup = BeautifulSoup(html_content, 'html.parser')
allTitles = []
allDescriptions =[]
jsondict = []

heading_titles = soup.select("#settings>thead>tr:nth-child(2)>td")
heading_descriptions = soup.select("#settings>thead>tr:nth-child(3)>td")

for index, heading_title in enumerate(heading_titles,1):
	
	if heading_title:
			title_text = heading_title.get_text(strip=True)
			
			title_text = title_text.replace("\t","").replace("\n"," ")
			allTitles.append(title_text)
	else:
		print("Heading 'Title' not found.")
			
for index, heading_description in enumerate(heading_descriptions,1):

	if heading_description:
			description_text = heading_description.get_text(strip=True)
			
			description_text = description_text.replace("\t","").replace("\n"," ")
			allDescriptions.append(description_text)
	else:
		print("Heading 'Description' not found.")

			
with open("readme.md", "w", encoding="utf-8") as f:
	for index, (title, desc) in enumerate(zip(allTitles,allDescriptions),1):
		 f.write(f'## {index}. **{title}**\n{desc}\n\n')
			
with open("readme.json", "w", encoding="utf-8") as f:
	for index, (title, desc) in enumerate(zip(allTitles,allDescriptions),1):
		jsondict.append({
			"psNo":index,
			"title": title,
			"desc": desc,
		})
	f.write(json.dumps(jsondict))