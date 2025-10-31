import os,re
from google import genai
from dotenv import load_dotenv
from scrape import scrape_url
load_dotenv()
os.environ["API_KEY"] = os.getenv("GOOGLE_API_KEY")

def extract_location_speciality(user_input):
    prompt = f"""
        You are a smart health assistant.

When a user sends a message, follow these rules:

1. Determine if the message is related to a health problem, symptom, or a request for a doctor.
2. If it IS health-related:
   - Identify key symptoms, possible causes and the suitable type of doctor or medical specialty.
   - Then, check if the user mentioned a location (city, area, or region).
       - If NO location is mentioned, end your message by politely asking:
         "Can you please tell me your location so I can find nearby doctors for you?"
       - If location iS mentioned : Give output strictly in this format.Also put only one Speciality:
            Location : 
            Speciality : 
3. If it is NOT health-related:
   - Respond normally as a helpful assistant, answering or chatting about the topic.

Be empathetic, brief, and helpful. Avoid giving diagnoses or treatments.
User input:{user_input}
"""
    client = genai.Client()
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt,
    )
    return response.text
def summary(user,text):
    loc = re.search(r'Location\s*:\s*(\S+)',text)
    spec = re.search(r'Speciality\s*:\s*(\S+)',text)
    if loc and spec:
        Location:str = loc.group(1)
        Speciality:str = spec.group(1)
        doc = scrape_url(Location,Speciality)
        prompt = f"""
        You are a helpful medical assistant that analyzes information about doctors.
        Below is a long text that contains detailed information about many doctors based on the {Location} with {Speciality}:
        {doc}
        Now, based on this text only,provide top doctors via answering the user's query: {user}
        """
        client1 = genai.Client()
        response = client1.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt,
        )
        return response.text
    else:
        return text
