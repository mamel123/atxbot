import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("ATX SHOP 1호점")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("환영 합니다 ATX SHOP입니다.")

    if message.content.startswith("하세요d"):
        await message.channel.send("환영 합니다 ATX SHOP입니다.")

    if message.content.startswith("문의"):
        await message.channel.send("문의는 kr.coca#9454")

    if message.content.startswith("관리자"):
        await message.channel.send("관리자 : kr.coca#9454")

    if message.content.startswith("ㅎㅇ"):
        await message.channel.send("환영 합니다 ATX SHOP입니다.")



client.run("NjMwMzUzNTA5MDYxMDk5NTMx.XZnMHA.IXN6V6O0tdGyhU1v2zVAB4K0VJg")
