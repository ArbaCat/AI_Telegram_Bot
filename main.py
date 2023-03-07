import openai                                                 #Import's from API's
from aiogram import Bot, types                                #
from aiogram.dispatcher import Dispatcher                     #
from aiogram.utils import executor                            #

token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'                        #telegram bot key
openai.api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'            #open ai key 


bot = Bot(token) #connect variable with bot 
dp = Dispatcher(bot) #connect dispatcher with bot 



@dp.message_handler()                                         #decorator which I'm yousing to call function every time when message comes 
async def send(message: types.Message):                       #function for generating response from OpenAI API "gpt-3.5-turbo" model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",                                #model which we are using
        temperature=0.9,                                      #"creativity" level                                   
        max_tokens=1000,                                      #number of maximum "tokens"(words, subwords)
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=None,
        messages=[{"role": "user", "content": message.text}]  #here I create list with two parameter dictionary inside     
    )
    await message.answer(response['choices'][0]['message'].content)  #response filttration. I tried to use ['text'], but is doesn't work, only with Eng text.
                                                                      #My friend tell that it's becouse of JSON, and I need to use ['message'].content

executor.start_polling(dp, skip_updates=True)                         #this line of code sets the bot in motion
                                                                      #and makes it ready to receive and respond to incoming messages from Telegram
