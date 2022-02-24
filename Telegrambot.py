import requests, time, json
from dict_helper import dict_object as object

class request: #as request
	def sendMessage(chat_id, text, **args):
		return ("sendMessage",{"chat_id":chat_id,"text":text, **args})
	def sendVoice(chat_id,voice):
		return ("sendVoice",{"chat_id":chat_id,"voice":voice})

class response: #as response
	def __getattr__(self, attr):
		method = getattr(request, attr)
		def temp(*args, **kwargs):
			response = method(*args, **kwargs)
			response[1].update({"method":response[0]})
			return response[1]
		return temp

response = response()

class bot:
	"""docstring for Telegrambot"""
	def __init__(self, token):
		self._token = token

	# def method(self, method, data):
	# 	return object(requests.post('https://api.telegram.org/bot' + self._token + '/' + method,data=data).json())

	def method(self, data):
		method, args = data
		#print ('https://api.telegram.org/bot' + self._token + '/' + method, args)
		return object(requests.post('https://api.telegram.org/bot' + self._token + '/' + method, json=args).json())

	def long_polling(self):
		offset = 0
		timeout = 5
		# while offset==0:
		# 	for update in self.method(("getUpdates",{"timeout":timeout})).result:
		# 		yield update
		# 		offset = update.update_id + 1

		while True:
			for update in self.method(("getUpdates",{"offset":offset, "timeout":timeout})).result:
				yield update
				offset = update.update_id + 1


	def sendMessage(self,chat_id,text):
		return self.method(request.sendMessage(chat_id,text))

	#@staticmethod
	def replyMarkup(keyboard):
		return {"reply_markup":keyboard}
		
#from bot import G
#class bot:
	# def getFile(self,i):
	# 	G.dbc.execute("select * from files where id=?",(i,))
	# 	temp = G.dbc.fetchone()

	# 	if time.time() - temp["time"]>3600:
	# 		temp.file_path = self._renewFile(i,True)

	# 	return self._fetchFile(temp.file_path)

	# def _renewFile(self,i,row_exists=False):
	# 	temp = self.method("getFile",{"id":i})
	# 	if row_exists: G.dbc.execute("update files(path,time) values(?,?) where id=?",(temp.file_path,time.time(),i))
	# 	else: G.dbc.execute("insert into files(id,path,time) values(?,?,?)",(i,temp.file_path,time.time()))
	# 	return temp.file_path

	# def _fetchFile(self,path):
	# 	pass
