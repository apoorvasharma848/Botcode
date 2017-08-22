import os,time
import random
import json
import sys
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

						  
CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [['Sales', 'Claims'],
                  ['Profitability','GWP']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

				  
def cmdStart(bot, update):
	update.message.reply_text(
		'Hello {} \n What would you like to analysis'.format(update.message.from_user.first_name),reply_markup=markup)
	return TYPING_REPLY
	#update.message.reply_text('Hello World!',reply_markup=markup)
#	update.message.reply_text('Hello World!',reply_markup=markup)

def txtStart(bot, update,user_data):
        update.message.reply_text(
                'Hello {} {} \n What would you like to analysis'.format(update.message.from_user.first_name,update.message.from_user.last_name),reply_markup=markup)
        return CHOOSING

	
def txtHowRudoing(bot, update,user_data):
	update.message.reply_text(
		'I am good {} \n What would you like to analysis'.format(update.message.from_user.first_name),reply_markup=markup)
	return CHOOSING

def txtWhatsUp(bot, update,user_data):
	update.message.reply_text(
		'Nothing much {}, daily routine work thanks for asking. \n What would you like to analysis'.format(update.message.from_user.first_name),reply_markup=markup)
	return CHOOSING

def txtHowisEverything(bot, update,user_data):
	update.message.reply_text(
		'Good {}. \n What would you like to analysis'.format(update.message.from_user.first_name),reply_markup=markup)
	return CHOOSING
		
def hello(bot, update):
	update.message.reply_text(
		'Hello {}'.format(update.message.from_user.first_name))

def txthello(bot, update): 
    user = update.message.from_user
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return ConversationHandler.END
		

def regular_choice(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('Your %s? Yes, I would love to hear about that!' % text.lower())

    return TYPING_REPLY

def sale_choice(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('Yesterday sales was 10 Lakh.')

    return TYPING_REPLY

def claim_choice(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('Yesterday claims was 2 Lakh.')

    return TYPING_REPLY

def profitability_choice(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('Yesterday profitability was 5 Lakh.')

    return TYPING_REPLY

def gwp_choice(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('Yesterday GWP was 50 Lakh.')

    return TYPING_REPLY
	
def abusive_choice(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('Please, don\'t use abusive language.\nCalm down and ask a question, I will try to answer.')

    return TYPING_REPLY

updater = Updater('421977871:AAFoXpqKB4x5k0GeI-u7bpTdzNQUwq1OOes')

updater.dispatcher.add_handler(CommandHandler('start', cmdStart))

updater.dispatcher.add_handler(RegexHandler('^(?i)(hi(there| there|)|hey(man| man|)|start|hello(there| there|))$',
                                    txtStart,
                                    pass_user_data=True))
									
updater.dispatcher.add_handler(RegexHandler('^(?i)(How\'s it going( \?|\?|)|How are you doing( \?|\?|)|How are you( \?|\?|))$',
									txtHowRudoing,
									pass_user_data=True))

updater.dispatcher.add_handler(RegexHandler('^(?i)(What\'s up( \?|\?|)|What\'s new( \?|\?|)|What\'s going on( \?|\?|)|Whazz(up| up))$',
                                    txtWhatsUp,
                                    pass_user_data=True))

updater.dispatcher.add_handler(RegexHandler('^(?i)(How\'s everything( \?|\?|)|How are things( \?|\?|)|How\'s life( \?|\?|)|How is life( \?|\?|)|How\'s your day( \?|\?)|How\'s your day going( \?|\?|))$',
                                    txtHowisEverything,
                                    pass_user_data=True))

#Sales Handler
updater.dispatcher.add_handler(RegexHandler('^(?i)(Sales|What was my sale|What was my sale yesterday|What was my sale of last year|What was my sale of last month)$',
                                    sale_choice,
                                    pass_user_data=True))

#Claims Handler									
updater.dispatcher.add_handler(RegexHandler('^(?i)(Claims|What was my claims|What was my claims yesterday|What was my claims of last year|What was my claims of last month|What was my claims of %)$',
                                    claim_choice,
                                    pass_user_data=True))

updater.dispatcher.add_handler(RegexHandler('^(?i)(profitability|What was my profitability|What was my profitability yesterday|What was my profitability of last year|What was my profitability of last month|What was my profitability of %)$',
                                    profitability_choice,
                                    pass_user_data=True))

updater.dispatcher.add_handler(RegexHandler('^(?i)(GWP|What was my gwp|What was my gwp yesterday|What was my gwp of last year|What was my gwp of last month|What was my gwp of %)$',
                                    gwp_choice,
                                    pass_user_data=True))

#Abusive Handler									
updater.dispatcher.add_handler(RegexHandler('^(?i)(felch|cunt|Alabama hot pocket|skullfuck|cum dumpster|cock-juggling thunder cunt|rusty trombone|Cleveland Steamer|blumpkin|cum guzzling cock sucker|glass bottom boat|suck a fat baby\'s dick|meat flap|fuck hole|ol\' one-eye|hairy axe wound|bitchass mother fucker|analconda|beef curtain|fucking pussy|assmucus|cumdump|eat hair pie|cum chugger|mother fucker|cumjunkie|roast beef curtains|motherfucking|fuck|cum freak|motherfucker|50 yard cunt punt|clitty litter|blue waffle|fuck yo mama|fuck me in the ass with no Vaseline|fist fuck|schlong juice|sausage queen|lick my froth|jenkem|fuckmeat|have a face like a hatful of assholes|get some squish|eat a dick|bang (one\'s) box|meat drapes|baby arm|buggery|squeeze a steamer|bust a load|fucktoy|facialize|chota bags|cock snot|clit licker|slaptard|dick hole|butt fuck|cuntsicle|cunt-struck|shit fucker|GMILF|cuntbag|slich|gangbang|DVA|pussy fart|ass fuck|feedbag material|buckle buffer|cum guzzler|dick sucker|cunt hole|Fucking hell|cock pocket|cocksucker|cunt face|give Scully|anal impaler|cringe (one) out|hemped up|smoke a sausage|eat fur pie|snowball|nut butter|get brain|suck a dick|mumble pants|get (one\'s) redwings|man chowder|mick|Andhra Black Cobra|shum|blow me|bisnotch|Jesus motherfucking Christ|tittie Christ|ham flap|fuck for Ol\' Glory)$',									
                                    abusive_choice,
                                    pass_user_data=True))
updater.start_polling()
updater.idle()
