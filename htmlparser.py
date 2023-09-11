from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
allTitles = []
allDescriptions =[]
# # Find the <th> element containing the heading "Description"
# heading_description = soup.find('th', string='Description')

# # Find the corresponding <td> element
# if heading_description:
#     td_element = heading_description.find_next('td')
    
#     # Extract the text from the <td> element
#     description_text = td_element.get_text(strip=True)
    
#     # Print the extracted description text
#     print(description_text)
# else:
#     print("Heading 'Description' not found.")

heading_titles = soup.find_all('th', string='''Problem Statement
																		Title''')

heading_descriptions = soup.find_all('th', string='Description')

# Find the corresponding <td> element
# if heading_description:
#     td_element = heading_description.find_next('td')
    
#     # Extract the text from the <td> element
#     description_text = td_element.get_text(strip=True)
    
#     # Print the extracted description text
#     print(description_text)
# else:
#     print("Heading 'Description' not found.")

    
for index, heading_title in enumerate(heading_titles,1):
    if heading_title:
            td_element = heading_title.find_next('td')
            
            # Extract the text from the <td> element
            title_text = td_element.get_text(strip=True)
            
            # Print the extracted title text
            # print(title_text)
            title_text = title_text.replace("\t","").replace("\n"," ")
            allTitles.append(title_text)
    else:
        print("Heading 'Title' not found.")

for index, heading_description in enumerate(heading_descriptions,1):
    if heading_description:
            td_element = heading_description.find_next('td')
            
            # Extract the text from the <td> element
            description_text = td_element.get_text(strip=True)
            
            # Print the extracted description text
            # print(description_text)
            description_text = description_text.replace("\t","").replace("\n"," ")
            allDescriptions.append(description_text)
    else:
        print("Heading 'Description' not found.")

with open("result.md", "w", encoding="utf-8") as f:
    for index, (title, desc) in enumerate(zip(allTitles,allDescriptions),1):
         f.write(f'## {index}. **{title}**\n{desc}\n\n')