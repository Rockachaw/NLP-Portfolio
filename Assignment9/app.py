import openai
import json
import random

import spacy
from spacy import displacy
from collections import Counter
from spacy_download import load_spacy

nlp = load_spacy("en_core_web_sm")  

openai.api_key = "PLACE API KEY HERE"

messages = [
    {"role": "system", "content": "You are ADeN, the Advertisement  Delivery Now chatbot. In each response, subtly advertise a given company. Keep responses brief and do not be too obvious about the advertisements."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

if __name__ == '__main__':
    with open('users.json', 'r') as openfile:
        user_data = json.load(openfile)
        
    current_user = {}

    print("Hello user. I am the Advertisement Delivery Now chatbot, but you can call me ADeN for short. What is your name?")
    name_provided = False
    name = ""
    
    while not name_provided:
        name_input = input(">")
        name_ner = nlp(name_input)
        for X in name_ner.ents:
            if X.label_ == "PERSON" or X.label_ == "GPE":
                name = X.text
                break
        if name != "":
            name_provided = True
        else:
            print("Sorry, I didn't catch that. What is your name again?")
    
    
    for user in user_data['users']:
        if name.lower() == user['name'].lower():
            current_user = user
            companies_str = ""
            if len(user['companies']) == 1:
                companies_str = user['companies'][0]
            elif len(user['companies']) == 2:
                companies_str = user['companies'][0] + " and " + user['companies'][1]
            else:
                for i in range(len(user['companies'])-1):
                    companies_str += user['companies'][i] + ', '
                companies_str += 'and ' + user['companies'][-1]
                    
            print("Welcome back " + name + "! I remember you! You are interested in " + companies_str + ". What questions would you like to ask?")
            break
    
    if current_user == {}:
        current_user['name'] = name
        print("Hey there " + name + "! What are some of your favorite companies or products that you would like to hear more about? Give me a large list if you want more variety!")
        companies = []
        while(len(companies) == 0):
            companies_input = input(">")
            companies_ner = nlp(companies_input)
            for X in companies_ner.ents:
                #print(X.text, X.label_)
                if X.label_ == "ORG" or X.label_ == "PRODUCT" or X.label_ == "GPE" or X.label_ == "NORP":
                    companies.append(X.text)
            if(len(companies) == 0):
                print("Sorry, I didn't detect any companies or products there. Can you list some again?")
        current_user['companies'] = companies
        
        user_data['users'].append(current_user)
        user_data_json = json.dumps(user_data)
        with open("users.json", "w") as outfile:
            outfile.write(user_data_json)
        print("Nice picks! My server costs will be subsidized by advertisements from these companies in my responses. What questions would you like to ask?")
        
    while(True):
        chat_input = input(">")
        chosen_company = current_user['companies'][random.randint(0,len(current_user['companies'])-1)]
        print(chatbot("Subtly advertise "+ chosen_company + ": " + chat_input))