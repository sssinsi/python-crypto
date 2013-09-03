#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random

message = 'this is message!'

random_func = Random.new().read
rsa = RSA.generate(1024,random_func)

#公開鍵と秘密鍵
public_pem = rsa.publickey().exportKey()
private_pem = rsa.exportKey(format='PEM', passphrase = 'hogehoge')

print 'public_pem:', public_pem
print 'private_pem',private_pem

#公開鍵による暗号化
crypt = rsa.publickey().encrypt(message,random_func)
print 'crypt:', crypt

#秘密鍵による復号化
decrypt = RSA.importKey(private_pem, 'hogehoge').decrypt(crypt)
print 'decrypt:', decrypt
