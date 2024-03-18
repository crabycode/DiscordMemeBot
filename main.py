import discord
import requests
import json
import random

def get_meme():
    response = requests.get("https://meme-api.com/gimme")
    json_data = json.loads(response.text)
    return json_data["url"]

def get_random_lofi():
    lofi_songs = [
        "https://youtu.be/4NRPEe7YnCQ?si=y0qy0XMwCdG0gXdw",
        "https://youtu.be/vJpo5dW3Ze4?si=LF5_YZDsgV2JZpPm",
        "https://youtu.be/-uxi6_5cFqw?si=iv8Qr2BEmIfpRIBV",
        "https://youtu.be/cqbomS1STFY?si=qEFzYdLB9m9KHpnH",
        "https://www.youtube.com/watch?v=o9m0sX2bjnw&ab_channel=TeamAnteiku"
    ]
    return random.choice(lofi_songs)

def roll_dice(min_num, max_num):
    return random.randint(min_num, max_num)

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$meme"):
            await message.channel.send(get_meme())

        if message.content.startswith("$lofi"):
            lofi_message = "Today's lofi suggestion: " + get_random_lofi()
            await message.channel.send(lofi_message)

        if message.content.startswith("$roll"):
            try:
                command, min_num, max_num = message.content.split()
                min_num = int(min_num)
                max_num = int(max_num)
            except ValueError:
                await message.channel.send("Invalid format. Please use $roll [min number] [max number]")
                return
            rolled_number = roll_dice(min_num, max_num)
            await message.channel.send(f"You rolled: {rolled_number}")

        if message.content.startswith("$nicecock"):
          await message.channel.send("Thank you!")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("MTE4MjI4MDI3MTg1MzI3MzEwOA.G0axLx.3b2OQsBhfHRjQ__PBs0IilXwsvnT0grQ7owYvo")