# copyright Β©οΈ 2021 nabilanavab
# !/usr/bin/python
# -*- coding: utf-8 -*-

#packages Used:
# pip install pyTelegramBotAPI
# pip install pillow
# pip install pyMuPdf
# pip install convertapi

import os
import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from PIL import Image
import shutil
from time import sleep
import fitz
import convertapi

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN, parse_mode="Markdown")

if os.getenv("CONVERT_API") != None:
	convertapi.api_secret = os.getenv("CONVERT_API")

@bot.message_handler(commands=["start"])
def strt(message):
	
	try:
		bot.send_chat_action(message.chat.id, "typing")
		strtMsg = f'''
Hey [{message.from_user.first_name}](tg://user?id={message.chat.id})..!! This bot will helps you to do many things with pdf's π₯³

Some of the main features are:
β `Convert images to PDF`
β `Convert PDF to images`
β `Convert files to pdf`




Join @RG_bots, for bot updates β₯οΈ


'''
		key = types.InlineKeyboardMarkup()
		key.add(types.InlineKeyboardButton("Source Code β€οΈ", callback_data="strtDevEdt"),types.InlineKeyboardButton("Explore More π₯³", callback_data="imgsToPdfEdit"))
		bot.send_message(message.chat.id, strtMsg, disable_web_page_preview=True, reply_markup=key)
	
		
		@bot.callback_query_handler(func=lambda call: call.data)
		def strtMsgEdt(call):
			edit = call.data
			
			if edit == 'strtDevEdt':
				
				try:
					aboutDev = f'''About Dev:

OwNeD By: @nabilanavab π
Update Channel: @nabiIanavab π

Lang Used: Pythonπ
[Source Code](https://github.com/nabilanavab/ilovepdf)

Join @nabiIanavab , if you β€ this 

[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)
'''
					key = types.InlineKeyboardMarkup()
					key.add(types.InlineKeyboardButton("π Home π‘", callback_data="back"))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = aboutDev, disable_web_page_preview=True, reply_markup=key)
				
				except:
					pass
				
			elif edit == 'imgsToPdfEdit':
				
				try:
					expMsg = f'''
Images to pdf :

		Just Send/forward me some images. When you are finished; use /generate to get your pdf..π

 β Image Sequence will be considered π€
 β For better quality pdfs(send images without Compression) π€§
 
 β `/cancel` - Delete's the current Queue π
 β `/id` - to get your telegram ID π€«
 
 β RENAME YOUR PDF:
 
	- By default, your telegram ID will be treated as your pdf name..π
	- `/generate fileName` - to change pdf name to fileNameπ€
	- `/generate name` - to get pdf with your telegram name

[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)'''
					key = types.InlineKeyboardMarkup()
					key.add(types.InlineKeyboardButton("π Home π‘", callback_data="back"),types.InlineKeyboardButton("PDF to images β‘οΈ", callback_data="pdfToImgsEdit"))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = expMsg, disable_web_page_preview=True, reply_markup=key)
				
				except:
					pass
				
			elif edit == 'pdfToImgsEdit':
				
				try:
					expMsg = f'''
PDF to images:

		Just Send/forward me a pdf file.

 β I will Convert it to images βοΈ
 β if Multiple pages in pdf(send as albums) π
 β Page numbers are sequentially ordered π¬
 β Send images faster than anyother bots π
 
1st bot on telegram wich send images without converting entire pdf to images

β οΈ Due to overload this bot will only convert files less than 10mb files..β οΈ

if you need to convert 10mb+ you can create your own bot.. Source code is mentioned in bio π

[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)'''
					key = types.InlineKeyboardMarkup()
					key.add(types.InlineKeyboardButton("π Imgs To Pdf", callback_data="imgsToPdfEdit"),types.InlineKeyboardButton("Home π‘", callback_data="back"),types.InlineKeyboardButton("file to Pdf β‘οΈ", callback_data="filsToPdfEdit"))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = expMsg, disable_web_page_preview=True, reply_markup=key)
				
				except:
					pass
				
			elif edit == 'filsToPdfEdit':
				
				try:
					expMsg = f'''
Files to PDF:

		Just Send/forward me a Supported file.. I will convert it to pdf and send it to you..π

β Supported files(.epub, .xps, .oxps, .cbz, .fb2) π
β No need to specify your telegram file extension π
β Only Images & ASCII characters Supported πͺ
β added 30+ new file formats that can be converted to pdf..
API LIMITS..π

β οΈ Due to overload this bot will only convert files less than 10mb files..β οΈ

if you need to convert 10mb+ you can create your own bot.. Source code is mentioned in bio π

[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)'''
					key = types.InlineKeyboardMarkup()
					key.add(types.InlineKeyboardButton("π PDF to imgs", callback_data="imgsToPdfEdit"),types.InlineKeyboardButton("Home π‘", callback_data="back"),types.InlineKeyboardButton("WARNING β οΈ", callback_data="warningEdit"))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = expMsg, disable_web_page_preview=True, reply_markup=key)
				
				except:
					pass
				
			elif edit == 'warningEdit':
				
				try:
					expMsg = f'''
WARNING MESSAGE β οΈ:

β This bot is completely free to use so please dont spam here π

β Please don't try to spread 18+ contents π

IF THERE IS ANY KIND OF REPORTING, BUGS, REQUESTS, AND SUGGESTIONS PLEASE CONTACT @nabilanavab

[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)
'''
					key = types.InlineKeyboardMarkup()
					key.add(types.InlineKeyboardButton("π WARNING β οΈ", callback_data="warningEdit"),types.InlineKeyboardButton("Home π‘", callback_data="back"))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = expMsg, disable_web_page_preview=True, reply_markup=key)
				
				except:
					pass
				
			elif edit == 'back':
				
				try:
					strtMsg = f'''
Hey..!! This bot will helps you to do many things with pdf's π₯³

Some of the main features are:
β `Convert images to PDF`
β `Convert PDF to images`
β `Convert files to pdf`

OwNeD By: @nabilanavab π
Update Channel: @nabiIanavab π€©

Join @nabiIanavab, if you β₯οΈ this bot

[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)
'''
					key = types.InlineKeyboardMarkup()
					key.add(types.InlineKeyboardButton("Source Code β€οΈ", callback_data="strtDevEdt"),types.InlineKeyboardButton("Explore More π₯³", callback_data="imgsToPdfEdit"))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = strtMsg, disable_web_page_preview=True, reply_markup=key)
				
				except:
					pass
				
	except:
		pass
	
