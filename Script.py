class script(object):
    START_TXT = """🔥𝓗𝓲 𝓣𝓱𝓮𝓻𝓮 {}

♨️𝗔𝗱𝗱 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝗻𝗱 𝗚𝗶𝘃𝗲 𝗔𝗱𝗺𝗶𝗻. 𝗙𝗿𝗼𝗺 𝗧𝗵𝗮𝘁 𝗧𝗶𝗺𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗪𝗶𝗹𝗹 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗠𝗼𝘃𝗶𝗲𝘀 𝗔𝗻𝗱 𝗦𝗲𝗿𝗶𝗲𝘀 𝗙𝗼𝗿 𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝘀. 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗛𝗮𝘃𝗲 𝗧𝗵𝗲 𝗟𝗮𝗿𝗴𝗲𝘀𝘁 𝗠𝗼𝘃𝗶𝗲 & 𝗦𝗲𝗿𝗶𝗲𝘀 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗜𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺😜

🤖By Using Our Service You Must Agree To Our Privacy Policy 👀"""
    HELP_TXT = """🙋‍♂️𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂🚀"""
    ABOUT_TXT = """<b>🙋‍♂️ I Aᴍ </b>: <a href=http://t.me/JellyBeanAutoFilterRobot>𝗝𝗲𝗹𝗹𝘆 𝗕𝗲𝗮𝗻 🍯</a>
<b>👨‍💻 Cʀᴇᴀᴛᴏʀ</b>: <a href=https://github.com/KisaraPesanjithPerera>★彡ᕲᗩᖇᖶᕼ ᐺᗩᕲᘿᖇ彡★</a>
<b>🌶 Pᴏᴡᴇʀᴇᴅ By</b>: @AnonymousBotsInfinity

<b>◇───────────────◇</b>

🎲 <b>Sᴇʀᴠᴇʀ</b> : Hᴇʀᴏᴋᴜ
🧩 <b>Lᴀɴɢᴜᴀɢᴇ</b> : Pyᴛʜᴏɴ
📚 <b>Lɪʙʀᴀʀy</b> : Pyʀᴏɢʀᴀᴍ
📝 <b>Bᴜɪʟᴅ Sᴛᴀᴛᴜꜱ</b> : V1.0.1 [ Bᴇᴛᴀ ]"""
    MANUELFILTER_TXT = """Help: <b>Filters🧿</b>

- Filter is the feature were users can set automated replies for a particular keyword and Jelly Bean 🍯 will respond whenever a keyword is found the message🍀

<b>NOTE📝:</b>
1. Jelly Bean 🍯 should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands & Usage🚀</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons🧿</b>

- Jelly Bean 🍯 supports both url and alert inline buttons🍀

<b>NOTE📝:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Jelly Bean 🍯 supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>📌URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/AnonymousBotsInfinity)</code>

<b>📌Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter🧿</b>

<b>NOTE📝:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
📂I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections🧿</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE📝:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage🚀</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules🧿</b>

<b>NOTE📝:</b>
These are the extra features of Jelly Bean🍯

<b>Commands and Usage🚀</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods🧿</b>

<b>NOTE📝:</b>
This module only works for my admins🍀

<b>Commands and Usage🚀</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>My Sᴛᴀᴛᴜꜱ</b> 🤗
    
📂 <b>Tᴏᴛᴀʟ Mᴏᴠɪᴇ Sᴀᴠᴇᴅ</b> : <code>{}</code>
👤 <b>Tᴏᴛᴀʟ Uꜱᴇʀꜱ</b> : <code>{}</code>
📝 <b>Tᴏᴛᴀʟ Gʀᴏᴜᴩꜱ</b> : <code>{}</code>
🔰 <b>Uꜱᴇᴅ Sᴩᴀᴄᴇ</b> : <code>{}</code> MB
🗃️ <b>Fʀᴇᴇ Sᴩᴀᴄᴇ</b> : <code>{}</code> MB

<b>◇───────────────◇</b>

<b>My Sᴇʀᴠᴇʀ Sᴛᴀᴛᴜꜱ</b> 🍀

<b>💻 Cᴩᴜ Uꜱᴀɢᴇ</b> : {}%
<b>☄️ Rᴀᴍ Uꜱᴀɢᴇ</b> : {}%"""

    CREDITS = """<b>Credit 🌟</b>
    
𝗝𝗲𝗹𝗹𝘆 𝗕𝗲𝗮𝗻 🍯 Is A Auto Filter Bot As Well As One Bot In Telegram That Can Download Movies & Series Inline📝

- <b>Developer 👨‍💻</b>
<b>★彡ᕲᗩᖇᖶᕼ ᐺᗩᕲᘿᖇ彡★</b>

- <b>Thanks To 👑</b>
<b>🏷️ Dan</b> For His Awsome Libary
<b>🏷️ Mahesh</b> For His Awesome Media-Search-bot
<b>🏷️ Trojanz</b> for Their Awesome Unlimited Filter Bot And AutoFilterBoT

⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- @AnonymousBotsInfinity"""
    LOG_TEXT_G = """#NewGroup
🍀Group = {}(<code>{}</code>)
🙋‍♂️Total Members = <code>{}</code>
🌺Added By - {}
"""
    LOG_TEXT_P = """#NewUser
⚙️ID - <code>{}</code>
🙋‍♂️Name - {}
"""
