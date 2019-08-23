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

class appflowparam(base_resource) :
	""" Configuration for AppFlow parameter resource. """
	def __init__(self) :
		self._templaterefresh = None
		self._appnamerefresh = None
		self._flowrecordinterval = None
		self._securityinsightrecordinterval = None
		self._udppmtu = None
		self._httpurl = None
		self._aaausername = None
		self._httpcookie = None
		self._httpreferer = None
		self._httpmethod = None
		self._httphost = None
		self._httpuseragent = None
		self._clienttrafficonly = None
		self._httpcontenttype = None
		self._httpauthorization = None
		self._httpvia = None
		self._httpxforwardedfor = None
		self._httplocation = None
		self._httpsetcookie = None
		self._httpsetcookie2 = None
		self._connectionchaining = None
		self._httpdomain = None
		self._skipcacheredirectionhttptransaction = None
		self._identifiername = None
		self._identifiersessionname = None
		self._observationdomainid = None
		self._observationdomainname = None
		self._feature = None
		self._subscriberawareness = None
		self._subscriberidobfuscation = None
		self._subscriberidobfuscationalgo = None
		self._gxsessionreporting = None
		self._securityinsighttraffic = None
		self._cacheinsight = None
		self._videoinsight = None
		self._httpquerywithurl = None
		self._urlcategory = None
		self._lsnlogging = None
		self._cqareporting = None
		self._emailaddress = None
		self._usagerecordinterval = None
		self._metrics = None
		self._events = None
		self._auditlogs = None
		self._observationpointid = None
		self._tcpattackcounterinterval = None
		self._tcpburstreporting = None
		self._tcpburstreportingthreshold = None

	@property
	def templaterefresh(self) :
		r"""Refresh interval, in seconds, at which to export the template data. Because data transmission is in UDP, the templates must be resent at regular intervals.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._templaterefresh
		except Exception as e:
			raise e

	@templaterefresh.setter
	def templaterefresh(self, templaterefresh) :
		r"""Refresh interval, in seconds, at which to export the template data. Because data transmission is in UDP, the templates must be resent at regular intervals.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._templaterefresh = templaterefresh
		except Exception as e:
			raise e

	@property
	def appnamerefresh(self) :
		r"""Interval, in seconds, at which to send Appnames to the configured collectors. Appname refers to the name of an entity (virtual server, service, or service group) in the Citrix ADC.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._appnamerefresh
		except Exception as e:
			raise e

	@appnamerefresh.setter
	def appnamerefresh(self, appnamerefresh) :
		r"""Interval, in seconds, at which to send Appnames to the configured collectors. Appname refers to the name of an entity (virtual server, service, or service group) in the Citrix ADC.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._appnamerefresh = appnamerefresh
		except Exception as e:
			raise e

	@property
	def flowrecordinterval(self) :
		r"""Interval, in seconds, at which to send flow records to the configured collectors.<br/>Default value: 60<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._flowrecordinterval
		except Exception as e:
			raise e

	@flowrecordinterval.setter
	def flowrecordinterval(self, flowrecordinterval) :
		r"""Interval, in seconds, at which to send flow records to the configured collectors.<br/>Default value: 60<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._flowrecordinterval = flowrecordinterval
		except Exception as e:
			raise e

	@property
	def securityinsightrecordinterval(self) :
		r"""Interval, in seconds, at which to send security insight flow records to the configured collectors.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._securityinsightrecordinterval
		except Exception as e:
			raise e

	@securityinsightrecordinterval.setter
	def securityinsightrecordinterval(self, securityinsightrecordinterval) :
		r"""Interval, in seconds, at which to send security insight flow records to the configured collectors.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._securityinsightrecordinterval = securityinsightrecordinterval
		except Exception as e:
			raise e

	@property
	def udppmtu(self) :
		r"""MTU, in bytes, for IPFIX UDP packets.<br/>Default value: 1472<br/>Minimum length =  128<br/>Maximum length =  1472.
		"""
		try :
			return self._udppmtu
		except Exception as e:
			raise e

	@udppmtu.setter
	def udppmtu(self, udppmtu) :
		r"""MTU, in bytes, for IPFIX UDP packets.<br/>Default value: 1472<br/>Minimum length =  128<br/>Maximum length =  1472
		"""
		try :
			self._udppmtu = udppmtu
		except Exception as e:
			raise e

	@property
	def httpurl(self) :
		r"""Include the http URL that the Citrix ADC received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpurl
		except Exception as e:
			raise e

	@httpurl.setter
	def httpurl(self, httpurl) :
		r"""Include the http URL that the Citrix ADC received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpurl = httpurl
		except Exception as e:
			raise e

	@property
	def aaausername(self) :
		r"""Enable AppFlow AAA Username logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._aaausername
		except Exception as e:
			raise e

	@aaausername.setter
	def aaausername(self, aaausername) :
		r"""Enable AppFlow AAA Username logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._aaausername = aaausername
		except Exception as e:
			raise e

	@property
	def httpcookie(self) :
		r"""Include the cookie that was in the HTTP request the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpcookie
		except Exception as e:
			raise e

	@httpcookie.setter
	def httpcookie(self, httpcookie) :
		r"""Include the cookie that was in the HTTP request the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpcookie = httpcookie
		except Exception as e:
			raise e

	@property
	def httpreferer(self) :
		r"""Include the web page that was last visited by the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpreferer
		except Exception as e:
			raise e

	@httpreferer.setter
	def httpreferer(self, httpreferer) :
		r"""Include the web page that was last visited by the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpreferer = httpreferer
		except Exception as e:
			raise e

	@property
	def httpmethod(self) :
		r"""Include the method that was specified in the HTTP request that the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpmethod
		except Exception as e:
			raise e

	@httpmethod.setter
	def httpmethod(self, httpmethod) :
		r"""Include the method that was specified in the HTTP request that the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpmethod = httpmethod
		except Exception as e:
			raise e

	@property
	def httphost(self) :
		r"""Include the host identified in the HTTP request that the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httphost
		except Exception as e:
			raise e

	@httphost.setter
	def httphost(self, httphost) :
		r"""Include the host identified in the HTTP request that the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httphost = httphost
		except Exception as e:
			raise e

	@property
	def httpuseragent(self) :
		r"""Include the client application through which the HTTP request was received by the Citrix ADC.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpuseragent
		except Exception as e:
			raise e

	@httpuseragent.setter
	def httpuseragent(self, httpuseragent) :
		r"""Include the client application through which the HTTP request was received by the Citrix ADC.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpuseragent = httpuseragent
		except Exception as e:
			raise e

	@property
	def clienttrafficonly(self) :
		r"""Generate AppFlow records for only the traffic from the client.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._clienttrafficonly
		except Exception as e:
			raise e

	@clienttrafficonly.setter
	def clienttrafficonly(self, clienttrafficonly) :
		r"""Generate AppFlow records for only the traffic from the client.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._clienttrafficonly = clienttrafficonly
		except Exception as e:
			raise e

	@property
	def httpcontenttype(self) :
		r"""Include the HTTP Content-Type header sent from the server to the client to determine the type of the content sent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpcontenttype
		except Exception as e:
			raise e

	@httpcontenttype.setter
	def httpcontenttype(self, httpcontenttype) :
		r"""Include the HTTP Content-Type header sent from the server to the client to determine the type of the content sent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpcontenttype = httpcontenttype
		except Exception as e:
			raise e

	@property
	def httpauthorization(self) :
		r"""Include the HTTP Authorization header information.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpauthorization
		except Exception as e:
			raise e

	@httpauthorization.setter
	def httpauthorization(self, httpauthorization) :
		r"""Include the HTTP Authorization header information.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpauthorization = httpauthorization
		except Exception as e:
			raise e

	@property
	def httpvia(self) :
		r"""Include the httpVia header which contains the IP address of proxy server through which the client accessed the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpvia
		except Exception as e:
			raise e

	@httpvia.setter
	def httpvia(self, httpvia) :
		r"""Include the httpVia header which contains the IP address of proxy server through which the client accessed the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpvia = httpvia
		except Exception as e:
			raise e

	@property
	def httpxforwardedfor(self) :
		r"""Include the httpXForwardedFor header, which contains the original IP Address of the client using a proxy server to access the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpxforwardedfor
		except Exception as e:
			raise e

	@httpxforwardedfor.setter
	def httpxforwardedfor(self, httpxforwardedfor) :
		r"""Include the httpXForwardedFor header, which contains the original IP Address of the client using a proxy server to access the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpxforwardedfor = httpxforwardedfor
		except Exception as e:
			raise e

	@property
	def httplocation(self) :
		r"""Include the HTTP location headers returned from the HTTP responses.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httplocation
		except Exception as e:
			raise e

	@httplocation.setter
	def httplocation(self, httplocation) :
		r"""Include the HTTP location headers returned from the HTTP responses.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httplocation = httplocation
		except Exception as e:
			raise e

	@property
	def httpsetcookie(self) :
		r"""Include the Set-cookie header sent from the server to the client in response to a HTTP request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpsetcookie
		except Exception as e:
			raise e

	@httpsetcookie.setter
	def httpsetcookie(self, httpsetcookie) :
		r"""Include the Set-cookie header sent from the server to the client in response to a HTTP request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpsetcookie = httpsetcookie
		except Exception as e:
			raise e

	@property
	def httpsetcookie2(self) :
		r"""Include the Set-cookie header sent from the server to the client in response to a HTTP request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpsetcookie2
		except Exception as e:
			raise e

	@httpsetcookie2.setter
	def httpsetcookie2(self, httpsetcookie2) :
		r"""Include the Set-cookie header sent from the server to the client in response to a HTTP request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpsetcookie2 = httpsetcookie2
		except Exception as e:
			raise e

	@property
	def connectionchaining(self) :
		r"""Enable connection chaining so that the client server flows of a connection are linked. Also the connection chain ID is propagated across Citrix ADCs, so that in a multi-hop environment the flows belonging to the same logical connection are linked. This id is also logged as part of appflow record.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._connectionchaining
		except Exception as e:
			raise e

	@connectionchaining.setter
	def connectionchaining(self, connectionchaining) :
		r"""Enable connection chaining so that the client server flows of a connection are linked. Also the connection chain ID is propagated across Citrix ADCs, so that in a multi-hop environment the flows belonging to the same logical connection are linked. This id is also logged as part of appflow record.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._connectionchaining = connectionchaining
		except Exception as e:
			raise e

	@property
	def httpdomain(self) :
		r"""Include the http domain request to be exported.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpdomain
		except Exception as e:
			raise e

	@httpdomain.setter
	def httpdomain(self, httpdomain) :
		r"""Include the http domain request to be exported.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpdomain = httpdomain
		except Exception as e:
			raise e

	@property
	def skipcacheredirectionhttptransaction(self) :
		r"""Skip Cache http transaction. This HTTP transaction is specific to Cache Redirection module. In Case of Cache Miss there will be another HTTP transaction initiated by the cache server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._skipcacheredirectionhttptransaction
		except Exception as e:
			raise e

	@skipcacheredirectionhttptransaction.setter
	def skipcacheredirectionhttptransaction(self, skipcacheredirectionhttptransaction) :
		r"""Skip Cache http transaction. This HTTP transaction is specific to Cache Redirection module. In Case of Cache Miss there will be another HTTP transaction initiated by the cache server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._skipcacheredirectionhttptransaction = skipcacheredirectionhttptransaction
		except Exception as e:
			raise e

	@property
	def identifiername(self) :
		r"""Include the stream identifier name to be exported.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._identifiername
		except Exception as e:
			raise e

	@identifiername.setter
	def identifiername(self, identifiername) :
		r"""Include the stream identifier name to be exported.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._identifiername = identifiername
		except Exception as e:
			raise e

	@property
	def identifiersessionname(self) :
		r"""Include the stream identifier session name to be exported.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._identifiersessionname
		except Exception as e:
			raise e

	@identifiersessionname.setter
	def identifiersessionname(self, identifiersessionname) :
		r"""Include the stream identifier session name to be exported.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._identifiersessionname = identifiersessionname
		except Exception as e:
			raise e

	@property
	def observationdomainid(self) :
		r"""An observation domain groups a set of Citrix ADCs based on deployment: cluster, HA etc. A unique Observation Domain ID is required to be assigned to each such group.<br/>Default value: 0<br/>Minimum length =  1000.
		"""
		try :
			return self._observationdomainid
		except Exception as e:
			raise e

	@observationdomainid.setter
	def observationdomainid(self, observationdomainid) :
		r"""An observation domain groups a set of Citrix ADCs based on deployment: cluster, HA etc. A unique Observation Domain ID is required to be assigned to each such group.<br/>Default value: 0<br/>Minimum length =  1000
		"""
		try :
			self._observationdomainid = observationdomainid
		except Exception as e:
			raise e

	@property
	def observationdomainname(self) :
		r"""Name of the Observation Domain defined by the observation domain ID.<br/>Maximum length =  127.
		"""
		try :
			return self._observationdomainname
		except Exception as e:
			raise e

	@observationdomainname.setter
	def observationdomainname(self, observationdomainname) :
		r"""Name of the Observation Domain defined by the observation domain ID.<br/>Maximum length =  127
		"""
		try :
			self._observationdomainname = observationdomainname
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
	def subscriberawareness(self) :
		r"""Enable this option for logging end user MSISDN in L4/L7 appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._subscriberawareness
		except Exception as e:
			raise e

	@subscriberawareness.setter
	def subscriberawareness(self, subscriberawareness) :
		r"""Enable this option for logging end user MSISDN in L4/L7 appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._subscriberawareness = subscriberawareness
		except Exception as e:
			raise e

	@property
	def subscriberidobfuscation(self) :
		r"""Enable this option for obfuscating MSISDN in L4/L7 appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._subscriberidobfuscation
		except Exception as e:
			raise e

	@subscriberidobfuscation.setter
	def subscriberidobfuscation(self, subscriberidobfuscation) :
		r"""Enable this option for obfuscating MSISDN in L4/L7 appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._subscriberidobfuscation = subscriberidobfuscation
		except Exception as e:
			raise e

	@property
	def subscriberidobfuscationalgo(self) :
		r"""Algorithm(MD5 or SHA256) to be used for obfuscating MSISDN.<br/>Default value: MD5<br/>Possible values = MD5, SHA256.
		"""
		try :
			return self._subscriberidobfuscationalgo
		except Exception as e:
			raise e

	@subscriberidobfuscationalgo.setter
	def subscriberidobfuscationalgo(self, subscriberidobfuscationalgo) :
		r"""Algorithm(MD5 or SHA256) to be used for obfuscating MSISDN.<br/>Default value: MD5<br/>Possible values = MD5, SHA256
		"""
		try :
			self._subscriberidobfuscationalgo = subscriberidobfuscationalgo
		except Exception as e:
			raise e

	@property
	def gxsessionreporting(self) :
		r"""Enable this option for Gx session reporting.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._gxsessionreporting
		except Exception as e:
			raise e

	@gxsessionreporting.setter
	def gxsessionreporting(self, gxsessionreporting) :
		r"""Enable this option for Gx session reporting.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._gxsessionreporting = gxsessionreporting
		except Exception as e:
			raise e

	@property
	def securityinsighttraffic(self) :
		r"""Enable/disable the feature individually on appflow action.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._securityinsighttraffic
		except Exception as e:
			raise e

	@securityinsighttraffic.setter
	def securityinsighttraffic(self, securityinsighttraffic) :
		r"""Enable/disable the feature individually on appflow action.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._securityinsighttraffic = securityinsighttraffic
		except Exception as e:
			raise e

	@property
	def cacheinsight(self) :
		r"""Flag to determine whether cache records need to be exported or not. If this flag is true and IC is enabled, cache records are exported instead of L7 HTTP records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cacheinsight
		except Exception as e:
			raise e

	@cacheinsight.setter
	def cacheinsight(self, cacheinsight) :
		r"""Flag to determine whether cache records need to be exported or not. If this flag is true and IC is enabled, cache records are exported instead of L7 HTTP records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cacheinsight = cacheinsight
		except Exception as e:
			raise e

	@property
	def videoinsight(self) :
		r"""Enable/disable the feature individually on appflow action.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._videoinsight
		except Exception as e:
			raise e

	@videoinsight.setter
	def videoinsight(self, videoinsight) :
		r"""Enable/disable the feature individually on appflow action.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._videoinsight = videoinsight
		except Exception as e:
			raise e

	@property
	def httpquerywithurl(self) :
		r"""Include the HTTP query segment along with the URL that the Citrix ADC received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpquerywithurl
		except Exception as e:
			raise e

	@httpquerywithurl.setter
	def httpquerywithurl(self, httpquerywithurl) :
		r"""Include the HTTP query segment along with the URL that the Citrix ADC received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpquerywithurl = httpquerywithurl
		except Exception as e:
			raise e

	@property
	def urlcategory(self) :
		r"""Include the URL category record.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._urlcategory
		except Exception as e:
			raise e

	@urlcategory.setter
	def urlcategory(self, urlcategory) :
		r"""Include the URL category record.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._urlcategory = urlcategory
		except Exception as e:
			raise e

	@property
	def lsnlogging(self) :
		r"""On enabling this option, the Citrix ADC will send the Large Scale Nat(LSN) records to the configured collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._lsnlogging
		except Exception as e:
			raise e

	@lsnlogging.setter
	def lsnlogging(self, lsnlogging) :
		r"""On enabling this option, the Citrix ADC will send the Large Scale Nat(LSN) records to the configured collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._lsnlogging = lsnlogging
		except Exception as e:
			raise e

	@property
	def cqareporting(self) :
		r"""TCP CQA reporting enable/disable knob.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cqareporting
		except Exception as e:
			raise e

	@cqareporting.setter
	def cqareporting(self, cqareporting) :
		r"""TCP CQA reporting enable/disable knob.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cqareporting = cqareporting
		except Exception as e:
			raise e

	@property
	def emailaddress(self) :
		r"""Enable AppFlow user email-id logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._emailaddress
		except Exception as e:
			raise e

	@emailaddress.setter
	def emailaddress(self, emailaddress) :
		r"""Enable AppFlow user email-id logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._emailaddress = emailaddress
		except Exception as e:
			raise e

	@property
	def usagerecordinterval(self) :
		r"""On enabling this option, the NGS will send bandwidth usage record to configured collectors.<br/>Default value: 0<br/>Maximum length =  7200.
		"""
		try :
			return self._usagerecordinterval
		except Exception as e:
			raise e

	@usagerecordinterval.setter
	def usagerecordinterval(self, usagerecordinterval) :
		r"""On enabling this option, the NGS will send bandwidth usage record to configured collectors.<br/>Default value: 0<br/>Maximum length =  7200
		"""
		try :
			self._usagerecordinterval = usagerecordinterval
		except Exception as e:
			raise e

	@property
	def metrics(self) :
		r"""Enable Citrix ADC Stats to be sent to the Telemetry Agent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._metrics
		except Exception as e:
			raise e

	@metrics.setter
	def metrics(self, metrics) :
		r"""Enable Citrix ADC Stats to be sent to the Telemetry Agent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._metrics = metrics
		except Exception as e:
			raise e

	@property
	def events(self) :
		r"""Enable Events to be sent to the Telemetry Agent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._events
		except Exception as e:
			raise e

	@events.setter
	def events(self, events) :
		r"""Enable Events to be sent to the Telemetry Agent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._events = events
		except Exception as e:
			raise e

	@property
	def auditlogs(self) :
		r"""Enable Auditlogs to be sent to the Telemetry Agent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._auditlogs
		except Exception as e:
			raise e

	@auditlogs.setter
	def auditlogs(self, auditlogs) :
		r"""Enable Auditlogs to be sent to the Telemetry Agent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._auditlogs = auditlogs
		except Exception as e:
			raise e

	@property
	def observationpointid(self) :
		r"""An observation point ID is identifier for the NetScaler from which appflow records are being exported. By default, the NetScaler IP is the observation point ID.<br/>Minimum length =  1.
		"""
		try :
			return self._observationpointid
		except Exception as e:
			raise e

	@observationpointid.setter
	def observationpointid(self, observationpointid) :
		r"""An observation point ID is identifier for the NetScaler from which appflow records are being exported. By default, the NetScaler IP is the observation point ID.<br/>Minimum length =  1
		"""
		try :
			self._observationpointid = observationpointid
		except Exception as e:
			raise e

	@property
	def tcpattackcounterinterval(self) :
		r"""Interval, in seconds, at which to send tcp attack counters to the configured collectors. If 0 is configured, the record is not sent.<br/>Default value: 0<br/>Maximum length =  3600.
		"""
		try :
			return self._tcpattackcounterinterval
		except Exception as e:
			raise e

	@tcpattackcounterinterval.setter
	def tcpattackcounterinterval(self, tcpattackcounterinterval) :
		r"""Interval, in seconds, at which to send tcp attack counters to the configured collectors. If 0 is configured, the record is not sent.<br/>Default value: 0<br/>Maximum length =  3600
		"""
		try :
			self._tcpattackcounterinterval = tcpattackcounterinterval
		except Exception as e:
			raise e

	@property
	def tcpburstreporting(self) :
		r"""TCP burst reporting enable/disable knob.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tcpburstreporting
		except Exception as e:
			raise e

	@property
	def tcpburstreportingthreshold(self) :
		r"""TCP burst reporting threshold.<br/>Default value: 1500<br/>Minimum value =  10<br/>Maximum value =  5000.
		"""
		try :
			return self._tcpburstreportingthreshold
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appflowparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appflowparam
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
		r""" Use this API to update appflowparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = appflowparam()
				updateresource.templaterefresh = resource.templaterefresh
				updateresource.appnamerefresh = resource.appnamerefresh
				updateresource.flowrecordinterval = resource.flowrecordinterval
				updateresource.securityinsightrecordinterval = resource.securityinsightrecordinterval
				updateresource.udppmtu = resource.udppmtu
				updateresource.httpurl = resource.httpurl
				updateresource.aaausername = resource.aaausername
				updateresource.httpcookie = resource.httpcookie
				updateresource.httpreferer = resource.httpreferer
				updateresource.httpmethod = resource.httpmethod
				updateresource.httphost = resource.httphost
				updateresource.httpuseragent = resource.httpuseragent
				updateresource.clienttrafficonly = resource.clienttrafficonly
				updateresource.httpcontenttype = resource.httpcontenttype
				updateresource.httpauthorization = resource.httpauthorization
				updateresource.httpvia = resource.httpvia
				updateresource.httpxforwardedfor = resource.httpxforwardedfor
				updateresource.httplocation = resource.httplocation
				updateresource.httpsetcookie = resource.httpsetcookie
				updateresource.httpsetcookie2 = resource.httpsetcookie2
				updateresource.connectionchaining = resource.connectionchaining
				updateresource.httpdomain = resource.httpdomain
				updateresource.skipcacheredirectionhttptransaction = resource.skipcacheredirectionhttptransaction
				updateresource.identifiername = resource.identifiername
				updateresource.identifiersessionname = resource.identifiersessionname
				updateresource.observationdomainid = resource.observationdomainid
				updateresource.observationdomainname = resource.observationdomainname
				updateresource.feature = resource.feature
				updateresource.subscriberawareness = resource.subscriberawareness
				updateresource.subscriberidobfuscation = resource.subscriberidobfuscation
				updateresource.subscriberidobfuscationalgo = resource.subscriberidobfuscationalgo
				updateresource.gxsessionreporting = resource.gxsessionreporting
				updateresource.securityinsighttraffic = resource.securityinsighttraffic
				updateresource.cacheinsight = resource.cacheinsight
				updateresource.videoinsight = resource.videoinsight
				updateresource.httpquerywithurl = resource.httpquerywithurl
				updateresource.urlcategory = resource.urlcategory
				updateresource.lsnlogging = resource.lsnlogging
				updateresource.cqareporting = resource.cqareporting
				updateresource.emailaddress = resource.emailaddress
				updateresource.usagerecordinterval = resource.usagerecordinterval
				updateresource.metrics = resource.metrics
				updateresource.events = resource.events
				updateresource.auditlogs = resource.auditlogs
				updateresource.observationpointid = resource.observationpointid
				updateresource.tcpattackcounterinterval = resource.tcpattackcounterinterval
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of appflowparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = appflowparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the appflowparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appflowparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Httpreferer:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cqareporting:
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

	class Httpsetcookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpvia:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Gxsessionreporting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpdomain:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Videoinsight:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpsetcookie2:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Auditlogs:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpquerywithurl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpauthorization:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Urlcategory:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Skipcacheredirectionhttptransaction:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Aaausername:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Lsnlogging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clienttrafficonly:
		YES = "YES"
		NO = "NO"

	class Securityinsighttraffic:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpcontenttype:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cacheinsight:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Emailaddress:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpmethod:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Subscriberawareness:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httplocation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Identifiersessionname:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tcpburstreporting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Metrics:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Connectionchaining:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Subscriberidobfuscation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpxforwardedfor:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Subscriberidobfuscationalgo:
		MD5 = "MD5"
		SHA256 = "SHA256"

	class Identifiername:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpcookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpurl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Events:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpuseragent:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httphost:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class appflowparam_response(base_response) :
	def __init__(self, length=1) :
		self.appflowparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appflowparam = [appflowparam() for _ in range(length)]

