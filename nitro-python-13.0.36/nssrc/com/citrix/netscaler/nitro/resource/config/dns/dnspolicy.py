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

class dnspolicy(base_resource) :
	""" Configuration for DNS policy resource. """
	def __init__(self) :
		self._name = None
		self._rule = None
		self._viewname = None
		self._preferredlocation = None
		self._preferredloclist = None
		self._drop = None
		self._cachebypass = None
		self._actionname = None
		self._logaction = None
		self._feature = None
		self._hits = None
		self._undefhits = None
		self._description = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the DNS policy.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the DNS policy.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def rule(self) :
		r"""Expression against which DNS traffic is evaluated.
		Note:
		* On the command line interface, if the expression includes blank spaces, the entire expression must be enclosed in double quotation marks.
		* If the expression itself includes double quotation marks, you must escape the quotations by using the  character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks. 
		Example: CLIENT.UDP.DNS.DOMAIN.EQ("domainname").
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		r"""Expression against which DNS traffic is evaluated.
		Note:
		* On the command line interface, if the expression includes blank spaces, the entire expression must be enclosed in double quotation marks.
		* If the expression itself includes double quotation marks, you must escape the quotations by using the  character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks. 
		Example: CLIENT.UDP.DNS.DOMAIN.EQ("domainname").
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def viewname(self) :
		r"""The view name that must be used for the given policy.
		"""
		try :
			return self._viewname
		except Exception as e:
			raise e

	@viewname.setter
	def viewname(self, viewname) :
		r"""The view name that must be used for the given policy.
		"""
		try :
			self._viewname = viewname
		except Exception as e:
			raise e

	@property
	def preferredlocation(self) :
		r"""The location used for the given policy. This is deprecated attribute. Please use -prefLocList.
		"""
		try :
			return self._preferredlocation
		except Exception as e:
			raise e

	@preferredlocation.setter
	def preferredlocation(self, preferredlocation) :
		r"""The location used for the given policy. This is deprecated attribute. Please use -prefLocList.
		"""
		try :
			self._preferredlocation = preferredlocation
		except Exception as e:
			raise e

	@property
	def preferredloclist(self) :
		r"""The location list in priority order used for the given policy.<br/>Minimum length =  1.
		"""
		try :
			return self._preferredloclist
		except Exception as e:
			raise e

	@preferredloclist.setter
	def preferredloclist(self, preferredloclist) :
		r"""The location list in priority order used for the given policy.<br/>Minimum length =  1
		"""
		try :
			self._preferredloclist = preferredloclist
		except Exception as e:
			raise e

	@property
	def drop(self) :
		r"""The dns packet must be dropped.<br/>Possible values = YES, NO.
		"""
		try :
			return self._drop
		except Exception as e:
			raise e

	@drop.setter
	def drop(self, drop) :
		r"""The dns packet must be dropped.<br/>Possible values = YES, NO
		"""
		try :
			self._drop = drop
		except Exception as e:
			raise e

	@property
	def cachebypass(self) :
		r"""By pass dns cache for this.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachebypass
		except Exception as e:
			raise e

	@cachebypass.setter
	def cachebypass(self, cachebypass) :
		r"""By pass dns cache for this.<br/>Possible values = YES, NO
		"""
		try :
			self._cachebypass = cachebypass
		except Exception as e:
			raise e

	@property
	def actionname(self) :
		r"""Name of the DNS action to perform when the rule evaluates to TRUE. The built in actions function as follows:
		* dns_default_act_Drop. Drop the DNS request.
		* dns_default_act_Cachebypass. Bypass the DNS cache and forward the request to the name server.
		You can create custom actions by using the add dns action command in the CLI or the DNS > Actions > Create DNS Action dialog box in the Citrix ADC configuration utility.
		"""
		try :
			return self._actionname
		except Exception as e:
			raise e

	@actionname.setter
	def actionname(self, actionname) :
		r"""Name of the DNS action to perform when the rule evaluates to TRUE. The built in actions function as follows:
		* dns_default_act_Drop. Drop the DNS request.
		* dns_default_act_Cachebypass. Bypass the DNS cache and forward the request to the name server.
		You can create custom actions by using the add dns action command in the CLI or the DNS > Actions > Create DNS Action dialog box in the Citrix ADC configuration utility.
		"""
		try :
			self._actionname = actionname
		except Exception as e:
			raise e

	@property
	def logaction(self) :
		r"""Name of the messagelog action to use for requests that match this policy.
		"""
		try :
			return self._logaction
		except Exception as e:
			raise e

	@logaction.setter
	def logaction(self, logaction) :
		r"""Name of the messagelog action to use for requests that match this policy.
		"""
		try :
			self._logaction = logaction
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
	def hits(self) :
		r"""The number of times the policy has been hit.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def undefhits(self) :
		r"""Number of Undef hits.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def description(self) :
		r"""Description of the policy.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnspolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnspolicy
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
		r""" Use this API to add dnspolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = dnspolicy()
				addresource.name = resource.name
				addresource.rule = resource.rule
				addresource.viewname = resource.viewname
				addresource.preferredlocation = resource.preferredlocation
				addresource.preferredloclist = resource.preferredloclist
				addresource.drop = resource.drop
				addresource.cachebypass = resource.cachebypass
				addresource.actionname = resource.actionname
				addresource.logaction = resource.logaction
				addresource.feature = resource.feature
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnspolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].rule = resource[i].rule
						addresources[i].viewname = resource[i].viewname
						addresources[i].preferredlocation = resource[i].preferredlocation
						addresources[i].preferredloclist = resource[i].preferredloclist
						addresources[i].drop = resource[i].drop
						addresources[i].cachebypass = resource[i].cachebypass
						addresources[i].actionname = resource[i].actionname
						addresources[i].logaction = resource[i].logaction
						addresources[i].feature = resource[i].feature
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete dnspolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnspolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnspolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnspolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update dnspolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnspolicy()
				updateresource.name = resource.name
				updateresource.rule = resource.rule
				updateresource.viewname = resource.viewname
				updateresource.preferredlocation = resource.preferredlocation
				updateresource.preferredloclist = resource.preferredloclist
				updateresource.drop = resource.drop
				updateresource.cachebypass = resource.cachebypass
				updateresource.actionname = resource.actionname
				updateresource.logaction = resource.logaction
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnspolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].rule = resource[i].rule
						updateresources[i].viewname = resource[i].viewname
						updateresources[i].preferredlocation = resource[i].preferredlocation
						updateresources[i].preferredloclist = resource[i].preferredloclist
						updateresources[i].drop = resource[i].drop
						updateresources[i].cachebypass = resource[i].cachebypass
						updateresources[i].actionname = resource[i].actionname
						updateresources[i].logaction = resource[i].logaction
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of dnspolicy resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnspolicy()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnspolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnspolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the dnspolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnspolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = dnspolicy()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [dnspolicy() for _ in range(len(name))]
						obj = [dnspolicy() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = dnspolicy()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of dnspolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnspolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the dnspolicy resources configured on NetScaler.
		"""
		try :
			obj = dnspolicy()
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
		r""" Use this API to count filtered the set of dnspolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnspolicy()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Cachebypass:
		YES = "YES"
		NO = "NO"

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

	class Drop:
		YES = "YES"
		NO = "NO"

class dnspolicy_response(base_response) :
	def __init__(self, length=1) :
		self.dnspolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnspolicy = [dnspolicy() for _ in range(length)]

