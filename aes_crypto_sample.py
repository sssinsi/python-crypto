#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Crypto.Cipher import AES

iv  = 'initialvector123'
key = '0123456789abcdef' #16byte multiple
message = 'this is message!' #16byte multiple

print 'original:', message

#Encryption
cipher = AES.new(key,AES.MODE_CBC,iv)
data = cipher.encrypt(message)
print 'cipher:',repr(data)

#Decryption
cipher2 = AES.new(key,AES.MODE_CBC,iv)
print 'decode:',cipher2.decrypt(data) #復号化
