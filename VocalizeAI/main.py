import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    
    engine.say(text)
    engine.runAndWait()
if __name__ == '__main__':
    print("Welcome to VocalizeAI!")
    while True:
        text = input("Enter whatever you want me to speak (type 'exit' to stop): ")
        
        if text.lower() == "exit":
            break
        text_to_speech(text)
