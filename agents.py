import os
import sys
import json
from dotenv import load_dotenv

# Add tools to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tools.search import search_linkedin_url
from tools.profile_fetcher import fetch_profile_data

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")

prompt_template = PromptTemplate(
    input_variables=["info"],
    template="""
You are a sarcastic and funny professional AI. Here's a LinkedIn profile summary in raw JSON:

{info}

Now, in 500 words, roast—uh, I mean, summarize—this person like a witty standup comedian. Be sarcastic but clever, funny but insightful. Highlight their skills, experience, and interesting quirks.
"""
)

chain = prompt_template | llm | StrOutputParser()

# Helper function to clean and truncate profile data
def clean_profile_data(profile_data, max_chars=4000):
    essential_fields = ['name', 'headline', 'location', 'summary', 'positions', 'skills']
    cleaned = {k: profile_data[k] for k in essential_fields if k in profile_data}
    
    cleaned_str = json.dumps(cleaned, indent=2)
    if len(cleaned_str) > max_chars:
        cleaned_str = cleaned_str[:max_chars] + "... [truncated]"
    return cleaned_str

def generate_sarcastic_profile_summary(name, keyword):
    linkedin_url = search_linkedin_url(name, keyword)
    if "linkedin.com/in" not in linkedin_url:
        return {"error": f"Could not find a valid LinkedIn profile: {linkedin_url}"}

    profile_data = fetch_profile_data(linkedin_url)
    if "error" in profile_data:
        return {"error": profile_data["error"]}

    cleaned_info = clean_profile_data(profile_data)
    profile_summary = chain.invoke({"info": cleaned_info})
    
    return {
        "summary": profile_summary,
        "url": linkedin_url
    }
