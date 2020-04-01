# encode your payload: http://string-functions.com/base64encode.aspx
# accrobata e gei
import os
import base64

xor = b'yourENCODEDpayload'

def xor_exec():
	xor_conn = base64.b64decode(xor)
	os.system(xor_conn.decode('utf-8'))
	#print('{}'.format(xor_conn))			<<-- uncomment if you want it to be spicy :/
	#os.system('clear')
	return

xor_exec()

'''
OLD SCRIPT

import base64

xor = b'yourENCODEDpayload'

def xor_exec():
	xor_conn = base64.b64decode(xor) 
	exec(xor_conn.decode('utf-8'))
	#print('{}'.format(xor_conn))
	return

xor_exec()
'''
