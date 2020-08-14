import discord
import random
from datetime import datetime

client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん'

@client.event
async def on_message(message):
    if message.author.id == 159985870458322944: # MEE6からのメッセージかどうかを判別
        if message.content.startswith("!levelup"):
            await message.delete() # メッセージを消去


            level = int(message.content.split()[-2]) # メッセージを分解
            t_name = message.content.split()[-1] # メッセージを分解
            target = discord.utils.get(message.server.members, mention=t_name) # レベルアップしたユーザーのIDを取得

            up=discord.Color(random.randint(0, 0xFFFFFF)) # 帯の色をランダムに決めるコード

            embed=discord.Embed(title="レベルアップ通知", description=f"{t_name}さん、が{level}レべになりました。", color=up) # レベルアップメッセージ
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(target))
            embed.set_footer(text="レベルアップ時刻:" + datetime.now().strftime(" %Y/%m/%d %H:%M:%S"))
            await message.channel.send(embed=embed)

            if level == 1: # レベル1になった時の処理
                levelrole1 = discord.utils.get(message.server.roles, name="チンカス")
                await target.add_roles(levelrole1)
                
            elif level == 5: # レベル5になった時の処理
                levelrole1 = discord.utils.get(message.server.roles, name="チンカス")
                levelrole5 = discord.utils.get(message.server.roles, name="初珍者")
                await target.add_roles(levelrole5)
                await target.remove_roles(levelrole1)
                
            elif level == 6: # レベル6になった時の処理
                levelrole5 = discord.utils.get(message.server.roles, name="初珍者")
                levelrole6 = discord.utils.get(message.server.roles, name="珍参者")
                await target.add_roles(levelrole6)
                await target.remove_roles(levelrole5)

            elif level == 7: # レベル7になった時の処理
                levelrole6 = discord.utils.get(message.server.roles, name="珍参者")
                levelrole7 = discord.utils.get(message.server.roles, name="珍遊詩人")
                await target.add_roles(levelrole7)
                await target.remove_roles(levelrole6)
                
           elif level == 8: # レベル8になった時の処理
                levelrole1 = discord.utils.get(message.server.roles, name="チンカス")
                levelrole8 = discord.utils.get(message.server.roles, name="珍者")
                await target.add_roles(levelrole8)
                await target.remove_roles(levelrole1)

client.run("NzQzNDE3ODgxNzEwMTY2MDk3.XzUX2w.-P6BKZkVVqTPV3ZrqBkwlwPs-sc") # Botのトークン
