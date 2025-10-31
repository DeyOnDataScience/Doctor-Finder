# Health Assistant Project
=====================================

## Project Description
The Health Assistant Project is a Python-based application designed to assist users with health-related queries. It uses natural language processing (NLP) to identify key symptoms, possible causes, and suitable medical specialties. The project also includes a web scraping feature to find nearby doctors based on the user's location and preferred specialty.

## Installation Steps
To install and run the Health Assistant Project, follow these steps:

1. **Clone the repository**: Clone the Health Assistant Project repository using Git.
2. **Install dependencies**: Install the required dependencies by running `pip install -r requirements.txt` in your terminal.
3. **Set up environment variables**: Create a `.env` file and add your Google API key as `GOOGLE_API_KEY`.
4. **Install the Google Client Library**: Install the Google Client Library by running `pip install google-api-python-client`.
5. **Install the BeautifulSoup and requests libraries**: Install the BeautifulSoup and requests libraries by running `pip install beautifulsoup4 requests`.

## Usage Examples
To use the Health Assistant Project, simply run the `main.py` file and enter your query when prompted.

```bash
python main.py
```

Example use case:

* Enter a health-related query: "I have a headache and fever and i am from Delhi."
* The application will respond with the identified location and specialty, if applicable.
* If no location is mentioned, the application will ask for the user's location to find nearby doctors.

## Features
The Health Assistant Project includes the following features:

* **Natural Language Processing (NLP)**: Uses the Google Client Library to analyze user queries and identify key symptoms, possible causes, and suitable medical specialties.
* **Web Scraping**: Uses the BeautifulSoup and requests libraries to scrape doctor information from a website based on the user's location and preferred specialty.
* **Location-based search**: Finds nearby doctors based on the user's location and preferred specialty.

## Folder Structure
The project folder structure is as follows:
```markdown
health-assistant/
|---- workflow.py
|---- main.py
|---- scrape.py
|---- requirements.txt
|---- .env
|---- README.md
```