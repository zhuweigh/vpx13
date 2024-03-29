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

class cachepolicy(base_resource) :
	""" Configuration for Integrated Cache policy resource. """
	def __init__(self) :
		self._policyname = None
		self._rule = None
		self._action = None
		self._storeingroup = None
		self._invalgroups = None
		self._invalobjects = None
		self._undefaction = None
		self._feature = None
		self._newname = None
		self._hits = None
		self._undefhits = None
		self._flags = None
		self.___count = None

	@property
	def policyname(self) :
		r"""Name for the policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the policy is created.<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		r"""Name for the policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the policy is created.<br/>Minimum length =  1
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def rule(self) :
		r"""Expression against which the traffic is evaluated.
		The following requirements apply only to the Citrix ADC CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		r"""Expression against which the traffic is evaluated.
		The following requirements apply only to the Citrix ADC CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def action(self) :
		r"""Action to apply to content that matches the policy. 
		* CACHE or MAY_CACHE action - positive cachability policy
		* NOCACHE or MAY_NOCACHE action - negative cachability policy
		* INVAL action - Dynamic Invalidation Policy.<br/>Possible values = CACHE, NOCACHE, MAY_CACHE, MAY_NOCACHE, INVAL.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		r"""Action to apply to content that matches the policy. 
		* CACHE or MAY_CACHE action - positive cachability policy
		* NOCACHE or MAY_NOCACHE action - negative cachability policy
		* INVAL action - Dynamic Invalidation Policy.<br/>Possible values = CACHE, NOCACHE, MAY_CACHE, MAY_NOCACHE, INVAL
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def storeingroup(self) :
		r"""Name of the content group in which to store the object when the final result of policy evaluation is CACHE. The content group must exist before being mentioned here. Use the "show cache contentgroup" command to view the list of existing content groups.<br/>Minimum length =  1.
		"""
		try :
			return self._storeingroup
		except Exception as e:
			raise e

	@storeingroup.setter
	def storeingroup(self, storeingroup) :
		r"""Name of the content group in which to store the object when the final result of policy evaluation is CACHE. The content group must exist before being mentioned here. Use the "show cache contentgroup" command to view the list of existing content groups.<br/>Minimum length =  1
		"""
		try :
			self._storeingroup = storeingroup
		except Exception as e:
			raise e

	@property
	def invalgroups(self) :
		r"""Content group(s) to be invalidated when the INVAL action is applied. Maximum number of content groups that can be specified is 16.<br/>Minimum length =  1.
		"""
		try :
			return self._invalgroups
		except Exception as e:
			raise e

	@invalgroups.setter
	def invalgroups(self, invalgroups) :
		r"""Content group(s) to be invalidated when the INVAL action is applied. Maximum number of content groups that can be specified is 16.<br/>Minimum length =  1
		"""
		try :
			self._invalgroups = invalgroups
		except Exception as e:
			raise e

	@property
	def invalobjects(self) :
		r"""Content groups(s) in which the objects will be invalidated if the action is INVAL.<br/>Minimum length =  1.
		"""
		try :
			return self._invalobjects
		except Exception as e:
			raise e

	@invalobjects.setter
	def invalobjects(self, invalobjects) :
		r"""Content groups(s) in which the objects will be invalidated if the action is INVAL.<br/>Minimum length =  1
		"""
		try :
			self._invalobjects = invalobjects
		except Exception as e:
			raise e

	@property
	def undefaction(self) :
		r"""Action to be performed when the result of rule evaluation is undefined.<br/>Possible values = NOCACHE, RESET.
		"""
		try :
			return self._undefaction
		except Exception as e:
			raise e

	@undefaction.setter
	def undefaction(self, undefaction) :
		r"""Action to be performed when the result of rule evaluation is undefined.<br/>Possible values = NOCACHE, RESET
		"""
		try :
			self._undefaction = undefaction
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
	def newname(self) :
		r"""New name for the cache policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the cache policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""Hits.
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
	def flags(self) :
		r"""Flag.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cachepolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cachepolicy
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.policyname is not None :
				return str(self.policyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add cachepolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = cachepolicy()
				addresource.policyname = resource.policyname
				addresource.rule = resource.rule
				addresource.action = resource.action
				addresource.storeingroup = resource.storeingroup
				addresource.invalgroups = resource.invalgroups
				addresource.invalobjects = resource.invalobjects
				addresource.undefaction = resource.undefaction
				addresource.feature = resource.feature
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ cachepolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].policyname = resource[i].policyname
						addresources[i].rule = resource[i].rule
						addresources[i].action = resource[i].action
						addresources[i].storeingroup = resource[i].storeingroup
						addresources[i].invalgroups = resource[i].invalgroups
						addresources[i].invalobjects = resource[i].invalobjects
						addresources[i].undefaction = resource[i].undefaction
						addresources[i].feature = resource[i].feature
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete cachepolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = cachepolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.policyname = resource
				else :
					deleteresource.policyname = resource.policyname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ cachepolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ cachepolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i].policyname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update cachepolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = cachepolicy()
				updateresource.policyname = resource.policyname
				updateresource.rule = resource.rule
				updateresource.action = resource.action
				updateresource.storeingroup = resource.storeingroup
				updateresource.invalgroups = resource.invalgroups
				updateresource.invalobjects = resource.invalobjects
				updateresource.undefaction = resource.undefaction
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ cachepolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].rule = resource[i].rule
						updateresources[i].action = resource[i].action
						updateresources[i].storeingroup = resource[i].storeingroup
						updateresources[i].invalgroups = resource[i].invalgroups
						updateresources[i].invalobjects = resource[i].invalobjects
						updateresources[i].undefaction = resource[i].undefaction
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of cachepolicy resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = cachepolicy()
				if type(resource) !=  type(unsetresource):
					unsetresource.policyname = resource
				else :
					unsetresource.policyname = resource.policyname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ cachepolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].policyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ cachepolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].policyname = resource[i].policyname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_policyname) :
		r""" Use this API to rename a cachepolicy resource.
		"""
		try :
			renameresource = cachepolicy()
			if type(resource) == cls :
				renameresource.policyname = resource.policyname
			else :
				renameresource.policyname = resource
			return renameresource.rename_resource(client,new_policyname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the cachepolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cachepolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = cachepolicy()
					obj.policyname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [cachepolicy() for _ in range(len(name))]
						obj = [cachepolicy() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = cachepolicy()
							obj[i].policyname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of cachepolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cachepolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the cachepolicy resources configured on NetScaler.
		"""
		try :
			obj = cachepolicy()
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
		r""" Use this API to count filtered the set of cachepolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cachepolicy()
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

	class Undefaction:
		NOCACHE = "NOCACHE"
		RESET = "RESET"

	class Action:
		CACHE = "CACHE"
		NOCACHE = "NOCACHE"
		MAY_CACHE = "MAY_CACHE"
		MAY_NOCACHE = "MAY_NOCACHE"
		INVAL = "INVAL"

class cachepolicy_response(base_response) :
	def __init__(self, length=1) :
		self.cachepolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cachepolicy = [cachepolicy() for _ in range(length)]

