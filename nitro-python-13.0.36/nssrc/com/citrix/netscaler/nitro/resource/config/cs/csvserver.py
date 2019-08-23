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

class csvserver(base_resource) :
	""" Configuration for CS virtual server resource. """
	def __init__(self) :
		self._name = None
		self._td = None
		self._servicetype = None
		self._ipv46 = None
		self._targettype = None
		self._dnsrecordtype = None
		self._persistenceid = None
		self._ippattern = None
		self._ipmask = None
		self._range = None
		self._port = None
		self._ipset = None
		self._state = None
		self._stateupdate = None
		self._cacheable = None
		self._redirecturl = None
		self._clttimeout = None
		self._precedence = None
		self._casesensitive = None
		self._somethod = None
		self._sopersistence = None
		self._sopersistencetimeout = None
		self._sothreshold = None
		self._sobackupaction = None
		self._redirectportrewrite = None
		self._downstateflush = None
		self._backupvserver = None
		self._disableprimaryondown = None
		self._insertvserveripport = None
		self._vipheader = None
		self._rtspnat = None
		self._authenticationhost = None
		self._authentication = None
		self._listenpolicy = None
		self._listenpriority = None
		self._authn401 = None
		self._authnvsname = None
		self._push = None
		self._pushvserver = None
		self._pushlabel = None
		self._pushmulticlients = None
		self._tcpprofilename = None
		self._httpprofilename = None
		self._dbprofilename = None
		self._oracleserverversion = None
		self._comment = None
		self._mssqlserverversion = None
		self._l2conn = None
		self._mysqlprotocolversion = None
		self._mysqlserverversion = None
		self._mysqlcharacterset = None
		self._mysqlservercapabilities = None
		self._appflowlog = None
		self._netprofile = None
		self._icmpvsrresponse = None
		self._rhistate = None
		self._authnprofile = None
		self._dnsprofilename = None
		self._persistencetype = None
		self._persistmask = None
		self._v6persistmasklen = None
		self._timeout = None
		self._cookiename = None
		self._persistencebackup = None
		self._backuppersistencetimeout = None
		self._domainname = None
		self._ttl = None
		self._backupip = None
		self._cookiedomain = None
		self._cookietimeout = None
		self._sitedomainttl = None
		self._newname = None
		self._ip = None
		self._value = None
		self._ngname = None
		self._type = None
		self._curstate = None
		self._sc = None
		self._status = None
		self._cachetype = None
		self._redirect = None
		self._homepage = None
		self._dnsvservername = None
		self._domain = None
		self._policyname = None
		self._servicename = None
		self._weight = None
		self._cachevserver = None
		self._targetvserver = None
		self._priority = None
		self._url = None
		self._gotopriorityexpression = None
		self._bindpoint = None
		self._invoke = None
		self._labeltype = None
		self._labelname = None
		self._gt2gb = None
		self._statechangetimesec = None
		self._statechangetimemsec = None
		self._tickssincelaststatechange = None
		self._ruletype = None
		self._lbvserver = None
		self._targetlbvserver = None
		self._analyticsprofile = None
		self._nodefaultbindings = None
		self._version = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the content switching virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. 
		Cannot be changed after the CS virtual server is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, my server or my server).<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the content switching virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. 
		Cannot be changed after the CS virtual server is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, my server or my server).<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		r"""Protocol used by the virtual server.<br/>Possible values = HTTP, SSL, TCP, FTP, RTSP, SSL_TCP, UDP, DNS, SIP_UDP, SIP_TCP, SIP_SSL, ANY, RADIUS, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, DNS_TCP, ORACLE, SMPP, PROXY.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@servicetype.setter
	def servicetype(self, servicetype) :
		r"""Protocol used by the virtual server.<br/>Possible values = HTTP, SSL, TCP, FTP, RTSP, SSL_TCP, UDP, DNS, SIP_UDP, SIP_TCP, SIP_SSL, ANY, RADIUS, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, DNS_TCP, ORACLE, SMPP, PROXY
		"""
		try :
			self._servicetype = servicetype
		except Exception as e:
			raise e

	@property
	def ipv46(self) :
		r"""IP address of the content switching virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._ipv46
		except Exception as e:
			raise e

	@ipv46.setter
	def ipv46(self, ipv46) :
		r"""IP address of the content switching virtual server.<br/>Minimum length =  1
		"""
		try :
			self._ipv46 = ipv46
		except Exception as e:
			raise e

	@property
	def targettype(self) :
		r"""Virtual server target type.<br/>Possible values = GSLB.
		"""
		try :
			return self._targettype
		except Exception as e:
			raise e

	@targettype.setter
	def targettype(self, targettype) :
		r"""Virtual server target type.<br/>Possible values = GSLB
		"""
		try :
			self._targettype = targettype
		except Exception as e:
			raise e

	@property
	def dnsrecordtype(self) :
		r""".<br/>Default value: NSGSLB_IPV4<br/>Possible values = A, AAAA, CNAME, NAPTR.
		"""
		try :
			return self._dnsrecordtype
		except Exception as e:
			raise e

	@dnsrecordtype.setter
	def dnsrecordtype(self, dnsrecordtype) :
		r""".<br/>Default value: NSGSLB_IPV4<br/>Possible values = A, AAAA, CNAME, NAPTR
		"""
		try :
			self._dnsrecordtype = dnsrecordtype
		except Exception as e:
			raise e

	@property
	def persistenceid(self) :
		r""".<br/>Maximum length =  65535.
		"""
		try :
			return self._persistenceid
		except Exception as e:
			raise e

	@persistenceid.setter
	def persistenceid(self, persistenceid) :
		r""".<br/>Maximum length =  65535
		"""
		try :
			self._persistenceid = persistenceid
		except Exception as e:
			raise e

	@property
	def ippattern(self) :
		r"""IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern. Mutually exclusive with the IP Address parameter. 
		For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is 255.255.240.0 (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to 198.51.111.254. You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).
		If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if the virtual servers, vs1 and vs2, have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.
		"""
		try :
			return self._ippattern
		except Exception as e:
			raise e

	@ippattern.setter
	def ippattern(self, ippattern) :
		r"""IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern. Mutually exclusive with the IP Address parameter. 
		For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is 255.255.240.0 (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to 198.51.111.254. You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).
		If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if the virtual servers, vs1 and vs2, have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.
		"""
		try :
			self._ippattern = ippattern
		except Exception as e:
			raise e

	@property
	def ipmask(self) :
		r"""IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.
		"""
		try :
			return self._ipmask
		except Exception as e:
			raise e

	@ipmask.setter
	def ipmask(self, ipmask) :
		r"""IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.
		"""
		try :
			self._ipmask = ipmask
		except Exception as e:
			raise e

	@property
	def range(self) :
		r"""Number of consecutive IP addresses, starting with the address specified by the IP Address parameter, to include in a range of addresses assigned to this virtual server.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  254.
		"""
		try :
			return self._range
		except Exception as e:
			raise e

	@range.setter
	def range(self, range) :
		r"""Number of consecutive IP addresses, starting with the address specified by the IP Address parameter, to include in a range of addresses assigned to this virtual server.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  254
		"""
		try :
			self._range = range
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Port number for content switching virtual server.<br/>Minimum length =  1<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Port number for content switching virtual server.<br/>Minimum length =  1<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def ipset(self) :
		r"""The list of IPv4/IPv6 addresses bound to ipset would form a part of listening service on the current cs vserver.<br/>Minimum length =  1.
		"""
		try :
			return self._ipset
		except Exception as e:
			raise e

	@ipset.setter
	def ipset(self, ipset) :
		r"""The list of IPv4/IPv6 addresses bound to ipset would form a part of listening service on the current cs vserver.<br/>Minimum length =  1
		"""
		try :
			self._ipset = ipset
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Initial state of the load balancing virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Initial state of the load balancing virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def stateupdate(self) :
		r"""Enable state updates for a specific content switching virtual server. By default, the Content Switching virtual server is always UP, regardless of the state of the Load Balancing virtual servers bound to it. This parameter interacts with the global setting as follows:
		Global Level | Vserver Level | Result
		ENABLED      ENABLED        ENABLED
		ENABLED      DISABLED       ENABLED
		DISABLED     ENABLED        ENABLED
		DISABLED     DISABLED       DISABLED
		If you want to enable state updates for only some content switching virtual servers, be sure to disable the state update parameter.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED, UPDATEONBACKENDUPDATE.
		"""
		try :
			return self._stateupdate
		except Exception as e:
			raise e

	@stateupdate.setter
	def stateupdate(self, stateupdate) :
		r"""Enable state updates for a specific content switching virtual server. By default, the Content Switching virtual server is always UP, regardless of the state of the Load Balancing virtual servers bound to it. This parameter interacts with the global setting as follows:
		Global Level | Vserver Level | Result
		ENABLED      ENABLED        ENABLED
		ENABLED      DISABLED       ENABLED
		DISABLED     ENABLED        ENABLED
		DISABLED     DISABLED       DISABLED
		If you want to enable state updates for only some content switching virtual servers, be sure to disable the state update parameter.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED, UPDATEONBACKENDUPDATE
		"""
		try :
			self._stateupdate = stateupdate
		except Exception as e:
			raise e

	@property
	def cacheable(self) :
		r"""Use this option to specify whether a virtual server, used for load balancing or content switching, routes requests to the cache redirection virtual server before sending it to the configured servers.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheable
		except Exception as e:
			raise e

	@cacheable.setter
	def cacheable(self, cacheable) :
		r"""Use this option to specify whether a virtual server, used for load balancing or content switching, routes requests to the cache redirection virtual server before sending it to the configured servers.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._cacheable = cacheable
		except Exception as e:
			raise e

	@property
	def redirecturl(self) :
		r"""URL to which traffic is redirected if the virtual server becomes unavailable. The service type of the virtual server should be either HTTP or SSL.
		Caution: Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._redirecturl
		except Exception as e:
			raise e

	@redirecturl.setter
	def redirecturl(self, redirecturl) :
		r"""URL to which traffic is redirected if the virtual server becomes unavailable. The service type of the virtual server should be either HTTP or SSL.
		Caution: Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.<br/>Minimum length =  1
		"""
		try :
			self._redirecturl = redirecturl
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		r"""Idle time, in seconds, after which the client connection is terminated. The default values are:
		180 seconds for HTTP/SSL-based services.
		9000 seconds for other TCP-based services.
		120 seconds for DNS-based services.
		120 seconds for other UDP-based services.<br/>Maximum length =  31536000.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@clttimeout.setter
	def clttimeout(self, clttimeout) :
		r"""Idle time, in seconds, after which the client connection is terminated. The default values are:
		180 seconds for HTTP/SSL-based services.
		9000 seconds for other TCP-based services.
		120 seconds for DNS-based services.
		120 seconds for other UDP-based services.<br/>Maximum length =  31536000
		"""
		try :
			self._clttimeout = clttimeout
		except Exception as e:
			raise e

	@property
	def precedence(self) :
		r"""Type of precedence to use for both RULE-based and URL-based policies on the content switching virtual server. With the default (RULE) setting, incoming requests are evaluated against the rule-based content switching policies. If none of the rules match, the URL in the request is evaluated against the URL-based content switching policies.<br/>Default value: RULE<br/>Possible values = RULE, URL.
		"""
		try :
			return self._precedence
		except Exception as e:
			raise e

	@precedence.setter
	def precedence(self, precedence) :
		r"""Type of precedence to use for both RULE-based and URL-based policies on the content switching virtual server. With the default (RULE) setting, incoming requests are evaluated against the rule-based content switching policies. If none of the rules match, the URL in the request is evaluated against the URL-based content switching policies.<br/>Default value: RULE<br/>Possible values = RULE, URL
		"""
		try :
			self._precedence = precedence
		except Exception as e:
			raise e

	@property
	def casesensitive(self) :
		r"""Consider case in URLs (for policies that use URLs instead of RULES). For example, with the ON setting, the URLs /a/1.html and /A/1.HTML are treated differently and can have different targets (set by content switching policies). With the OFF setting, /a/1.html and /A/1.HTML are switched to the same target.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._casesensitive
		except Exception as e:
			raise e

	@casesensitive.setter
	def casesensitive(self, casesensitive) :
		r"""Consider case in URLs (for policies that use URLs instead of RULES). For example, with the ON setting, the URLs /a/1.html and /A/1.HTML are treated differently and can have different targets (set by content switching policies). With the OFF setting, /a/1.html and /A/1.HTML are switched to the same target.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._casesensitive = casesensitive
		except Exception as e:
			raise e

	@property
	def somethod(self) :
		r"""Type of spillover used to divert traffic to the backup virtual server when the primary virtual server reaches the spillover threshold. Connection spillover is based on the number of connections. Bandwidth spillover is based on the total Kbps of incoming and outgoing traffic.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE.
		"""
		try :
			return self._somethod
		except Exception as e:
			raise e

	@somethod.setter
	def somethod(self, somethod) :
		r"""Type of spillover used to divert traffic to the backup virtual server when the primary virtual server reaches the spillover threshold. Connection spillover is based on the number of connections. Bandwidth spillover is based on the total Kbps of incoming and outgoing traffic.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE
		"""
		try :
			self._somethod = somethod
		except Exception as e:
			raise e

	@property
	def sopersistence(self) :
		r"""Maintain source-IP based persistence on primary and backup virtual servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sopersistence
		except Exception as e:
			raise e

	@sopersistence.setter
	def sopersistence(self, sopersistence) :
		r"""Maintain source-IP based persistence on primary and backup virtual servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sopersistence = sopersistence
		except Exception as e:
			raise e

	@property
	def sopersistencetimeout(self) :
		r"""Time-out value, in minutes, for spillover persistence.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440.
		"""
		try :
			return self._sopersistencetimeout
		except Exception as e:
			raise e

	@sopersistencetimeout.setter
	def sopersistencetimeout(self, sopersistencetimeout) :
		r"""Time-out value, in minutes, for spillover persistence.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440
		"""
		try :
			self._sopersistencetimeout = sopersistencetimeout
		except Exception as e:
			raise e

	@property
	def sothreshold(self) :
		r"""Depending on the spillover method, the maximum number of connections or the maximum total bandwidth (Kbps) that a virtual server can handle before spillover occurs.<br/>Minimum length =  1<br/>Maximum length =  4294967287.
		"""
		try :
			return self._sothreshold
		except Exception as e:
			raise e

	@sothreshold.setter
	def sothreshold(self, sothreshold) :
		r"""Depending on the spillover method, the maximum number of connections or the maximum total bandwidth (Kbps) that a virtual server can handle before spillover occurs.<br/>Minimum length =  1<br/>Maximum length =  4294967287
		"""
		try :
			self._sothreshold = sothreshold
		except Exception as e:
			raise e

	@property
	def sobackupaction(self) :
		r"""Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.<br/>Possible values = DROP, ACCEPT, REDIRECT.
		"""
		try :
			return self._sobackupaction
		except Exception as e:
			raise e

	@sobackupaction.setter
	def sobackupaction(self, sobackupaction) :
		r"""Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.<br/>Possible values = DROP, ACCEPT, REDIRECT
		"""
		try :
			self._sobackupaction = sobackupaction
		except Exception as e:
			raise e

	@property
	def redirectportrewrite(self) :
		r"""State of port rewrite while performing HTTP redirect.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._redirectportrewrite
		except Exception as e:
			raise e

	@redirectportrewrite.setter
	def redirectportrewrite(self, redirectportrewrite) :
		r"""State of port rewrite while performing HTTP redirect.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._redirectportrewrite = redirectportrewrite
		except Exception as e:
			raise e

	@property
	def downstateflush(self) :
		r"""Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._downstateflush
		except Exception as e:
			raise e

	@downstateflush.setter
	def downstateflush(self, downstateflush) :
		r"""Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._downstateflush = downstateflush
		except Exception as e:
			raise e

	@property
	def backupvserver(self) :
		r"""Name of the backup virtual server that you are configuring. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the backup virtual server is created. You can assign a different backup virtual server or rename the existing virtual server.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks.<br/>Minimum length =  1.
		"""
		try :
			return self._backupvserver
		except Exception as e:
			raise e

	@backupvserver.setter
	def backupvserver(self, backupvserver) :
		r"""Name of the backup virtual server that you are configuring. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the backup virtual server is created. You can assign a different backup virtual server or rename the existing virtual server.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks.<br/>Minimum length =  1
		"""
		try :
			self._backupvserver = backupvserver
		except Exception as e:
			raise e

	@property
	def disableprimaryondown(self) :
		r"""Continue forwarding the traffic to backup virtual server even after the primary server comes UP from the DOWN state.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._disableprimaryondown
		except Exception as e:
			raise e

	@disableprimaryondown.setter
	def disableprimaryondown(self, disableprimaryondown) :
		r"""Continue forwarding the traffic to backup virtual server even after the primary server comes UP from the DOWN state.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._disableprimaryondown = disableprimaryondown
		except Exception as e:
			raise e

	@property
	def insertvserveripport(self) :
		r"""Insert the virtual server's VIP address and port number in the request header. Available values function as follows:
		VIPADDR - Header contains the vserver's IP address and port number without any translation.
		OFF     - The virtual IP and port header insertion option is disabled.
		V6TOV4MAPPING - Header contains the mapped IPv4 address corresponding to the IPv6 address of the vserver and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the set ns ip6 command.<br/>Possible values = OFF, VIPADDR, V6TOV4MAPPING.
		"""
		try :
			return self._insertvserveripport
		except Exception as e:
			raise e

	@insertvserveripport.setter
	def insertvserveripport(self, insertvserveripport) :
		r"""Insert the virtual server's VIP address and port number in the request header. Available values function as follows:
		VIPADDR - Header contains the vserver's IP address and port number without any translation.
		OFF     - The virtual IP and port header insertion option is disabled.
		V6TOV4MAPPING - Header contains the mapped IPv4 address corresponding to the IPv6 address of the vserver and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the set ns ip6 command.<br/>Possible values = OFF, VIPADDR, V6TOV4MAPPING
		"""
		try :
			self._insertvserveripport = insertvserveripport
		except Exception as e:
			raise e

	@property
	def vipheader(self) :
		r"""Name of virtual server IP and port header, for use with the VServer IP Port Insertion parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._vipheader
		except Exception as e:
			raise e

	@vipheader.setter
	def vipheader(self, vipheader) :
		r"""Name of virtual server IP and port header, for use with the VServer IP Port Insertion parameter.<br/>Minimum length =  1
		"""
		try :
			self._vipheader = vipheader
		except Exception as e:
			raise e

	@property
	def rtspnat(self) :
		r"""Enable network address translation (NAT) for real-time streaming protocol (RTSP) connections.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._rtspnat
		except Exception as e:
			raise e

	@rtspnat.setter
	def rtspnat(self, rtspnat) :
		r"""Enable network address translation (NAT) for real-time streaming protocol (RTSP) connections.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._rtspnat = rtspnat
		except Exception as e:
			raise e

	@property
	def authenticationhost(self) :
		r"""FQDN of the authentication virtual server. The service type of the virtual server should be either HTTP or SSL.<br/>Minimum length =  3<br/>Maximum length =  252.
		"""
		try :
			return self._authenticationhost
		except Exception as e:
			raise e

	@authenticationhost.setter
	def authenticationhost(self, authenticationhost) :
		r"""FQDN of the authentication virtual server. The service type of the virtual server should be either HTTP or SSL.<br/>Minimum length =  3<br/>Maximum length =  252
		"""
		try :
			self._authenticationhost = authenticationhost
		except Exception as e:
			raise e

	@property
	def authentication(self) :
		r"""Authenticate users who request a connection to the content switching virtual server.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._authentication
		except Exception as e:
			raise e

	@authentication.setter
	def authentication(self, authentication) :
		r"""Authenticate users who request a connection to the content switching virtual server.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._authentication = authentication
		except Exception as e:
			raise e

	@property
	def listenpolicy(self) :
		r"""String specifying the listen policy for the content switching virtual server. Can be either the name of an existing expression or an in-line expression.<br/>Default value: "NONE".
		"""
		try :
			return self._listenpolicy
		except Exception as e:
			raise e

	@listenpolicy.setter
	def listenpolicy(self, listenpolicy) :
		r"""String specifying the listen policy for the content switching virtual server. Can be either the name of an existing expression or an in-line expression.<br/>Default value: "NONE"
		"""
		try :
			self._listenpolicy = listenpolicy
		except Exception as e:
			raise e

	@property
	def listenpriority(self) :
		r"""Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.<br/>Default value: 101<br/>Maximum length =  100.
		"""
		try :
			return self._listenpriority
		except Exception as e:
			raise e

	@listenpriority.setter
	def listenpriority(self, listenpriority) :
		r"""Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.<br/>Default value: 101<br/>Maximum length =  100
		"""
		try :
			self._listenpriority = listenpriority
		except Exception as e:
			raise e

	@property
	def authn401(self) :
		r"""Enable HTTP 401-response based authentication.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._authn401
		except Exception as e:
			raise e

	@authn401.setter
	def authn401(self, authn401) :
		r"""Enable HTTP 401-response based authentication.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._authn401 = authn401
		except Exception as e:
			raise e

	@property
	def authnvsname(self) :
		r"""Name of authentication virtual server that authenticates the incoming user requests to this content switching virtual server. .<br/>Minimum length =  1<br/>Maximum length =  252.
		"""
		try :
			return self._authnvsname
		except Exception as e:
			raise e

	@authnvsname.setter
	def authnvsname(self, authnvsname) :
		r"""Name of authentication virtual server that authenticates the incoming user requests to this content switching virtual server. .<br/>Minimum length =  1<br/>Maximum length =  252
		"""
		try :
			self._authnvsname = authnvsname
		except Exception as e:
			raise e

	@property
	def push(self) :
		r"""Process traffic with the push virtual server that is bound to this content switching virtual server (specified by the Push VServer parameter). The service type of the push virtual server should be either HTTP or SSL.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._push
		except Exception as e:
			raise e

	@push.setter
	def push(self, push) :
		r"""Process traffic with the push virtual server that is bound to this content switching virtual server (specified by the Push VServer parameter). The service type of the push virtual server should be either HTTP or SSL.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._push = push
		except Exception as e:
			raise e

	@property
	def pushvserver(self) :
		r"""Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes updates received on the client-facing load balancing virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._pushvserver
		except Exception as e:
			raise e

	@pushvserver.setter
	def pushvserver(self, pushvserver) :
		r"""Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes updates received on the client-facing load balancing virtual server.<br/>Minimum length =  1
		"""
		try :
			self._pushvserver = pushvserver
		except Exception as e:
			raise e

	@property
	def pushlabel(self) :
		r"""Expression for extracting the label from the response received from server. This string can be either an existing rule name or an inline expression. The service type of the virtual server should be either HTTP or SSL.<br/>Default value: "none".
		"""
		try :
			return self._pushlabel
		except Exception as e:
			raise e

	@pushlabel.setter
	def pushlabel(self, pushlabel) :
		r"""Expression for extracting the label from the response received from server. This string can be either an existing rule name or an inline expression. The service type of the virtual server should be either HTTP or SSL.<br/>Default value: "none"
		"""
		try :
			self._pushlabel = pushlabel
		except Exception as e:
			raise e

	@property
	def pushmulticlients(self) :
		r"""Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._pushmulticlients
		except Exception as e:
			raise e

	@pushmulticlients.setter
	def pushmulticlients(self, pushmulticlients) :
		r"""Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._pushmulticlients = pushmulticlients
		except Exception as e:
			raise e

	@property
	def tcpprofilename(self) :
		r"""Name of the TCP profile containing TCP configuration settings for the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._tcpprofilename
		except Exception as e:
			raise e

	@tcpprofilename.setter
	def tcpprofilename(self, tcpprofilename) :
		r"""Name of the TCP profile containing TCP configuration settings for the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._tcpprofilename = tcpprofilename
		except Exception as e:
			raise e

	@property
	def httpprofilename(self) :
		r"""Name of the HTTP profile containing HTTP configuration settings for the virtual server. The service type of the virtual server should be either HTTP or SSL.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._httpprofilename
		except Exception as e:
			raise e

	@httpprofilename.setter
	def httpprofilename(self, httpprofilename) :
		r"""Name of the HTTP profile containing HTTP configuration settings for the virtual server. The service type of the virtual server should be either HTTP or SSL.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._httpprofilename = httpprofilename
		except Exception as e:
			raise e

	@property
	def dbprofilename(self) :
		r"""Name of the DB profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._dbprofilename
		except Exception as e:
			raise e

	@dbprofilename.setter
	def dbprofilename(self, dbprofilename) :
		r"""Name of the DB profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._dbprofilename = dbprofilename
		except Exception as e:
			raise e

	@property
	def oracleserverversion(self) :
		r"""Oracle server version.<br/>Default value: 10G<br/>Possible values = 10G, 11G.
		"""
		try :
			return self._oracleserverversion
		except Exception as e:
			raise e

	@oracleserverversion.setter
	def oracleserverversion(self, oracleserverversion) :
		r"""Oracle server version.<br/>Default value: 10G<br/>Possible values = 10G, 11G
		"""
		try :
			self._oracleserverversion = oracleserverversion
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Information about this virtual server.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Information about this virtual server.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def mssqlserverversion(self) :
		r"""The version of the MSSQL server.<br/>Default value: 2008R2<br/>Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012, 2014.
		"""
		try :
			return self._mssqlserverversion
		except Exception as e:
			raise e

	@mssqlserverversion.setter
	def mssqlserverversion(self, mssqlserverversion) :
		r"""The version of the MSSQL server.<br/>Default value: 2008R2<br/>Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012, 2014
		"""
		try :
			self._mssqlserverversion = mssqlserverversion
		except Exception as e:
			raise e

	@property
	def l2conn(self) :
		r"""Use L2 Parameters to identify a connection.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._l2conn
		except Exception as e:
			raise e

	@l2conn.setter
	def l2conn(self, l2conn) :
		r"""Use L2 Parameters to identify a connection.<br/>Possible values = ON, OFF
		"""
		try :
			self._l2conn = l2conn
		except Exception as e:
			raise e

	@property
	def mysqlprotocolversion(self) :
		r"""The protocol version returned by the mysql vserver.<br/>Default value: 10.
		"""
		try :
			return self._mysqlprotocolversion
		except Exception as e:
			raise e

	@mysqlprotocolversion.setter
	def mysqlprotocolversion(self, mysqlprotocolversion) :
		r"""The protocol version returned by the mysql vserver.<br/>Default value: 10
		"""
		try :
			self._mysqlprotocolversion = mysqlprotocolversion
		except Exception as e:
			raise e

	@property
	def mysqlserverversion(self) :
		r"""The server version string returned by the mysql vserver.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._mysqlserverversion
		except Exception as e:
			raise e

	@mysqlserverversion.setter
	def mysqlserverversion(self, mysqlserverversion) :
		r"""The server version string returned by the mysql vserver.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._mysqlserverversion = mysqlserverversion
		except Exception as e:
			raise e

	@property
	def mysqlcharacterset(self) :
		r"""The character set returned by the mysql vserver.<br/>Default value: 8.
		"""
		try :
			return self._mysqlcharacterset
		except Exception as e:
			raise e

	@mysqlcharacterset.setter
	def mysqlcharacterset(self, mysqlcharacterset) :
		r"""The character set returned by the mysql vserver.<br/>Default value: 8
		"""
		try :
			self._mysqlcharacterset = mysqlcharacterset
		except Exception as e:
			raise e

	@property
	def mysqlservercapabilities(self) :
		r"""The server capabilities returned by the mysql vserver.<br/>Default value: 41613.
		"""
		try :
			return self._mysqlservercapabilities
		except Exception as e:
			raise e

	@mysqlservercapabilities.setter
	def mysqlservercapabilities(self, mysqlservercapabilities) :
		r"""The server capabilities returned by the mysql vserver.<br/>Default value: 41613
		"""
		try :
			self._mysqlservercapabilities = mysqlservercapabilities
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		r"""Enable logging appflow flow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		r"""Enable logging appflow flow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def netprofile(self) :
		r"""The name of the network profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._netprofile
		except Exception as e:
			raise e

	@netprofile.setter
	def netprofile(self, netprofile) :
		r"""The name of the network profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._netprofile = netprofile
		except Exception as e:
			raise e

	@property
	def icmpvsrresponse(self) :
		r"""Can be active or passive.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE.
		"""
		try :
			return self._icmpvsrresponse
		except Exception as e:
			raise e

	@icmpvsrresponse.setter
	def icmpvsrresponse(self, icmpvsrresponse) :
		r"""Can be active or passive.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE
		"""
		try :
			self._icmpvsrresponse = icmpvsrresponse
		except Exception as e:
			raise e

	@property
	def rhistate(self) :
		r"""A host route is injected according to the setting on the virtual servers
		* If set to PASSIVE on all the virtual servers that share the IP address, the appliance always injects the hostroute.
		* If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.
		* If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance, injects even if one virtual server set to ACTIVE is UP.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE.
		"""
		try :
			return self._rhistate
		except Exception as e:
			raise e

	@rhistate.setter
	def rhistate(self, rhistate) :
		r"""A host route is injected according to the setting on the virtual servers
		* If set to PASSIVE on all the virtual servers that share the IP address, the appliance always injects the hostroute.
		* If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.
		* If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance, injects even if one virtual server set to ACTIVE is UP.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE
		"""
		try :
			self._rhistate = rhistate
		except Exception as e:
			raise e

	@property
	def authnprofile(self) :
		r"""Name of the authentication profile to be used when authentication is turned on.
		"""
		try :
			return self._authnprofile
		except Exception as e:
			raise e

	@authnprofile.setter
	def authnprofile(self, authnprofile) :
		r"""Name of the authentication profile to be used when authentication is turned on.
		"""
		try :
			self._authnprofile = authnprofile
		except Exception as e:
			raise e

	@property
	def dnsprofilename(self) :
		r"""Name of the DNS profile to be associated with the VServer. DNS profile properties will applied to the transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._dnsprofilename
		except Exception as e:
			raise e

	@dnsprofilename.setter
	def dnsprofilename(self, dnsprofilename) :
		r"""Name of the DNS profile to be associated with the VServer. DNS profile properties will applied to the transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._dnsprofilename = dnsprofilename
		except Exception as e:
			raise e

	@property
	def persistencetype(self) :
		r""" Type of persistence for the virtual server. Available settings function as follows:
		* SOURCEIP - Connections from the same client IP address belong to the same persistence session.
		* COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from a server, belong to the same persistence session.
		* SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session.<br/>Possible values = SOURCEIP, COOKIEINSERT, SSLSESSION, NONE.
		"""
		try :
			return self._persistencetype
		except Exception as e:
			raise e

	@persistencetype.setter
	def persistencetype(self, persistencetype) :
		r""" Type of persistence for the virtual server. Available settings function as follows:
		* SOURCEIP - Connections from the same client IP address belong to the same persistence session.
		* COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from a server, belong to the same persistence session.
		* SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session.<br/>Possible values = SOURCEIP, COOKIEINSERT, SSLSESSION, NONE
		"""
		try :
			self._persistencetype = persistencetype
		except Exception as e:
			raise e

	@property
	def persistmask(self) :
		r"""Persistence mask for IP based persistence types, for IPv4 virtual servers.<br/>Minimum length =  1.
		"""
		try :
			return self._persistmask
		except Exception as e:
			raise e

	@persistmask.setter
	def persistmask(self, persistmask) :
		r"""Persistence mask for IP based persistence types, for IPv4 virtual servers.<br/>Minimum length =  1
		"""
		try :
			self._persistmask = persistmask
		except Exception as e:
			raise e

	@property
	def v6persistmasklen(self) :
		r"""Persistence mask for IP based persistence types, for IPv6 virtual servers.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._v6persistmasklen
		except Exception as e:
			raise e

	@v6persistmasklen.setter
	def v6persistmasklen(self, v6persistmasklen) :
		r"""Persistence mask for IP based persistence types, for IPv6 virtual servers.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._v6persistmasklen = v6persistmasklen
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		r"""Time period for which a persistence session is in effect.<br/>Default value: 2<br/>Maximum length =  1440.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		r"""Time period for which a persistence session is in effect.<br/>Default value: 2<br/>Maximum length =  1440
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	@property
	def cookiename(self) :
		r"""Use this parameter to  specify the cookie name for COOKIE peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.
		"""
		try :
			return self._cookiename
		except Exception as e:
			raise e

	@cookiename.setter
	def cookiename(self, cookiename) :
		r"""Use this parameter to  specify the cookie name for COOKIE peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.
		"""
		try :
			self._cookiename = cookiename
		except Exception as e:
			raise e

	@property
	def persistencebackup(self) :
		r"""Backup persistence type for the virtual server. Becomes operational if the primary persistence mechanism fails.<br/>Possible values = SOURCEIP, NONE.
		"""
		try :
			return self._persistencebackup
		except Exception as e:
			raise e

	@persistencebackup.setter
	def persistencebackup(self, persistencebackup) :
		r"""Backup persistence type for the virtual server. Becomes operational if the primary persistence mechanism fails.<br/>Possible values = SOURCEIP, NONE
		"""
		try :
			self._persistencebackup = persistencebackup
		except Exception as e:
			raise e

	@property
	def backuppersistencetimeout(self) :
		r"""Time period for which backup persistence is in effect.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440.
		"""
		try :
			return self._backuppersistencetimeout
		except Exception as e:
			raise e

	@backuppersistencetimeout.setter
	def backuppersistencetimeout(self, backuppersistencetimeout) :
		r"""Time period for which backup persistence is in effect.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440
		"""
		try :
			self._backuppersistencetimeout = backuppersistencetimeout
		except Exception as e:
			raise e

	@property
	def domainname(self) :
		r"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._domainname
		except Exception as e:
			raise e

	@domainname.setter
	def domainname(self, domainname) :
		r"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1
		"""
		try :
			self._domainname = domainname
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r""".<br/>Minimum length =  1.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		r""".<br/>Minimum length =  1
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def backupip(self) :
		r""".<br/>Minimum length =  1.
		"""
		try :
			return self._backupip
		except Exception as e:
			raise e

	@backupip.setter
	def backupip(self, backupip) :
		r""".<br/>Minimum length =  1
		"""
		try :
			self._backupip = backupip
		except Exception as e:
			raise e

	@property
	def cookiedomain(self) :
		r""".<br/>Minimum length =  1.
		"""
		try :
			return self._cookiedomain
		except Exception as e:
			raise e

	@cookiedomain.setter
	def cookiedomain(self, cookiedomain) :
		r""".<br/>Minimum length =  1
		"""
		try :
			self._cookiedomain = cookiedomain
		except Exception as e:
			raise e

	@property
	def cookietimeout(self) :
		r""".<br/>Maximum length =  1440.
		"""
		try :
			return self._cookietimeout
		except Exception as e:
			raise e

	@cookietimeout.setter
	def cookietimeout(self, cookietimeout) :
		r""".<br/>Maximum length =  1440
		"""
		try :
			self._cookietimeout = cookietimeout
		except Exception as e:
			raise e

	@property
	def sitedomainttl(self) :
		r""".<br/>Minimum length =  1.
		"""
		try :
			return self._sitedomainttl
		except Exception as e:
			raise e

	@sitedomainttl.setter
	def sitedomainttl(self, sitedomainttl) :
		r""".<br/>Minimum length =  1
		"""
		try :
			self._sitedomainttl = sitedomainttl
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. 
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my name" or 'my name').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. 
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my name" or 'my name').<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def ip(self) :
		r"""The IP address of the virtual server.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@property
	def value(self) :
		r"""The ssl card status for the transparent ssl cs vserver.<br/>Possible values = Certkey not bound, SSL feature disabled.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@property
	def ngname(self) :
		r"""Nodegroup devno to which this csvserver belongs to.
		"""
		try :
			return self._ngname
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Virtual server type.<br/>Possible values = CONTENT, ADDRESS.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		r"""The state of the cs vserver.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def sc(self) :
		r"""The state of SureConnect the specified virtual server.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sc
		except Exception as e:
			raise e

	@property
	def status(self) :
		r"""Status.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def cachetype(self) :
		r"""Cache type.<br/>Possible values = TRANSPARENT, REVERSE, FORWARD.
		"""
		try :
			return self._cachetype
		except Exception as e:
			raise e

	@property
	def redirect(self) :
		r"""Redirect URL string.<br/>Possible values = CACHE, POLICY, ORIGIN.
		"""
		try :
			return self._redirect
		except Exception as e:
			raise e

	@property
	def homepage(self) :
		r"""Home page.
		"""
		try :
			return self._homepage
		except Exception as e:
			raise e

	@property
	def dnsvservername(self) :
		r"""DNS vserver name.
		"""
		try :
			return self._dnsvservername
		except Exception as e:
			raise e

	@property
	def domain(self) :
		r"""Domain.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		r"""Policies bound to this vserver.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		r"""Service name.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Weight for this service.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@property
	def cachevserver(self) :
		r"""Cache vserver name.
		"""
		try :
			return self._cachevserver
		except Exception as e:
			raise e

	@property
	def targetvserver(self) :
		r"""target vserver name.
		"""
		try :
			return self._targetvserver
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""Priority for the policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def url(self) :
		r"""URL string.
		"""
		try :
			return self._url
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

	@property
	def bindpoint(self) :
		r"""The bindpoint to which the policy is bound.<br/>Possible values = REQUEST, RESPONSE, ICA_REQUEST, OTHERTCP_REQUEST.
		"""
		try :
			return self._bindpoint
		except Exception as e:
			raise e

	@property
	def invoke(self) :
		r"""Invoke flag.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		r"""The invocation type.<br/>Possible values = reqvserver, resvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		r"""Name of the label invoked.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@property
	def gt2gb(self) :
		r"""This argument has no effect.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._gt2gb
		except Exception as e:
			raise e

	@property
	def statechangetimesec(self) :
		r"""Time when last state change happened. Seconds part.
		"""
		try :
			return self._statechangetimesec
		except Exception as e:
			raise e

	@property
	def statechangetimemsec(self) :
		r"""Time at which last state change happened. Milliseconds part.
		"""
		try :
			return self._statechangetimemsec
		except Exception as e:
			raise e

	@property
	def tickssincelaststatechange(self) :
		r"""Time in 10 millisecond ticks since the last state change.
		"""
		try :
			return self._tickssincelaststatechange
		except Exception as e:
			raise e

	@property
	def ruletype(self) :
		r"""Rule type.
		"""
		try :
			return self._ruletype
		except Exception as e:
			raise e

	@property
	def lbvserver(self) :
		r"""Name of the default lb vserver bound. Use this param for Default binding only. For Example: bind cs vserver cs1 -lbvserver lb1.<br/>Minimum length =  1.
		"""
		try :
			return self._lbvserver
		except Exception as e:
			raise e

	@property
	def targetlbvserver(self) :
		r"""target vserver name.
		"""
		try :
			return self._targetlbvserver
		except Exception as e:
			raise e

	@property
	def analyticsprofile(self) :
		r"""Name of the analytics profile bound to the LB vserver.
		"""
		try :
			return self._analyticsprofile
		except Exception as e:
			raise e

	@property
	def nodefaultbindings(self) :
		r"""to determine if the configuration will have default ssl CIPHER and ECC curve bindings.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._nodefaultbindings
		except Exception as e:
			raise e

	@property
	def version(self) :
		r"""Cookie version.
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(csvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.csvserver
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
		r""" Use this API to add csvserver.
		"""
		try :
			if type(resource) is not list :
				addresource = csvserver()
				addresource.name = resource.name
				addresource.td = resource.td
				addresource.servicetype = resource.servicetype
				addresource.ipv46 = resource.ipv46
				addresource.targettype = resource.targettype
				addresource.dnsrecordtype = resource.dnsrecordtype
				addresource.persistenceid = resource.persistenceid
				addresource.ippattern = resource.ippattern
				addresource.ipmask = resource.ipmask
				addresource.range = resource.range
				addresource.port = resource.port
				addresource.ipset = resource.ipset
				addresource.state = resource.state
				addresource.stateupdate = resource.stateupdate
				addresource.cacheable = resource.cacheable
				addresource.redirecturl = resource.redirecturl
				addresource.clttimeout = resource.clttimeout
				addresource.precedence = resource.precedence
				addresource.casesensitive = resource.casesensitive
				addresource.somethod = resource.somethod
				addresource.sopersistence = resource.sopersistence
				addresource.sopersistencetimeout = resource.sopersistencetimeout
				addresource.sothreshold = resource.sothreshold
				addresource.sobackupaction = resource.sobackupaction
				addresource.redirectportrewrite = resource.redirectportrewrite
				addresource.downstateflush = resource.downstateflush
				addresource.backupvserver = resource.backupvserver
				addresource.disableprimaryondown = resource.disableprimaryondown
				addresource.insertvserveripport = resource.insertvserveripport
				addresource.vipheader = resource.vipheader
				addresource.rtspnat = resource.rtspnat
				addresource.authenticationhost = resource.authenticationhost
				addresource.authentication = resource.authentication
				addresource.listenpolicy = resource.listenpolicy
				addresource.listenpriority = resource.listenpriority
				addresource.authn401 = resource.authn401
				addresource.authnvsname = resource.authnvsname
				addresource.push = resource.push
				addresource.pushvserver = resource.pushvserver
				addresource.pushlabel = resource.pushlabel
				addresource.pushmulticlients = resource.pushmulticlients
				addresource.tcpprofilename = resource.tcpprofilename
				addresource.httpprofilename = resource.httpprofilename
				addresource.dbprofilename = resource.dbprofilename
				addresource.oracleserverversion = resource.oracleserverversion
				addresource.comment = resource.comment
				addresource.mssqlserverversion = resource.mssqlserverversion
				addresource.l2conn = resource.l2conn
				addresource.mysqlprotocolversion = resource.mysqlprotocolversion
				addresource.mysqlserverversion = resource.mysqlserverversion
				addresource.mysqlcharacterset = resource.mysqlcharacterset
				addresource.mysqlservercapabilities = resource.mysqlservercapabilities
				addresource.appflowlog = resource.appflowlog
				addresource.netprofile = resource.netprofile
				addresource.icmpvsrresponse = resource.icmpvsrresponse
				addresource.rhistate = resource.rhistate
				addresource.authnprofile = resource.authnprofile
				addresource.dnsprofilename = resource.dnsprofilename
				addresource.persistencetype = resource.persistencetype
				addresource.persistmask = resource.persistmask
				addresource.v6persistmasklen = resource.v6persistmasklen
				addresource.timeout = resource.timeout
				addresource.cookiename = resource.cookiename
				addresource.persistencebackup = resource.persistencebackup
				addresource.backuppersistencetimeout = resource.backuppersistencetimeout
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ csvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].td = resource[i].td
						addresources[i].servicetype = resource[i].servicetype
						addresources[i].ipv46 = resource[i].ipv46
						addresources[i].targettype = resource[i].targettype
						addresources[i].dnsrecordtype = resource[i].dnsrecordtype
						addresources[i].persistenceid = resource[i].persistenceid
						addresources[i].ippattern = resource[i].ippattern
						addresources[i].ipmask = resource[i].ipmask
						addresources[i].range = resource[i].range
						addresources[i].port = resource[i].port
						addresources[i].ipset = resource[i].ipset
						addresources[i].state = resource[i].state
						addresources[i].stateupdate = resource[i].stateupdate
						addresources[i].cacheable = resource[i].cacheable
						addresources[i].redirecturl = resource[i].redirecturl
						addresources[i].clttimeout = resource[i].clttimeout
						addresources[i].precedence = resource[i].precedence
						addresources[i].casesensitive = resource[i].casesensitive
						addresources[i].somethod = resource[i].somethod
						addresources[i].sopersistence = resource[i].sopersistence
						addresources[i].sopersistencetimeout = resource[i].sopersistencetimeout
						addresources[i].sothreshold = resource[i].sothreshold
						addresources[i].sobackupaction = resource[i].sobackupaction
						addresources[i].redirectportrewrite = resource[i].redirectportrewrite
						addresources[i].downstateflush = resource[i].downstateflush
						addresources[i].backupvserver = resource[i].backupvserver
						addresources[i].disableprimaryondown = resource[i].disableprimaryondown
						addresources[i].insertvserveripport = resource[i].insertvserveripport
						addresources[i].vipheader = resource[i].vipheader
						addresources[i].rtspnat = resource[i].rtspnat
						addresources[i].authenticationhost = resource[i].authenticationhost
						addresources[i].authentication = resource[i].authentication
						addresources[i].listenpolicy = resource[i].listenpolicy
						addresources[i].listenpriority = resource[i].listenpriority
						addresources[i].authn401 = resource[i].authn401
						addresources[i].authnvsname = resource[i].authnvsname
						addresources[i].push = resource[i].push
						addresources[i].pushvserver = resource[i].pushvserver
						addresources[i].pushlabel = resource[i].pushlabel
						addresources[i].pushmulticlients = resource[i].pushmulticlients
						addresources[i].tcpprofilename = resource[i].tcpprofilename
						addresources[i].httpprofilename = resource[i].httpprofilename
						addresources[i].dbprofilename = resource[i].dbprofilename
						addresources[i].oracleserverversion = resource[i].oracleserverversion
						addresources[i].comment = resource[i].comment
						addresources[i].mssqlserverversion = resource[i].mssqlserverversion
						addresources[i].l2conn = resource[i].l2conn
						addresources[i].mysqlprotocolversion = resource[i].mysqlprotocolversion
						addresources[i].mysqlserverversion = resource[i].mysqlserverversion
						addresources[i].mysqlcharacterset = resource[i].mysqlcharacterset
						addresources[i].mysqlservercapabilities = resource[i].mysqlservercapabilities
						addresources[i].appflowlog = resource[i].appflowlog
						addresources[i].netprofile = resource[i].netprofile
						addresources[i].icmpvsrresponse = resource[i].icmpvsrresponse
						addresources[i].rhistate = resource[i].rhistate
						addresources[i].authnprofile = resource[i].authnprofile
						addresources[i].dnsprofilename = resource[i].dnsprofilename
						addresources[i].persistencetype = resource[i].persistencetype
						addresources[i].persistmask = resource[i].persistmask
						addresources[i].v6persistmasklen = resource[i].v6persistmasklen
						addresources[i].timeout = resource[i].timeout
						addresources[i].cookiename = resource[i].cookiename
						addresources[i].persistencebackup = resource[i].persistencebackup
						addresources[i].backuppersistencetimeout = resource[i].backuppersistencetimeout
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete csvserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = csvserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ csvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ csvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update csvserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = csvserver()
				updateresource.name = resource.name
				updateresource.ipv46 = resource.ipv46
				updateresource.ipset = resource.ipset
				updateresource.ippattern = resource.ippattern
				updateresource.ipmask = resource.ipmask
				updateresource.stateupdate = resource.stateupdate
				updateresource.precedence = resource.precedence
				updateresource.casesensitive = resource.casesensitive
				updateresource.backupvserver = resource.backupvserver
				updateresource.redirecturl = resource.redirecturl
				updateresource.cacheable = resource.cacheable
				updateresource.clttimeout = resource.clttimeout
				updateresource.somethod = resource.somethod
				updateresource.sopersistence = resource.sopersistence
				updateresource.sopersistencetimeout = resource.sopersistencetimeout
				updateresource.sothreshold = resource.sothreshold
				updateresource.sobackupaction = resource.sobackupaction
				updateresource.redirectportrewrite = resource.redirectportrewrite
				updateresource.downstateflush = resource.downstateflush
				updateresource.disableprimaryondown = resource.disableprimaryondown
				updateresource.insertvserveripport = resource.insertvserveripport
				updateresource.vipheader = resource.vipheader
				updateresource.rtspnat = resource.rtspnat
				updateresource.authenticationhost = resource.authenticationhost
				updateresource.authentication = resource.authentication
				updateresource.listenpolicy = resource.listenpolicy
				updateresource.listenpriority = resource.listenpriority
				updateresource.authn401 = resource.authn401
				updateresource.authnvsname = resource.authnvsname
				updateresource.push = resource.push
				updateresource.pushvserver = resource.pushvserver
				updateresource.pushlabel = resource.pushlabel
				updateresource.pushmulticlients = resource.pushmulticlients
				updateresource.tcpprofilename = resource.tcpprofilename
				updateresource.httpprofilename = resource.httpprofilename
				updateresource.dbprofilename = resource.dbprofilename
				updateresource.comment = resource.comment
				updateresource.l2conn = resource.l2conn
				updateresource.mssqlserverversion = resource.mssqlserverversion
				updateresource.mysqlprotocolversion = resource.mysqlprotocolversion
				updateresource.oracleserverversion = resource.oracleserverversion
				updateresource.mysqlserverversion = resource.mysqlserverversion
				updateresource.mysqlcharacterset = resource.mysqlcharacterset
				updateresource.mysqlservercapabilities = resource.mysqlservercapabilities
				updateresource.appflowlog = resource.appflowlog
				updateresource.netprofile = resource.netprofile
				updateresource.authnprofile = resource.authnprofile
				updateresource.icmpvsrresponse = resource.icmpvsrresponse
				updateresource.rhistate = resource.rhistate
				updateresource.dnsprofilename = resource.dnsprofilename
				updateresource.dnsrecordtype = resource.dnsrecordtype
				updateresource.persistenceid = resource.persistenceid
				updateresource.domainname = resource.domainname
				updateresource.ttl = resource.ttl
				updateresource.backupip = resource.backupip
				updateresource.cookiedomain = resource.cookiedomain
				updateresource.cookietimeout = resource.cookietimeout
				updateresource.sitedomainttl = resource.sitedomainttl
				updateresource.persistencetype = resource.persistencetype
				updateresource.persistmask = resource.persistmask
				updateresource.v6persistmasklen = resource.v6persistmasklen
				updateresource.timeout = resource.timeout
				updateresource.cookiename = resource.cookiename
				updateresource.persistencebackup = resource.persistencebackup
				updateresource.backuppersistencetimeout = resource.backuppersistencetimeout
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ csvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ipv46 = resource[i].ipv46
						updateresources[i].ipset = resource[i].ipset
						updateresources[i].ippattern = resource[i].ippattern
						updateresources[i].ipmask = resource[i].ipmask
						updateresources[i].stateupdate = resource[i].stateupdate
						updateresources[i].precedence = resource[i].precedence
						updateresources[i].casesensitive = resource[i].casesensitive
						updateresources[i].backupvserver = resource[i].backupvserver
						updateresources[i].redirecturl = resource[i].redirecturl
						updateresources[i].cacheable = resource[i].cacheable
						updateresources[i].clttimeout = resource[i].clttimeout
						updateresources[i].somethod = resource[i].somethod
						updateresources[i].sopersistence = resource[i].sopersistence
						updateresources[i].sopersistencetimeout = resource[i].sopersistencetimeout
						updateresources[i].sothreshold = resource[i].sothreshold
						updateresources[i].sobackupaction = resource[i].sobackupaction
						updateresources[i].redirectportrewrite = resource[i].redirectportrewrite
						updateresources[i].downstateflush = resource[i].downstateflush
						updateresources[i].disableprimaryondown = resource[i].disableprimaryondown
						updateresources[i].insertvserveripport = resource[i].insertvserveripport
						updateresources[i].vipheader = resource[i].vipheader
						updateresources[i].rtspnat = resource[i].rtspnat
						updateresources[i].authenticationhost = resource[i].authenticationhost
						updateresources[i].authentication = resource[i].authentication
						updateresources[i].listenpolicy = resource[i].listenpolicy
						updateresources[i].listenpriority = resource[i].listenpriority
						updateresources[i].authn401 = resource[i].authn401
						updateresources[i].authnvsname = resource[i].authnvsname
						updateresources[i].push = resource[i].push
						updateresources[i].pushvserver = resource[i].pushvserver
						updateresources[i].pushlabel = resource[i].pushlabel
						updateresources[i].pushmulticlients = resource[i].pushmulticlients
						updateresources[i].tcpprofilename = resource[i].tcpprofilename
						updateresources[i].httpprofilename = resource[i].httpprofilename
						updateresources[i].dbprofilename = resource[i].dbprofilename
						updateresources[i].comment = resource[i].comment
						updateresources[i].l2conn = resource[i].l2conn
						updateresources[i].mssqlserverversion = resource[i].mssqlserverversion
						updateresources[i].mysqlprotocolversion = resource[i].mysqlprotocolversion
						updateresources[i].oracleserverversion = resource[i].oracleserverversion
						updateresources[i].mysqlserverversion = resource[i].mysqlserverversion
						updateresources[i].mysqlcharacterset = resource[i].mysqlcharacterset
						updateresources[i].mysqlservercapabilities = resource[i].mysqlservercapabilities
						updateresources[i].appflowlog = resource[i].appflowlog
						updateresources[i].netprofile = resource[i].netprofile
						updateresources[i].authnprofile = resource[i].authnprofile
						updateresources[i].icmpvsrresponse = resource[i].icmpvsrresponse
						updateresources[i].rhistate = resource[i].rhistate
						updateresources[i].dnsprofilename = resource[i].dnsprofilename
						updateresources[i].dnsrecordtype = resource[i].dnsrecordtype
						updateresources[i].persistenceid = resource[i].persistenceid
						updateresources[i].domainname = resource[i].domainname
						updateresources[i].ttl = resource[i].ttl
						updateresources[i].backupip = resource[i].backupip
						updateresources[i].cookiedomain = resource[i].cookiedomain
						updateresources[i].cookietimeout = resource[i].cookietimeout
						updateresources[i].sitedomainttl = resource[i].sitedomainttl
						updateresources[i].persistencetype = resource[i].persistencetype
						updateresources[i].persistmask = resource[i].persistmask
						updateresources[i].v6persistmasklen = resource[i].v6persistmasklen
						updateresources[i].timeout = resource[i].timeout
						updateresources[i].cookiename = resource[i].cookiename
						updateresources[i].persistencebackup = resource[i].persistencebackup
						updateresources[i].backuppersistencetimeout = resource[i].backuppersistencetimeout
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of csvserver resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = csvserver()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ csvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ csvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable csvserver.
		"""
		try :
			if type(resource) is not list :
				enableresource = csvserver()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ csvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ csvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable csvserver.
		"""
		try :
			if type(resource) is not list :
				disableresource = csvserver()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ csvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ csvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a csvserver resource.
		"""
		try :
			renameresource = csvserver()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the csvserver resources that are configured on netscaler.
		"""
		response = None
		try :
			if not name :
				obj = csvserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = csvserver()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [csvserver() for _ in range(len(name))]
						obj = [csvserver() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = csvserver()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of csvserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = csvserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the csvserver resources configured on NetScaler.
		"""
		try :
			obj = csvserver()
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
		r""" Use this API to count filtered the set of csvserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = csvserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sc:
		ON = "ON"
		OFF = "OFF"

	class Oracleserverversion:
		_10G = "10G"
		_11G = "11G"

	class Rhistate:
		PASSIVE = "PASSIVE"
		ACTIVE = "ACTIVE"

	class Stateupdate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"
		UPDATEONBACKENDUPDATE = "UPDATEONBACKENDUPDATE"

	class Authentication:
		ON = "ON"
		OFF = "OFF"

	class Redirectportrewrite:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cachetype:
		TRANSPARENT = "TRANSPARENT"
		REVERSE = "REVERSE"
		FORWARD = "FORWARD"

	class Nodefaultbindings:
		YES = "YES"
		NO = "NO"

	class Downstateflush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dnsrecordtype:
		A = "A"
		AAAA = "AAAA"
		CNAME = "CNAME"
		NAPTR = "NAPTR"

	class Targettype:
		GSLB = "GSLB"

	class Servicetype:
		HTTP = "HTTP"
		SSL = "SSL"
		TCP = "TCP"
		FTP = "FTP"
		RTSP = "RTSP"
		SSL_TCP = "SSL_TCP"
		UDP = "UDP"
		DNS = "DNS"
		SIP_UDP = "SIP_UDP"
		SIP_TCP = "SIP_TCP"
		SIP_SSL = "SIP_SSL"
		ANY = "ANY"
		RADIUS = "RADIUS"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		DNS_TCP = "DNS_TCP"
		ORACLE = "ORACLE"
		SMPP = "SMPP"
		PROXY = "PROXY"

	class Icmpvsrresponse:
		PASSIVE = "PASSIVE"
		ACTIVE = "ACTIVE"

	class Casesensitive:
		ON = "ON"
		OFF = "OFF"

	class Value:
		Certkey_not_bound = "Certkey not bound"
		SSL_feature_disabled = "SSL feature disabled"

	class L2conn:
		ON = "ON"
		OFF = "OFF"

	class Sobackupaction:
		DROP = "DROP"
		ACCEPT = "ACCEPT"
		REDIRECT = "REDIRECT"

	class Gt2gb:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Push:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Type:
		CONTENT = "CONTENT"
		ADDRESS = "ADDRESS"

	class Rtspnat:
		ON = "ON"
		OFF = "OFF"

	class Disableprimaryondown:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Authn401:
		ON = "ON"
		OFF = "OFF"

	class Cacheable:
		YES = "YES"
		NO = "NO"

	class Somethod:
		CONNECTION = "CONNECTION"
		DYNAMICCONNECTION = "DYNAMICCONNECTION"
		BANDWIDTH = "BANDWIDTH"
		HEALTH = "HEALTH"
		NONE = "NONE"

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"
		ICA_REQUEST = "ICA_REQUEST"
		OTHERTCP_REQUEST = "OTHERTCP_REQUEST"

	class Sopersistence:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Redirect:
		CACHE = "CACHE"
		POLICY = "POLICY"
		ORIGIN = "ORIGIN"

	class Pushmulticlients:
		YES = "YES"
		NO = "NO"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

	class Persistencebackup:
		SOURCEIP = "SOURCEIP"
		NONE = "NONE"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Precedence:
		RULE = "RULE"
		URL = "URL"

	class Curstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Persistencetype:
		SOURCEIP = "SOURCEIP"
		COOKIEINSERT = "COOKIEINSERT"
		SSLSESSION = "SSLSESSION"
		NONE = "NONE"

	class Insertvserveripport:
		OFF = "OFF"
		VIPADDR = "VIPADDR"
		V6TOV4MAPPING = "V6TOV4MAPPING"

	class Mssqlserverversion:
		_70 = "70"
		_2000 = "2000"
		_2000SP1 = "2000SP1"
		_2005 = "2005"
		_2008 = "2008"
		_2008R2 = "2008R2"
		_2012 = "2012"
		_2014 = "2014"

class csvserver_response(base_response) :
	def __init__(self, length=1) :
		self.csvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.csvserver = [csvserver() for _ in range(length)]

