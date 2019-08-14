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

class tunnelglobal_tunneltrafficpolicy_binding(base_resource) :
	""" Binding class showing the tunneltrafficpolicy that can be bound to tunnelglobal.
	"""
	def __init__(self) :
		self._policyname = None
		self._priority = None
		self._state = None
		self._feature = None
		self._type = None
		self._numpol = None
		self._gotopriorityexpression = None
		self._policytype = None
		self._globalbindtype = None
		self.___count = None

	@property
	def priority(self) :
		r"""Priority.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""Priority.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def globalbindtype(self) :
		r""".<br/>Default value: SYSTEM_GLOBAL<br/>Possible values = SYSTEM_GLOBAL, VPN_GLOBAL, RNAT_GLOBAL.
		"""
		try :
			return self._globalbindtype
		except Exception as e:
			raise e

	@globalbindtype.setter
	def globalbindtype(self, globalbindtype) :
		r""".<br/>Default value: SYSTEM_GLOBAL<br/>Possible values = SYSTEM_GLOBAL, VPN_GLOBAL, RNAT_GLOBAL
		"""
		try :
			self._globalbindtype = globalbindtype
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		r"""Policy name.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		r"""Policy name.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Current state of the binding. If the binding is enabled, the policy is active.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Current state of the binding. If the binding is enabled, the policy is active.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
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
	def gotopriorityexpression(self) :
		r"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		r"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Bind point to which the policy is bound.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Bind point to which the policy is bound.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def numpol(self) :
		r"""The number of policies bound to the bindpoint.
		"""
		try :
			return self._numpol
		except Exception as e:
			raise e

	@property
	def policytype(self) :
		r"""Policy type (Classic/Advanced) to be bound.Used for display.<br/>Possible values = Classic Policy, Advanced Policy.
		"""
		try :
			return self._policytype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(tunnelglobal_tunneltrafficpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tunnelglobal_tunneltrafficpolicy_binding
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
				updateresource = tunnelglobal_tunneltrafficpolicy_binding()
				updateresource.policyname = resource.policyname
				updateresource.priority = resource.priority
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.state = resource.state
				updateresource.type = resource.type
				updateresource.feature = resource.feature
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [tunnelglobal_tunneltrafficpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].priority = resource[i].priority
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
						updateresources[i].state = resource[i].state
						updateresources[i].type = resource[i].type
						updateresources[i].feature = resource[i].feature
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = tunnelglobal_tunneltrafficpolicy_binding()
				deleteresource.policyname = resource.policyname
				deleteresource.type = resource.type
				deleteresource.priority = resource.priority
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [tunnelglobal_tunneltrafficpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].policyname = resource[i].policyname
						deleteresources[i].type = resource[i].type
						deleteresources[i].priority = resource[i].priority
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		r""" Use this API to fetch a tunnelglobal_tunneltrafficpolicy_binding resources.
		"""
		try :
			obj = tunnelglobal_tunneltrafficpolicy_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		r""" Use this API to fetch filtered set of tunnelglobal_tunneltrafficpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = tunnelglobal_tunneltrafficpolicy_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		r""" Use this API to count tunnelglobal_tunneltrafficpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = tunnelglobal_tunneltrafficpolicy_binding()
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
		r""" Use this API to count the filtered set of tunnelglobal_tunneltrafficpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = tunnelglobal_tunneltrafficpolicy_binding()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
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

	class Globalbindtype:
		SYSTEM_GLOBAL = "SYSTEM_GLOBAL"
		VPN_GLOBAL = "VPN_GLOBAL"
		RNAT_GLOBAL = "RNAT_GLOBAL"

	class Type:
		REQ_OVERRIDE = "REQ_OVERRIDE"
		REQ_DEFAULT = "REQ_DEFAULT"
		RES_OVERRIDE = "RES_OVERRIDE"
		RES_DEFAULT = "RES_DEFAULT"

	class Policytype:
		Classic_Policy = "Classic Policy"
		Advanced_Policy = "Advanced Policy"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class tunnelglobal_tunneltrafficpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.tunnelglobal_tunneltrafficpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.tunnelglobal_tunneltrafficpolicy_binding = [tunnelglobal_tunneltrafficpolicy_binding() for _ in range(length)]

