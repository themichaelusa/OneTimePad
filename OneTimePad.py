from os import urandom, getcwd

class OneTimePad(object):

	def __init__(self):
		self.encryptedData, self.salt1, self.salt2 = (None,)*3

	def encrypt(self, message):
		key = str(urandom(len(message)))
		saltedKey = self.saltKey(key)
		self.encryptedData = self.stringsXOR(message, saltedKey)
		randomFileName = self.generateRandomFilename()
		self.writePadComponentsToFile(randomFileName, key)
		self.showEncryptionMessage(randomFileName)
   
	def decrypt(self, encryptedData, salt1, salt2, key):
		saltedKey = self.salt1 + str(key) + self.salt2
		decryptedData = self.stringsXOR(encryptedData, saltedKey)
		randomFileName = self.generateRandomFilename()
		self.writeDecryptedDataToFile(randomFileName, decryptedData)
		self.showEncryptionMessage(randomFileName)

	def generateRandomFilename(self):
		return str(urandom(16)) + ".txt"

	def saltKey(self, key):
   		self.salt1, self.salt2 = (str(urandom(256)),)*2
   		return self.salt1 + str(key) + self.salt2

	def stringsXOR(self, message, key):
		return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(message, key))

	def showEncryptionMessage(self, filename): 
		print("PAD_NAME: " + filename)
		print("PAD_LOCATION: " + getcwd())

	def writePadComponentsToFile(self, filename, key):
		with open(filename, "a+") as file:
			file.write("DATA: \n" + self.encryptedData + "\n\n")
			file.write("SALT_1: \n" + self.salt1 + "\n\n")
			file.write("SALT_2: \n" + self.salt2 + "\n\n")
			file.write("KEY: \n" + key)

	def writeDecryptedDataToFile(self, filename, decryptedData):
		with open(filename, "a+") as file:
			file.write("DATA: \n" + decryptedData)
