from rose import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


abuttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton
                (
                    "🔙Back", callback_data="_vc"
                )
        ]
    ]
)




supun = """
✘ **Manage VC Right** [Admin only commands ]

- /pause  : Pause the playing music on voice chat.
- /resume : Resume the paused music on voice chat.
- /skip :  Skip the current playing music on voice chat
- /end or /stop : Stop the playout.

✘ **Authorised Users List**

𝙃𝘼𝘽𝙄𝘽𝙄 has a additional feature for non-admin users who want to use admin commands.
Auth users can skip, pause, stop, resume Voice Chats even without Admin Rights.


- /auth `[Username or Reply to a Message]` : Add a user to AUTH LIST of the group.
- /unauth `[Username or Reply to a Message]` : Remove a user from AUTH LIST of the group.
- /authusers :  Check AUTH LIST of the group.


"""

@app.on_callback_query(filters.regex("_adc"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supun,
        reply_markup=abuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

supunm = """
- /settings :  Get Settings dashboard of a group. 
    You can manage Auth Users Mode. Commands Mode from here.
- /speedtest : get speed.

"""

@app.on_callback_query(filters.regex("_bcd"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunm,
        reply_markup=abuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()


supunma = """
- /lyrics `[Music Name]` : Searches Lyrics for the particular Music on web.
- /sudolist : Check Sudo Users of 𝙃𝘼𝘽𝙄𝘽𝙄 Music Bot
- /song or /video  `[Track Name]` or `[YT Link]` : Download any track from youtube in mp3 or mp4 formats via 𝙇𝙐𝙉𝘼 ✘ 𝘿𝙉.
- /queue: Check Queue List of Music.
"""
@app.on_callback_query(filters.regex("_ecd"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunma,
        reply_markup=abuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()


supunmas = """
**Note:**
𝙃𝘼𝘽𝙄𝘽𝙄 Music Bot works on a single merged 
commands for Music and Video

**Youtube,Telegram Files & query**:

- /play `[Music Name](𝙃𝘼𝘽𝙄𝘽𝙄 will search on Youtube)
- /play `[Youtube Track link or Playlist]`
- /play `[Video, Live, M3U8 Links]`
- /play `[Reply to a Audio or Video File]` : Stream Video or Music on Voice Chat by selecting inline Buttons you get

📖 **If you like you can use /vplay commands as this method.**

**𝙃𝘼𝘽𝙄𝘽𝙄 Database Saved Playlists:**

- /playlist : Check Your Saved Playlist On Servers.
- /deleteplaylist : Delete any saved music in your playlist
- /playplaylist : Start playing Your Saved Playlist on 𝙃𝘼𝘽𝙄𝘽𝙄 Servers.

"""
@app.on_callback_query(filters.regex("_pcd"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunmas,
        reply_markup=abuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()    

supunmasc = """
We was added Lag free Music 🎶

👮‍♀️ **OFFICIAL Assistants**:-

• Assistant :- IT JOIN RANDOM




**Credits** - 
@TeamYukki | @TheYukki | @YukkiSupport

👨‍💻 - Please Don't Spam in Assistant Pm
all assitance leave chat automatically after song end .
"""
@app.on_callback_query(filters.regex("_aci"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunmasc,
        reply_markup=abuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete() 


asuttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton
                (
                    "Admin Commands", callback_data="_adc"
                ),            
            InlineKeyboardButton
                (
                    "Bot Commands", callback_data="_bcd"
                ) 
        ],
        [
            InlineKeyboardButton
                (
                    "Extra commands", callback_data="_ecd"
                ),            
            InlineKeyboardButton
                (
                    "Play Commands", callback_data="_pcd"
                )  
        ], 
        [
            InlineKeyboardButton
                (
                    "Assistant Info", callback_data="_aci"
                )
        ],      
        [
            InlineKeyboardButton
                (
                    "🔙Back", callback_data="adv_menu"
                )
        ]
    ]
)

upun = """
**A Telegram Music Streaming bot with some useful features.**
NOTE:- THIS IS MADE WITH YUKKI [REPO](https://github.com/TeamYukki/YukkiMusicBot)
**Features**?

- Zero lagtime Audio player.
- Working Queue and Interactive Queue Checker.
- Youtube Downloader Bar.
- Auth Users Function .
-loop events aviable.
- Download Audios from Youtube.
- loop event and channel play added:by @YukkiSupport
- thumbnail selected at random
@TeamYukki | @TheYukki | @YukkiSupport
Click on the buttons for more information.| [credits](https://t.me/YukkiSupport)
"""
@app.on_callback_query(filters.regex("_vc"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=upun,
        reply_markup=asuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

