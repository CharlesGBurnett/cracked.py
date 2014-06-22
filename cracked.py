#!/usr/bin/python
import itertools
import string
import hashlib
import sys

# Should take in what hash algo to use,  what hash to 
# check,the number of characters to check, and what alphabet to use
# That is arg0, arg1, arg2, and arg3 respectively


def main():
	if sys.argv[1] and sys.argv[2] and sys.argv[3]:
		hashCrack(sys.argv[1], sys.argv[2], int(sys.argv[3]))
	else:
		print "Invalid arguements, try again"


def stringGen(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

  
def hashCrack(hashAlgo, hashToUse, maxLength):
	print "Algorithm to use: " + hashAlgo
	if hashAlgo == "sha1":
		sha1Crack(hashToUse, maxLength)
	elif hashAlgo == "sha256":
		sha256Crack(hashToUse, maxLength)
	elif hashAlgo == "sha512":
		sha512Crack(hashToUse, maxLength)
	elif hashAlgo == "md5":
		md5Crack(hashToUse, maxLength)
	else:
		print "invalid algorithm"
		return

def md5Crack(hashToUse, maxLength):
	i=0
	for attempt in stringGen(string.ascii_lowercase, maxLength):
			i+=1
			aHash = hashlib.md5(attempt).hexdigest()
			if aHash == hashToUse:
				print "matched: " + attempt
				return
	print "Not found."
        	
def sha1Crack(hashToUse, maxLength):
	i=0
	for attempt in stringGen(string.ascii_lowercase, maxLength):
			i+=1
			aHash = hashlib.sha1(attempt).hexdigest()
			if aHash == hashToUse:
				print "matched: " + attempt 
				return
	print "Not found."

def sha256Crack(hashToUse, maxLength):
	i=0
	for attempt in stringGen(string.ascii_lowercase, maxLength):
			i+=1
			aHash = hashlib.sha256(attempt).hexdigest()
			print aHash + " = " + attempt
			if aHash == hashToUse:
				print "matched: " + attempt
				return
	print "Not found."

def sha512Crack(hashToUse, maxLength):
	i=0
	for attempt in stringGen(string.ascii_lowercase, maxLength):
			i+=1
			aHash = hashlib.sha512(attempt).hexdigest()
			if aHash == hashToUse:
				print "matched: " + attempt 
				return
	print "Not found."

        		
if __name__ == '__main__':
	main()
