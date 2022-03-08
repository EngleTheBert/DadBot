import os
import discord
import requests
import json
my_secret = os.environ['bot_token']

client = discord.Client()

def get_joke():
  url = "https://dad-jokes.p.rapidapi.com/random/joke"
  headers = {
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
    'x-rapidapi-key': "565410c998msh6abc5d964119a12p114756jsnc00f0c1ba696"
    }
  response = requests.request("GET", url, headers=headers)
  json_data = json.loads(response.text)
  joke = json_data['body'][0]['setup'] + json_data['body'][0]['punchline']
  return(joke)
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']
  return(quote)
  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('How you doing sport!')
    
  if message.content.startswith('$joke'):
    joke = get_joke()
    await message.channel.send(joke)
    
  if message.content.startswith('$advice'):
    quote = get_quote()
    await message.channel.send(quote)
    
client.run(my_secret)
