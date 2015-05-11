__author__ = 'andersonpaac'
import argparse


def args():
  	parser=argparse.ArgumentParser()
	parser.add_argument("-k","--key",default="")
   	parser.add_argument("-e","--email",default="")
	return parser
