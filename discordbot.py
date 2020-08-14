# Botがログインしたら
@client.event
async def on_ready():
    msg = "やあ！TEST Botです．よろしくね！"
    await client.send_message(text_chat,msg)

# こんにちはメッセージ
@client.event
async def on_message(message):
    if message.content.startswith("こんにちは"):
        if client.user != message.author:
            msg = "こんにちは " + message.author.name + "さん！"
            await client.send_message(message.channel, msg)

# メンバのステータスが変更されたら
@client.event
async def on_member_update(before, after):
    if before.status != after.status:
        msg = after.display_name + " さんが " + str(after.status) + " になりました"
        await client.send_message(text_chat,msg)

client.run("DISCORD_BOT_TOKEN") # Botのトークン
