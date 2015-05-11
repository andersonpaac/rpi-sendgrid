import sendgrid
import parser.parser as arg
import os
import datetime
import socket
import fcntl
import struct
import subprocess as sub

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
	sgclient = sendgrid.SendGridClient(key)
	cont = contentstosend()
	sbj = "RPi Update: "+str(datetime.datetime.now())
	print cont
	#message = sendgrid.Mail(to=reciever, subject=sbj,, text=cont, from_email='sender')

def contentstosend():
    p = sub.Popen('ifconfig',stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = p.communicate()
    ip = output[393:414]
    p = sub.Popen('iwconfig',stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = p.communicate()
    essid = output[0:45]
    return ip+" "+essid

def main():
	parser = arg.args()
	sendmail(parser.parse_args())
main()
