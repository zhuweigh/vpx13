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

class dnsaction64(base_resource) :
	""" Configuration for dns64 action resource. """
	def __init__(self) :
		self._actionname = None
		self._prefix = None
		self._mappedrule = None
		self._excluderule = None
		self._feature = None
		self.___count = None

	@property
	def actionname(self) :
		r"""Name of the dns64 action.
		"""
		try :
			return self._actionname
		except Exception as e:
			raise e

	@actionname.setter
	def actionname(self, actionname) :
		r"""Name of the dns64 action.
		"""
		try :
			self._actionname = actionname
		except Exception as e:
			raise e

	@property
	def prefix(self) :
		r"""The dns64 prefix to be used if the after evaluating the rules.
		"""
		try :
			return self._prefix
		except Exception as e:
			raise e

	@prefix.setter
	def prefix(self, prefix) :
		r"""The dns64 prefix to be used if the after evaluating the rules.
		"""
		try :
			self._prefix = prefix
		except Exception as e:
			raise e

	@property
	def mappedrule(self) :
		r"""The expression to select the criteria for ipv4 addresses to be used for synthesis.
		Only if the mappedrule is evaluated to true the corresponding ipv4 address is used for synthesis using respective prefix, 
		otherwise the A RR is discarded.
		"""
		try :
			return self._mappedrule
		except Exception as e:
			raise e

	@mappedrule.setter
	def mappedrule(self, mappedrule) :
		r"""The expression to select the criteria for ipv4 addresses to be used for synthesis.
		Only if the mappedrule is evaluated to true the corresponding ipv4 address is used for synthesis using respective prefix, 
		otherwise the A RR is discarded.
		"""
		try :
			self._mappedrule = mappedrule
		except Exception as e:
			raise e

	@property
	def excluderule(self) :
		r"""The expression to select the criteria for eliminating the corresponding ipv6 addresses from the response.
		"""
		try :
			return self._excluderule
		except Exception as e:
			raise e

	@excluderule.setter
	def excluderule(self, excluderule) :
		r"""The expression to select the criteria for eliminating the corresponding ipv6 addresses from the response.
		"""
		try :
			self._excluderule = excluderule
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

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsaction64_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsaction64
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.actionname is not None :
				return str(self.actionname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add dnsaction64.
		"""
		try :
			if type(resource) is not list :
				addresource = dnsaction64()
				addresource.actionname = resource.actionname
				addresource.prefix = resource.prefix
				addresource.mappedrule = resource.mappedrule
				addresource.excluderule = resource.excluderule
				addresource.feature = resource.feature
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnsaction64() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].actionname = resource[i].actionname
						addresources[i].prefix = resource[i].prefix
						addresources[i].mappedrule = resource[i].mappedrule
						addresources[i].excluderule = resource[i].excluderule
						addresources[i].feature = resource[i].feature
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete dnsaction64.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnsaction64()
				if type(resource) !=  type(deleteresource):
					deleteresource.actionname = resource
				else :
					deleteresource.actionname = resource.actionname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsaction64() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].actionname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsaction64() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].actionname = resource[i].actionname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update dnsaction64.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnsaction64()
				updateresource.actionname = resource.actionname
				updateresource.prefix = resource.prefix
				updateresource.mappedrule = resource.mappedrule
				updateresource.excluderule = resource.excluderule
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnsaction64() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].actionname = resource[i].actionname
						updateresources[i].prefix = resource[i].prefix
						updateresources[i].mappedrule = resource[i].mappedrule
						updateresources[i].excluderule = resource[i].excluderule
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of dnsaction64 resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnsaction64()
				if type(resource) !=  type(unsetresource):
					unsetresource.actionname = resource
				else :
					unsetresource.actionname = resource.actionname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnsaction64() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].actionname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnsaction64() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].actionname = resource[i].actionname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the dnsaction64 resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsaction64()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = dnsaction64()
					obj.actionname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [dnsaction64() for _ in range(len(name))]
						obj = [dnsaction64() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = dnsaction64()
							obj[i].actionname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of dnsaction64 resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsaction64()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the dnsaction64 resources configured on NetScaler.
		"""
		try :
			obj = dnsaction64()
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
		r""" Use this API to count filtered the set of dnsaction64 resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsaction64()
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

class dnsaction64_response(base_response) :
	def __init__(self, length=1) :
		self.dnsaction64 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsaction64 = [dnsaction64() for _ in range(length)]