@bot.message_handler(commands=["id"])
def UsrId(message):
	bot.send_chat_action(message.chat.id, "typing")
	bot.send_message(message.chat.id, f'Your ID - `{message.chat.id}`')
	

@bot.message_handler(commands=["help"])
def hlp(message):
	
	try:
		bot.send_chat_action(message.chat.id, "typing")
		hlpMsg = f'''
Help message:

 β Hit on /start to get the welcome message

 β Then Use `Explore more π₯³` button for more help ππ₯΄
 
[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)
'''
		key = types.InlineKeyboardMarkup()
		key.add(types.InlineKeyboardButton("Close β", callback_data="close"))
		bot.send_message(message.chat.id, hlpMsg, disable_web_page_preview=True, reply_markup=key)
		
		@bot.callback_query_handler(func=lambda call: call.data)
		def helpMsgClose(call):
			
			edit = call.data
			if edit == 'close':
				bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
				bot.delete_message(chat_id=call.message.chat.id, message_id=message.message_id)
		
	except:
		pass


@bot.message_handler(commands=["feedback"])
def feedback(message):
	bot.send_chat_action(message.chat.id, "typing")
	feedbackMsg = f'''
[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)
'''
	bot.send_message(message.chat.id, feedbackMsg, disable_web_page_preview=True)

PDF = {}
media = {}

