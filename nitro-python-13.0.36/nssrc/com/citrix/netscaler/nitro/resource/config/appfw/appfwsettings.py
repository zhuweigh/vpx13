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

class appfwsettings(base_resource) :
	""" Configuration for AS settings resource. """
	def __init__(self) :
		self._defaultprofile = None
		self._undefaction = None
		self._sessiontimeout = None
		self._learnratelimit = None
		self._sessionlifetime = None
		self._sessioncookiename = None
		self._clientiploggingheader = None
		self._importsizelimit = None
		self._signatureautoupdate = None
		self._signatureurl = None
		self._cookiepostencryptprefix = None
		self._logmalformedreq = None
		self._geolocationlogging = None
		self._ceflogging = None
		self._entitydecoding = None
		self._useconfigurablesecretkey = None
		self._sessionlimit = None
		self._malformedreqaction = None

	@property
	def defaultprofile(self) :
		r"""Profile to use when a connection does not match any policy. Default setting is APPFW_BYPASS, which sends unmatched connections back to the Citrix ADC without attempting to filter them further.<br/>Default value: APPFW_BYPASS<br/>Minimum length =  1.
		"""
		try :
			return self._defaultprofile
		except Exception as e:
			raise e

	@defaultprofile.setter
	def defaultprofile(self, defaultprofile) :
		r"""Profile to use when a connection does not match any policy. Default setting is APPFW_BYPASS, which sends unmatched connections back to the Citrix ADC without attempting to filter them further.<br/>Default value: APPFW_BYPASS<br/>Minimum length =  1
		"""
		try :
			self._defaultprofile = defaultprofile
		except Exception as e:
			raise e

	@property
	def undefaction(self) :
		r"""Profile to use when an application firewall policy evaluates to undefined (UNDEF). 
		An UNDEF event indicates an internal error condition. The APPFW_BLOCK built-in profile is the default setting. You can specify a different built-in or user-created profile as the UNDEF profile.<br/>Default value: APPFW_BLOCK<br/>Minimum length =  1.
		"""
		try :
			return self._undefaction
		except Exception as e:
			raise e

	@undefaction.setter
	def undefaction(self, undefaction) :
		r"""Profile to use when an application firewall policy evaluates to undefined (UNDEF). 
		An UNDEF event indicates an internal error condition. The APPFW_BLOCK built-in profile is the default setting. You can specify a different built-in or user-created profile as the UNDEF profile.<br/>Default value: APPFW_BLOCK<br/>Minimum length =  1
		"""
		try :
			self._undefaction = undefaction
		except Exception as e:
			raise e

	@property
	def sessiontimeout(self) :
		r"""Timeout, in seconds, after which a user session is terminated. Before continuing to use the protected web site, the user must establish a new session by opening a designated start URL.<br/>Default value: 900<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._sessiontimeout
		except Exception as e:
			raise e

	@sessiontimeout.setter
	def sessiontimeout(self, sessiontimeout) :
		r"""Timeout, in seconds, after which a user session is terminated. Before continuing to use the protected web site, the user must establish a new session by opening a designated start URL.<br/>Default value: 900<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._sessiontimeout = sessiontimeout
		except Exception as e:
			raise e

	@property
	def learnratelimit(self) :
		r"""Maximum number of connections per second that the application firewall learning engine examines to generate new relaxations for learning-enabled security checks. The application firewall drops any connections above this limit from the list of connections used by the learning engine.<br/>Default value: 400<br/>Minimum length =  1<br/>Maximum length =  1000.
		"""
		try :
			return self._learnratelimit
		except Exception as e:
			raise e

	@learnratelimit.setter
	def learnratelimit(self, learnratelimit) :
		r"""Maximum number of connections per second that the application firewall learning engine examines to generate new relaxations for learning-enabled security checks. The application firewall drops any connections above this limit from the list of connections used by the learning engine.<br/>Default value: 400<br/>Minimum length =  1<br/>Maximum length =  1000
		"""
		try :
			self._learnratelimit = learnratelimit
		except Exception as e:
			raise e

	@property
	def sessionlifetime(self) :
		r"""Maximum amount of time (in seconds) that the application firewall allows a user session to remain active, regardless of user activity. After this time, the user session is terminated. Before continuing to use the protected web site, the user must establish a new session by opening a designated start URL.<br/>Default value: 0<br/>Maximum length =  2147483647.
		"""
		try :
			return self._sessionlifetime
		except Exception as e:
			raise e

	@sessionlifetime.setter
	def sessionlifetime(self, sessionlifetime) :
		r"""Maximum amount of time (in seconds) that the application firewall allows a user session to remain active, regardless of user activity. After this time, the user session is terminated. Before continuing to use the protected web site, the user must establish a new session by opening a designated start URL.<br/>Default value: 0<br/>Maximum length =  2147483647
		"""
		try :
			self._sessionlifetime = sessionlifetime
		except Exception as e:
			raise e

	@property
	def sessioncookiename(self) :
		r"""Name of the session cookie that the application firewall uses to track user sessions. 
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1.
		"""
		try :
			return self._sessioncookiename
		except Exception as e:
			raise e

	@sessioncookiename.setter
	def sessioncookiename(self, sessioncookiename) :
		r"""Name of the session cookie that the application firewall uses to track user sessions. 
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1
		"""
		try :
			self._sessioncookiename = sessioncookiename
		except Exception as e:
			raise e

	@property
	def clientiploggingheader(self) :
		r"""Name of an HTTP header that contains the IP address that the client used to connect to the protected web site or service.
		"""
		try :
			return self._clientiploggingheader
		except Exception as e:
			raise e

	@clientiploggingheader.setter
	def clientiploggingheader(self, clientiploggingheader) :
		r"""Name of an HTTP header that contains the IP address that the client used to connect to the protected web site or service.
		"""
		try :
			self._clientiploggingheader = clientiploggingheader
		except Exception as e:
			raise e

	@property
	def importsizelimit(self) :
		r"""Cumulative total maximum number of bytes in web forms imported to a protected web site. If a user attempts to upload files with a total byte count higher than the specified limit, the application firewall blocks the request.<br/>Default value: 134217728<br/>Minimum length =  1<br/>Maximum length =  268435456.
		"""
		try :
			return self._importsizelimit
		except Exception as e:
			raise e

	@importsizelimit.setter
	def importsizelimit(self, importsizelimit) :
		r"""Cumulative total maximum number of bytes in web forms imported to a protected web site. If a user attempts to upload files with a total byte count higher than the specified limit, the application firewall blocks the request.<br/>Default value: 134217728<br/>Minimum length =  1<br/>Maximum length =  268435456
		"""
		try :
			self._importsizelimit = importsizelimit
		except Exception as e:
			raise e

	@property
	def signatureautoupdate(self) :
		r"""Flag used to enable/disable auto update signatures.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._signatureautoupdate
		except Exception as e:
			raise e

	@signatureautoupdate.setter
	def signatureautoupdate(self, signatureautoupdate) :
		r"""Flag used to enable/disable auto update signatures.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._signatureautoupdate = signatureautoupdate
		except Exception as e:
			raise e

	@property
	def signatureurl(self) :
		r"""URL to download the mapping file from server.<br/>Default value: https://s3.amazonaws.com/NSAppFwSignatures/SignaturesMapping.xml.
		"""
		try :
			return self._signatureurl
		except Exception as e:
			raise e

	@signatureurl.setter
	def signatureurl(self, signatureurl) :
		r"""URL to download the mapping file from server.<br/>Default value: https://s3.amazonaws.com/NSAppFwSignatures/SignaturesMapping.xml
		"""
		try :
			self._signatureurl = signatureurl
		except Exception as e:
			raise e

	@property
	def cookiepostencryptprefix(self) :
		r"""String that is prepended to all encrypted cookie values.<br/>Minimum length =  1.
		"""
		try :
			return self._cookiepostencryptprefix
		except Exception as e:
			raise e

	@cookiepostencryptprefix.setter
	def cookiepostencryptprefix(self, cookiepostencryptprefix) :
		r"""String that is prepended to all encrypted cookie values.<br/>Minimum length =  1
		"""
		try :
			self._cookiepostencryptprefix = cookiepostencryptprefix
		except Exception as e:
			raise e

	@property
	def logmalformedreq(self) :
		r"""Log requests that are so malformed that application firewall parsing doesn't occur.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._logmalformedreq
		except Exception as e:
			raise e

	@logmalformedreq.setter
	def logmalformedreq(self, logmalformedreq) :
		r"""Log requests that are so malformed that application firewall parsing doesn't occur.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._logmalformedreq = logmalformedreq
		except Exception as e:
			raise e

	@property
	def geolocationlogging(self) :
		r"""Enable Geo-Location Logging in CEF format logs.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._geolocationlogging
		except Exception as e:
			raise e

	@geolocationlogging.setter
	def geolocationlogging(self, geolocationlogging) :
		r"""Enable Geo-Location Logging in CEF format logs.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._geolocationlogging = geolocationlogging
		except Exception as e:
			raise e

	@property
	def ceflogging(self) :
		r"""Enable CEF format logs.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._ceflogging
		except Exception as e:
			raise e

	@ceflogging.setter
	def ceflogging(self, ceflogging) :
		r"""Enable CEF format logs.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._ceflogging = ceflogging
		except Exception as e:
			raise e

	@property
	def entitydecoding(self) :
		r"""Transform multibyte (double- or half-width) characters to single width characters.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._entitydecoding
		except Exception as e:
			raise e

	@entitydecoding.setter
	def entitydecoding(self, entitydecoding) :
		r"""Transform multibyte (double- or half-width) characters to single width characters.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._entitydecoding = entitydecoding
		except Exception as e:
			raise e

	@property
	def useconfigurablesecretkey(self) :
		r"""Use configurable secret key in AppFw operations.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._useconfigurablesecretkey
		except Exception as e:
			raise e

	@useconfigurablesecretkey.setter
	def useconfigurablesecretkey(self, useconfigurablesecretkey) :
		r"""Use configurable secret key in AppFw operations.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._useconfigurablesecretkey = useconfigurablesecretkey
		except Exception as e:
			raise e

	@property
	def sessionlimit(self) :
		r"""Maximum number of sessions that the application firewall allows to be active, regardless of user activity. After the max_limit reaches, No more user session will be created .<br/>Default value: 100000<br/>Minimum length =  0<br/>Maximum length =  500000.
		"""
		try :
			return self._sessionlimit
		except Exception as e:
			raise e

	@sessionlimit.setter
	def sessionlimit(self, sessionlimit) :
		r"""Maximum number of sessions that the application firewall allows to be active, regardless of user activity. After the max_limit reaches, No more user session will be created .<br/>Default value: 100000<br/>Minimum length =  0<br/>Maximum length =  500000
		"""
		try :
			self._sessionlimit = sessionlimit
		except Exception as e:
			raise e

	@property
	def malformedreqaction(self) :
		r""" flag to define action on malformed requests that application firewall cannot parse.<br/>Possible values = none, block, log, stats.
		"""
		try :
			return self._malformedreqaction
		except Exception as e:
			raise e

	@malformedreqaction.setter
	def malformedreqaction(self, malformedreqaction) :
		r""" flag to define action on malformed requests that application firewall cannot parse.<br/>Possible values = none, block, log, stats
		"""
		try :
			self._malformedreqaction = malformedreqaction
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwsettings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwsettings
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
		r""" Use this API to update appfwsettings.
		"""
		try :
			if type(resource) is not list :
				updateresource = appfwsettings()
				updateresource.defaultprofile = resource.defaultprofile
				updateresource.undefaction = resource.undefaction
				updateresource.sessiontimeout = resource.sessiontimeout
				updateresource.learnratelimit = resource.learnratelimit
				updateresource.sessionlifetime = resource.sessionlifetime
				updateresource.sessioncookiename = resource.sessioncookiename
				updateresource.clientiploggingheader = resource.clientiploggingheader
				updateresource.importsizelimit = resource.importsizelimit
				updateresource.signatureautoupdate = resource.signatureautoupdate
				updateresource.signatureurl = resource.signatureurl
				updateresource.cookiepostencryptprefix = resource.cookiepostencryptprefix
				updateresource.logmalformedreq = resource.logmalformedreq
				updateresource.geolocationlogging = resource.geolocationlogging
				updateresource.ceflogging = resource.ceflogging
				updateresource.entitydecoding = resource.entitydecoding
				updateresource.useconfigurablesecretkey = resource.useconfigurablesecretkey
				updateresource.sessionlimit = resource.sessionlimit
				updateresource.malformedreqaction = resource.malformedreqaction
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of appfwsettings resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = appfwsettings()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the appfwsettings resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appfwsettings()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Malformedreqaction:
		none = "none"
		block = "block"
		log = "log"
		stats = "stats"

	class Ceflogging:
		ON = "ON"
		OFF = "OFF"

	class Logmalformedreq:
		ON = "ON"
		OFF = "OFF"

	class Signatureautoupdate:
		ON = "ON"
		OFF = "OFF"

	class Useconfigurablesecretkey:
		ON = "ON"
		OFF = "OFF"

	class Geolocationlogging:
		ON = "ON"
		OFF = "OFF"

	class Entitydecoding:
		ON = "ON"
		OFF = "OFF"

class appfwsettings_response(base_response) :
	def __init__(self, length=1) :
		self.appfwsettings = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwsettings = [appfwsettings() for _ in range(length)]

