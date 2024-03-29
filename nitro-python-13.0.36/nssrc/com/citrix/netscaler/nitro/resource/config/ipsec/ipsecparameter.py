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

class ipsecparameter(base_resource) :
	""" Configuration for IPSEC paramter resource. """
	def __init__(self) :
		self._ikeversion = None
		self._encalgo = None
		self._hashalgo = None
		self._lifetime = None
		self._livenesscheckinterval = None
		self._replaywindowsize = None
		self._ikeretryinterval = None
		self._perfectforwardsecrecy = None
		self._retransmissiontime = None
		self._responderonly = None

	@property
	def ikeversion(self) :
		r"""IKE Protocol Version.<br/>Default value: V2<br/>Possible values = V1, V2.
		"""
		try :
			return self._ikeversion
		except Exception as e:
			raise e

	@ikeversion.setter
	def ikeversion(self, ikeversion) :
		r"""IKE Protocol Version.<br/>Default value: V2<br/>Possible values = V1, V2
		"""
		try :
			self._ikeversion = ikeversion
		except Exception as e:
			raise e

	@property
	def encalgo(self) :
		r"""Type of encryption algorithm (Note: Selection of AES enables AES128).<br/>Default value: AES<br/>Possible values = AES, 3DES, AES192, AES256.
		"""
		try :
			return self._encalgo
		except Exception as e:
			raise e

	@encalgo.setter
	def encalgo(self, encalgo) :
		r"""Type of encryption algorithm (Note: Selection of AES enables AES128).<br/>Default value: AES<br/>Possible values = AES, 3DES, AES192, AES256
		"""
		try :
			self._encalgo = encalgo
		except Exception as e:
			raise e

	@property
	def hashalgo(self) :
		r"""Type of hashing algorithm.<br/>Default value: HMAC_SHA256<br/>Possible values = HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5.
		"""
		try :
			return self._hashalgo
		except Exception as e:
			raise e

	@hashalgo.setter
	def hashalgo(self, hashalgo) :
		r"""Type of hashing algorithm.<br/>Default value: HMAC_SHA256<br/>Possible values = HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5
		"""
		try :
			self._hashalgo = hashalgo
		except Exception as e:
			raise e

	@property
	def lifetime(self) :
		r"""Lifetime of IKE SA in seconds. Lifetime of IPSec SA will be (lifetime of IKE SA/8).<br/>Minimum length =  480<br/>Maximum length =  31536000.
		"""
		try :
			return self._lifetime
		except Exception as e:
			raise e

	@lifetime.setter
	def lifetime(self, lifetime) :
		r"""Lifetime of IKE SA in seconds. Lifetime of IPSec SA will be (lifetime of IKE SA/8).<br/>Minimum length =  480<br/>Maximum length =  31536000
		"""
		try :
			self._lifetime = lifetime
		except Exception as e:
			raise e

	@property
	def livenesscheckinterval(self) :
		r"""Number of seconds after which a notify payload is sent to check the liveliness of the peer. Additional retries are done as per retransmit interval setting. Zero value disables liveliness checks.<br/>Maximum length =  64999.
		"""
		try :
			return self._livenesscheckinterval
		except Exception as e:
			raise e

	@livenesscheckinterval.setter
	def livenesscheckinterval(self, livenesscheckinterval) :
		r"""Number of seconds after which a notify payload is sent to check the liveliness of the peer. Additional retries are done as per retransmit interval setting. Zero value disables liveliness checks.<br/>Maximum length =  64999
		"""
		try :
			self._livenesscheckinterval = livenesscheckinterval
		except Exception as e:
			raise e

	@property
	def replaywindowsize(self) :
		r"""IPSec Replay window size for the data traffic.<br/>Maximum length =  16384.
		"""
		try :
			return self._replaywindowsize
		except Exception as e:
			raise e

	@replaywindowsize.setter
	def replaywindowsize(self, replaywindowsize) :
		r"""IPSec Replay window size for the data traffic.<br/>Maximum length =  16384
		"""
		try :
			self._replaywindowsize = replaywindowsize
		except Exception as e:
			raise e

	@property
	def ikeretryinterval(self) :
		r"""IKE retry interval for bringing up the connection.<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._ikeretryinterval
		except Exception as e:
			raise e

	@ikeretryinterval.setter
	def ikeretryinterval(self, ikeretryinterval) :
		r"""IKE retry interval for bringing up the connection.<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._ikeretryinterval = ikeretryinterval
		except Exception as e:
			raise e

	@property
	def perfectforwardsecrecy(self) :
		r"""Enable/Disable PFS.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._perfectforwardsecrecy
		except Exception as e:
			raise e

	@perfectforwardsecrecy.setter
	def perfectforwardsecrecy(self, perfectforwardsecrecy) :
		r"""Enable/Disable PFS.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._perfectforwardsecrecy = perfectforwardsecrecy
		except Exception as e:
			raise e

	@property
	def retransmissiontime(self) :
		r"""The interval in seconds to retry sending the IKE messages to peer, three consecutive attempts are done with doubled interval after every failure,
		increases for every retransmit till 6 retransmits.<br/>Minimum length =  1<br/>Maximum length =  99.
		"""
		try :
			return self._retransmissiontime
		except Exception as e:
			raise e

	@retransmissiontime.setter
	def retransmissiontime(self, retransmissiontime) :
		r"""The interval in seconds to retry sending the IKE messages to peer, three consecutive attempts are done with doubled interval after every failure,
		increases for every retransmit till 6 retransmits.<br/>Minimum length =  1<br/>Maximum length =  99
		"""
		try :
			self._retransmissiontime = retransmissiontime
		except Exception as e:
			raise e

	@property
	def responderonly(self) :
		r"""Responder Only config for IKED.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._responderonly
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ipsecparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ipsecparameter
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update ipsecparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = ipsecparameter()
				updateresource.ikeversion = resource.ikeversion
				updateresource.encalgo = resource.encalgo
				updateresource.hashalgo = resource.hashalgo
				updateresource.lifetime = resource.lifetime
				updateresource.livenesscheckinterval = resource.livenesscheckinterval
				updateresource.replaywindowsize = resource.replaywindowsize
				updateresource.ikeretryinterval = resource.ikeretryinterval
				updateresource.perfectforwardsecrecy = resource.perfectforwardsecrecy
				updateresource.retransmissiontime = resource.retransmissiontime
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of ipsecparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = ipsecparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the ipsecparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ipsecparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Perfectforwardsecrecy:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

	class Responderonly:
		YES = "YES"
		NO = "NO"

	class Ikeversion:
		V1 = "V1"
		V2 = "V2"

	class Hashalgo:
		HMAC_SHA1 = "HMAC_SHA1"
		HMAC_SHA256 = "HMAC_SHA256"
		HMAC_SHA384 = "HMAC_SHA384"
		HMAC_SHA512 = "HMAC_SHA512"
		HMAC_MD5 = "HMAC_MD5"

	class Encalgo:
		AES = "AES"
		_3DES = "3DES"
		AES192 = "AES192"
		AES256 = "AES256"

class ipsecparameter_response(base_response) :
	def __init__(self, length=1) :
		self.ipsecparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ipsecparameter = [ipsecparameter() for _ in range(length)]

