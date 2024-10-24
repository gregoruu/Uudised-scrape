import discord
import responses

async def saada_sonum(sonum, kasutaja_sonum):
    try:
        response = responses.vastus(kasutaja_sonum)
        await sonum.channel.send(response)

    except Exception as i:
        print(i)
def run_discord_bot():
    token="MTI5OTA5NTcyOTQyNzQ1MTk2OA.Gn4eCJ.UHvbUZb2lqw02KseKGUd2fAs8Yr1aqHVXTcQXI"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f"{client.user} töötab")
    
    @client.event
    async def on_message(sonum):
        if sonum.author==client.user:
            return 
        nimi=str(sonum.author)
        kiri=str(sonum.content)
        print(f"{kiri} sonumi saatis {nimi}")
        await saada_sonum(sonum, kiri)
    client.run(token)