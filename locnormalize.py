# script responds well to excel files exported as:
# 1. single column list
# 2. empty tabs removed
# 3. Windows formatted text (.txt)

import re
from sys import argv
from os.path import exists

script, test_file = argv
openy = open('jd2012a.txt', 'r')
slist = openy.readlines()


# slist = ['NA9053.H76 I6 2012',
# 'ND511.5.G679 A4 2012',
# 'N2250.S36 S36 2012',
# 'N2250.S36 S36 2012',
# 'TR647 .T92 2012',
# 'ND212.5.M63 M63 2011',
# 'ND1040 .C65 2009',
# 'NB379.B67 A4 2012',
# 'ND588.P6547 A4 2012',
# 'N6537.J6 A4 2012b']

		
class FindElement:
	def alpha(self, callnumber_string):
		p = r'^[A-Z]{1,3}'
		alpha_part = re.findall(p, callnumber_string)
		return alpha_part

	# def m_alpha(self, callnumber_string):
	# 	p = r'^[A-Z]{1,3}'
	# 	m = re.match(p, callnumber_string)
	# 	x = callnumber_string[:m.start()] + callnumber_string[:m.end()]
	# 	return x

	# def decimal(self, callnumber_string):
	# 	p = r'[0-9]{1,4}[ ]?[.]?[0-9]?(?=\.[A-Z])'
	# 	decimal = re.findall(p, callnumber_string)
	# 	return decimal

	def num(self, callnumber_string):
		p = r'[0-9]{1,4}'
		number_part = re.findall(p, callnumber_string)
		try:
			return [number_part[0]]
		except:
			return [" "]

	def dec(self, callnumber_string):
		p = r'[.][0-9]'
		dec_part = re.findall(p, callnumber_string)
		try:
			return [dec_part[0]]
		except:
			return [".0"]

	def cut1(self, callnumber_string):
		p = r'\.[A-Z][0-9]{1,7}'
		cutter1 = re.findall(p, callnumber_string)
		try:
			return [cutter1[0]]
		except:
			return [" "]

	def cut2(self, callnumber_string):
		p = r'(?<=[ ])[A-Z][0-9]{1,6}'
		cutter2 = re.findall(p, callnumber_string)
		try:
			return [cutter2[0]]
		except:
			return [" "]
		

	def date(self, callnumber_string):
		p = r'(?<=[ ])[0-9][0-9][0-9][0-9][a-zA-Z]?'
		date = re.findall(p, callnumber_string)
		try:
			return [date[0]]
		except:
			return [" "]


find = FindElement()

def normalize(x):
	return ((4 - len(x)) * "0")

l = []
for i in slist:
	l.append(	find.alpha(i) + 
				find.num(i) +
				find.dec(i) + 
				find.cut1(i) + 
				find.cut2(i) + 
				find.date(i) +
				["|"] + 
				[i] +
				["*|"]
			)



ll = []
for item in l:
	x = [item[0], normalize(item[1]) + item[1] + item[2], item[3], item[4], item[5], item[6], item[7], item[8]]
	# print x
	ll.append(x)

writeVar = """%s""" % sorted(ll)

wv1 = writeVar.replace('[', '')
wv2 = wv1.replace(']', '')
wv3 = wv2.replace('\'', '')
wv4 = wv3.replace(',', '')
wv5 = wv4.replace('*|', '\n')
wv6 = wv5.replace('\n ', '\n')
wv7 = wv6.replace('\\r\\n', '')
wv8 = wv7.replace('|', ',')

out_file = open(test_file, 'w')
out_file.write(wv8)

out_file.close()




