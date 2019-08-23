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

class streamidentifier(base_resource) :
	""" Configuration for identifier resource. """
	def __init__(self) :
		self._name = None
		self._selectorname = None
		self._interval = None
		self._samplecount = None
		self._sort = None
		self._snmptrap = None
		self._appflowlog = None
		self._trackackonlypackets = None
		self._tracktransactions = None
		self._maxtransactionthreshold = None
		self._mintransactionthreshold = None
		self._acceptancethreshold = None
		self._breachthreshold = None
		self._feature = None
		self._rule = None
		self.___count = None

	@property
	def name(self) :
		r"""The name of stream identifier.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""The name of stream identifier.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def selectorname(self) :
		r"""Name of the selector to use with the stream identifier.<br/>Minimum length =  1.
		"""
		try :
			return self._selectorname
		except Exception as e:
			raise e

	@selectorname.setter
	def selectorname(self, selectorname) :
		r"""Name of the selector to use with the stream identifier.<br/>Minimum length =  1
		"""
		try :
			self._selectorname = selectorname
		except Exception as e:
			raise e

	@property
	def interval(self) :
		r"""Number of minutes of data to use when calculating session statistics (number of requests, bandwidth, and response times). The interval is a moving window that keeps the most recently collected data. Older data is discarded at regular intervals.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._interval
		except Exception as e:
			raise e

	@interval.setter
	def interval(self, interval) :
		r"""Number of minutes of data to use when calculating session statistics (number of requests, bandwidth, and response times). The interval is a moving window that keeps the most recently collected data. Older data is discarded at regular intervals.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._interval = interval
		except Exception as e:
			raise e

	@property
	def samplecount(self) :
		r"""Size of the sample from which to select a request for evaluation. The smaller the sample count, the more accurate is the statistical data. To evaluate all requests, set the sample count to 1. However, such a low setting can result in excessive consumption of memory and processing resources.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._samplecount
		except Exception as e:
			raise e

	@samplecount.setter
	def samplecount(self, samplecount) :
		r"""Size of the sample from which to select a request for evaluation. The smaller the sample count, the more accurate is the statistical data. To evaluate all requests, set the sample count to 1. However, such a low setting can result in excessive consumption of memory and processing resources.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._samplecount = samplecount
		except Exception as e:
			raise e

	@property
	def sort(self) :
		r"""Sort stored records by the specified statistics column, in descending order. Performed during data collection, the sorting enables real-time data evaluation through Citrix ADC policies (for example, compression and caching policies) that use functions such as IS_TOP(n).<br/>Default value: REQUESTS<br/>Possible values = REQUESTS, CONNECTIONS, RESPTIME, BANDWIDTH, RESPTIME_BREACHES, NONE.
		"""
		try :
			return self._sort
		except Exception as e:
			raise e

	@sort.setter
	def sort(self, sort) :
		r"""Sort stored records by the specified statistics column, in descending order. Performed during data collection, the sorting enables real-time data evaluation through Citrix ADC policies (for example, compression and caching policies) that use functions such as IS_TOP(n).<br/>Default value: REQUESTS<br/>Possible values = REQUESTS, CONNECTIONS, RESPTIME, BANDWIDTH, RESPTIME_BREACHES, NONE
		"""
		try :
			self._sort = sort
		except Exception as e:
			raise e

	@property
	def snmptrap(self) :
		r"""Enable/disable SNMP trap for stream identifier.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._snmptrap
		except Exception as e:
			raise e

	@snmptrap.setter
	def snmptrap(self, snmptrap) :
		r"""Enable/disable SNMP trap for stream identifier.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._snmptrap = snmptrap
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		r"""Enable/disable Appflow logging for stream identifier.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		r"""Enable/disable Appflow logging for stream identifier.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def trackackonlypackets(self) :
		r"""Track ack only packets as well. This setting is applicable only when packet rate limiting is being used.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._trackackonlypackets
		except Exception as e:
			raise e

	@trackackonlypackets.setter
	def trackackonlypackets(self, trackackonlypackets) :
		r"""Track ack only packets as well. This setting is applicable only when packet rate limiting is being used.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._trackackonlypackets = trackackonlypackets
		except Exception as e:
			raise e

	@property
	def tracktransactions(self) :
		r"""Track transactions exceeding configured threshold. Transaction tracking can be enabled for following metric: ResponseTime.
		By default transaction tracking is disabled.<br/>Default value: NONE<br/>Possible values = RESPTIME, NONE.
		"""
		try :
			return self._tracktransactions
		except Exception as e:
			raise e

	@tracktransactions.setter
	def tracktransactions(self, tracktransactions) :
		r"""Track transactions exceeding configured threshold. Transaction tracking can be enabled for following metric: ResponseTime.
		By default transaction tracking is disabled.<br/>Default value: NONE<br/>Possible values = RESPTIME, NONE
		"""
		try :
			self._tracktransactions = tracktransactions
		except Exception as e:
			raise e

	@property
	def maxtransactionthreshold(self) :
		r"""Maximum per transcation value of metric. Metric to be tracked is specified by tracktransactions attribute.<br/>Default value: 0.
		"""
		try :
			return self._maxtransactionthreshold
		except Exception as e:
			raise e

	@maxtransactionthreshold.setter
	def maxtransactionthreshold(self, maxtransactionthreshold) :
		r"""Maximum per transcation value of metric. Metric to be tracked is specified by tracktransactions attribute.<br/>Default value: 0
		"""
		try :
			self._maxtransactionthreshold = maxtransactionthreshold
		except Exception as e:
			raise e

	@property
	def mintransactionthreshold(self) :
		r"""Minimum per transcation value of metric. Metric to be tracked is specified by tracktransactions attribute.<br/>Default value: 0.
		"""
		try :
			return self._mintransactionthreshold
		except Exception as e:
			raise e

	@mintransactionthreshold.setter
	def mintransactionthreshold(self, mintransactionthreshold) :
		r"""Minimum per transcation value of metric. Metric to be tracked is specified by tracktransactions attribute.<br/>Default value: 0
		"""
		try :
			self._mintransactionthreshold = mintransactionthreshold
		except Exception as e:
			raise e

	@property
	def acceptancethreshold(self) :
		r"""Non-Breaching transactions to Total transactions threshold expressed in percent.
		Maximum of 6 decimal places is supported.<br/>Default value: 0.000000<br/>Maximum length =  10.
		"""
		try :
			return self._acceptancethreshold
		except Exception as e:
			raise e

	@acceptancethreshold.setter
	def acceptancethreshold(self, acceptancethreshold) :
		r"""Non-Breaching transactions to Total transactions threshold expressed in percent.
		Maximum of 6 decimal places is supported.<br/>Default value: 0.000000<br/>Maximum length =  10
		"""
		try :
			self._acceptancethreshold = acceptancethreshold
		except Exception as e:
			raise e

	@property
	def breachthreshold(self) :
		r"""Breaching transactions threshold calculated over interval.<br/>Default value: 0.
		"""
		try :
			return self._breachthreshold
		except Exception as e:
			raise e

	@breachthreshold.setter
	def breachthreshold(self, breachthreshold) :
		r"""Breaching transactions threshold calculated over interval.<br/>Default value: 0
		"""
		try :
			self._breachthreshold = breachthreshold
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
	def rule(self) :
		r"""Rule.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(streamidentifier_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.streamidentifier
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
		r""" Use this API to add streamidentifier.
		"""
		try :
			if type(resource) is not list :
				addresource = streamidentifier()
				addresource.name = resource.name
				addresource.selectorname = resource.selectorname
				addresource.interval = resource.interval
				addresource.samplecount = resource.samplecount
				addresource.sort = resource.sort
				addresource.snmptrap = resource.snmptrap
				addresource.appflowlog = resource.appflowlog
				addresource.trackackonlypackets = resource.trackackonlypackets
				addresource.tracktransactions = resource.tracktransactions
				addresource.maxtransactionthreshold = resource.maxtransactionthreshold
				addresource.mintransactionthreshold = resource.mintransactionthreshold
				addresource.acceptancethreshold = resource.acceptancethreshold
				addresource.breachthreshold = resource.breachthreshold
				addresource.feature = resource.feature
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ streamidentifier() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].selectorname = resource[i].selectorname
						addresources[i].interval = resource[i].interval
						addresources[i].samplecount = resource[i].samplecount
						addresources[i].sort = resource[i].sort
						addresources[i].snmptrap = resource[i].snmptrap
						addresources[i].appflowlog = resource[i].appflowlog
						addresources[i].trackackonlypackets = resource[i].trackackonlypackets
						addresources[i].tracktransactions = resource[i].tracktransactions
						addresources[i].maxtransactionthreshold = resource[i].maxtransactionthreshold
						addresources[i].mintransactionthreshold = resource[i].mintransactionthreshold
						addresources[i].acceptancethreshold = resource[i].acceptancethreshold
						addresources[i].breachthreshold = resource[i].breachthreshold
						addresources[i].feature = resource[i].feature
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update streamidentifier.
		"""
		try :
			if type(resource) is not list :
				updateresource = streamidentifier()
				updateresource.name = resource.name
				updateresource.selectorname = resource.selectorname
				updateresource.interval = resource.interval
				updateresource.samplecount = resource.samplecount
				updateresource.sort = resource.sort
				updateresource.snmptrap = resource.snmptrap
				updateresource.appflowlog = resource.appflowlog
				updateresource.trackackonlypackets = resource.trackackonlypackets
				updateresource.tracktransactions = resource.tracktransactions
				updateresource.maxtransactionthreshold = resource.maxtransactionthreshold
				updateresource.mintransactionthreshold = resource.mintransactionthreshold
				updateresource.acceptancethreshold = resource.acceptancethreshold
				updateresource.breachthreshold = resource.breachthreshold
				updateresource.feature = resource.feature
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ streamidentifier() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].selectorname = resource[i].selectorname
						updateresources[i].interval = resource[i].interval
						updateresources[i].samplecount = resource[i].samplecount
						updateresources[i].sort = resource[i].sort
						updateresources[i].snmptrap = resource[i].snmptrap
						updateresources[i].appflowlog = resource[i].appflowlog
						updateresources[i].trackackonlypackets = resource[i].trackackonlypackets
						updateresources[i].tracktransactions = resource[i].tracktransactions
						updateresources[i].maxtransactionthreshold = resource[i].maxtransactionthreshold
						updateresources[i].mintransactionthreshold = resource[i].mintransactionthreshold
						updateresources[i].acceptancethreshold = resource[i].acceptancethreshold
						updateresources[i].breachthreshold = resource[i].breachthreshold
						updateresources[i].feature = resource[i].feature
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of streamidentifier resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = streamidentifier()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ streamidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ streamidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete streamidentifier.
		"""
		try :
			if type(resource) is not list :
				deleteresource = streamidentifier()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ streamidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ streamidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the streamidentifier resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = streamidentifier()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = streamidentifier()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [streamidentifier() for _ in range(len(name))]
						obj = [streamidentifier() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = streamidentifier()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of streamidentifier resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = streamidentifier()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the streamidentifier resources configured on NetScaler.
		"""
		try :
			obj = streamidentifier()
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
		r""" Use this API to count filtered the set of streamidentifier resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = streamidentifier()
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

	class Snmptrap:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Trackackonlypackets:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tracktransactions:
		RESPTIME = "RESPTIME"
		NONE = "NONE"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sort:
		REQUESTS = "REQUESTS"
		CONNECTIONS = "CONNECTIONS"
		RESPTIME = "RESPTIME"
		BANDWIDTH = "BANDWIDTH"
		RESPTIME_BREACHES = "RESPTIME_BREACHES"
		NONE = "NONE"

class streamidentifier_response(base_response) :
	def __init__(self, length=1) :
		self.streamidentifier = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.streamidentifier = [streamidentifier() for _ in range(length)]

