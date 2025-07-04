from AppOpener import close,open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os


env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

# Define CSS classes for parsing specific elements in HTML content.
classes = ["zCubwf", "hgKElc", "LTK00 SY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
          "IZ6rdc", "05uR6d LTK00", "vlzY6d", "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb_gsrt", "sXLa0e",
          "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]
# Define a user-agent for making web requests.
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
# Initialize the Groq client with the API key.
client = Groq(api_key=GroqAPIKey)
# Predefined professional responses for user interactions.
professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with."
    "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
]
# List to store chatbot messages.
messages = []

# System message to provide context to the chatbot.
SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like letters,codes,application,notes,songs,poems etc"}]
# Function to perform a Google search.
def GoogleSearch(Topic):
    search (Topic) # Use pywhatkit's search function to perform a Google search.
    return True # Indicate success.
# Function to generate content using AI and save it to a file.
def Content (Topic):
    # Nested function to open a file in Notepad.
    def OpenNotepad (File):
        default_text_editor = 'notepad.exe' # Default text editor.
        subprocess.Popen([default_text_editor, File]) # Open the file in Notepad.

    def ContentWriterAI (prompt):
        messages.append({"role": "user", "content": f"{prompt}"}) # Add the user's prompt to messages.

        completion = client.chat.completions.create(
        model="llama3-70b-8192",# Specify the AI model.
        messages=SystemChatBot + messages, # Include system instructions and chat history.
        max_tokens=2048, # Limit the maximum tokens in the response.
        temperature=0.7, # Adjust response randomness.
        top_p=1, # Use nucleus sampling for response diversity.
        stream=True, # Enable streaming response.
        stop=None # Allow the model to determine stopping conditions.
        )
        Answer =""
    # Process streamed response chunks.
        for chunk in completion:
            if chunk.choices[0].delta.content: # Check for content in the current chunk.
                Answer += chunk.choices[0].delta.content # Append the content to the answer.
        Answer = Answer.replace("</s>", "") # Remove unwanted tokens from the response.
        messages.append({"role": "assistant", "content": Answer}) # Add the AI's response to messages
        return Answer
    Topic: str = Topic.replace("Content", "") # Remove "Content" from the topic.
    ContentByAI = ContentWriterAI(Topic) # Generate content using AI.
# Save the generated content to a text file.
    with open(rf"Data\{Topic.lower().replace(' ','')}.txt", "w", encoding="utf-8") as file:
        file.write(ContentByAI) # Write the content to the file.
        file.close()
    OpenNotepad (rf"Data\{Topic.lower().replace(' ','')}.txt") # Open the file in Notepad.
    return True # Indicate success.

# Function to search for a topic on YouTube.
def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}" # Construct the YouTube search
    webbrowser.open(Url4Search) # Open the search URL in a web browser.
    return True # Indicate success.
# Function to play a video on YouTube.
def PlayYoutube(query):
    playonyt(query) # Use pywhatkit's playonyt function to play the video.
    return True # Indicate success.


def OpenApp(app, sess=requests.session()):
    try:
        appopen(app, match_closest=True, output=True, throw_error=True) # Attempt to open the app.
        return True # Indicate success.
    except:
        # Nested function to extract links from HTML content.
        def extract_links(html):
            if html is None:
                return [ ]
            soup = BeautifulSoup(html, 'html.parser') # Parse the HTML content.
            links = soup.find_all('a', {'jsname': 'UWckNb'}) # Find relevant links.
            return [link.get('href') for link in links] # Return the links.
        # Nested function to perform a Google search and retrieve HTML.
        def search_google(query):
            url = f"https://www.google.com/search?q={query}" # Construct th
            headers = {"User-Agent": useragent} # Use the predefined user-agent.
            response = sess.get(url, headers=headers) # Perform the GET request.
            if response.status_code == 200:
                return response.text # Return the HTML content.
            else:
                print("Failed to retrieve search results.") # Print an error message.
            return None
        html = search_google(app) # Perform the Google search.
        if html:
            link = extract_links(html)[0] # Extract the first link from the search results.
            webopen(link) # Open the link in a web browser.
        return True # Indicate success.
    
def CloseApp(app):
    if "chrome" in app:
        pass
    else:
        try:
            close(app, match_closest=True,output=True,throw_error=True)
            return True
        except:
            return False
        
def System(command):
    def mute():
        keyboard.press_and_release("volume mute")
    def unmute():
        keyboard.press_and_release("volume mute")
    def volume_up():
        keyboard.press_and_release("volume up")
    def volume_down():
        keyboard.press_and_release("volume down")

    if command == "mute":
        mute()
    elif command == "unmute":
        unmute()
    elif command == "volume up":
        volume_up()
    elif command == "volume down":
        volume_down()
    return True

async def TranslateAndeExecute(commands: list[str]):
    funcs = []
    for command in commands:
        if command.startswith("open "):
            if "open it" in command:
                pass
            if "open file" == command:
                pass
            else:
                fun = asyncio.to_thread(OpenApp, command.removeprefix("open "))
                funcs.append(fun)
        elif command.startswith("general"):
            pass
        elif command.startswith("realtime"):
            pass
        elif command.startswith("close"):
            fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
            funcs.append(fun)
        elif command.startswith("play "):
            fun = asyncio.to_thread(PlayYoutube,command.removeprefix("play "))
            funcs.append(fun)
        elif command.startswith("content "):
            fun = asyncio.to_thread(Content,command.removeprefix("content "))
            funcs.append(fun)
        elif command.startswith("google search "):
            fun = asyncio.to_thread(GoogleSearch,command.removeprefix("google search "))
            funcs.append(fun)
        elif command.startswith("youtube search "):
            fun = asyncio.to_thread(YouTubeSearch,command.removeprefix("youtube search "))
            funcs.append(fun)
        elif command.startswith("system "):
            fun = asyncio.to_thread(System,command.removeprefix("system "))
            funcs.append(fun)
        else:
            print(f"No function found for {command}")
    results = await asyncio.gather(*funcs)

    for result in results:
        if isinstance(result,str):
            yield result
        else:
            yield result

async def Automation(commands: list[str]):
    async for result in TranslateAndeExecute(commands):
        pass
    return True



        





