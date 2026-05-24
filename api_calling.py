from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io

#loading the envirnment variable 
load_dotenv()


my_api_key = os.getenv("GEMINI_API_KEY")

#initializing a client

client = genai.Client(api_key=my_api_key) # connecting client to gemini server through Api key



#note generator 

def note_generator(images):

    prompt = """Summarize the picture in note format at max 100 words,
     make sure to add necessary markdown to differentiate different section"""

    response =  client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents =[images,prompt]
    )

    return response.text

def audio_transcription(text):

    speech = gTTS(text,lang='en',slow = False)

    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer

def quiz_generator(images,difficulty):

    prompt = f"""Generate 5 quizs based on the picture with {difficulty} difficulty level, 
    make sure to add necessary markdown to differentiate different options. And also make sure to give the correct answer at the end of each quiz with necessary markdown"""

    response =  client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents =[images,prompt]
    )

    return response.text
