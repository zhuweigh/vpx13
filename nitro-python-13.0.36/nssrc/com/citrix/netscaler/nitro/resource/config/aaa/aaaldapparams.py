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

class aaaldapparams(base_resource) :
	""" Configuration for LDAP parameter resource. """
	def __init__(self) :
		self._serverip = None
		self._serverport = None
		self._authtimeout = None
		self._ldapbase = None
		self._ldapbinddn = None
		self._ldapbinddnpassword = None
		self._ldaploginname = None
		self._searchfilter = None
		self._groupattrname = None
		self._subattributename = None
		self._sectype = None
		self._svrtype = None
		self._ssonameattribute = None
		self._passwdchange = None
		self._nestedgroupextraction = None
		self._maxnestinglevel = None
		self._groupnameidentifier = None
		self._groupsearchattribute = None
		self._groupsearchsubattribute = None
		self._groupsearchfilter = None
		self._defaultauthenticationgroup = None
		self._feature = None
		self._groupauthname = None

	@property
	def serverip(self) :
		r"""IP address of your LDAP server.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		r"""IP address of your LDAP server.
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		r"""Port number on which the LDAP server listens for connections.<br/>Default value: 389<br/>Minimum length =  1.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		r"""Port number on which the LDAP server listens for connections.<br/>Default value: 389<br/>Minimum length =  1
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def authtimeout(self) :
		r"""Maximum number of seconds that the Citrix ADC waits for a response from the LDAP server.<br/>Default value: 3<br/>Minimum length =  1.
		"""
		try :
			return self._authtimeout
		except Exception as e:
			raise e

	@authtimeout.setter
	def authtimeout(self, authtimeout) :
		r"""Maximum number of seconds that the Citrix ADC waits for a response from the LDAP server.<br/>Default value: 3<br/>Minimum length =  1
		"""
		try :
			self._authtimeout = authtimeout
		except Exception as e:
			raise e

	@property
	def ldapbase(self) :
		r"""Base (the server and location) from which LDAP search commands should start. 
		If the LDAP server is running locally, the default value of base is dc=netscaler, dc=com.
		"""
		try :
			return self._ldapbase
		except Exception as e:
			raise e

	@ldapbase.setter
	def ldapbase(self, ldapbase) :
		r"""Base (the server and location) from which LDAP search commands should start. 
		If the LDAP server is running locally, the default value of base is dc=netscaler, dc=com.
		"""
		try :
			self._ldapbase = ldapbase
		except Exception as e:
			raise e

	@property
	def ldapbinddn(self) :
		r"""Complete distinguished name (DN) string used for binding to the LDAP server.
		"""
		try :
			return self._ldapbinddn
		except Exception as e:
			raise e

	@ldapbinddn.setter
	def ldapbinddn(self, ldapbinddn) :
		r"""Complete distinguished name (DN) string used for binding to the LDAP server.
		"""
		try :
			self._ldapbinddn = ldapbinddn
		except Exception as e:
			raise e

	@property
	def ldapbinddnpassword(self) :
		r"""Password for binding to the LDAP server.<br/>Minimum length =  1.
		"""
		try :
			return self._ldapbinddnpassword
		except Exception as e:
			raise e

	@ldapbinddnpassword.setter
	def ldapbinddnpassword(self, ldapbinddnpassword) :
		r"""Password for binding to the LDAP server.<br/>Minimum length =  1
		"""
		try :
			self._ldapbinddnpassword = ldapbinddnpassword
		except Exception as e:
			raise e

	@property
	def ldaploginname(self) :
		r"""Name attribute that the Citrix ADC uses to query the external LDAP server or an Active Directory.
		"""
		try :
			return self._ldaploginname
		except Exception as e:
			raise e

	@ldaploginname.setter
	def ldaploginname(self, ldaploginname) :
		r"""Name attribute that the Citrix ADC uses to query the external LDAP server or an Active Directory.
		"""
		try :
			self._ldaploginname = ldaploginname
		except Exception as e:
			raise e

	@property
	def searchfilter(self) :
		r"""String to be combined with the default LDAP user search string to form the value to use when executing an LDAP search. 
		For example, the following values:
		vpnallowed=true,
		ldaploginame=""samaccount""
		when combined with the user-supplied username ""bob"", yield the following LDAP search string:
		""(&(vpnallowed=true)(samaccount=bob)"".<br/>Minimum length =  1.
		"""
		try :
			return self._searchfilter
		except Exception as e:
			raise e

	@searchfilter.setter
	def searchfilter(self, searchfilter) :
		r"""String to be combined with the default LDAP user search string to form the value to use when executing an LDAP search. 
		For example, the following values:
		vpnallowed=true,
		ldaploginame=""samaccount""
		when combined with the user-supplied username ""bob"", yield the following LDAP search string:
		""(&(vpnallowed=true)(samaccount=bob)"".<br/>Minimum length =  1
		"""
		try :
			self._searchfilter = searchfilter
		except Exception as e:
			raise e

	@property
	def groupattrname(self) :
		r"""Attribute name used for group extraction from the LDAP server.
		"""
		try :
			return self._groupattrname
		except Exception as e:
			raise e

	@groupattrname.setter
	def groupattrname(self, groupattrname) :
		r"""Attribute name used for group extraction from the LDAP server.
		"""
		try :
			self._groupattrname = groupattrname
		except Exception as e:
			raise e

	@property
	def subattributename(self) :
		r"""Subattribute name used for group extraction from the LDAP server.
		"""
		try :
			return self._subattributename
		except Exception as e:
			raise e

	@subattributename.setter
	def subattributename(self, subattributename) :
		r"""Subattribute name used for group extraction from the LDAP server.
		"""
		try :
			self._subattributename = subattributename
		except Exception as e:
			raise e

	@property
	def sectype(self) :
		r"""Type of security used for communications between the Citrix ADC and the LDAP server. For the PLAINTEXT setting, no encryption is required.<br/>Default value: PLAINTEXT<br/>Possible values = PLAINTEXT, TLS, SSL.
		"""
		try :
			return self._sectype
		except Exception as e:
			raise e

	@sectype.setter
	def sectype(self, sectype) :
		r"""Type of security used for communications between the Citrix ADC and the LDAP server. For the PLAINTEXT setting, no encryption is required.<br/>Default value: PLAINTEXT<br/>Possible values = PLAINTEXT, TLS, SSL
		"""
		try :
			self._sectype = sectype
		except Exception as e:
			raise e

	@property
	def svrtype(self) :
		r"""The type of LDAP server.<br/>Default value: AAA_LDAP_SERVER_TYPE_DEFAULT<br/>Possible values = AD, NDS.
		"""
		try :
			return self._svrtype
		except Exception as e:
			raise e

	@svrtype.setter
	def svrtype(self, svrtype) :
		r"""The type of LDAP server.<br/>Default value: AAA_LDAP_SERVER_TYPE_DEFAULT<br/>Possible values = AD, NDS
		"""
		try :
			self._svrtype = svrtype
		except Exception as e:
			raise e

	@property
	def ssonameattribute(self) :
		r"""Attribute used by the Citrix ADC to query an external LDAP server or Active Directory for an alternative username. 
		This alternative username is then used for single sign-on (SSO).
		"""
		try :
			return self._ssonameattribute
		except Exception as e:
			raise e

	@ssonameattribute.setter
	def ssonameattribute(self, ssonameattribute) :
		r"""Attribute used by the Citrix ADC to query an external LDAP server or Active Directory for an alternative username. 
		This alternative username is then used for single sign-on (SSO).
		"""
		try :
			self._ssonameattribute = ssonameattribute
		except Exception as e:
			raise e

	@property
	def passwdchange(self) :
		r"""Accept password change requests.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._passwdchange
		except Exception as e:
			raise e

	@passwdchange.setter
	def passwdchange(self, passwdchange) :
		r"""Accept password change requests.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._passwdchange = passwdchange
		except Exception as e:
			raise e

	@property
	def nestedgroupextraction(self) :
		r"""Queries the external LDAP server to determine whether the specified group belongs to another group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._nestedgroupextraction
		except Exception as e:
			raise e

	@nestedgroupextraction.setter
	def nestedgroupextraction(self, nestedgroupextraction) :
		r"""Queries the external LDAP server to determine whether the specified group belongs to another group.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._nestedgroupextraction = nestedgroupextraction
		except Exception as e:
			raise e

	@property
	def maxnestinglevel(self) :
		r"""Number of levels up to which the system can query nested LDAP groups.<br/>Default value: 2<br/>Minimum length =  2.
		"""
		try :
			return self._maxnestinglevel
		except Exception as e:
			raise e

	@maxnestinglevel.setter
	def maxnestinglevel(self, maxnestinglevel) :
		r"""Number of levels up to which the system can query nested LDAP groups.<br/>Default value: 2<br/>Minimum length =  2
		"""
		try :
			self._maxnestinglevel = maxnestinglevel
		except Exception as e:
			raise e

	@property
	def groupnameidentifier(self) :
		r"""LDAP-group attribute that uniquely identifies the group. No two groups on one LDAP server can have the same group name identifier.
		"""
		try :
			return self._groupnameidentifier
		except Exception as e:
			raise e

	@groupnameidentifier.setter
	def groupnameidentifier(self, groupnameidentifier) :
		r"""LDAP-group attribute that uniquely identifies the group. No two groups on one LDAP server can have the same group name identifier.
		"""
		try :
			self._groupnameidentifier = groupnameidentifier
		except Exception as e:
			raise e

	@property
	def groupsearchattribute(self) :
		r"""LDAP-group attribute that designates the parent group of the specified group. Use this attribute to search for a group's parent group.
		"""
		try :
			return self._groupsearchattribute
		except Exception as e:
			raise e

	@groupsearchattribute.setter
	def groupsearchattribute(self, groupsearchattribute) :
		r"""LDAP-group attribute that designates the parent group of the specified group. Use this attribute to search for a group's parent group.
		"""
		try :
			self._groupsearchattribute = groupsearchattribute
		except Exception as e:
			raise e

	@property
	def groupsearchsubattribute(self) :
		r"""LDAP-group subattribute that designates the parent group of the specified group. Use this attribute to search for a group's parent group.
		"""
		try :
			return self._groupsearchsubattribute
		except Exception as e:
			raise e

	@groupsearchsubattribute.setter
	def groupsearchsubattribute(self, groupsearchsubattribute) :
		r"""LDAP-group subattribute that designates the parent group of the specified group. Use this attribute to search for a group's parent group.
		"""
		try :
			self._groupsearchsubattribute = groupsearchsubattribute
		except Exception as e:
			raise e

	@property
	def groupsearchfilter(self) :
		r"""Search-expression that can be specified for sending group-search requests to the LDAP server.
		"""
		try :
			return self._groupsearchfilter
		except Exception as e:
			raise e

	@groupsearchfilter.setter
	def groupsearchfilter(self, groupsearchfilter) :
		r"""Search-expression that can be specified for sending group-search requests to the LDAP server.
		"""
		try :
			self._groupsearchfilter = groupsearchfilter
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
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
	def groupauthname(self) :
		r"""To associate AAA users with an AAA group, use the command
		"bind AAA group ... -username ...".
		You can bind different policies to each AAA group. Use the command
		"bind AAA group ... -policy ...".
		"""
		try :
			return self._groupauthname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaaldapparams_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaaldapparams
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
		r""" Use this API to update aaaldapparams.
		"""
		try :
			if type(resource) is not list :
				updateresource = aaaldapparams()
				updateresource.serverip = resource.serverip
				updateresource.serverport = resource.serverport
				updateresource.authtimeout = resource.authtimeout
				updateresource.ldapbase = resource.ldapbase
				updateresource.ldapbinddn = resource.ldapbinddn
				updateresource.ldapbinddnpassword = resource.ldapbinddnpassword
				updateresource.ldaploginname = resource.ldaploginname
				updateresource.searchfilter = resource.searchfilter
				updateresource.groupattrname = resource.groupattrname
				updateresource.subattributename = resource.subattributename
				updateresource.sectype = resource.sectype
				updateresource.svrtype = resource.svrtype
				updateresource.ssonameattribute = resource.ssonameattribute
				updateresource.passwdchange = resource.passwdchange
				updateresource.nestedgroupextraction = resource.nestedgroupextraction
				updateresource.maxnestinglevel = resource.maxnestinglevel
				updateresource.groupnameidentifier = resource.groupnameidentifier
				updateresource.groupsearchattribute = resource.groupsearchattribute
				updateresource.groupsearchsubattribute = resource.groupsearchsubattribute
				updateresource.groupsearchfilter = resource.groupsearchfilter
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				updateresource.feature = resource.feature
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of aaaldapparams resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = aaaldapparams()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the aaaldapparams resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaaldapparams()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Passwdchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sectype:
		PLAINTEXT = "PLAINTEXT"
		TLS = "TLS"
		SSL = "SSL"

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

	class Svrtype:
		AD = "AD"
		NDS = "NDS"

	class Nestedgroupextraction:
		ON = "ON"
		OFF = "OFF"

class aaaldapparams_response(base_response) :
	def __init__(self, length=1) :
		self.aaaldapparams = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaaldapparams = [aaaldapparams() for _ in range(length)]

