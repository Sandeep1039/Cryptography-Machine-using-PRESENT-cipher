from pypresent import Present
import Padding
import sys

text="hello"
k="00000000000000000000"

if (len(sys.argv)>1):
	text=str(sys.argv[1])

if (len(sys.argv)>2):
	k=str(sys.argv[2])

text = Padding.appendPadding(text,blocksize=8,mode='CMS')

print ('Text:\t'+text)
print ('Key:\t'+k)
print ('--------')
print
key = bytes.fromhex(k)
   
 
cipher = Present(key) 
encrypted = cipher.encrypt(text.encode())
print ('Cipher:\t\t'+encrypted.hex())
decrypted = cipher.decrypt(encrypted)

print ('Decrypted:\t'+decrypted.hex())
print ('Decrypted:\t'+Padding.removePadding(decrypted.decode(),blocksize=8,mode='CMS'))