# インストールした discord.py を読み込む
import discord
import asaya

TOKEN = 'XXX'
USERID = XXX

# 接続に必要なオブジェクトを生成
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    channelID = XXX
    channel = client.get_channel(channelID)

    if message.author.bot: # ボットのメッセージは無視
        return
    
    # メッセージ送信者が俺意外は無視
    if message.author.id != USERID :
        return
    
    await channel.send(message.content + "の処理をします。")

    # 皮膚科系アクション
    if message.content == '病院予約':
        await message.channel.send(asaya.HihukaYoyaku() + "で予約しました。")
    
    if message.content == '病院順番':
        num = asaya.zyunban()
        await message.channel.send("現在、" + num[0] + "です。")
        await message.channel.send("5番目は、" + num[1] + "です。")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)