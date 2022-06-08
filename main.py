import discord
import os

# Create new discord client agent
chary_client = discord.Client()
# store API token
my_secret = os.environ['token']

target_string = 'chary'
target_tag = 'stay'
thank = "I would like to thank you for your participation."


def remove_punctuation(message):
    punctuation = ".?!,;"  # punctuation dictionary
    cleared = message  # copy message to working variable
    for char in cleared:
        if char in punctuation:
            # replace punctuation with spaces
            cleared = cleared.replace(char, '')
    return cleared

# Verify Bot is connected and ready
@chary_client.event
async def on_ready():
    print("Mr. Chary is online and here to stay")

# When a message is posted in any channel
@chary_client.event
async def on_message(message):
    # remove punctuation, capital letter, and trailing whitespace
    clear_post = remove_punctuation(message.content).strip().lower()

    # ignore messages from itself
    if message.author == chary_client.user:
        return

    elif "participated" in clear_post:
        print(f"{message.author}: {message.content[:70]}")
        print(f"RESPONSE-> {thank}")
        await message.channel.send(thank)
      
    # the post matches the sample string
    elif target_string in clear_post:
        print(f"{message.author}: {message.content[:70]}")
        if target_tag in clear_post:
            # respond
            print(f"RESPONSE->I am here to stay")
            await message.channel.send('I am here to stay')
        else:
            print(f"RESPONSE->I am here")
            await message.channel.send('I am here')
          
# token confirmation to communicate with Discord API
chary_client.run(my_secret)
