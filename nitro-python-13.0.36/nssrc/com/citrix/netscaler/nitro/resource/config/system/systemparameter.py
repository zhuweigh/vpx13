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

class systemparameter(base_resource) :
	""" Configuration for system parameter resource. """
	def __init__(self) :
		self._rbaonresponse = None
		self._promptstring = None
		self._natpcbforceflushlimit = None
		self._natpcbrstontimeout = None
		self._timeout = None
		self._localauth = None
		self._minpasswordlen = None
		self._strongpassword = None
		self._restrictedtimeout = None
		self._fipsusermode = None
		self._doppler = None
		self._googleanalytics = None
		self._totalauthtimeout = None
		self._cliloglevel = None
		self._forcepasswordchange = None
		self._basicauth = None
		self._reauthonauthparamchange = None
		self._removesensitivefiles = None
		self._maxclient = None
		self._allowdefaultpartition = None

	@property
	def rbaonresponse(self) :
		r"""Enable or disable Role-Based Authentication (RBA) on responses.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rbaonresponse
		except Exception as e:
			raise e

	@rbaonresponse.setter
	def rbaonresponse(self, rbaonresponse) :
		r"""Enable or disable Role-Based Authentication (RBA) on responses.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rbaonresponse = rbaonresponse
		except Exception as e:
			raise e

	@property
	def promptstring(self) :
		r"""String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables: 
		* %u - Will be replaced by the user name.
		* %h - Will be replaced by the hostname of the Citrix ADC.
		* %t - Will be replaced by the current time in 12-hour format.
		* %T - Will be replaced by the current time in 24-hour format.
		* %d - Will be replaced by the current date.
		* %s - Will be replaced by the state of the Citrix ADC.
		Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1.
		"""
		try :
			return self._promptstring
		except Exception as e:
			raise e

	@promptstring.setter
	def promptstring(self, promptstring) :
		r"""String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables: 
		* %u - Will be replaced by the user name.
		* %h - Will be replaced by the hostname of the Citrix ADC.
		* %t - Will be replaced by the current time in 12-hour format.
		* %T - Will be replaced by the current time in 24-hour format.
		* %d - Will be replaced by the current date.
		* %s - Will be replaced by the state of the Citrix ADC.
		Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1
		"""
		try :
			self._promptstring = promptstring
		except Exception as e:
			raise e

	@property
	def natpcbforceflushlimit(self) :
		r"""Flush the system if the number of Network Address Translation Protocol Control Blocks (NATPCBs) exceeds this value.<br/>Default value: 2147483647<br/>Minimum length =  1000.
		"""
		try :
			return self._natpcbforceflushlimit
		except Exception as e:
			raise e

	@natpcbforceflushlimit.setter
	def natpcbforceflushlimit(self, natpcbforceflushlimit) :
		r"""Flush the system if the number of Network Address Translation Protocol Control Blocks (NATPCBs) exceeds this value.<br/>Default value: 2147483647<br/>Minimum length =  1000
		"""
		try :
			self._natpcbforceflushlimit = natpcbforceflushlimit
		except Exception as e:
			raise e

	@property
	def natpcbrstontimeout(self) :
		r"""Send a reset signal to client and server connections when their NATPCBs time out. Avoids the buildup of idle TCP connections on both the sides.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._natpcbrstontimeout
		except Exception as e:
			raise e

	@natpcbrstontimeout.setter
	def natpcbrstontimeout(self, natpcbrstontimeout) :
		r"""Send a reset signal to client and server connections when their NATPCBs time out. Avoids the buildup of idle TCP connections on both the sides.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._natpcbrstontimeout = natpcbrstontimeout
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		r"""CLI session inactivity timeout, in seconds. If Restrictedtimeout argument is enabled, Timeout can have values in the range [300-86400] seconds.
		If Restrictedtimeout argument is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		r"""CLI session inactivity timeout, in seconds. If Restrictedtimeout argument is enabled, Timeout can have values in the range [300-86400] seconds.
		If Restrictedtimeout argument is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	@property
	def localauth(self) :
		r"""When enabled, local users can access Citrix ADC even when external authentication is configured. When disabled, local users are not allowed to access the Citrix ADC, Local users can access the Citrix ADC only when the configured external authentication servers are unavailable. This parameter is not applicable to SSH Key-based authentication.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._localauth
		except Exception as e:
			raise e

	@localauth.setter
	def localauth(self, localauth) :
		r"""When enabled, local users can access Citrix ADC even when external authentication is configured. When disabled, local users are not allowed to access the Citrix ADC, Local users can access the Citrix ADC only when the configured external authentication servers are unavailable. This parameter is not applicable to SSH Key-based authentication.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._localauth = localauth
		except Exception as e:
			raise e

	@property
	def minpasswordlen(self) :
		r"""Minimum length of system user password. When strong password is enabled default minimum length is 4. User entered value can be greater than or equal to 4. Default mininum value is 1 when strong password is disabled. Maximum value is 127 in both cases.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._minpasswordlen
		except Exception as e:
			raise e

	@minpasswordlen.setter
	def minpasswordlen(self, minpasswordlen) :
		r"""Minimum length of system user password. When strong password is enabled default minimum length is 4. User entered value can be greater than or equal to 4. Default mininum value is 1 when strong password is disabled. Maximum value is 127 in both cases.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._minpasswordlen = minpasswordlen
		except Exception as e:
			raise e

	@property
	def strongpassword(self) :
		r"""After enabling strong password (enableall / enablelocal - not included in exclude list), all the passwords / sensitive information must have - Atleast 1 Lower case character, Atleast 1 Upper case character, Atleast 1 numeric character, Atleast 1 special character ( ~, `, !, @, #, $, %, ^, &, *, -, _, =, +, {, }, [, ], |, \, :, <, >, /, ., ,, " "). Exclude list in case of enablelocal is - NS_FIPS, NS_CRL, NS_RSAKEY, NS_PKCS12, NS_PKCS8, NS_LDAP, NS_TACACS, NS_TACACSACTION, NS_RADIUS, NS_RADIUSACTION, NS_ENCRYPTION_PARAMS. So no Strong Password checks will be performed on these ObjectType commands for enablelocal case.<br/>Default value: disabled<br/>Possible values = enableall, enablelocal, disabled.
		"""
		try :
			return self._strongpassword
		except Exception as e:
			raise e

	@strongpassword.setter
	def strongpassword(self, strongpassword) :
		r"""After enabling strong password (enableall / enablelocal - not included in exclude list), all the passwords / sensitive information must have - Atleast 1 Lower case character, Atleast 1 Upper case character, Atleast 1 numeric character, Atleast 1 special character ( ~, `, !, @, #, $, %, ^, &, *, -, _, =, +, {, }, [, ], |, \, :, <, >, /, ., ,, " "). Exclude list in case of enablelocal is - NS_FIPS, NS_CRL, NS_RSAKEY, NS_PKCS12, NS_PKCS8, NS_LDAP, NS_TACACS, NS_TACACSACTION, NS_RADIUS, NS_RADIUSACTION, NS_ENCRYPTION_PARAMS. So no Strong Password checks will be performed on these ObjectType commands for enablelocal case.<br/>Default value: disabled<br/>Possible values = enableall, enablelocal, disabled
		"""
		try :
			self._strongpassword = strongpassword
		except Exception as e:
			raise e

	@property
	def restrictedtimeout(self) :
		r"""Enable/Disable the restricted timeout behaviour. When enabled, timeout cannot be configured beyond admin configured timeout  and also it will have the [minimum - maximum] range check. When disabled, timeout will have the old behaviour. By default the value is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._restrictedtimeout
		except Exception as e:
			raise e

	@restrictedtimeout.setter
	def restrictedtimeout(self, restrictedtimeout) :
		r"""Enable/Disable the restricted timeout behaviour. When enabled, timeout cannot be configured beyond admin configured timeout  and also it will have the [minimum - maximum] range check. When disabled, timeout will have the old behaviour. By default the value is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._restrictedtimeout = restrictedtimeout
		except Exception as e:
			raise e

	@property
	def fipsusermode(self) :
		r"""Use this option to set the FIPS mode for key user-land processes. When enabled, these user-land processes will operate in FIPS mode. In this mode, theses processes will use FIPS 140-2 Level-1 certified crypto algorithms. Default is disabled, wherein, these user-land processes will not operate in FIPS mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._fipsusermode
		except Exception as e:
			raise e

	@fipsusermode.setter
	def fipsusermode(self, fipsusermode) :
		r"""Use this option to set the FIPS mode for key user-land processes. When enabled, these user-land processes will operate in FIPS mode. In this mode, theses processes will use FIPS 140-2 Level-1 certified crypto algorithms. Default is disabled, wherein, these user-land processes will not operate in FIPS mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._fipsusermode = fipsusermode
		except Exception as e:
			raise e

	@property
	def doppler(self) :
		r"""Enable or disable Doppler.<br/>Default value: 0<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._doppler
		except Exception as e:
			raise e

	@doppler.setter
	def doppler(self, doppler) :
		r"""Enable or disable Doppler.<br/>Default value: 0<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._doppler = doppler
		except Exception as e:
			raise e

	@property
	def googleanalytics(self) :
		r"""Enable or disable Google analytics.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._googleanalytics
		except Exception as e:
			raise e

	@googleanalytics.setter
	def googleanalytics(self, googleanalytics) :
		r"""Enable or disable Google analytics.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._googleanalytics = googleanalytics
		except Exception as e:
			raise e

	@property
	def totalauthtimeout(self) :
		r"""Total time a request can take for authentication/authorization.<br/>Default value: 20<br/>Minimum length =  5<br/>Maximum length =  120.
		"""
		try :
			return self._totalauthtimeout
		except Exception as e:
			raise e

	@totalauthtimeout.setter
	def totalauthtimeout(self, totalauthtimeout) :
		r"""Total time a request can take for authentication/authorization.<br/>Default value: 20<br/>Minimum length =  5<br/>Maximum length =  120
		"""
		try :
			self._totalauthtimeout = totalauthtimeout
		except Exception as e:
			raise e

	@property
	def cliloglevel(self) :
		r"""Audit log level, which specifies the types of events to log for cli executed commands.
		Available values function as follows:
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Default value: INFORMATIONAL<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG.
		"""
		try :
			return self._cliloglevel
		except Exception as e:
			raise e

	@cliloglevel.setter
	def cliloglevel(self, cliloglevel) :
		r"""Audit log level, which specifies the types of events to log for cli executed commands.
		Available values function as follows:
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Default value: INFORMATIONAL<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG
		"""
		try :
			self._cliloglevel = cliloglevel
		except Exception as e:
			raise e

	@property
	def forcepasswordchange(self) :
		r"""Enable or disable force password change for nsroot user.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._forcepasswordchange
		except Exception as e:
			raise e

	@forcepasswordchange.setter
	def forcepasswordchange(self, forcepasswordchange) :
		r"""Enable or disable force password change for nsroot user.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._forcepasswordchange = forcepasswordchange
		except Exception as e:
			raise e

	@property
	def basicauth(self) :
		r"""Enable or disable basic authentication for Nitro API.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._basicauth
		except Exception as e:
			raise e

	@basicauth.setter
	def basicauth(self, basicauth) :
		r"""Enable or disable basic authentication for Nitro API.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._basicauth = basicauth
		except Exception as e:
			raise e

	@property
	def reauthonauthparamchange(self) :
		r"""Enable or disable External user reauthentication when authentication parameter changes.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._reauthonauthparamchange
		except Exception as e:
			raise e

	@reauthonauthparamchange.setter
	def reauthonauthparamchange(self, reauthonauthparamchange) :
		r"""Enable or disable External user reauthentication when authentication parameter changes.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._reauthonauthparamchange = reauthonauthparamchange
		except Exception as e:
			raise e

	@property
	def removesensitivefiles(self) :
		r"""Use this option to remove the sensitive files from the system like authorise keys, public keys etc. The commands which will remove sensitive files when this system paramter is enabled are rm cluster instance, rm cluster node, rm ha node, clear config full, join cluster and add cluster instance.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._removesensitivefiles
		except Exception as e:
			raise e

	@removesensitivefiles.setter
	def removesensitivefiles(self, removesensitivefiles) :
		r"""Use this option to remove the sensitive files from the system like authorise keys, public keys etc. The commands which will remove sensitive files when this system paramter is enabled are rm cluster instance, rm cluster node, rm ha node, clear config full, join cluster and add cluster instance.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._removesensitivefiles = removesensitivefiles
		except Exception as e:
			raise e

	@property
	def maxclient(self) :
		r"""Maximum number of client connection allowed by the system.<br/>Minimum value =  20<br/>Maximum value =  40.
		"""
		try :
			return self._maxclient
		except Exception as e:
			raise e

	@property
	def allowdefaultpartition(self) :
		r"""Enable/Disable the allowing partition users to access default partition.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._allowdefaultpartition
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemparameter
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
		r""" Use this API to update systemparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = systemparameter()
				updateresource.rbaonresponse = resource.rbaonresponse
				updateresource.promptstring = resource.promptstring
				updateresource.natpcbforceflushlimit = resource.natpcbforceflushlimit
				updateresource.natpcbrstontimeout = resource.natpcbrstontimeout
				updateresource.timeout = resource.timeout
				updateresource.localauth = resource.localauth
				updateresource.minpasswordlen = resource.minpasswordlen
				updateresource.strongpassword = resource.strongpassword
				updateresource.restrictedtimeout = resource.restrictedtimeout
				updateresource.fipsusermode = resource.fipsusermode
				updateresource.doppler = resource.doppler
				updateresource.googleanalytics = resource.googleanalytics
				updateresource.totalauthtimeout = resource.totalauthtimeout
				updateresource.cliloglevel = resource.cliloglevel
				updateresource.forcepasswordchange = resource.forcepasswordchange
				updateresource.basicauth = resource.basicauth
				updateresource.reauthonauthparamchange = resource.reauthonauthparamchange
				updateresource.removesensitivefiles = resource.removesensitivefiles
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of systemparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = systemparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the systemparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Strongpassword:
		enableall = "enableall"
		enablelocal = "enablelocal"
		disabled = "disabled"

	class Reauthonauthparamchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Forcepasswordchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Localauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Fipsusermode:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Removesensitivefiles:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Doppler:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Basicauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Googleanalytics:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Restrictedtimeout:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rbaonresponse:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cliloglevel:
		EMERGENCY = "EMERGENCY"
		ALERT = "ALERT"
		CRITICAL = "CRITICAL"
		ERROR = "ERROR"
		WARNING = "WARNING"
		NOTICE = "NOTICE"
		INFORMATIONAL = "INFORMATIONAL"
		DEBUG = "DEBUG"

	class Allowdefaultpartition:
		YES = "YES"
		NO = "NO"

	class Natpcbrstontimeout:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class systemparameter_response(base_response) :
	def __init__(self, length=1) :
		self.systemparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemparameter = [systemparameter() for _ in range(length)]

