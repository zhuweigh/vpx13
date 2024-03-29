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

class sslfipskey(base_resource) :
	""" Configuration for FIPS key resource. """
	def __init__(self) :
		self._fipskeyname = None
		self._keytype = None
		self._exponent = None
		self._modulus = None
		self._curve = None
		self._key = None
		self._inform = None
		self._wrapkeyname = None
		self._iv = None
		self._size = None
		self.___count = None

	@property
	def fipskeyname(self) :
		r"""Name for the FIPS key. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the FIPS key is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my fipskey" or 'my fipskey').<br/>Minimum length =  1.
		"""
		try :
			return self._fipskeyname
		except Exception as e:
			raise e

	@fipskeyname.setter
	def fipskeyname(self, fipskeyname) :
		r"""Name for the FIPS key. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the FIPS key is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my fipskey" or 'my fipskey').<br/>Minimum length =  1
		"""
		try :
			self._fipskeyname = fipskeyname
		except Exception as e:
			raise e

	@property
	def keytype(self) :
		r"""Only RSA key and ECDSA Key are supported.<br/>Default value: RSA<br/>Possible values = RSA, ECDSA.
		"""
		try :
			return self._keytype
		except Exception as e:
			raise e

	@keytype.setter
	def keytype(self, keytype) :
		r"""Only RSA key and ECDSA Key are supported.<br/>Default value: RSA<br/>Possible values = RSA, ECDSA
		"""
		try :
			self._keytype = keytype
		except Exception as e:
			raise e

	@property
	def exponent(self) :
		r"""Exponent value for the FIPS key to be created. Available values function as follows:
		3=3 (hexadecimal)
		F4=10001 (hexadecimal).<br/>Default value: 3<br/>Possible values = 3, F4.
		"""
		try :
			return self._exponent
		except Exception as e:
			raise e

	@exponent.setter
	def exponent(self, exponent) :
		r"""Exponent value for the FIPS key to be created. Available values function as follows:
		3=3 (hexadecimal)
		F4=10001 (hexadecimal).<br/>Default value: 3<br/>Possible values = 3, F4
		"""
		try :
			self._exponent = exponent
		except Exception as e:
			raise e

	@property
	def modulus(self) :
		r"""Modulus, in multiples of 64, of the FIPS key to be created.<br/>Maximum length =  4096.
		"""
		try :
			return self._modulus
		except Exception as e:
			raise e

	@modulus.setter
	def modulus(self, modulus) :
		r"""Modulus, in multiples of 64, of the FIPS key to be created.<br/>Maximum length =  4096
		"""
		try :
			self._modulus = modulus
		except Exception as e:
			raise e

	@property
	def curve(self) :
		r"""Only p_256 (prime256v1) and P_384 (secp384r1) are supported.<br/>Default value: P_256<br/>Possible values = P_256, P_384.
		"""
		try :
			return self._curve
		except Exception as e:
			raise e

	@curve.setter
	def curve(self, curve) :
		r"""Only p_256 (prime256v1) and P_384 (secp384r1) are supported.<br/>Default value: P_256<br/>Possible values = P_256, P_384
		"""
		try :
			self._curve = curve
		except Exception as e:
			raise e

	@property
	def key(self) :
		r"""Name of and, optionally, path to the key file to be imported.
		/nsconfig/ssl/ is the default path.<br/>Minimum length =  1.
		"""
		try :
			return self._key
		except Exception as e:
			raise e

	@key.setter
	def key(self, key) :
		r"""Name of and, optionally, path to the key file to be imported.
		/nsconfig/ssl/ is the default path.<br/>Minimum length =  1
		"""
		try :
			self._key = key
		except Exception as e:
			raise e

	@property
	def inform(self) :
		r"""Input format of the key file. Available formats are:
		SIM - Secure Information Management; select when importing a FIPS key. If the external FIPS key is encrypted, first decrypt it, and then import it.
		PEM - Privacy Enhanced Mail; select when importing a non-FIPS key.
		<br/>Default value: SIM<br/>Possible values = SIM, DER, PEM.
		"""
		try :
			return self._inform
		except Exception as e:
			raise e

	@inform.setter
	def inform(self, inform) :
		r"""Input format of the key file. Available formats are:
		SIM - Secure Information Management; select when importing a FIPS key. If the external FIPS key is encrypted, first decrypt it, and then import it.
		PEM - Privacy Enhanced Mail; select when importing a non-FIPS key.
		<br/>Default value: SIM<br/>Possible values = SIM, DER, PEM
		"""
		try :
			self._inform = inform
		except Exception as e:
			raise e

	@property
	def wrapkeyname(self) :
		r"""Name of the wrap key to use for importing the key. Required for importing a non-FIPS key.<br/>Minimum length =  1.
		"""
		try :
			return self._wrapkeyname
		except Exception as e:
			raise e

	@wrapkeyname.setter
	def wrapkeyname(self, wrapkeyname) :
		r"""Name of the wrap key to use for importing the key. Required for importing a non-FIPS key.<br/>Minimum length =  1
		"""
		try :
			self._wrapkeyname = wrapkeyname
		except Exception as e:
			raise e

	@property
	def iv(self) :
		r"""Initialization Vector (IV) to use for importing the key. Required for importing a non-FIPS key.<br/>Minimum length =  1.
		"""
		try :
			return self._iv
		except Exception as e:
			raise e

	@iv.setter
	def iv(self, iv) :
		r"""Initialization Vector (IV) to use for importing the key. Required for importing a non-FIPS key.<br/>Minimum length =  1
		"""
		try :
			self._iv = iv
		except Exception as e:
			raise e

	@property
	def size(self) :
		r"""Size.
		"""
		try :
			return self._size
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslfipskey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslfipskey
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.fipskeyname is not None :
				return str(self.fipskeyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def create(cls, client, resource) :
		r""" Use this API to create sslfipskey.
		"""
		try :
			if type(resource) is not list :
				createresource = sslfipskey()
				createresource.fipskeyname = resource.fipskeyname
				createresource.keytype = resource.keytype
				createresource.exponent = resource.exponent
				createresource.modulus = resource.modulus
				createresource.curve = resource.curve
				return createresource.perform_operation(client,"create")
			else :
				if (resource and len(resource) > 0) :
					createresources = [ sslfipskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						createresources[i].fipskeyname = resource[i].fipskeyname
						createresources[i].keytype = resource[i].keytype
						createresources[i].exponent = resource[i].exponent
						createresources[i].modulus = resource[i].modulus
						createresources[i].curve = resource[i].curve
				result = cls.perform_operation_bulk_request(client, createresources,"create")
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete sslfipskey.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslfipskey()
				if type(resource) !=  type(deleteresource):
					deleteresource.fipskeyname = resource
				else :
					deleteresource.fipskeyname = resource.fipskeyname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslfipskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].fipskeyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslfipskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].fipskeyname = resource[i].fipskeyname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def Import(cls, client, resource) :
		r""" Use this API to Import sslfipskey.
		"""
		try :
			if type(resource) is not list :
				Importresource = sslfipskey()
				Importresource.fipskeyname = resource.fipskeyname
				Importresource.key = resource.key
				Importresource.inform = resource.inform
				Importresource.wrapkeyname = resource.wrapkeyname
				Importresource.iv = resource.iv
				Importresource.exponent = resource.exponent
				return Importresource.perform_operation(client,"Import")
			else :
				if (resource and len(resource) > 0) :
					Importresources = [ sslfipskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						Importresources[i].fipskeyname = resource[i].fipskeyname
						Importresources[i].key = resource[i].key
						Importresources[i].inform = resource[i].inform
						Importresources[i].wrapkeyname = resource[i].wrapkeyname
						Importresources[i].iv = resource[i].iv
						Importresources[i].exponent = resource[i].exponent
				result = cls.perform_operation_bulk_request(client, Importresources,"Import")
			return result
		except Exception as e :
			raise e

	@classmethod
	def export(cls, client, resource) :
		r""" Use this API to export sslfipskey.
		"""
		try :
			if type(resource) is not list :
				exportresource = sslfipskey()
				exportresource.fipskeyname = resource.fipskeyname
				exportresource.key = resource.key
				return exportresource.perform_operation(client,"export")
			else :
				if (resource and len(resource) > 0) :
					exportresources = [ sslfipskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						exportresources[i].fipskeyname = resource[i].fipskeyname
						exportresources[i].key = resource[i].key
				result = cls.perform_operation_bulk_request(client, exportresources,"export")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslfipskey resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslfipskey()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = sslfipskey()
					obj.fipskeyname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [sslfipskey() for _ in range(len(name))]
						obj = [sslfipskey() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = sslfipskey()
							obj[i].fipskeyname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of sslfipskey resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslfipskey()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the sslfipskey resources configured on NetScaler.
		"""
		try :
			obj = sslfipskey()
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
		r""" Use this API to count filtered the set of sslfipskey resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslfipskey()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Keytype:
		RSA = "RSA"
		ECDSA = "ECDSA"

	class Inform:
		SIM = "SIM"
		DER = "DER"
		PEM = "PEM"

	class Curve:
		P_256 = "P_256"
		P_384 = "P_384"

	class Exponent:
		_3 = "3"
		F4 = "F4"

class sslfipskey_response(base_response) :
	def __init__(self, length=1) :
		self.sslfipskey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslfipskey = [sslfipskey() for _ in range(length)]

