import discord

# Create new discord client agent
chary_client = discord.Client()
# store API token
token = '[removed]'
target_string = ' chary'
target_tag = 'stay'

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
    print("Mr. Chary is here to stay")

# When a message is posted in any channel
@chary_client.event
async def on_message(message):
    # remove punctuation, capital letter, and trailing whitespace
    clear_post = remove_punctuation(message.content).strip().lower()

    # ignore messages from itself
    if message.author == chary_client.user:
        return

    # the post matches the sample string
    elif target_string in clear_post:
        if target_tag in clear_post:
            # respond
            await message.channel.send('I am here to stay')
        else:
            await message.channel.send('I am here')

# token confirmation to communicate with Discord API
chary_client.run(token)