@bot.message_handler(content_types=['photo'])
def pic(message):
	try:
		bot.send_chat_action(message.chat.id, "typing")
		picMsgId = bot.reply_to(message, "`Downloading your Image..β³`",)
		
		if not isinstance(PDF.get(message.chat.id), list):
			PDF[message.chat.id] = []
		file_info = bot.get_file(message.photo[-1].file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		
		try:
			os.makedirs(f'./{message.chat.id}/imgs')
		
		except:
			pass
		
		with open(f'./{message.chat.id}/imgs/{message.chat.id}.jpg', 'wb') as new_file:
			new_file.write(downloaded_file)
		img = Image.open(f'./{message.chat.id}/imgs/{message.chat.id}.jpg').convert("RGB")
		PDF[message.chat.id].append(img)
		bot.edit_message_text(chat_id= message.chat.id, text = f'''`Added {len(PDF[message.chat.id])} page/'s to your pdf..`π€

/generate to generate PDF π€''', message_id = picMsgId.message_id)
	
	except:
		pass

@bot.message_handler(content_types=['document'])
def fls(message):
	
	try:
		bot.send_chat_action(message.chat.id, "typing")
		isPdfOrImg = message.document.file_name
		fileSize = message.document.file_size
		
		fileNm, fileExt = os.path.splitext(isPdfOrImg)
		suprtedFile = ['.jpg','.jpeg','.png']
		suprtedPdfFile = ['.epub', '.xps', '.oxps', '.cbz', '.fb2']
		suprtedPdfFile2 = [".csv",".doc",".docx",".dot",".dotx",".log",".mpp",".mpt",".odt",".pot",".potx",".pps",".ppsx",".ppt",".pptx",".pub",".rtf",".txt",".vdx",".vsd",".vsdx",".vst",".vstx",".wpd",".wps",".wri",".xls",".xlsb",".xlsx",".xlt",".xltx",".xml"]
		
		if fileSize >= 10000000:
			
			try:
				bot.send_chat_action(message.chat.id, "typing")
				unSuprtd = bot.send_message(message.chat.id, f'''`please Send me a file less than 10mb Size`πͺ

Or Create pdf bot your Own.. link in bio''')
				sleep(15)
				bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
				bot.delete_message(chat_id = message.chat.id, message_id = unSuprtd.message_id)
			except:
				pass
			
		elif fileExt in suprtedFile:
		
			try:
				picMsgId = bot.reply_to(message, "`Downloading your Image..β³`",)
				
				if not isinstance(PDF.get(message.chat.id), list):
					PDF[message.chat.id] = []
				
				file_info = bot.get_file(message.document.file_id)
				downloaded_file = bot.download_file(file_info.file_path)
				
				os.makedirs(f'./{message.chat.id}/imgs')
				with open(f'./{message.chat.id}/imgs/{message.chat.id}{isPdfOrImg}', 'wb') as new_file:
					new_file.write(downloaded_file)
				
				img = Image.open(f'./{message.chat.id}/imgs/{message.chat.id}{isPdfOrImg}').convert("RGB")
				PDF[message.chat.id].append(img)
				bot.edit_message_text(chat_id= message.chat.id, text = f'''`Added {len(PDF[message.chat.id])} page/'s to your pdf..`π€

/generate to generate PDF π€''', message_id = picMsgId.message_id)
				
			except Exception as e:
				
				bot.edit_message_text(chat_id = message.chat.id, text = f'''Something went wrong..π

`ERROR: {e}`''', message_id = picMsgId.message_id)
				sleep(5)
				bot.delete_message(chat_id = message.chat.id, message_id = picMsgId.message_id)
				bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
			
		elif fileExt.lower() == '.pdf':
			
			try:
				bot.send_chat_action(message.chat.id, "typing")
				pdfMsgId = bot.reply_to(message, "`Downloading your pdf..β³`",)
				
				file_info = bot.get_file(message.document.file_id)
				downloaded_file = bot.download_file(file_info.file_path)
				
				os.mkdir(f'./{message.message_id}pdf{message.chat.id}')
				with open(f'./{message.message_id}pdf{message.chat.id}/pdf.pdf', 'wb') as new_file:
					new_file.write(downloaded_file)
				
				doc = fitz.open(f'./{message.message_id}pdf{message.chat.id}/pdf.pdf')
				zoom = 1
				mat = fitz.Matrix(zoom, zoom)
				noOfPages = doc.pageCount
				percNo = 0
				
				bot.edit_message_text(chat_id = message.chat.id, text = f'`Total pages: {noOfPages}`', message_id = pdfMsgId.message_id)
				totalPgList = list(range(0, noOfPages))
				
				for i in range(0, noOfPages, 10):
					pgList = totalPgList[i:i+10]
					os.mkdir(f'./{message.message_id}pdf{message.chat.id}/pgs')
					
					for pageNo in pgList:
						page = doc.loadPage(pageNo)
						pix = page.getPixmap(matrix = mat)
						cnvrtpg = pageNo + 1
						
						bot.edit_message_text(chat_id = message.chat.id, text = f'`Converted: {cnvrtpg}/{noOfPages} pgs`', message_id = pdfMsgId.message_id)
						
						with open(f'./{message.message_id}pdf{message.chat.id}/pgs/{pageNo}.jpg','wb') as f:
							pix.writePNG(f'./{message.message_id}pdf{message.chat.id}/pgs/{pageNo}.jpg')
						
					directory = f'./{message.message_id}pdf{message.chat.id}/pgs'
					imag = [os.path.join(directory, file) for file in os.listdir(directory)]
					imag.sort(key=os.path.getctime)
					
					percNo = percNo + len(imag)
					media[message.chat.id] = []
					LrgFileNo = 0
					percentage = (percNo*100)/noOfPages
					
					bot.edit_message_text(chat_id = message.chat.id, text = f'`Uploaded : {percentage:.2f}%`', message_id = pdfMsgId.message_id)
					
					for file in imag:
						if os.path.getsize(file) >= 1000000:
							
							picture = Image.open(file)
							CmpImg = f'./{message.message_id}pdf{message.chat.id}/pgs/temp{LrgFileNo}.jpeg'
							picture.save(CmpImg, "JPEG", optimize=True, quality=50) 
							
							LrgFileNo += 1
							if os.path.getsize(CmpImg) >= 1000000:
								continue
							
							else:
								fi = open(CmpImg, "rb")
								media[message.chat.id].append(InputMediaPhoto (fi))
								continue
						
						fi = open(file, "rb")
						media[message.chat.id].append(InputMediaPhoto (fi))
						
					shutil.rmtree(f'./{message.message_id}pdf{message.chat.id}/pgs')
					sleep(3)
					bot.send_chat_action(message.chat.id, "upload_photo")
					bot.send_media_group(message.chat.id, media[message.chat.id])
					del media[message.chat.id]
					
				bot.edit_message_text(chat_id = message.chat.id, text = f'`Uploading Completed.. π`', message_id = pdfMsgId.message_id)
				
				shutil.rmtree(f'./{message.message_id}pdf{message.chat.id}')
				
				sleep(10)
				bot.send_chat_action(message.chat.id, "typing")
				feedbackMsg = f'''
[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)
'''
				bot.send_message(message.chat.id, feedbackMsg, disable_web_page_preview=True)
				
				os.remove(f'./{message.message_id}pdf{message.chat.id}/pdf.pdf')
				bot.edit_message_text(chat_id = message.chat.id, text = f'`started Uploading..π`', message_id = pdfMsgId.message_id)
				
			except Exception as e:
				
				try:
					shutil.rmtree(f'./{message.message_id}pdf{message.chat.id}')
					
					bot.edit_message_text(chat_id = message.chat.id, text = f'''Something went wrong..π

`ERROR: {e}`''', message_id = pdfMsgId.message_id)
					
					sleep(15)
					bot.delete_message(chat_id = message.chat.id, message_id = pdfMsgId.message_id)
					bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
				except:
					pass
		
		elif fileExt.lower() in suprtedPdfFile:
			
			try:
				
				bot.send_chat_action(message.chat.id, "typing")
				pdfMsgId = bot.reply_to(message, "`Downloading your file..β³`",)
				
				file_info = bot.get_file(message.document.file_id)
				downloaded_file = bot.download_file(file_info.file_path)
				
				os.mkdir(f'./{message.message_id}pdf{message.chat.id}')
				with open(f'./{message.message_id}pdf{message.chat.id}/{isPdfOrImg}', 'wb') as new_file:
					new_file.write(downloaded_file)
				
				bot.edit_message_text(chat_id = message.chat.id, text = f'Creating pdf..π', message_id = pdfMsgId.message_id)
				Document = fitz.open(f'./{message.message_id}pdf{message.chat.id}/{isPdfOrImg}')
				b = Document.convert_to_pdf()
				pdf = fitz.open("pdf", b)
				pdf.save(f'./{message.message_id}pdf{message.chat.id}/{fileNm}.pdf', garbage=4, deflate=True)
				pdf.close()
				bot.edit_message_text(chat_id = message.chat.id, text = f'Started Uploading..π', message_id = pdfMsgId.message_id)
				
				sendfile = open(f'./{message.message_id}pdf{message.chat.id}/{fileNm}.pdf','rb')
				bot.send_document(message.chat.id, sendfile, caption = f'` Converted: {fileExt} to pdf`')
				bot.edit_message_text(chat_id = message.chat.id, text = f'Uploading Completed..β€οΈ', message_id = pdfMsgId.message_id)
				
				shutil.rmtree(f'./{message.message_id}pdf{message.chat.id}')

				sleep(10)
				bot.send_chat_action(message.chat.id, "typing")
				feedbackMsg = f'''
[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)
'''
				bot.send_message(message.chat.id, feedbackMsg, disable_web_page_preview=True)
		
			except Exception as e:
				
				try:
					shutil.rmtree(f'./{message.message_id}pdf{message.chat.id}')
					bot.edit_message_text(chat_id = message.chat.id, text = f'''Something went wrong..π

`ERROR: {e}`''', message_id = pdfMsgId.message_id)
					
					sleep(15)
					bot.delete_message(chat_id = message.chat.id, message_id = pdfMsgId.message_id)
					bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
				
				except:
					pass
		
		elif fileExt.lower() in suprtedPdfFile2:
			
			if os.getenv("CONVERT_API") == None:
				
				pdfMsgId = bot.reply_to(message, "`Owner Forgot to add ConvertAPI.. contact Owner π`",)
				sleep(15)
				bot.delete_message(chat_id = message.chat.id, message_id = pdfMsgId.message_id)
			
			else:
				
				try:
					
					bot.send_chat_action(message.chat.id, "typing")
					pdfMsgId = bot.reply_to(message, "`Downloading your file..β³`",)
					
					file_info = bot.get_file(message.document.file_id)
					downloaded_file = bot.download_file(file_info.file_path)
					
					os.mkdir(f'./{message.message_id}pdf{message.chat.id}')
					with open(f'./{message.message_id}pdf{message.chat.id}/{isPdfOrImg}', 'wb') as new_file:
						new_file.write(downloaded_file)
					
					bot.edit_message_text(chat_id = message.chat.id, text = f'Creating pdf..π', message_id = pdfMsgId.message_id)
					convertapi.convert('pdf', {'File': f'./{message.message_id}pdf{message.chat.id}/{isPdfOrImg}'}, from_format = fileExt[1:]).save_files(f'./{message.message_id}pdf{message.chat.id}/{fileNm}.pdf')
					bot.edit_message_text(chat_id = message.chat.id, text = f'Uploading Completed..β€οΈ', message_id = pdfMsgId.message_id)
					sendfile = open(f'./{message.message_id}pdf{message.chat.id}/{fileNm}.pdf','rb')
					bot.send_document(message.chat.id, sendfile, caption = f'` Converted: {fileExt} to pdf`')
					
					shutil.rmtree(f'./{message.message_id}pdf{message.chat.id}')
					
					sleep(10)
					bot.send_chat_action(message.chat.id, "typing")
					feedbackMsg = f'''
[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)
'''
					bot.send_message(message.chat.id, feedbackMsg, disable_web_page_preview=True)
				
				except Exception as e:
					
					try:
						shutil.rmtree(f'./{message.message_id}pdf{message.chat.id}')
						bot.edit_message_text(chat_id = message.chat.id, text = f'''ConvertAPI limit reaches.. contact Owner''', message_id = pdfMsgId.message_id)
						
					except:
						pass
		
		else:
			
			try:
				bot.send_chat_action(message.chat.id, "typing")
				unSuprtd = bot.send_message(message.chat.id, f'''`unsupported file..π`''')
				sleep(15)
				bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
				bot.delete_message(chat_id = message.chat.id, message_id = unSuprtd.message_id)
			except:
				pass
			
	except:
		pass
	
@bot.message_handler(commands=["cancel"])
def delQueue(message):
	
	try:
		bot.send_chat_action(message.chat.id, "typing")
		shutil.rmtree(f'./{message.chat.id}')
		bot.reply_to(message, "`Queue deleted Successfully..`π€§")
		
		try:
			del PDF[message.chat.id]
		except:
			pass
		
	except:
		bot.reply_to(message, "`No Queue founded`π²")
	
@bot.message_handler(commands=["generate"])
def generate(message):
	try:
		bot.send_chat_action(message.chat.id, "typing")
		newName = message.text.replace('/generate', '')
		images = PDF.get(message.chat.id)
		
		if isinstance(images, list):
			pgnmbr = len(PDF[message.chat.id])
			del PDF[message.chat.id]
		
		if not images:
			ntFnded = bot.reply_to(message, "`No image founded.!!`π")
			sleep(5)
			bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
			bot.delete_message(chat_id = message.chat.id, message_id = ntFnded.message_id)
			return
		
		gnrtMsgId = bot.send_message(message.chat.id, f'`Generating pdf..π`')
		
		if newName == f" name":
			fileName = f"{message.from_user.first_name}" + ".pdf"
		
		elif len(newName) > 0 and len(newName) <= 10:
			fileName = f"{newName}" + ".pdf"
		
		elif len(newName) > 10:
			fileName = f"{message.from_user.first_name}" + ".pdf"
		
		else:
			fileName = f"{message.chat.id}" + ".pdf"
		
		path = os.path.join(f'./{message.chat.id}', fileName)
		images[0].save(path, save_all=True, append_images=images[1:])
		bot.edit_message_text(chat_id= message.chat.id, text = f'`Uploading pdf...β€οΈ`', message_id = gnrtMsgId.message_id)
		bot.send_chat_action(message.chat.id, "upload_document")
		
		sendfile = open(path,'rb')
		bot.send_document(message.chat.id, sendfile, caption = f'file Name: `{fileName}`\n\n`Total pg\'s: {pgnmbr}`')
		bot.edit_message_text(chat_id= message.chat.id, text = f'`Successfully Uploaded π€«`', message_id = gnrtMsgId.message_id)
		
		shutil.rmtree(f'./{message.chat.id}')
		
		sleep(10)
		bot.send_chat_action(message.chat.id, "typing")
		feedbackMsg = f'''
[Write a feedback π](https://t.me/nabilanavabchannel/17?comment=10)
'''
		bot.send_message(message.chat.id, feedbackMsg, disable_web_page_preview=True)
	
	except:
		pass
	
@bot.message_handler(content_types=['text', 'audio', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact'])
def unSuprtd(message):
	
	try:
		bot.send_chat_action(message.chat.id, "typing")
		unSuprtd = bot.send_message(message.chat.id, f'`unsupported file.. please send me an image..π¬`')
		sleep(5)
		bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
		bot.delete_message(chat_id = message.chat.id, message_id = unSuprtd.message_id)
	
	except:
		pass
	
bot.polling()
