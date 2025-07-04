from groq import Groq
from json import load,dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key = GroqAPIKey)
messages = []
System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

SystemChatBot = [
    {"role" : "system" , "content" : System}
]
try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
except FileNotFoundError:
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)

def RealtimeInformation():
    current_data_time = datetime.datetime.now()
    day = current_data_time.strftime("%A")
    date = current_data_time.strftime("%d")
    month = current_data_time.strftime("%B")
    year = current_data_time.strftime("%Y")
    hour = current_data_time.strftime("%H")
    minute = current_data_time.strftime("%M")
    second = current_data_time.strftime("%S")

    data = f"PLease use this real-time information if needed,\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}"
    data += f"Time: {hour}\n Hour: {minute}\n Minute: {second}seconds.\n"
    return data

def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer

def ChatBot(Query):
    try:
        with open(r"Data\ChatLog.json", "r") as f:
            messages = load(f)
        messages.append({"role":"user", "content":f"{Query}"})

        completion = client.chat.completions.create(
        model="llama3-70b-8192", # Specify the AI model to use.
        messages = SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages, # Include system instructions, real-time info, a
        max_tokens=1024, # Limit the maximum tokens in the response.
        temperature=0.7, # Adjust response randomness (higher means more random).
        top_p=1, # Use nucleus sampling to control diversity.
        stream=True, # Enable streaming response.
        stop=None # Allow the model to determine when to stop.
        )
        Answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content: # Check if there's content in the current chunk.
                Answer += chunk.choices[0].delta.content # Append the content to the answer.
        Answer = Answer.replace("</s>", "") # Clean up any unwanted tokens from the response.
                 # Append the chatbot's response to the messages list.
        messages.append({"role": "assistant", "content": Answer})
                    # Save the updated chat log to the JSON file.
        with open(r"Data\ChatLog.json", "w") as f:
            dump(messages, f, indent=4)
            # Return the formatted response.
        return AnswerModifier(Answer=Answer)
    except Exception as e:
        print (f"Error: {e}")
        with open(r"Data\ChatLog.json", "w") as f:
            dump([], f, indent=4)
        return ChatBot(Query) # Retry the query after resetting the log.
# Main program entry point.
if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ") # Prompt the user for a question.
        print(ChatBot(user_input)) # Call the chatbot
