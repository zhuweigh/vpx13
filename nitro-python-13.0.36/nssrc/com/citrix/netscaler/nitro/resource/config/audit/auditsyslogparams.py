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

class auditsyslogparams(base_resource) :
	""" Configuration for system log parameters resource. """
	def __init__(self) :
		self._serverip = None
		self._serverport = None
		self._dateformat = None
		self._loglevel = None
		self._logfacility = None
		self._tcp = None
		self._acl = None
		self._timezone = None
		self._userdefinedauditlog = None
		self._appflowexport = None
		self._feature = None
		self._lsn = None
		self._alg = None
		self._subscriberlog = None
		self._dns = None
		self._sslinterception = None
		self._urlfiltering = None

	@property
	def serverip(self) :
		r"""IP address of the syslog server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		r"""IP address of the syslog server.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		r"""Port on which the syslog server accepts connections.<br/>Minimum length =  1.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		r"""Port on which the syslog server accepts connections.<br/>Minimum length =  1
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def dateformat(self) :
		r"""Format of dates in the logs.
		Supported formats are: 
		* MMDDYYYY - U.S. style month/date/year format.
		* DDMMYYYY. European style  -date/month/year format.
		* YYYYMMDD - ISO style year/month/date format.<br/>Possible values = MMDDYYYY, DDMMYYYY, YYYYMMDD.
		"""
		try :
			return self._dateformat
		except Exception as e:
			raise e

	@dateformat.setter
	def dateformat(self, dateformat) :
		r"""Format of dates in the logs.
		Supported formats are: 
		* MMDDYYYY - U.S. style month/date/year format.
		* DDMMYYYY. European style  -date/month/year format.
		* YYYYMMDD - ISO style year/month/date format.<br/>Possible values = MMDDYYYY, DDMMYYYY, YYYYMMDD
		"""
		try :
			self._dateformat = dateformat
		except Exception as e:
			raise e

	@property
	def loglevel(self) :
		r"""Types of information to be logged. 
		Available settings function as follows: 
		* ALL - All events.
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.
		* NONE - No events.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG, NONE.
		"""
		try :
			return self._loglevel
		except Exception as e:
			raise e

	@loglevel.setter
	def loglevel(self, loglevel) :
		r"""Types of information to be logged. 
		Available settings function as follows: 
		* ALL - All events.
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.
		* NONE - No events.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG, NONE
		"""
		try :
			self._loglevel = loglevel
		except Exception as e:
			raise e

	@property
	def logfacility(self) :
		r"""Facility value, as defined in RFC 3164, assigned to the log message. 
		Log facility values are numbers 0 to 7 (LOCAL0 through LOCAL7). Each number indicates where a specific message originated from, such as the Citrix ADC itself, the VPN, or external.<br/>Possible values = LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7.
		"""
		try :
			return self._logfacility
		except Exception as e:
			raise e

	@logfacility.setter
	def logfacility(self, logfacility) :
		r"""Facility value, as defined in RFC 3164, assigned to the log message. 
		Log facility values are numbers 0 to 7 (LOCAL0 through LOCAL7). Each number indicates where a specific message originated from, such as the Citrix ADC itself, the VPN, or external.<br/>Possible values = LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7
		"""
		try :
			self._logfacility = logfacility
		except Exception as e:
			raise e

	@property
	def tcp(self) :
		r"""Log TCP messages.<br/>Possible values = NONE, ALL.
		"""
		try :
			return self._tcp
		except Exception as e:
			raise e

	@tcp.setter
	def tcp(self, tcp) :
		r"""Log TCP messages.<br/>Possible values = NONE, ALL
		"""
		try :
			self._tcp = tcp
		except Exception as e:
			raise e

	@property
	def acl(self) :
		r"""Log access control list (ACL) messages.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._acl
		except Exception as e:
			raise e

	@acl.setter
	def acl(self, acl) :
		r"""Log access control list (ACL) messages.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._acl = acl
		except Exception as e:
			raise e

	@property
	def timezone(self) :
		r"""Time zone used for date and timestamps in the logs. 
		Available settings function as follows: 
		* GMT_TIME - Coordinated Universal Time.
		* LOCAL_TIME  Use the server's timezone setting.<br/>Possible values = GMT_TIME, LOCAL_TIME.
		"""
		try :
			return self._timezone
		except Exception as e:
			raise e

	@timezone.setter
	def timezone(self, timezone) :
		r"""Time zone used for date and timestamps in the logs. 
		Available settings function as follows: 
		* GMT_TIME - Coordinated Universal Time.
		* LOCAL_TIME  Use the server's timezone setting.<br/>Possible values = GMT_TIME, LOCAL_TIME
		"""
		try :
			self._timezone = timezone
		except Exception as e:
			raise e

	@property
	def userdefinedauditlog(self) :
		r"""Log user-configurable log messages to syslog. 
		Setting this parameter to NO causes audit to ignore all user-configured message actions. Setting this parameter to YES causes audit to log user-configured message actions that meet the other logging criteria.<br/>Possible values = YES, NO.
		"""
		try :
			return self._userdefinedauditlog
		except Exception as e:
			raise e

	@userdefinedauditlog.setter
	def userdefinedauditlog(self, userdefinedauditlog) :
		r"""Log user-configurable log messages to syslog. 
		Setting this parameter to NO causes audit to ignore all user-configured message actions. Setting this parameter to YES causes audit to log user-configured message actions that meet the other logging criteria.<br/>Possible values = YES, NO
		"""
		try :
			self._userdefinedauditlog = userdefinedauditlog
		except Exception as e:
			raise e

	@property
	def appflowexport(self) :
		r"""Export log messages to AppFlow collectors.
		Appflow collectors are entities to which log messages can be sent so that some action can be performed on them.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowexport
		except Exception as e:
			raise e

	@appflowexport.setter
	def appflowexport(self, appflowexport) :
		r"""Export log messages to AppFlow collectors.
		Appflow collectors are entities to which log messages can be sent so that some action can be performed on them.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowexport = appflowexport
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
	def lsn(self) :
		r"""Log the LSN messages.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._lsn
		except Exception as e:
			raise e

	@lsn.setter
	def lsn(self, lsn) :
		r"""Log the LSN messages.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._lsn = lsn
		except Exception as e:
			raise e

	@property
	def alg(self) :
		r"""Log the ALG messages.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._alg
		except Exception as e:
			raise e

	@alg.setter
	def alg(self, alg) :
		r"""Log the ALG messages.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._alg = alg
		except Exception as e:
			raise e

	@property
	def subscriberlog(self) :
		r"""Log subscriber session event information.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._subscriberlog
		except Exception as e:
			raise e

	@subscriberlog.setter
	def subscriberlog(self, subscriberlog) :
		r"""Log subscriber session event information.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._subscriberlog = subscriberlog
		except Exception as e:
			raise e

	@property
	def dns(self) :
		r"""Log DNS related syslog messages.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dns
		except Exception as e:
			raise e

	@dns.setter
	def dns(self, dns) :
		r"""Log DNS related syslog messages.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dns = dns
		except Exception as e:
			raise e

	@property
	def sslinterception(self) :
		r"""Log SSL Interceptionn event information.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslinterception
		except Exception as e:
			raise e

	@sslinterception.setter
	def sslinterception(self, sslinterception) :
		r"""Log SSL Interceptionn event information.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslinterception = sslinterception
		except Exception as e:
			raise e

	@property
	def urlfiltering(self) :
		r"""Log URL filtering event information.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._urlfiltering
		except Exception as e:
			raise e

	@urlfiltering.setter
	def urlfiltering(self, urlfiltering) :
		r"""Log URL filtering event information.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._urlfiltering = urlfiltering
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(auditsyslogparams_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.auditsyslogparams
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
		r""" Use this API to update auditsyslogparams.
		"""
		try :
			if type(resource) is not list :
				updateresource = auditsyslogparams()
				updateresource.serverip = resource.serverip
				updateresource.serverport = resource.serverport
				updateresource.dateformat = resource.dateformat
				updateresource.loglevel = resource.loglevel
				updateresource.logfacility = resource.logfacility
				updateresource.tcp = resource.tcp
				updateresource.acl = resource.acl
				updateresource.timezone = resource.timezone
				updateresource.userdefinedauditlog = resource.userdefinedauditlog
				updateresource.appflowexport = resource.appflowexport
				updateresource.feature = resource.feature
				updateresource.lsn = resource.lsn
				updateresource.alg = resource.alg
				updateresource.subscriberlog = resource.subscriberlog
				updateresource.dns = resource.dns
				updateresource.sslinterception = resource.sslinterception
				updateresource.urlfiltering = resource.urlfiltering
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of auditsyslogparams resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = auditsyslogparams()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the auditsyslogparams resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = auditsyslogparams()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Timezone:
		GMT_TIME = "GMT_TIME"
		LOCAL_TIME = "LOCAL_TIME"

	class Acl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Subscriberlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Logfacility:
		LOCAL0 = "LOCAL0"
		LOCAL1 = "LOCAL1"
		LOCAL2 = "LOCAL2"
		LOCAL3 = "LOCAL3"
		LOCAL4 = "LOCAL4"
		LOCAL5 = "LOCAL5"
		LOCAL6 = "LOCAL6"
		LOCAL7 = "LOCAL7"

	class Sslinterception:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Urlfiltering:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dns:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

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

	class Userdefinedauditlog:
		YES = "YES"
		NO = "NO"

	class Dateformat:
		MMDDYYYY = "MMDDYYYY"
		DDMMYYYY = "DDMMYYYY"
		YYYYMMDD = "YYYYMMDD"

	class Lsn:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Alg:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Loglevel:
		ALL = "ALL"
		EMERGENCY = "EMERGENCY"
		ALERT = "ALERT"
		CRITICAL = "CRITICAL"
		ERROR = "ERROR"
		WARNING = "WARNING"
		NOTICE = "NOTICE"
		INFORMATIONAL = "INFORMATIONAL"
		DEBUG = "DEBUG"
		NONE = "NONE"

	class Tcp:
		NONE = "NONE"
		ALL = "ALL"

	class Appflowexport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class auditsyslogparams_response(base_response) :
	def __init__(self, length=1) :
		self.auditsyslogparams = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.auditsyslogparams = [auditsyslogparams() for _ in range(length)]

