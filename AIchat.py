from characterai import PyCAI
from googletrans import Translator

client = PyCAI("...")

char = "..."

chat = client.chat.get_chat(char)

participants = chat['participants']

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants[1]['user']['username']

def callAI(message):
    x = translate_text(message,"en")
    print(message,x)

    data = client.chat.send_message(chat['external_id'], tgt, x)
    text = data['replies'][0]['text']

    message_result = translate_text(text,"th")
    return message_result
