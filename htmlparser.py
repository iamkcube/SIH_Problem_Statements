from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
allTitles = []
allDescriptions =[]

heading_titles = soup.find_all('th', string='''Problem Statement
																		Title''')

heading_descriptions = soup.find_all('th', string='Description')

for index, heading_title in enumerate(heading_titles,1):
    
    if heading_title:
            td_element = heading_title.find_next('td')
            title_text = td_element.get_text(strip=True)
            
            title_text = title_text.replace("\t","").replace("\n"," ").replace("ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢", "'")
            allTitles.append(title_text)
    else:
        print("Heading 'Title' not found.")
            
for index, heading_description in enumerate(heading_descriptions,1):

    if heading_description:
            td_element = heading_description.find_next('td')
            description_text = td_element.get_text(strip=True)
            
            description_text = description_text.replace("\t","").replace("\n"," ").replace("ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢", "'")
            allDescriptions.append(description_text)
    else:
        print("Heading 'Description' not found.")

            
with open("readme.md", "w", encoding="utf-8") as f:
    for index, (title, desc) in enumerate(zip(allTitles,allDescriptions),1):
         f.write(f'## {index}. **{title}**\n{desc}\n\n')