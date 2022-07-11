from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


strtbtn = [
    [
        InlineKeyboardButton(text='sᴜᴘᴘᴏʀᴛ', url="https://t.me/tamilbots"),
        InlineKeyboardButton(text='ᴅᴇᴠ', url="https://t.me/aboutmk")
    ],
    [        
        InlineKeyboardButton(text='ᴄᴏᴍᴍᴀɴᴅs', callback_data="help_")
    ]
]


homebtn = [
    [      
        InlineKeyboardButton(text='Go Home!', callback_data="home_")
    ]
]
