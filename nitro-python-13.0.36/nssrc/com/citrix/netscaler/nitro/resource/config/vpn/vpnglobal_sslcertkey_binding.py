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

class vpnglobal_sslcertkey_binding(base_resource) :
	""" Binding class showing the sslcertkey that can be bound to vpnglobal.
	"""
	def __init__(self) :
		self._certkeyname = None
		self._cacert = None
		self._userdataencryptionkey = None
		self._crlcheck = None
		self._ocspcheck = None
		self._gotopriorityexpression = None
		self._feature = None
		self.___count = None

	@property
	def crlcheck(self) :
		r"""The state of the CRL check parameter (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._crlcheck
		except Exception as e:
			raise e

	@crlcheck.setter
	def crlcheck(self, crlcheck) :
		r"""The state of the CRL check parameter (Mandatory/Optional).<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._crlcheck = crlcheck
		except Exception as e:
			raise e

	@property
	def cacert(self) :
		r"""The name of the CA certificate binding.
		"""
		try :
			return self._cacert
		except Exception as e:
			raise e

	@cacert.setter
	def cacert(self, cacert) :
		r"""The name of the CA certificate binding.
		"""
		try :
			self._cacert = cacert
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	@feature.setter
	def feature(self, feature) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			self._feature = feature
		except Exception as e:
			raise e

	@property
	def certkeyname(self) :
		r"""SSL certkey to use in signing tokens.
		"""
		try :
			return self._certkeyname
		except Exception as e:
			raise e

	@certkeyname.setter
	def certkeyname(self, certkeyname) :
		r"""SSL certkey to use in signing tokens.
		"""
		try :
			self._certkeyname = certkeyname
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		r"""Applicable only to advance vpn session policy. An expression or other value specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		r"""Applicable only to advance vpn session policy. An expression or other value specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def ocspcheck(self) :
		r"""The state of the OCSP check parameter (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._ocspcheck
		except Exception as e:
			raise e

	@ocspcheck.setter
	def ocspcheck(self, ocspcheck) :
		r"""The state of the OCSP check parameter (Mandatory/Optional).<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._ocspcheck = ocspcheck
		except Exception as e:
			raise e

	@property
	def userdataencryptionkey(self) :
		r"""Certificate to be used for encrypting user data like KB Question and Answers, Alternate Email Address, etc.
		"""
		try :
			return self._userdataencryptionkey
		except Exception as e:
			raise e

	@userdataencryptionkey.setter
	def userdataencryptionkey(self, userdataencryptionkey) :
		r"""Certificate to be used for encrypting user data like KB Question and Answers, Alternate Email Address, etc.
		"""
		try :
			self._userdataencryptionkey = userdataencryptionkey
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnglobal_sslcertkey_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnglobal_sslcertkey_binding
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
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = vpnglobal_sslcertkey_binding()
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.certkeyname = resource.certkeyname
				updateresource.userdataencryptionkey = resource.userdataencryptionkey
				updateresource.cacert = resource.cacert
				updateresource.crlcheck = resource.crlcheck
				updateresource.ocspcheck = resource.ocspcheck
				updateresource.feature = resource.feature
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [vpnglobal_sslcertkey_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
						updateresources[i].certkeyname = resource[i].certkeyname
						updateresources[i].userdataencryptionkey = resource[i].userdataencryptionkey
						updateresources[i].cacert = resource[i].cacert
						updateresources[i].crlcheck = resource[i].crlcheck
						updateresources[i].ocspcheck = resource[i].ocspcheck
						updateresources[i].feature = resource[i].feature
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = vpnglobal_sslcertkey_binding()
				deleteresource.certkeyname = resource.certkeyname
				deleteresource.userdataencryptionkey = resource.userdataencryptionkey
				deleteresource.cacert = resource.cacert
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [vpnglobal_sslcertkey_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].certkeyname = resource[i].certkeyname
						deleteresources[i].userdataencryptionkey = resource[i].userdataencryptionkey
						deleteresources[i].cacert = resource[i].cacert
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		r""" Use this API to fetch a vpnglobal_sslcertkey_binding resources.
		"""
		try :
			obj = vpnglobal_sslcertkey_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		r""" Use this API to fetch filtered set of vpnglobal_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnglobal_sslcertkey_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		r""" Use this API to count vpnglobal_sslcertkey_binding resources configued on NetScaler.
		"""
		try :
			obj = vpnglobal_sslcertkey_binding()
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, filter_) :
		r""" Use this API to count the filtered set of vpnglobal_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnglobal_sslcertkey_binding()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

class vpnglobal_sslcertkey_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vpnglobal_sslcertkey_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnglobal_sslcertkey_binding = [vpnglobal_sslcertkey_binding() for _ in range(length)]

