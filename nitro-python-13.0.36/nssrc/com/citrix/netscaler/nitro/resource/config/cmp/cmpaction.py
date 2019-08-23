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

class cmpaction(base_resource) :
	""" Configuration for compression action resource. """
	def __init__(self) :
		self._name = None
		self._cmptype = None
		self._addvaryheader = None
		self._varyheadervalue = None
		self._feature = None
		self._deltatype = None
		self._newname = None
		self._isdefault = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of the compression action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the action is added. 
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cmp action" or 'my cmp action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the compression action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the action is added. 
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cmp action" or 'my cmp action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def cmptype(self) :
		r"""Type of compression performed by this action. 
		Available settings function as follows: 
		* COMPRESS - Apply GZIP or DEFLATE compression to the response, depending on the request header. Prefer GZIP.
		* GZIP - Apply GZIP compression.
		* DEFLATE - Apply DEFLATE compression.
		* NOCOMPRESS - Do not compress the response if the request matches a policy that uses this action.<br/>Possible values = compress, gzip, deflate, nocompress.
		"""
		try :
			return self._cmptype
		except Exception as e:
			raise e

	@cmptype.setter
	def cmptype(self, cmptype) :
		r"""Type of compression performed by this action. 
		Available settings function as follows: 
		* COMPRESS - Apply GZIP or DEFLATE compression to the response, depending on the request header. Prefer GZIP.
		* GZIP - Apply GZIP compression.
		* DEFLATE - Apply DEFLATE compression.
		* NOCOMPRESS - Do not compress the response if the request matches a policy that uses this action.<br/>Possible values = compress, gzip, deflate, nocompress
		"""
		try :
			self._cmptype = cmptype
		except Exception as e:
			raise e

	@property
	def addvaryheader(self) :
		r"""Control insertion of the Vary header in HTTP responses compressed by Citrix ADC. Intermediate caches store different versions of the response for different values of the headers present in the Vary response header.<br/>Default value: GLOBAL<br/>Possible values = GLOBAL, DISABLED, ENABLED.
		"""
		try :
			return self._addvaryheader
		except Exception as e:
			raise e

	@addvaryheader.setter
	def addvaryheader(self, addvaryheader) :
		r"""Control insertion of the Vary header in HTTP responses compressed by Citrix ADC. Intermediate caches store different versions of the response for different values of the headers present in the Vary response header.<br/>Default value: GLOBAL<br/>Possible values = GLOBAL, DISABLED, ENABLED
		"""
		try :
			self._addvaryheader = addvaryheader
		except Exception as e:
			raise e

	@property
	def varyheadervalue(self) :
		r"""The value of the HTTP Vary header for compressed responses.<br/>Minimum length =  1.
		"""
		try :
			return self._varyheadervalue
		except Exception as e:
			raise e

	@varyheadervalue.setter
	def varyheadervalue(self, varyheadervalue) :
		r"""The value of the HTTP Vary header for compressed responses.<br/>Minimum length =  1
		"""
		try :
			self._varyheadervalue = varyheadervalue
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
	def deltatype(self) :
		r"""The type of delta action (if delta type compression action is defined).<br/>Default value: PERURL<br/>Possible values = PERURL, PERPOLICY.
		"""
		try :
			return self._deltatype
		except Exception as e:
			raise e

	@deltatype.setter
	def deltatype(self, deltatype) :
		r"""The type of delta action (if delta type compression action is defined).<br/>Default value: PERURL<br/>Possible values = PERURL, PERPOLICY
		"""
		try :
			self._deltatype = deltatype
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the compression action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at
		(@), equals (=), and hyphen (-) characters. 
		Choose a name that can be correlated with the function that the action performs. 
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cmp action" or 'my cmp action').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the compression action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at
		(@), equals (=), and hyphen (-) characters. 
		Choose a name that can be correlated with the function that the action performs. 
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cmp action" or 'my cmp action').<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		r"""A value of true is returned if it is a default policy.
		"""
		try :
			return self._isdefault
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cmpaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cmpaction
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
		r""" Use this API to add cmpaction.
		"""
		try :
			if type(resource) is not list :
				addresource = cmpaction()
				addresource.name = resource.name
				addresource.cmptype = resource.cmptype
				addresource.addvaryheader = resource.addvaryheader
				addresource.varyheadervalue = resource.varyheadervalue
				addresource.feature = resource.feature
				addresource.deltatype = resource.deltatype
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ cmpaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].cmptype = resource[i].cmptype
						addresources[i].addvaryheader = resource[i].addvaryheader
						addresources[i].varyheadervalue = resource[i].varyheadervalue
						addresources[i].feature = resource[i].feature
						addresources[i].deltatype = resource[i].deltatype
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete cmpaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = cmpaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ cmpaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ cmpaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update cmpaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = cmpaction()
				updateresource.name = resource.name
				updateresource.cmptype = resource.cmptype
				updateresource.addvaryheader = resource.addvaryheader
				updateresource.varyheadervalue = resource.varyheadervalue
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ cmpaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].cmptype = resource[i].cmptype
						updateresources[i].addvaryheader = resource[i].addvaryheader
						updateresources[i].varyheadervalue = resource[i].varyheadervalue
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of cmpaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = cmpaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ cmpaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ cmpaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a cmpaction resource.
		"""
		try :
			renameresource = cmpaction()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the cmpaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cmpaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = cmpaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [cmpaction() for _ in range(len(name))]
						obj = [cmpaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = cmpaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of cmpaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cmpaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the cmpaction resources configured on NetScaler.
		"""
		try :
			obj = cmpaction()
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
		r""" Use this API to count filtered the set of cmpaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cmpaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


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

	class Cmptype:
		compress = "compress"
		gzip = "gzip"
		deflate = "deflate"
		nocompress = "nocompress"

	class Addvaryheader:
		GLOBAL = "GLOBAL"
		DISABLED = "DISABLED"
		ENABLED = "ENABLED"

	class Deltatype:
		PERURL = "PERURL"
		PERPOLICY = "PERPOLICY"

class cmpaction_response(base_response) :
	def __init__(self, length=1) :
		self.cmpaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cmpaction = [cmpaction() for _ in range(length)]

