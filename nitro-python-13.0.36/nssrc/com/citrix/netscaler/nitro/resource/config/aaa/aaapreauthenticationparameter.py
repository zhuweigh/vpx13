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

class aaapreauthenticationparameter(base_resource) :
	""" Configuration for pre authentication parameter resource. """
	def __init__(self) :
		self._preauthenticationaction = None
		self._rule = None
		self._killprocess = None
		self._deletefiles = None
		self._feature = None

	@property
	def preauthenticationaction(self) :
		r"""Deny or allow login on the basis of end point analysis results.<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._preauthenticationaction
		except Exception as e:
			raise e

	@preauthenticationaction.setter
	def preauthenticationaction(self, preauthenticationaction) :
		r"""Deny or allow login on the basis of end point analysis results.<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._preauthenticationaction = preauthenticationaction
		except Exception as e:
			raise e

	@property
	def rule(self) :
		r"""Name of the Citrix ADC named rule, or an expression, to be evaluated by the EPA tool.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		r"""Name of the Citrix ADC named rule, or an expression, to be evaluated by the EPA tool.
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def killprocess(self) :
		r"""String specifying the name of a process to be terminated by the EPA tool.
		"""
		try :
			return self._killprocess
		except Exception as e:
			raise e

	@killprocess.setter
	def killprocess(self, killprocess) :
		r"""String specifying the name of a process to be terminated by the EPA tool.
		"""
		try :
			self._killprocess = killprocess
		except Exception as e:
			raise e

	@property
	def deletefiles(self) :
		r"""String specifying the path(s) to and name(s) of the files to be deleted by the EPA tool, as a string of between 1 and 1023 characters.
		"""
		try :
			return self._deletefiles
		except Exception as e:
			raise e

	@deletefiles.setter
	def deletefiles(self, deletefiles) :
		r"""String specifying the path(s) to and name(s) of the files to be deleted by the EPA tool, as a string of between 1 and 1023 characters.
		"""
		try :
			self._deletefiles = deletefiles
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
			result = service.payload_formatter.string_to_resource(aaapreauthenticationparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaapreauthenticationparameter
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
		r""" Use this API to update aaapreauthenticationparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = aaapreauthenticationparameter()
				updateresource.preauthenticationaction = resource.preauthenticationaction
				updateresource.rule = resource.rule
				updateresource.killprocess = resource.killprocess
				updateresource.deletefiles = resource.deletefiles
				updateresource.feature = resource.feature
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of aaapreauthenticationparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = aaapreauthenticationparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the aaapreauthenticationparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaapreauthenticationparameter()
				response = obj.get_resources(client, option_)
			return response
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

	class Preauthenticationaction:
		ALLOW = "ALLOW"
		DENY = "DENY"

class aaapreauthenticationparameter_response(base_response) :
	def __init__(self, length=1) :
		self.aaapreauthenticationparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaapreauthenticationparameter = [aaapreauthenticationparameter() for _ in range(length)]

