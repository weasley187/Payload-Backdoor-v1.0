# encode your payload: http://string-functions.com/base64encode.aspx
# accrobata e gei

import base64

def exec_xor():
	xor = 'yourcode'
	decode = str(base64.b64decode(xor))
	exec(decode)
	#print('{}'.format(decode))
	
exec_xor()