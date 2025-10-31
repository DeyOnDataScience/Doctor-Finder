from bs4 import BeautifulSoup
import requests

def scrape_url(Location, Speciality, limit=10):
    url = f"Site url to scrape" 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    doctors = soup.find_all("div", class_="info-section")
    info_list = []
    
    for doc in doctors[:limit]:
        name = doc.find("h2")
        speciality = doc.find("div", class_="uv2-spacer--xs-top")
        experience = doc.find("span", class_="uv2-spacer--xs-right")
        location = doc.find("div", class_="uv2-spacer--xs-top-2")

        text = []
        if name: text.append(f"Name: {name.get_text(strip=True)}")
        if speciality: text.append(f"Speciality: {speciality.get_text(strip=True)}")
        if experience: text.append(f"Experience: {experience.get_text(strip=True)}")
        if location: text.append(f"Location: {location.get_text(strip=True)}")

        info_list.append("\n".join(text))
    
    result = "\n\n".join(info_list)
    
    # Optional length safeguard
    if len(result) > 15000:
        result = result[:15000] + "\n\n[Truncated]"
    
    return result
