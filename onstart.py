import sendgrid
import parser.parser as arg
import os
import datetime
import socket
import fcntl
import struct

receiver = "andersonpaac@gmail.com"
sender = receiver
def sendmail(args):
	global sender,receiver
	if args.key=="" or args.email=="":
		dict1 = dict(os.environ)
		key = dict1["SENDGRID_API_KEY"]
	else:
		key = args.key
		sender,receiver = args.email
	sgclient = sg = sendgrid.SendGridClient('key')
	cont = contentstosend("en0")
	sbj = "RPi Update: "+str(datetime.datetime.now())
	print cont
	#message = sendgrid.Mail(to=reciever, subject=sbj,, text=cont, from_email='sender')

def contentstosend(interface):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),0x8915,struct.pack('256s', interface[:15]))[20:24])
	


def main():
	parser = arg.args()
	sendmail(parser.parse_args())
main()
