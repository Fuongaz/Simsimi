from requests import post
import sys

lang='vi'
api_key='NKgBCOSLgb-s0fc50JuFtWA6sV5koCzJBlwfeMTF'

def getAnswers(message):
	headers = {
		'Content-Type': 'application/json',
		'x-api-key': api_key
	}

	data = "{\n\t\"utext\": \""+message+"\", \n\t\"lang\": \""+lang+"\" \n}"

	url = "https://wsapi.simsimi.com/190410/talk/"
	result = post(url, data=data.encode('utf-8'), headers=headers)
	response = result.json()
	if response['status'] == 200:
		return response['atext']
	if response['status'] == 228:
		return 'Nói dì đó, Tui hông hỉuu'
	print('Đã có lỗi xãy ra!!')
	sys.exit()

def sendQuestion():
	question = input() 
	if question.lower() == 'dừng' or question.lower() == 'stop': 
		print('- Thui bai bai nha :<')
		sys.exit()
	answers = getAnswers(message=question)
	print("-",answers)
	sendQuestion()

if __name__ == '__main__':
	print('Nhập "dừng" để thoát chương trình\n')
	print('- Nói gì đó dzơ pẩn dzới tớ đi~')
	sendQuestion()