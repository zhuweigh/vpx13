#
# Copyright (c) 2008-2019 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class nsencryptionkey(base_resource) :
	""" Configuration for encryption key resource. """
	def __init__(self) :
		self._name = None
		self._method = None
		self._keyvalue = None
		self._padding = None
		self._iv = None
		self._comment = None
		self.___count = None

	@property
	def name(self) :
		r"""Key name.  This follows the same syntax rules as other expression entity names:
		It must begin with an alpha character (A-Z or a-z) or an underscore (_).
		The rest of the characters must be alpha, numeric (0-9) or underscores.
		It cannot be re or xp (reserved for regular and XPath expressions).
		It cannot be an expression reserved word (e.g. SYS or HTTP).
		It cannot be used for an existing expression object (HTTP callout, patset, dataset, stringmap, or named expression).<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Key name.  This follows the same syntax rules as other expression entity names:
		It must begin with an alpha character (A-Z or a-z) or an underscore (_).
		The rest of the characters must be alpha, numeric (0-9) or underscores.
		It cannot be re or xp (reserved for regular and XPath expressions).
		It cannot be an expression reserved word (e.g. SYS or HTTP).
		It cannot be used for an existing expression object (HTTP callout, patset, dataset, stringmap, or named expression).<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def method(self) :
		r"""Cipher method to be used to encrypt and decrypt content.
		NONE - no encryption or decryption is performed The output of ENCRYPT() and DECRYPT() is the same as the input.
		RC4  - the RC4 stream cipher with a 128 bit (16 byte) key; RC4 is now considered insecure and should only be used if required by existing applciations.
		DES[-<mode>] - the Data Encryption Standard (DES) block cipher with a 64-bit (8 byte) key, with 56 data bits and 8 parity bits. DES is considered less secure than DES3 or AES so it should only be used if required by an existing applicastion. The optional mode is described below; DES without a mode is equivalent to DES-CBC.
		DES3[-<mode>] - the Triple Data Encryption Standard (DES) block cipher with a 192-bit (24 byte) key. The optional mode is described below; DES3 without a mode is equivalent to DES3-CBC.
		AES<keysize>[-<mode>] - the Advanced Encryption Standard block cipher, available with 128 bit (16 byte), 192 bit (24 byte), and 256 bit (32 byte) keys. The optional mode is described below; AES<keysize> without a mode is equivalent to AES<keysize>-CBC.
		For a block cipher, the <mode> specifies how multiple blocks of plaintext are encrypted and how the Initialization Vector (IV) is used. Choices are
		CBC (Cipher Block Chaining) - Each block of plaintext is XORed with the previous ciphertext block, or IV for the first block, before being encrypted. Padding is required if the plaintext is not a multiple of the cipher block size.
		CFB (Cipher Feedback) - The previous ciphertext block, or the IV for the first block, is encrypted and the output is XORed with the current plaintext block to create the current ciphertext block. The 128-bit version of CFB is provided. Padding is not required.
		OFB (Output Feedback) - A keystream is generated by applying the cipher successfully to the IV and XORing the keystream blocks with the plaintext. Padding is not required.
		ECB (Electronic Codebook) - Each block of plaintext is independently encrypted. An IV is not used. Padding is required. This mode is considered less secure than the other modes because the same plaintext always produces the same encrypted text and should only be used if required by an existing application.<br/>Possible values = NONE, RC4, DES3, AES128, AES192, AES256, DES, DES-CBC, DES-CFB, DES-OFB, DES-ECB, DES3-CBC, DES3-CFB, DES3-OFB, DES3-ECB, AES128-CBC, AES128-CFB, AES128-OFB, AES128-ECB, AES192-CBC, AES192-CFB, AES192-OFB, AES192-ECB, AES256-CBC, AES256-CFB, AES256-OFB, AES256-ECB.
		"""
		try :
			return self._method
		except Exception as e:
			raise e

	@method.setter
	def method(self, method) :
		r"""Cipher method to be used to encrypt and decrypt content.
		NONE - no encryption or decryption is performed The output of ENCRYPT() and DECRYPT() is the same as the input.
		RC4  - the RC4 stream cipher with a 128 bit (16 byte) key; RC4 is now considered insecure and should only be used if required by existing applciations.
		DES[-<mode>] - the Data Encryption Standard (DES) block cipher with a 64-bit (8 byte) key, with 56 data bits and 8 parity bits. DES is considered less secure than DES3 or AES so it should only be used if required by an existing applicastion. The optional mode is described below; DES without a mode is equivalent to DES-CBC.
		DES3[-<mode>] - the Triple Data Encryption Standard (DES) block cipher with a 192-bit (24 byte) key. The optional mode is described below; DES3 without a mode is equivalent to DES3-CBC.
		AES<keysize>[-<mode>] - the Advanced Encryption Standard block cipher, available with 128 bit (16 byte), 192 bit (24 byte), and 256 bit (32 byte) keys. The optional mode is described below; AES<keysize> without a mode is equivalent to AES<keysize>-CBC.
		For a block cipher, the <mode> specifies how multiple blocks of plaintext are encrypted and how the Initialization Vector (IV) is used. Choices are
		CBC (Cipher Block Chaining) - Each block of plaintext is XORed with the previous ciphertext block, or IV for the first block, before being encrypted. Padding is required if the plaintext is not a multiple of the cipher block size.
		CFB (Cipher Feedback) - The previous ciphertext block, or the IV for the first block, is encrypted and the output is XORed with the current plaintext block to create the current ciphertext block. The 128-bit version of CFB is provided. Padding is not required.
		OFB (Output Feedback) - A keystream is generated by applying the cipher successfully to the IV and XORing the keystream blocks with the plaintext. Padding is not required.
		ECB (Electronic Codebook) - Each block of plaintext is independently encrypted. An IV is not used. Padding is required. This mode is considered less secure than the other modes because the same plaintext always produces the same encrypted text and should only be used if required by an existing application.<br/>Possible values = NONE, RC4, DES3, AES128, AES192, AES256, DES, DES-CBC, DES-CFB, DES-OFB, DES-ECB, DES3-CBC, DES3-CFB, DES3-OFB, DES3-ECB, AES128-CBC, AES128-CFB, AES128-OFB, AES128-ECB, AES192-CBC, AES192-CFB, AES192-OFB, AES192-ECB, AES256-CBC, AES256-CFB, AES256-OFB, AES256-ECB
		"""
		try :
			self._method = method
		except Exception as e:
			raise e

	@property
	def keyvalue(self) :
		r"""The hex-encoded key value. The length is determined by the cipher method:
		RC4    - 16 bytes
		DES    -  8 bytes (all modes)
		DES3   - 24 bytes (all modes)
		AES128 - 16 bytes (all modes)
		AES192 - 24 bytes (all modes)
		AES256 - 32 bytes (all modes)
		Note that the keyValue will be encrypted when it it is saved.
		"""
		try :
			return self._keyvalue
		except Exception as e:
			raise e

	@keyvalue.setter
	def keyvalue(self, keyvalue) :
		r"""The hex-encoded key value. The length is determined by the cipher method:
		RC4    - 16 bytes
		DES    -  8 bytes (all modes)
		DES3   - 24 bytes (all modes)
		AES128 - 16 bytes (all modes)
		AES192 - 24 bytes (all modes)
		AES256 - 32 bytes (all modes)
		Note that the keyValue will be encrypted when it it is saved.
		"""
		try :
			self._keyvalue = keyvalue
		except Exception as e:
			raise e

	@property
	def padding(self) :
		r"""Enables or disables the padding of plaintext to meet the block size requirements of block ciphers:
		ON - For encryption, PKCS5/7 padding is used, which appends n bytes of value n on the end of the plaintext to bring it to the cipher block lnegth. If the plaintext length is alraady a multiple of the block length, an additional block with bytes of value block_length will be added. For decryption, ISO 10126 padding is accepted, which expects the last byte of the block to be the number of added pad bytes. Note that this accepts PKCS5/7 padding, as well as ANSI_X923 padding. Padding ON is the default for the ECB and CBD modes.
		OFF - No padding. An Undef error will occur with the ECB or CBC modes if the plaintext length is not a multitple of the cipher block size. This can be used with the CFB and OFB modes, and with the ECB and CBC modes if the plaintext will always be an integral number of blocks, or if custom padding is implemented using a policy extension function. Padding OFf is the default for CFB and OFB modes.<br/>Default value: DEFAULT<br/>Possible values = OFF, ON.
		"""
		try :
			return self._padding
		except Exception as e:
			raise e

	@padding.setter
	def padding(self, padding) :
		r"""Enables or disables the padding of plaintext to meet the block size requirements of block ciphers:
		ON - For encryption, PKCS5/7 padding is used, which appends n bytes of value n on the end of the plaintext to bring it to the cipher block lnegth. If the plaintext length is alraady a multiple of the block length, an additional block with bytes of value block_length will be added. For decryption, ISO 10126 padding is accepted, which expects the last byte of the block to be the number of added pad bytes. Note that this accepts PKCS5/7 padding, as well as ANSI_X923 padding. Padding ON is the default for the ECB and CBD modes.
		OFF - No padding. An Undef error will occur with the ECB or CBC modes if the plaintext length is not a multitple of the cipher block size. This can be used with the CFB and OFB modes, and with the ECB and CBC modes if the plaintext will always be an integral number of blocks, or if custom padding is implemented using a policy extension function. Padding OFf is the default for CFB and OFB modes.<br/>Default value: DEFAULT<br/>Possible values = OFF, ON
		"""
		try :
			self._padding = padding
		except Exception as e:
			raise e

	@property
	def iv(self) :
		r"""The initalization voector (IV) for a block cipher, one block of data used to initialize the encryption. The best practice is to not specify an IV, in which case a new random IV will be generated for each encryption. The format must be iv_data or keyid_iv_data to include the generated IV in the encrypted data. The IV should only be specified if it cannot be included in the encrypted data. The IV length is the cipher block size:
		RC4    - not used (error if IV is specified)
		DES    -  8 bytes (all modes)
		DES3   -  8 bytes (all modes)
		AES128 - 16 bytes (all modes)
		AES192 - 16 bytes (all modes)
		AES256 - 16 bytes (all modes).
		"""
		try :
			return self._iv
		except Exception as e:
			raise e

	@iv.setter
	def iv(self, iv) :
		r"""The initalization voector (IV) for a block cipher, one block of data used to initialize the encryption. The best practice is to not specify an IV, in which case a new random IV will be generated for each encryption. The format must be iv_data or keyid_iv_data to include the generated IV in the encrypted data. The IV should only be specified if it cannot be included in the encrypted data. The IV length is the cipher block size:
		RC4    - not used (error if IV is specified)
		DES    -  8 bytes (all modes)
		DES3   -  8 bytes (all modes)
		AES128 - 16 bytes (all modes)
		AES192 - 16 bytes (all modes)
		AES256 - 16 bytes (all modes).
		"""
		try :
			self._iv = iv
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Comments associated with this encryption key.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Comments associated with this encryption key.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsencryptionkey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsencryptionkey
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nsencryptionkey.
		"""
		try :
			if type(resource) is not list :
				addresource = nsencryptionkey()
				addresource.name = resource.name
				addresource.method = resource.method
				addresource.keyvalue = resource.keyvalue
				addresource.padding = resource.padding
				addresource.iv = resource.iv
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsencryptionkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].method = resource[i].method
						addresources[i].keyvalue = resource[i].keyvalue
						addresources[i].padding = resource[i].padding
						addresources[i].iv = resource[i].iv
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsencryptionkey.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsencryptionkey()
				updateresource.name = resource.name
				updateresource.method = resource.method
				updateresource.keyvalue = resource.keyvalue
				updateresource.padding = resource.padding
				updateresource.iv = resource.iv
				updateresource.comment = resource.comment
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsencryptionkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].method = resource[i].method
						updateresources[i].keyvalue = resource[i].keyvalue
						updateresources[i].padding = resource[i].padding
						updateresources[i].iv = resource[i].iv
						updateresources[i].comment = resource[i].comment
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsencryptionkey resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsencryptionkey()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsencryptionkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsencryptionkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nsencryptionkey.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsencryptionkey()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsencryptionkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsencryptionkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsencryptionkey resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsencryptionkey()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nsencryptionkey()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nsencryptionkey() for _ in range(len(name))]
						obj = [nsencryptionkey() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nsencryptionkey()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nsencryptionkey resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsencryptionkey()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nsencryptionkey resources configured on NetScaler.
		"""
		try :
			obj = nsencryptionkey()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of nsencryptionkey resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsencryptionkey()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Method:
		NONE = "NONE"
		RC4 = "RC4"
		DES3 = "DES3"
		AES128 = "AES128"
		AES192 = "AES192"
		AES256 = "AES256"
		DES = "DES"
		DES_CBC = "DES-CBC"
		DES_CFB = "DES-CFB"
		DES_OFB = "DES-OFB"
		DES_ECB = "DES-ECB"
		DES3_CBC = "DES3-CBC"
		DES3_CFB = "DES3-CFB"
		DES3_OFB = "DES3-OFB"
		DES3_ECB = "DES3-ECB"
		AES128_CBC = "AES128-CBC"
		AES128_CFB = "AES128-CFB"
		AES128_OFB = "AES128-OFB"
		AES128_ECB = "AES128-ECB"
		AES192_CBC = "AES192-CBC"
		AES192_CFB = "AES192-CFB"
		AES192_OFB = "AES192-OFB"
		AES192_ECB = "AES192-ECB"
		AES256_CBC = "AES256-CBC"
		AES256_CFB = "AES256-CFB"
		AES256_OFB = "AES256-OFB"
		AES256_ECB = "AES256-ECB"

	class Padding:
		OFF = "OFF"
		ON = "ON"

class nsencryptionkey_response(base_response) :
	def __init__(self, length=1) :
		self.nsencryptionkey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsencryptionkey = [nsencryptionkey() for _ in range(length)]

