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

class appfwprofile(base_resource) :
	""" Configuration for application firewall profile resource. """
	def __init__(self) :
		self._name = None
		self._defaults = None
		self._feature = None
		self._starturlaction = None
		self._contenttypeaction = None
		self._inspectcontenttypes = None
		self._starturlclosure = None
		self._denyurlaction = None
		self._refererheadercheck = None
		self._cookieconsistencyaction = None
		self._cookietransforms = None
		self._cookieencryption = None
		self._cookieproxying = None
		self._addcookieflags = None
		self._fieldconsistencyaction = None
		self._csrftagaction = None
		self._crosssitescriptingaction = None
		self._crosssitescriptingtransformunsafehtml = None
		self._crosssitescriptingcheckcompleteurls = None
		self._sqlinjectionaction = None
		self._sqlinjectiontransformspecialchars = None
		self._sqlinjectiononlycheckfieldswithsqlchars = None
		self._sqlinjectiontype = None
		self._sqlinjectionchecksqlwildchars = None
		self._fieldformataction = None
		self._defaultfieldformattype = None
		self._defaultfieldformatminlength = None
		self._defaultfieldformatmaxlength = None
		self._bufferoverflowaction = None
		self._bufferoverflowmaxurllength = None
		self._bufferoverflowmaxheaderlength = None
		self._bufferoverflowmaxcookielength = None
		self._creditcardaction = None
		self._creditcard = None
		self._creditcardmaxallowed = None
		self._creditcardxout = None
		self._dosecurecreditcardlogging = None
		self._streaming = None
		self._trace = None
		self._requestcontenttype = None
		self._responsecontenttype = None
		self._xmldosaction = None
		self._xmlformataction = None
		self._xmlsqlinjectionaction = None
		self._xmlsqlinjectiononlycheckfieldswithsqlchars = None
		self._xmlsqlinjectiontype = None
		self._xmlsqlinjectionchecksqlwildchars = None
		self._xmlsqlinjectionparsecomments = None
		self._xmlxssaction = None
		self._xmlwsiaction = None
		self._xmlattachmentaction = None
		self._xmlvalidationaction = None
		self._xmlerrorobject = None
		self._customsettings = None
		self._signatures = None
		self._xmlsoapfaultaction = None
		self._usehtmlerrorobject = None
		self._errorurl = None
		self._htmlerrorobject = None
		self._logeverypolicyhit = None
		self._stripcomments = None
		self._striphtmlcomments = None
		self._stripxmlcomments = None
		self._exemptclosureurlsfromsecuritychecks = None
		self._defaultcharset = None
		self._postbodylimit = None
		self._fileuploadmaxnum = None
		self._canonicalizehtmlresponse = None
		self._enableformtagging = None
		self._sessionlessfieldconsistency = None
		self._sessionlessurlclosure = None
		self._semicolonfieldseparator = None
		self._excludefileuploadfromchecks = None
		self._sqlinjectionparsecomments = None
		self._invalidpercenthandling = None
		self._type = None
		self._checkrequestheaders = None
		self._optimizepartialreqs = None
		self._urldecoderequestcookies = None
		self._comment = None
		self._percentdecoderecursively = None
		self._multipleheaderaction = None
		self._rfcprofile = None
		self._archivename = None
		self._state = None
		self._csrftag = None
		self._builtin_depr = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the profile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore (_) characters. Cannot be changed after the profile is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my profile" or 'my profile').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the profile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore (_) characters. Cannot be changed after the profile is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my profile" or 'my profile').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def defaults(self) :
		r"""Default configuration to apply to the profile. Basic defaults are intended for standard content that requires little further configuration, such as static web site content. Advanced defaults are intended for specialized content that requires significant specialized configuration, such as heavily scripted or dynamic content.
		CLI users: When adding an application firewall profile, you can set either the defaults or the type, but not both. To set both options, create the profile by using the add appfw profile command, and then use the set appfw profile command to configure the other option.<br/>Possible values = basic, advanced.
		"""
		try :
			return self._defaults
		except Exception as e:
			raise e

	@defaults.setter
	def defaults(self, defaults) :
		r"""Default configuration to apply to the profile. Basic defaults are intended for standard content that requires little further configuration, such as static web site content. Advanced defaults are intended for specialized content that requires significant specialized configuration, such as heavily scripted or dynamic content.
		CLI users: When adding an application firewall profile, you can set either the defaults or the type, but not both. To set both options, create the profile by using the add appfw profile command, and then use the set appfw profile command to configure the other option.<br/>Possible values = basic, advanced
		"""
		try :
			self._defaults = defaults
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
	def starturlaction(self) :
		r"""One or more Start URL actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -startURLaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -startURLaction none".<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._starturlaction
		except Exception as e:
			raise e

	@starturlaction.setter
	def starturlaction(self, starturlaction) :
		r"""One or more Start URL actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -startURLaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -startURLaction none".<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._starturlaction = starturlaction
		except Exception as e:
			raise e

	@property
	def contenttypeaction(self) :
		r"""One or more Content-type actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -contentTypeaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -contentTypeaction none".<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._contenttypeaction
		except Exception as e:
			raise e

	@contenttypeaction.setter
	def contenttypeaction(self, contenttypeaction) :
		r"""One or more Content-type actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -contentTypeaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -contentTypeaction none".<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._contenttypeaction = contenttypeaction
		except Exception as e:
			raise e

	@property
	def inspectcontenttypes(self) :
		r"""One or more InspectContentType lists. 
		* application/x-www-form-urlencoded
		* multipart/form-data
		* text/x-gwt-rpc
		CLI users: To enable, type "set appfw profile -InspectContentTypes" followed by the content types to be inspected.<br/>Possible values = none, application/x-www-form-urlencoded, multipart/form-data, text/x-gwt-rpc.
		"""
		try :
			return self._inspectcontenttypes
		except Exception as e:
			raise e

	@inspectcontenttypes.setter
	def inspectcontenttypes(self, inspectcontenttypes) :
		r"""One or more InspectContentType lists. 
		* application/x-www-form-urlencoded
		* multipart/form-data
		* text/x-gwt-rpc
		CLI users: To enable, type "set appfw profile -InspectContentTypes" followed by the content types to be inspected.<br/>Possible values = none, application/x-www-form-urlencoded, multipart/form-data, text/x-gwt-rpc
		"""
		try :
			self._inspectcontenttypes = inspectcontenttypes
		except Exception as e:
			raise e

	@property
	def starturlclosure(self) :
		r"""Toggle  the state of Start URL Closure.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._starturlclosure
		except Exception as e:
			raise e

	@starturlclosure.setter
	def starturlclosure(self, starturlclosure) :
		r"""Toggle  the state of Start URL Closure.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._starturlclosure = starturlclosure
		except Exception as e:
			raise e

	@property
	def denyurlaction(self) :
		r"""One or more Deny URL actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		NOTE: The Deny URL check takes precedence over the Start URL check. If you enable blocking for the Deny URL check, the application firewall blocks any URL that is explicitly blocked by a Deny URL, even if the same URL would otherwise be allowed by the Start URL check.
		CLI users: To enable one or more actions, type "set appfw profile -denyURLaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -denyURLaction none".<br/>Possible values = none, block, log, stats.
		"""
		try :
			return self._denyurlaction
		except Exception as e:
			raise e

	@denyurlaction.setter
	def denyurlaction(self, denyurlaction) :
		r"""One or more Deny URL actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		NOTE: The Deny URL check takes precedence over the Start URL check. If you enable blocking for the Deny URL check, the application firewall blocks any URL that is explicitly blocked by a Deny URL, even if the same URL would otherwise be allowed by the Start URL check.
		CLI users: To enable one or more actions, type "set appfw profile -denyURLaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -denyURLaction none".<br/>Possible values = none, block, log, stats
		"""
		try :
			self._denyurlaction = denyurlaction
		except Exception as e:
			raise e

	@property
	def refererheadercheck(self) :
		r"""Enable validation of Referer headers. 
		Referer validation ensures that a web form that a user sends to your web site originally came from your web site, not an outside attacker. 
		Although this parameter is part of the Start URL check, referer validation protects against cross-site request forgery (CSRF) attacks, not Start URL attacks.<br/>Default value: OFF<br/>Possible values = OFF, if_present, AlwaysExceptStartURLs, AlwaysExceptFirstRequest.
		"""
		try :
			return self._refererheadercheck
		except Exception as e:
			raise e

	@refererheadercheck.setter
	def refererheadercheck(self, refererheadercheck) :
		r"""Enable validation of Referer headers. 
		Referer validation ensures that a web form that a user sends to your web site originally came from your web site, not an outside attacker. 
		Although this parameter is part of the Start URL check, referer validation protects against cross-site request forgery (CSRF) attacks, not Start URL attacks.<br/>Default value: OFF<br/>Possible values = OFF, if_present, AlwaysExceptStartURLs, AlwaysExceptFirstRequest
		"""
		try :
			self._refererheadercheck = refererheadercheck
		except Exception as e:
			raise e

	@property
	def cookieconsistencyaction(self) :
		r"""One or more Cookie Consistency actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -cookieConsistencyAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -cookieConsistencyAction none".<br/>Default value: none<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._cookieconsistencyaction
		except Exception as e:
			raise e

	@cookieconsistencyaction.setter
	def cookieconsistencyaction(self, cookieconsistencyaction) :
		r"""One or more Cookie Consistency actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -cookieConsistencyAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -cookieConsistencyAction none".<br/>Default value: none<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._cookieconsistencyaction = cookieconsistencyaction
		except Exception as e:
			raise e

	@property
	def cookietransforms(self) :
		r"""Perform the specified type of cookie transformation. 
		Available settings function as follows: 
		* Encryption - Encrypt cookies.
		* Proxying - Mask contents of server cookies by sending proxy cookie to users.
		* Cookie flags - Flag cookies as HTTP only to prevent scripts on user's browser from accessing and possibly modifying them.
		CAUTION: Make sure that this parameter is set to ON if you are configuring any cookie transformations. If it is set to OFF, no cookie transformations are performed regardless of any other settings.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._cookietransforms
		except Exception as e:
			raise e

	@cookietransforms.setter
	def cookietransforms(self, cookietransforms) :
		r"""Perform the specified type of cookie transformation. 
		Available settings function as follows: 
		* Encryption - Encrypt cookies.
		* Proxying - Mask contents of server cookies by sending proxy cookie to users.
		* Cookie flags - Flag cookies as HTTP only to prevent scripts on user's browser from accessing and possibly modifying them.
		CAUTION: Make sure that this parameter is set to ON if you are configuring any cookie transformations. If it is set to OFF, no cookie transformations are performed regardless of any other settings.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._cookietransforms = cookietransforms
		except Exception as e:
			raise e

	@property
	def cookieencryption(self) :
		r"""Type of cookie encryption. Available settings function as follows:
		* None - Do not encrypt cookies.
		* Decrypt Only - Decrypt encrypted cookies, but do not encrypt cookies.
		* Encrypt Session Only - Encrypt session cookies, but not permanent cookies.
		* Encrypt All - Encrypt all cookies.<br/>Default value: none<br/>Possible values = none, decryptOnly, encryptSessionOnly, encryptAll.
		"""
		try :
			return self._cookieencryption
		except Exception as e:
			raise e

	@cookieencryption.setter
	def cookieencryption(self, cookieencryption) :
		r"""Type of cookie encryption. Available settings function as follows:
		* None - Do not encrypt cookies.
		* Decrypt Only - Decrypt encrypted cookies, but do not encrypt cookies.
		* Encrypt Session Only - Encrypt session cookies, but not permanent cookies.
		* Encrypt All - Encrypt all cookies.<br/>Default value: none<br/>Possible values = none, decryptOnly, encryptSessionOnly, encryptAll
		"""
		try :
			self._cookieencryption = cookieencryption
		except Exception as e:
			raise e

	@property
	def cookieproxying(self) :
		r"""Cookie proxy setting. Available settings function as follows:
		* None - Do not proxy cookies.
		* Session Only - Proxy session cookies by using the Citrix ADC session ID, but do not proxy permanent cookies.<br/>Default value: none<br/>Possible values = none, sessionOnly.
		"""
		try :
			return self._cookieproxying
		except Exception as e:
			raise e

	@cookieproxying.setter
	def cookieproxying(self, cookieproxying) :
		r"""Cookie proxy setting. Available settings function as follows:
		* None - Do not proxy cookies.
		* Session Only - Proxy session cookies by using the Citrix ADC session ID, but do not proxy permanent cookies.<br/>Default value: none<br/>Possible values = none, sessionOnly
		"""
		try :
			self._cookieproxying = cookieproxying
		except Exception as e:
			raise e

	@property
	def addcookieflags(self) :
		r"""Add the specified flags to cookies. Available settings function as follows:
		* None - Do not add flags to cookies.
		* HTTP Only - Add the HTTP Only flag to cookies, which prevents scripts from accessing cookies.
		* Secure - Add Secure flag to cookies.
		* All - Add both HTTPOnly and Secure flags to cookies.<br/>Default value: none<br/>Possible values = none, httpOnly, secure, all.
		"""
		try :
			return self._addcookieflags
		except Exception as e:
			raise e

	@addcookieflags.setter
	def addcookieflags(self, addcookieflags) :
		r"""Add the specified flags to cookies. Available settings function as follows:
		* None - Do not add flags to cookies.
		* HTTP Only - Add the HTTP Only flag to cookies, which prevents scripts from accessing cookies.
		* Secure - Add Secure flag to cookies.
		* All - Add both HTTPOnly and Secure flags to cookies.<br/>Default value: none<br/>Possible values = none, httpOnly, secure, all
		"""
		try :
			self._addcookieflags = addcookieflags
		except Exception as e:
			raise e

	@property
	def fieldconsistencyaction(self) :
		r"""One or more Form Field Consistency actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -fieldConsistencyaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -fieldConsistencyAction none".<br/>Default value: none<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._fieldconsistencyaction
		except Exception as e:
			raise e

	@fieldconsistencyaction.setter
	def fieldconsistencyaction(self, fieldconsistencyaction) :
		r"""One or more Form Field Consistency actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -fieldConsistencyaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -fieldConsistencyAction none".<br/>Default value: none<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._fieldconsistencyaction = fieldconsistencyaction
		except Exception as e:
			raise e

	@property
	def csrftagaction(self) :
		r"""One or more Cross-Site Request Forgery (CSRF) Tagging actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -CSRFTagAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -CSRFTagAction none".<br/>Default value: none<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._csrftagaction
		except Exception as e:
			raise e

	@csrftagaction.setter
	def csrftagaction(self, csrftagaction) :
		r"""One or more Cross-Site Request Forgery (CSRF) Tagging actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -CSRFTagAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -CSRFTagAction none".<br/>Default value: none<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._csrftagaction = csrftagaction
		except Exception as e:
			raise e

	@property
	def crosssitescriptingaction(self) :
		r"""One or more Cross-Site Scripting (XSS) actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -crossSiteScriptingAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -crossSiteScriptingAction none".<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._crosssitescriptingaction
		except Exception as e:
			raise e

	@crosssitescriptingaction.setter
	def crosssitescriptingaction(self, crosssitescriptingaction) :
		r"""One or more Cross-Site Scripting (XSS) actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -crossSiteScriptingAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -crossSiteScriptingAction none".<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._crosssitescriptingaction = crosssitescriptingaction
		except Exception as e:
			raise e

	@property
	def crosssitescriptingtransformunsafehtml(self) :
		r"""Transform cross-site scripts. This setting configures the application firewall to disable dangerous HTML instead of blocking the request. 
		CAUTION: Make sure that this parameter is set to ON if you are configuring any cross-site scripting transformations. If it is set to OFF, no cross-site scripting transformations are performed regardless of any other settings.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._crosssitescriptingtransformunsafehtml
		except Exception as e:
			raise e

	@crosssitescriptingtransformunsafehtml.setter
	def crosssitescriptingtransformunsafehtml(self, crosssitescriptingtransformunsafehtml) :
		r"""Transform cross-site scripts. This setting configures the application firewall to disable dangerous HTML instead of blocking the request. 
		CAUTION: Make sure that this parameter is set to ON if you are configuring any cross-site scripting transformations. If it is set to OFF, no cross-site scripting transformations are performed regardless of any other settings.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._crosssitescriptingtransformunsafehtml = crosssitescriptingtransformunsafehtml
		except Exception as e:
			raise e

	@property
	def crosssitescriptingcheckcompleteurls(self) :
		r"""Check complete URLs for cross-site scripts, instead of just the query portions of URLs.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._crosssitescriptingcheckcompleteurls
		except Exception as e:
			raise e

	@crosssitescriptingcheckcompleteurls.setter
	def crosssitescriptingcheckcompleteurls(self, crosssitescriptingcheckcompleteurls) :
		r"""Check complete URLs for cross-site scripts, instead of just the query portions of URLs.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._crosssitescriptingcheckcompleteurls = crosssitescriptingcheckcompleteurls
		except Exception as e:
			raise e

	@property
	def sqlinjectionaction(self) :
		r"""One or more HTML SQL Injection actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -SQLInjectionAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -SQLInjectionAction none".<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._sqlinjectionaction
		except Exception as e:
			raise e

	@sqlinjectionaction.setter
	def sqlinjectionaction(self, sqlinjectionaction) :
		r"""One or more HTML SQL Injection actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -SQLInjectionAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -SQLInjectionAction none".<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._sqlinjectionaction = sqlinjectionaction
		except Exception as e:
			raise e

	@property
	def sqlinjectiontransformspecialchars(self) :
		r"""Transform injected SQL code. This setting configures the application firewall to disable SQL special strings instead of blocking the request. Since most SQL servers require a special string to activate an SQL keyword, in most cases a request that contains injected SQL code is safe if special strings are disabled.
		CAUTION: Make sure that this parameter is set to ON if you are configuring any SQL injection transformations. If it is set to OFF, no SQL injection transformations are performed regardless of any other settings.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sqlinjectiontransformspecialchars
		except Exception as e:
			raise e

	@sqlinjectiontransformspecialchars.setter
	def sqlinjectiontransformspecialchars(self, sqlinjectiontransformspecialchars) :
		r"""Transform injected SQL code. This setting configures the application firewall to disable SQL special strings instead of blocking the request. Since most SQL servers require a special string to activate an SQL keyword, in most cases a request that contains injected SQL code is safe if special strings are disabled.
		CAUTION: Make sure that this parameter is set to ON if you are configuring any SQL injection transformations. If it is set to OFF, no SQL injection transformations are performed regardless of any other settings.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sqlinjectiontransformspecialchars = sqlinjectiontransformspecialchars
		except Exception as e:
			raise e

	@property
	def sqlinjectiononlycheckfieldswithsqlchars(self) :
		r"""Check only form fields that contain SQL special strings (characters) for injected SQL code.
		Most SQL servers require a special string to activate an SQL request, so SQL code without a special string is harmless to most SQL servers.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sqlinjectiononlycheckfieldswithsqlchars
		except Exception as e:
			raise e

	@sqlinjectiononlycheckfieldswithsqlchars.setter
	def sqlinjectiononlycheckfieldswithsqlchars(self, sqlinjectiononlycheckfieldswithsqlchars) :
		r"""Check only form fields that contain SQL special strings (characters) for injected SQL code.
		Most SQL servers require a special string to activate an SQL request, so SQL code without a special string is harmless to most SQL servers.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._sqlinjectiononlycheckfieldswithsqlchars = sqlinjectiononlycheckfieldswithsqlchars
		except Exception as e:
			raise e

	@property
	def sqlinjectiontype(self) :
		r"""Available SQL injection types. 
		-SQLSplChar              : Checks for SQL Special Chars
		-SQLKeyword		 : Checks for SQL Keywords
		-SQLSplCharANDKeyword    : Checks for both and blocks if both are found
		-SQLSplCharORKeyword     : Checks for both and blocks if anyone is found.<br/>Default value: SQLSplCharANDKeyword<br/>Possible values = SQLSplChar, SQLKeyword, SQLSplCharORKeyword, SQLSplCharANDKeyword.
		"""
		try :
			return self._sqlinjectiontype
		except Exception as e:
			raise e

	@sqlinjectiontype.setter
	def sqlinjectiontype(self, sqlinjectiontype) :
		r"""Available SQL injection types. 
		-SQLSplChar              : Checks for SQL Special Chars
		-SQLKeyword		 : Checks for SQL Keywords
		-SQLSplCharANDKeyword    : Checks for both and blocks if both are found
		-SQLSplCharORKeyword     : Checks for both and blocks if anyone is found.<br/>Default value: SQLSplCharANDKeyword<br/>Possible values = SQLSplChar, SQLKeyword, SQLSplCharORKeyword, SQLSplCharANDKeyword
		"""
		try :
			self._sqlinjectiontype = sqlinjectiontype
		except Exception as e:
			raise e

	@property
	def sqlinjectionchecksqlwildchars(self) :
		r"""Check for form fields that contain SQL wild chars .<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sqlinjectionchecksqlwildchars
		except Exception as e:
			raise e

	@sqlinjectionchecksqlwildchars.setter
	def sqlinjectionchecksqlwildchars(self, sqlinjectionchecksqlwildchars) :
		r"""Check for form fields that contain SQL wild chars .<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sqlinjectionchecksqlwildchars = sqlinjectionchecksqlwildchars
		except Exception as e:
			raise e

	@property
	def fieldformataction(self) :
		r"""One or more Field Format actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of suggested web form fields and field format assignments.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -fieldFormatAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -fieldFormatAction none".<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._fieldformataction
		except Exception as e:
			raise e

	@fieldformataction.setter
	def fieldformataction(self, fieldformataction) :
		r"""One or more Field Format actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of suggested web form fields and field format assignments.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -fieldFormatAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -fieldFormatAction none".<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._fieldformataction = fieldformataction
		except Exception as e:
			raise e

	@property
	def defaultfieldformattype(self) :
		r"""Designate a default field type to be applied to web form fields that do not have a field type explicitly assigned to them.<br/>Minimum length =  1.
		"""
		try :
			return self._defaultfieldformattype
		except Exception as e:
			raise e

	@defaultfieldformattype.setter
	def defaultfieldformattype(self, defaultfieldformattype) :
		r"""Designate a default field type to be applied to web form fields that do not have a field type explicitly assigned to them.<br/>Minimum length =  1
		"""
		try :
			self._defaultfieldformattype = defaultfieldformattype
		except Exception as e:
			raise e

	@property
	def defaultfieldformatminlength(self) :
		r"""Minimum length, in characters, for data entered into a field that is assigned the default field type. 
		To disable the minimum and maximum length settings and allow data of any length to be entered into the field, set this parameter to zero (0).<br/>Default value: 0<br/>Minimum length =  0<br/>Maximum length =  2147483647.
		"""
		try :
			return self._defaultfieldformatminlength
		except Exception as e:
			raise e

	@defaultfieldformatminlength.setter
	def defaultfieldformatminlength(self, defaultfieldformatminlength) :
		r"""Minimum length, in characters, for data entered into a field that is assigned the default field type. 
		To disable the minimum and maximum length settings and allow data of any length to be entered into the field, set this parameter to zero (0).<br/>Default value: 0<br/>Minimum length =  0<br/>Maximum length =  2147483647
		"""
		try :
			self._defaultfieldformatminlength = defaultfieldformatminlength
		except Exception as e:
			raise e

	@property
	def defaultfieldformatmaxlength(self) :
		r"""Maximum length, in characters, for data entered into a field that is assigned the default field type.<br/>Default value: 65535<br/>Minimum length =  1<br/>Maximum length =  2147483647.
		"""
		try :
			return self._defaultfieldformatmaxlength
		except Exception as e:
			raise e

	@defaultfieldformatmaxlength.setter
	def defaultfieldformatmaxlength(self, defaultfieldformatmaxlength) :
		r"""Maximum length, in characters, for data entered into a field that is assigned the default field type.<br/>Default value: 65535<br/>Minimum length =  1<br/>Maximum length =  2147483647
		"""
		try :
			self._defaultfieldformatmaxlength = defaultfieldformatmaxlength
		except Exception as e:
			raise e

	@property
	def bufferoverflowaction(self) :
		r"""One or more Buffer Overflow actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -bufferOverflowAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -bufferOverflowAction none".<br/>Possible values = none, block, log, stats.
		"""
		try :
			return self._bufferoverflowaction
		except Exception as e:
			raise e

	@bufferoverflowaction.setter
	def bufferoverflowaction(self, bufferoverflowaction) :
		r"""One or more Buffer Overflow actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -bufferOverflowAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -bufferOverflowAction none".<br/>Possible values = none, block, log, stats
		"""
		try :
			self._bufferoverflowaction = bufferoverflowaction
		except Exception as e:
			raise e

	@property
	def bufferoverflowmaxurllength(self) :
		r"""Maximum length, in characters, for URLs on your protected web sites. Requests with longer URLs are blocked.<br/>Default value: 1024<br/>Minimum length =  0<br/>Maximum length =  65535.
		"""
		try :
			return self._bufferoverflowmaxurllength
		except Exception as e:
			raise e

	@bufferoverflowmaxurllength.setter
	def bufferoverflowmaxurllength(self, bufferoverflowmaxurllength) :
		r"""Maximum length, in characters, for URLs on your protected web sites. Requests with longer URLs are blocked.<br/>Default value: 1024<br/>Minimum length =  0<br/>Maximum length =  65535
		"""
		try :
			self._bufferoverflowmaxurllength = bufferoverflowmaxurllength
		except Exception as e:
			raise e

	@property
	def bufferoverflowmaxheaderlength(self) :
		r"""Maximum length, in characters, for HTTP headers in requests sent to your protected web sites. Requests with longer headers are blocked.<br/>Default value: 4096<br/>Minimum length =  0<br/>Maximum length =  65535.
		"""
		try :
			return self._bufferoverflowmaxheaderlength
		except Exception as e:
			raise e

	@bufferoverflowmaxheaderlength.setter
	def bufferoverflowmaxheaderlength(self, bufferoverflowmaxheaderlength) :
		r"""Maximum length, in characters, for HTTP headers in requests sent to your protected web sites. Requests with longer headers are blocked.<br/>Default value: 4096<br/>Minimum length =  0<br/>Maximum length =  65535
		"""
		try :
			self._bufferoverflowmaxheaderlength = bufferoverflowmaxheaderlength
		except Exception as e:
			raise e

	@property
	def bufferoverflowmaxcookielength(self) :
		r"""Maximum length, in characters, for cookies sent to your protected web sites. Requests with longer cookies are blocked.<br/>Default value: 4096<br/>Minimum length =  0<br/>Maximum length =  65535.
		"""
		try :
			return self._bufferoverflowmaxcookielength
		except Exception as e:
			raise e

	@bufferoverflowmaxcookielength.setter
	def bufferoverflowmaxcookielength(self, bufferoverflowmaxcookielength) :
		r"""Maximum length, in characters, for cookies sent to your protected web sites. Requests with longer cookies are blocked.<br/>Default value: 4096<br/>Minimum length =  0<br/>Maximum length =  65535
		"""
		try :
			self._bufferoverflowmaxcookielength = bufferoverflowmaxcookielength
		except Exception as e:
			raise e

	@property
	def creditcardaction(self) :
		r"""One or more Credit Card actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -creditCardAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -creditCardAction none".<br/>Default value: none<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._creditcardaction
		except Exception as e:
			raise e

	@creditcardaction.setter
	def creditcardaction(self, creditcardaction) :
		r"""One or more Credit Card actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -creditCardAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -creditCardAction none".<br/>Default value: none<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._creditcardaction = creditcardaction
		except Exception as e:
			raise e

	@property
	def creditcard(self) :
		r"""Credit card types that the application firewall should protect.<br/>Default value: none<br/>Possible values = none, visa, mastercard, discover, amex, jcb, dinersclub.
		"""
		try :
			return self._creditcard
		except Exception as e:
			raise e

	@creditcard.setter
	def creditcard(self, creditcard) :
		r"""Credit card types that the application firewall should protect.<br/>Default value: none<br/>Possible values = none, visa, mastercard, discover, amex, jcb, dinersclub
		"""
		try :
			self._creditcard = creditcard
		except Exception as e:
			raise e

	@property
	def creditcardmaxallowed(self) :
		r"""This parameter value is used by the block action. It represents the maximum number of credit card numbers that can appear on a web page served by your protected web sites. Pages that contain more credit card numbers are blocked.<br/>Maximum length =  255.
		"""
		try :
			return self._creditcardmaxallowed
		except Exception as e:
			raise e

	@creditcardmaxallowed.setter
	def creditcardmaxallowed(self, creditcardmaxallowed) :
		r"""This parameter value is used by the block action. It represents the maximum number of credit card numbers that can appear on a web page served by your protected web sites. Pages that contain more credit card numbers are blocked.<br/>Maximum length =  255
		"""
		try :
			self._creditcardmaxallowed = creditcardmaxallowed
		except Exception as e:
			raise e

	@property
	def creditcardxout(self) :
		r"""Mask any credit card number detected in a response by replacing each digit, except the digits in the final group, with the letter "X.".<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._creditcardxout
		except Exception as e:
			raise e

	@creditcardxout.setter
	def creditcardxout(self, creditcardxout) :
		r"""Mask any credit card number detected in a response by replacing each digit, except the digits in the final group, with the letter "X.".<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._creditcardxout = creditcardxout
		except Exception as e:
			raise e

	@property
	def dosecurecreditcardlogging(self) :
		r"""Setting this option logs credit card numbers in the response when the match is found.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._dosecurecreditcardlogging
		except Exception as e:
			raise e

	@dosecurecreditcardlogging.setter
	def dosecurecreditcardlogging(self, dosecurecreditcardlogging) :
		r"""Setting this option logs credit card numbers in the response when the match is found.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._dosecurecreditcardlogging = dosecurecreditcardlogging
		except Exception as e:
			raise e

	@property
	def streaming(self) :
		r"""Setting this option converts content-length form submission requests (requests with content-type "application/x-www-form-urlencoded" or "multipart/form-data") to chunked requests when atleast one of the following protections : SQL injection protection, XSS protection, form field consistency protection, starturl closure, CSRF tagging is enabled. Please make sure that the backend server accepts chunked requests before enabling this option.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._streaming
		except Exception as e:
			raise e

	@streaming.setter
	def streaming(self, streaming) :
		r"""Setting this option converts content-length form submission requests (requests with content-type "application/x-www-form-urlencoded" or "multipart/form-data") to chunked requests when atleast one of the following protections : SQL injection protection, XSS protection, form field consistency protection, starturl closure, CSRF tagging is enabled. Please make sure that the backend server accepts chunked requests before enabling this option.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._streaming = streaming
		except Exception as e:
			raise e

	@property
	def trace(self) :
		r"""Toggle  the state of trace.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._trace
		except Exception as e:
			raise e

	@trace.setter
	def trace(self, trace) :
		r"""Toggle  the state of trace.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._trace = trace
		except Exception as e:
			raise e

	@property
	def requestcontenttype(self) :
		r"""Default Content-Type header for requests. 
		A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (_) characters.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._requestcontenttype
		except Exception as e:
			raise e

	@requestcontenttype.setter
	def requestcontenttype(self, requestcontenttype) :
		r"""Default Content-Type header for requests. 
		A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (_) characters.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._requestcontenttype = requestcontenttype
		except Exception as e:
			raise e

	@property
	def responsecontenttype(self) :
		r"""Default Content-Type header for responses. 
		A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (_) characters.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._responsecontenttype
		except Exception as e:
			raise e

	@responsecontenttype.setter
	def responsecontenttype(self, responsecontenttype) :
		r"""Default Content-Type header for responses. 
		A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (_) characters.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._responsecontenttype = responsecontenttype
		except Exception as e:
			raise e

	@property
	def xmldosaction(self) :
		r"""One or more XML Denial-of-Service (XDoS) actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLDoSAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLDoSAction none".<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._xmldosaction
		except Exception as e:
			raise e

	@xmldosaction.setter
	def xmldosaction(self, xmldosaction) :
		r"""One or more XML Denial-of-Service (XDoS) actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLDoSAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLDoSAction none".<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._xmldosaction = xmldosaction
		except Exception as e:
			raise e

	@property
	def xmlformataction(self) :
		r"""One or more XML Format actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLFormatAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLFormatAction none".<br/>Possible values = none, block, log, stats.
		"""
		try :
			return self._xmlformataction
		except Exception as e:
			raise e

	@xmlformataction.setter
	def xmlformataction(self, xmlformataction) :
		r"""One or more XML Format actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLFormatAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLFormatAction none".<br/>Possible values = none, block, log, stats
		"""
		try :
			self._xmlformataction = xmlformataction
		except Exception as e:
			raise e

	@property
	def xmlsqlinjectionaction(self) :
		r"""One or more XML SQL Injection actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLSQLInjectionAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLSQLInjectionAction none".<br/>Possible values = none, block, log, stats.
		"""
		try :
			return self._xmlsqlinjectionaction
		except Exception as e:
			raise e

	@xmlsqlinjectionaction.setter
	def xmlsqlinjectionaction(self, xmlsqlinjectionaction) :
		r"""One or more XML SQL Injection actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLSQLInjectionAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLSQLInjectionAction none".<br/>Possible values = none, block, log, stats
		"""
		try :
			self._xmlsqlinjectionaction = xmlsqlinjectionaction
		except Exception as e:
			raise e

	@property
	def xmlsqlinjectiononlycheckfieldswithsqlchars(self) :
		r"""Check only form fields that contain SQL special characters, which most SQL servers require before accepting an SQL command, for injected SQL.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlsqlinjectiononlycheckfieldswithsqlchars
		except Exception as e:
			raise e

	@xmlsqlinjectiononlycheckfieldswithsqlchars.setter
	def xmlsqlinjectiononlycheckfieldswithsqlchars(self, xmlsqlinjectiononlycheckfieldswithsqlchars) :
		r"""Check only form fields that contain SQL special characters, which most SQL servers require before accepting an SQL command, for injected SQL.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlsqlinjectiononlycheckfieldswithsqlchars = xmlsqlinjectiononlycheckfieldswithsqlchars
		except Exception as e:
			raise e

	@property
	def xmlsqlinjectiontype(self) :
		r"""Available SQL injection types.
		-SQLSplChar              : Checks for SQL Special Chars
		-SQLKeyword              : Checks for SQL Keywords
		-SQLSplCharANDKeyword    : Checks for both and blocks if both are found
		-SQLSplCharORKeyword     : Checks for both and blocks if anyone is found.<br/>Default value: SQLSplCharANDKeyword<br/>Possible values = SQLSplChar, SQLKeyword, SQLSplCharORKeyword, SQLSplCharANDKeyword.
		"""
		try :
			return self._xmlsqlinjectiontype
		except Exception as e:
			raise e

	@xmlsqlinjectiontype.setter
	def xmlsqlinjectiontype(self, xmlsqlinjectiontype) :
		r"""Available SQL injection types.
		-SQLSplChar              : Checks for SQL Special Chars
		-SQLKeyword              : Checks for SQL Keywords
		-SQLSplCharANDKeyword    : Checks for both and blocks if both are found
		-SQLSplCharORKeyword     : Checks for both and blocks if anyone is found.<br/>Default value: SQLSplCharANDKeyword<br/>Possible values = SQLSplChar, SQLKeyword, SQLSplCharORKeyword, SQLSplCharANDKeyword
		"""
		try :
			self._xmlsqlinjectiontype = xmlsqlinjectiontype
		except Exception as e:
			raise e

	@property
	def xmlsqlinjectionchecksqlwildchars(self) :
		r"""Check for form fields that contain SQL wild chars .<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlsqlinjectionchecksqlwildchars
		except Exception as e:
			raise e

	@xmlsqlinjectionchecksqlwildchars.setter
	def xmlsqlinjectionchecksqlwildchars(self, xmlsqlinjectionchecksqlwildchars) :
		r"""Check for form fields that contain SQL wild chars .<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlsqlinjectionchecksqlwildchars = xmlsqlinjectionchecksqlwildchars
		except Exception as e:
			raise e

	@property
	def xmlsqlinjectionparsecomments(self) :
		r"""Parse comments in XML Data and exempt those sections of the request that are from the XML SQL Injection check. You must configure the type of comments that the application firewall is to detect and exempt from this security check. Available settings function as follows:
		* Check all - Check all content.
		* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. 
		* Nested - Exempt content that is part of a nested (Microsoft-style) comment.
		* ANSI Nested - Exempt content that is part of any type of comment.<br/>Default value: checkall<br/>Possible values = checkall, ansi, nested, ansinested.
		"""
		try :
			return self._xmlsqlinjectionparsecomments
		except Exception as e:
			raise e

	@xmlsqlinjectionparsecomments.setter
	def xmlsqlinjectionparsecomments(self, xmlsqlinjectionparsecomments) :
		r"""Parse comments in XML Data and exempt those sections of the request that are from the XML SQL Injection check. You must configure the type of comments that the application firewall is to detect and exempt from this security check. Available settings function as follows:
		* Check all - Check all content.
		* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. 
		* Nested - Exempt content that is part of a nested (Microsoft-style) comment.
		* ANSI Nested - Exempt content that is part of any type of comment.<br/>Default value: checkall<br/>Possible values = checkall, ansi, nested, ansinested
		"""
		try :
			self._xmlsqlinjectionparsecomments = xmlsqlinjectionparsecomments
		except Exception as e:
			raise e

	@property
	def xmlxssaction(self) :
		r"""One or more XML Cross-Site Scripting actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLXSSAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLXSSAction none".<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._xmlxssaction
		except Exception as e:
			raise e

	@xmlxssaction.setter
	def xmlxssaction(self, xmlxssaction) :
		r"""One or more XML Cross-Site Scripting actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLXSSAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLXSSAction none".<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._xmlxssaction = xmlxssaction
		except Exception as e:
			raise e

	@property
	def xmlwsiaction(self) :
		r"""One or more Web Services Interoperability (WSI) actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLWSIAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLWSIAction none".<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._xmlwsiaction
		except Exception as e:
			raise e

	@xmlwsiaction.setter
	def xmlwsiaction(self, xmlwsiaction) :
		r"""One or more Web Services Interoperability (WSI) actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLWSIAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLWSIAction none".<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._xmlwsiaction = xmlwsiaction
		except Exception as e:
			raise e

	@property
	def xmlattachmentaction(self) :
		r"""One or more XML Attachment actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLAttachmentAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLAttachmentAction none".<br/>Possible values = none, block, learn, log, stats.
		"""
		try :
			return self._xmlattachmentaction
		except Exception as e:
			raise e

	@xmlattachmentaction.setter
	def xmlattachmentaction(self, xmlattachmentaction) :
		r"""One or more XML Attachment actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Learn - Use the learning engine to generate a list of exceptions to this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLAttachmentAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLAttachmentAction none".<br/>Possible values = none, block, learn, log, stats
		"""
		try :
			self._xmlattachmentaction = xmlattachmentaction
		except Exception as e:
			raise e

	@property
	def xmlvalidationaction(self) :
		r"""One or more XML Validation actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check. 
		CLI users: To enable one or more actions, type "set appfw profile -XMLValidationAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLValidationAction none".<br/>Possible values = none, block, log, stats.
		"""
		try :
			return self._xmlvalidationaction
		except Exception as e:
			raise e

	@xmlvalidationaction.setter
	def xmlvalidationaction(self, xmlvalidationaction) :
		r"""One or more XML Validation actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check. 
		CLI users: To enable one or more actions, type "set appfw profile -XMLValidationAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLValidationAction none".<br/>Possible values = none, block, log, stats
		"""
		try :
			self._xmlvalidationaction = xmlvalidationaction
		except Exception as e:
			raise e

	@property
	def xmlerrorobject(self) :
		r"""Name to assign to the XML Error Object, which the application firewall displays when a user request is blocked.
		Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at (@), equals \(=\), colon \(:\), and underscore characters. Cannot be changed after the XML error object is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my XML error object" or 'my XML error object'\).<br/>Minimum length =  1.
		"""
		try :
			return self._xmlerrorobject
		except Exception as e:
			raise e

	@xmlerrorobject.setter
	def xmlerrorobject(self, xmlerrorobject) :
		r"""Name to assign to the XML Error Object, which the application firewall displays when a user request is blocked.
		Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at (@), equals \(=\), colon \(:\), and underscore characters. Cannot be changed after the XML error object is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my XML error object" or 'my XML error object'\).<br/>Minimum length =  1
		"""
		try :
			self._xmlerrorobject = xmlerrorobject
		except Exception as e:
			raise e

	@property
	def customsettings(self) :
		r"""Object name for custom settings.
		This check is applicable to Profile Type: HTML, XML. .<br/>Minimum length =  1.
		"""
		try :
			return self._customsettings
		except Exception as e:
			raise e

	@customsettings.setter
	def customsettings(self, customsettings) :
		r"""Object name for custom settings.
		This check is applicable to Profile Type: HTML, XML. .<br/>Minimum length =  1
		"""
		try :
			self._customsettings = customsettings
		except Exception as e:
			raise e

	@property
	def signatures(self) :
		r"""Object name for signatures.
		This check is applicable to Profile Type: HTML, XML. .<br/>Minimum length =  1.
		"""
		try :
			return self._signatures
		except Exception as e:
			raise e

	@signatures.setter
	def signatures(self, signatures) :
		r"""Object name for signatures.
		This check is applicable to Profile Type: HTML, XML. .<br/>Minimum length =  1
		"""
		try :
			self._signatures = signatures
		except Exception as e:
			raise e

	@property
	def xmlsoapfaultaction(self) :
		r"""One or more XML SOAP Fault Filtering actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		* Remove - Remove all violations for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLSOAPFaultAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLSOAPFaultAction none".<br/>Possible values = none, block, log, remove, stats.
		"""
		try :
			return self._xmlsoapfaultaction
		except Exception as e:
			raise e

	@xmlsoapfaultaction.setter
	def xmlsoapfaultaction(self, xmlsoapfaultaction) :
		r"""One or more XML SOAP Fault Filtering actions. Available settings function as follows:
		* Block - Block connections that violate this security check.
		* Log - Log violations of this security check.
		* Stats - Generate statistics for this security check.
		* None - Disable all actions for this security check.
		* Remove - Remove all violations for this security check.
		CLI users: To enable one or more actions, type "set appfw profile -XMLSOAPFaultAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLSOAPFaultAction none".<br/>Possible values = none, block, log, remove, stats
		"""
		try :
			self._xmlsoapfaultaction = xmlsoapfaultaction
		except Exception as e:
			raise e

	@property
	def usehtmlerrorobject(self) :
		r"""Send an imported HTML Error object to a user when a request is blocked, instead of redirecting the user to the designated Error URL.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._usehtmlerrorobject
		except Exception as e:
			raise e

	@usehtmlerrorobject.setter
	def usehtmlerrorobject(self, usehtmlerrorobject) :
		r"""Send an imported HTML Error object to a user when a request is blocked, instead of redirecting the user to the designated Error URL.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._usehtmlerrorobject = usehtmlerrorobject
		except Exception as e:
			raise e

	@property
	def errorurl(self) :
		r"""URL that application firewall uses as the Error URL.<br/>Minimum length =  1.
		"""
		try :
			return self._errorurl
		except Exception as e:
			raise e

	@errorurl.setter
	def errorurl(self, errorurl) :
		r"""URL that application firewall uses as the Error URL.<br/>Minimum length =  1
		"""
		try :
			self._errorurl = errorurl
		except Exception as e:
			raise e

	@property
	def htmlerrorobject(self) :
		r"""Name to assign to the HTML Error Object. 
		Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at (@), equals \(=\), colon \(:\), and underscore characters. Cannot be changed after the HTML error object is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my HTML error object" or 'my HTML error object'\).<br/>Minimum length =  1.
		"""
		try :
			return self._htmlerrorobject
		except Exception as e:
			raise e

	@htmlerrorobject.setter
	def htmlerrorobject(self, htmlerrorobject) :
		r"""Name to assign to the HTML Error Object. 
		Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at (@), equals \(=\), colon \(:\), and underscore characters. Cannot be changed after the HTML error object is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my HTML error object" or 'my HTML error object'\).<br/>Minimum length =  1
		"""
		try :
			self._htmlerrorobject = htmlerrorobject
		except Exception as e:
			raise e

	@property
	def logeverypolicyhit(self) :
		r"""Log every profile match, regardless of security checks results.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._logeverypolicyhit
		except Exception as e:
			raise e

	@logeverypolicyhit.setter
	def logeverypolicyhit(self, logeverypolicyhit) :
		r"""Log every profile match, regardless of security checks results.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._logeverypolicyhit = logeverypolicyhit
		except Exception as e:
			raise e

	@property
	def stripcomments(self) :
		r"""Strip HTML comments.
		This check is applicable to Profile Type: HTML. .<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._stripcomments
		except Exception as e:
			raise e

	@stripcomments.setter
	def stripcomments(self, stripcomments) :
		r"""Strip HTML comments.
		This check is applicable to Profile Type: HTML. .<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._stripcomments = stripcomments
		except Exception as e:
			raise e

	@property
	def striphtmlcomments(self) :
		r"""Strip HTML comments before forwarding a web page sent by a protected web site in response to a user request.<br/>Default value: none<br/>Possible values = none, all, exclude_script_tag.
		"""
		try :
			return self._striphtmlcomments
		except Exception as e:
			raise e

	@striphtmlcomments.setter
	def striphtmlcomments(self, striphtmlcomments) :
		r"""Strip HTML comments before forwarding a web page sent by a protected web site in response to a user request.<br/>Default value: none<br/>Possible values = none, all, exclude_script_tag
		"""
		try :
			self._striphtmlcomments = striphtmlcomments
		except Exception as e:
			raise e

	@property
	def stripxmlcomments(self) :
		r"""Strip XML comments before forwarding a web page sent by a protected web site in response to a user request.<br/>Default value: none<br/>Possible values = none, all.
		"""
		try :
			return self._stripxmlcomments
		except Exception as e:
			raise e

	@stripxmlcomments.setter
	def stripxmlcomments(self, stripxmlcomments) :
		r"""Strip XML comments before forwarding a web page sent by a protected web site in response to a user request.<br/>Default value: none<br/>Possible values = none, all
		"""
		try :
			self._stripxmlcomments = stripxmlcomments
		except Exception as e:
			raise e

	@property
	def exemptclosureurlsfromsecuritychecks(self) :
		r"""Exempt URLs that pass the Start URL closure check from SQL injection, cross-site script, field format and field consistency security checks at locations other than headers.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._exemptclosureurlsfromsecuritychecks
		except Exception as e:
			raise e

	@exemptclosureurlsfromsecuritychecks.setter
	def exemptclosureurlsfromsecuritychecks(self, exemptclosureurlsfromsecuritychecks) :
		r"""Exempt URLs that pass the Start URL closure check from SQL injection, cross-site script, field format and field consistency security checks at locations other than headers.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._exemptclosureurlsfromsecuritychecks = exemptclosureurlsfromsecuritychecks
		except Exception as e:
			raise e

	@property
	def defaultcharset(self) :
		r"""Default character set for protected web pages. Web pages sent by your protected web sites in response to user requests are assigned this character set if the page does not already specify a character set. The character sets supported by the application firewall are: 
		* iso-8859-1 (English US)
		* big5 (Chinese Traditional)
		* gb2312 (Chinese Simplified)
		* sjis (Japanese Shift-JIS)
		* euc-jp (Japanese EUC-JP)
		* iso-8859-9 (Turkish)
		* utf-8 (Unicode)
		* euc-kr (Korean).<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._defaultcharset
		except Exception as e:
			raise e

	@defaultcharset.setter
	def defaultcharset(self, defaultcharset) :
		r"""Default character set for protected web pages. Web pages sent by your protected web sites in response to user requests are assigned this character set if the page does not already specify a character set. The character sets supported by the application firewall are: 
		* iso-8859-1 (English US)
		* big5 (Chinese Traditional)
		* gb2312 (Chinese Simplified)
		* sjis (Japanese Shift-JIS)
		* euc-jp (Japanese EUC-JP)
		* iso-8859-9 (Turkish)
		* utf-8 (Unicode)
		* euc-kr (Korean).<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._defaultcharset = defaultcharset
		except Exception as e:
			raise e

	@property
	def postbodylimit(self) :
		r"""Maximum allowed HTTP post body size, in bytes.<br/>Default value: 20000000.
		"""
		try :
			return self._postbodylimit
		except Exception as e:
			raise e

	@postbodylimit.setter
	def postbodylimit(self, postbodylimit) :
		r"""Maximum allowed HTTP post body size, in bytes.<br/>Default value: 20000000
		"""
		try :
			self._postbodylimit = postbodylimit
		except Exception as e:
			raise e

	@property
	def fileuploadmaxnum(self) :
		r"""Maximum allowed number of file uploads per form-submission request. The maximum setting (65535) allows an unlimited number of uploads.<br/>Default value: 65535<br/>Maximum length =  65535.
		"""
		try :
			return self._fileuploadmaxnum
		except Exception as e:
			raise e

	@fileuploadmaxnum.setter
	def fileuploadmaxnum(self, fileuploadmaxnum) :
		r"""Maximum allowed number of file uploads per form-submission request. The maximum setting (65535) allows an unlimited number of uploads.<br/>Default value: 65535<br/>Maximum length =  65535
		"""
		try :
			self._fileuploadmaxnum = fileuploadmaxnum
		except Exception as e:
			raise e

	@property
	def canonicalizehtmlresponse(self) :
		r"""Perform HTML entity encoding for any special characters in responses sent by your protected web sites.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._canonicalizehtmlresponse
		except Exception as e:
			raise e

	@canonicalizehtmlresponse.setter
	def canonicalizehtmlresponse(self, canonicalizehtmlresponse) :
		r"""Perform HTML entity encoding for any special characters in responses sent by your protected web sites.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._canonicalizehtmlresponse = canonicalizehtmlresponse
		except Exception as e:
			raise e

	@property
	def enableformtagging(self) :
		r"""Enable tagging of web form fields for use by the Form Field Consistency and CSRF Form Tagging checks.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._enableformtagging
		except Exception as e:
			raise e

	@enableformtagging.setter
	def enableformtagging(self, enableformtagging) :
		r"""Enable tagging of web form fields for use by the Form Field Consistency and CSRF Form Tagging checks.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._enableformtagging = enableformtagging
		except Exception as e:
			raise e

	@property
	def sessionlessfieldconsistency(self) :
		r"""Perform sessionless Field Consistency Checks.<br/>Default value: OFF<br/>Possible values = OFF, ON, postOnly.
		"""
		try :
			return self._sessionlessfieldconsistency
		except Exception as e:
			raise e

	@sessionlessfieldconsistency.setter
	def sessionlessfieldconsistency(self, sessionlessfieldconsistency) :
		r"""Perform sessionless Field Consistency Checks.<br/>Default value: OFF<br/>Possible values = OFF, ON, postOnly
		"""
		try :
			self._sessionlessfieldconsistency = sessionlessfieldconsistency
		except Exception as e:
			raise e

	@property
	def sessionlessurlclosure(self) :
		r"""Enable session less URL Closure Checks.
		This check is applicable to Profile Type: HTML. .<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sessionlessurlclosure
		except Exception as e:
			raise e

	@sessionlessurlclosure.setter
	def sessionlessurlclosure(self, sessionlessurlclosure) :
		r"""Enable session less URL Closure Checks.
		This check is applicable to Profile Type: HTML. .<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sessionlessurlclosure = sessionlessurlclosure
		except Exception as e:
			raise e

	@property
	def semicolonfieldseparator(self) :
		r"""Allow ';' as a form field separator in URL queries and POST form bodies. .<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._semicolonfieldseparator
		except Exception as e:
			raise e

	@semicolonfieldseparator.setter
	def semicolonfieldseparator(self, semicolonfieldseparator) :
		r"""Allow ';' as a form field separator in URL queries and POST form bodies. .<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._semicolonfieldseparator = semicolonfieldseparator
		except Exception as e:
			raise e

	@property
	def excludefileuploadfromchecks(self) :
		r"""Exclude uploaded files from Form checks.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._excludefileuploadfromchecks
		except Exception as e:
			raise e

	@excludefileuploadfromchecks.setter
	def excludefileuploadfromchecks(self, excludefileuploadfromchecks) :
		r"""Exclude uploaded files from Form checks.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._excludefileuploadfromchecks = excludefileuploadfromchecks
		except Exception as e:
			raise e

	@property
	def sqlinjectionparsecomments(self) :
		r"""Parse HTML comments and exempt them from the HTML SQL Injection check. You must specify the type of comments that the application firewall is to detect and exempt from this security check. Available settings function as follows:
		* Check all - Check all content.
		* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. 
		* Nested - Exempt content that is part of a nested (Microsoft-style) comment.
		* ANSI Nested - Exempt content that is part of any type of comment.<br/>Possible values = checkall, ansi, nested, ansinested.
		"""
		try :
			return self._sqlinjectionparsecomments
		except Exception as e:
			raise e

	@sqlinjectionparsecomments.setter
	def sqlinjectionparsecomments(self, sqlinjectionparsecomments) :
		r"""Parse HTML comments and exempt them from the HTML SQL Injection check. You must specify the type of comments that the application firewall is to detect and exempt from this security check. Available settings function as follows:
		* Check all - Check all content.
		* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. 
		* Nested - Exempt content that is part of a nested (Microsoft-style) comment.
		* ANSI Nested - Exempt content that is part of any type of comment.<br/>Possible values = checkall, ansi, nested, ansinested
		"""
		try :
			self._sqlinjectionparsecomments = sqlinjectionparsecomments
		except Exception as e:
			raise e

	@property
	def invalidpercenthandling(self) :
		r"""Configure the method that the application firewall uses to handle percent-encoded names and values. Available settings function as follows: 
		* apache_mode - Apache format.
		* asp_mode - Microsoft ASP format.
		* secure_mode - Secure format.<br/>Default value: secure_mode<br/>Possible values = apache_mode, asp_mode, secure_mode.
		"""
		try :
			return self._invalidpercenthandling
		except Exception as e:
			raise e

	@invalidpercenthandling.setter
	def invalidpercenthandling(self, invalidpercenthandling) :
		r"""Configure the method that the application firewall uses to handle percent-encoded names and values. Available settings function as follows: 
		* apache_mode - Apache format.
		* asp_mode - Microsoft ASP format.
		* secure_mode - Secure format.<br/>Default value: secure_mode<br/>Possible values = apache_mode, asp_mode, secure_mode
		"""
		try :
			self._invalidpercenthandling = invalidpercenthandling
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Application firewall profile type, which controls which security checks and settings are applied to content that is filtered with the profile. Available settings function as follows:
		* HTML - HTML-based web sites.
		* XML - XML-based web sites and services.
		* HTML XML (Web 2.0) - Sites that contain both HTML and XML content, such as ATOM feeds, blogs, and RSS feeds.<br/>Default value: HTML<br/>Possible values = HTML, XML.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Application firewall profile type, which controls which security checks and settings are applied to content that is filtered with the profile. Available settings function as follows:
		* HTML - HTML-based web sites.
		* XML - XML-based web sites and services.
		* HTML XML (Web 2.0) - Sites that contain both HTML and XML content, such as ATOM feeds, blogs, and RSS feeds.<br/>Default value: HTML<br/>Possible values = HTML, XML
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def checkrequestheaders(self) :
		r"""Check request headers as well as web forms for injected SQL and cross-site scripts.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._checkrequestheaders
		except Exception as e:
			raise e

	@checkrequestheaders.setter
	def checkrequestheaders(self, checkrequestheaders) :
		r"""Check request headers as well as web forms for injected SQL and cross-site scripts.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._checkrequestheaders = checkrequestheaders
		except Exception as e:
			raise e

	@property
	def optimizepartialreqs(self) :
		r"""Optimize handle of HTTP partial requests i.e. those with range headers.
		Available settings are as follows: 
		* ON  - Partial requests by the client result in partial requests to the backend server in most cases.
		* OFF - Partial requests by the client are changed to full requests to the backend server.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._optimizepartialreqs
		except Exception as e:
			raise e

	@optimizepartialreqs.setter
	def optimizepartialreqs(self, optimizepartialreqs) :
		r"""Optimize handle of HTTP partial requests i.e. those with range headers.
		Available settings are as follows: 
		* ON  - Partial requests by the client result in partial requests to the backend server in most cases.
		* OFF - Partial requests by the client are changed to full requests to the backend server.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._optimizepartialreqs = optimizepartialreqs
		except Exception as e:
			raise e

	@property
	def urldecoderequestcookies(self) :
		r"""URL Decode request cookies before subjecting them to SQL and cross-site scripting checks.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._urldecoderequestcookies
		except Exception as e:
			raise e

	@urldecoderequestcookies.setter
	def urldecoderequestcookies(self, urldecoderequestcookies) :
		r"""URL Decode request cookies before subjecting them to SQL and cross-site scripting checks.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._urldecoderequestcookies = urldecoderequestcookies
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def percentdecoderecursively(self) :
		r"""Configure whether the application firewall should use percentage recursive decoding.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._percentdecoderecursively
		except Exception as e:
			raise e

	@percentdecoderecursively.setter
	def percentdecoderecursively(self, percentdecoderecursively) :
		r"""Configure whether the application firewall should use percentage recursive decoding.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._percentdecoderecursively = percentdecoderecursively
		except Exception as e:
			raise e

	@property
	def multipleheaderaction(self) :
		r"""One or more multiple header actions. Available settings function as follows:
		* Block - Block connections that have multiple headers.
		* Log - Log connections that have multiple headers.
		* KeepLast - Keep only last header when multiple headers are present.
		CLI users: To enable one or more actions, type "set appfw profile -multipleHeaderAction" followed by the actions to be enabled.<br/>Possible values = block, keepLast, log, none.
		"""
		try :
			return self._multipleheaderaction
		except Exception as e:
			raise e

	@multipleheaderaction.setter
	def multipleheaderaction(self, multipleheaderaction) :
		r"""One or more multiple header actions. Available settings function as follows:
		* Block - Block connections that have multiple headers.
		* Log - Log connections that have multiple headers.
		* KeepLast - Keep only last header when multiple headers are present.
		CLI users: To enable one or more actions, type "set appfw profile -multipleHeaderAction" followed by the actions to be enabled.<br/>Possible values = block, keepLast, log, none
		"""
		try :
			self._multipleheaderaction = multipleheaderaction
		except Exception as e:
			raise e

	@property
	def rfcprofile(self) :
		r"""Object name of the rfc profile.<br/>Minimum length =  1.
		"""
		try :
			return self._rfcprofile
		except Exception as e:
			raise e

	@rfcprofile.setter
	def rfcprofile(self, rfcprofile) :
		r"""Object name of the rfc profile.<br/>Minimum length =  1
		"""
		try :
			self._rfcprofile = rfcprofile
		except Exception as e:
			raise e

	@property
	def archivename(self) :
		r"""Source for tar archive.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._archivename
		except Exception as e:
			raise e

	@archivename.setter
	def archivename(self, archivename) :
		r"""Source for tar archive.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._archivename = archivename
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Enabled.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def csrftag(self) :
		r"""The web form originating URL.
		"""
		try :
			return self._csrftag
		except Exception as e:
			raise e

	@property
	def builtin_depr(self) :
		r"""Indicates that a profile is a built-in entity.
		"""
		try :
			return self._builtin_depr
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile
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
		r""" Use this API to add appfwprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = appfwprofile()
				addresource.name = resource.name
				addresource.defaults = resource.defaults
				addresource.feature = resource.feature
				addresource.starturlaction = resource.starturlaction
				addresource.contenttypeaction = resource.contenttypeaction
				addresource.inspectcontenttypes = resource.inspectcontenttypes
				addresource.starturlclosure = resource.starturlclosure
				addresource.denyurlaction = resource.denyurlaction
				addresource.refererheadercheck = resource.refererheadercheck
				addresource.cookieconsistencyaction = resource.cookieconsistencyaction
				addresource.cookietransforms = resource.cookietransforms
				addresource.cookieencryption = resource.cookieencryption
				addresource.cookieproxying = resource.cookieproxying
				addresource.addcookieflags = resource.addcookieflags
				addresource.fieldconsistencyaction = resource.fieldconsistencyaction
				addresource.csrftagaction = resource.csrftagaction
				addresource.crosssitescriptingaction = resource.crosssitescriptingaction
				addresource.crosssitescriptingtransformunsafehtml = resource.crosssitescriptingtransformunsafehtml
				addresource.crosssitescriptingcheckcompleteurls = resource.crosssitescriptingcheckcompleteurls
				addresource.sqlinjectionaction = resource.sqlinjectionaction
				addresource.sqlinjectiontransformspecialchars = resource.sqlinjectiontransformspecialchars
				addresource.sqlinjectiononlycheckfieldswithsqlchars = resource.sqlinjectiononlycheckfieldswithsqlchars
				addresource.sqlinjectiontype = resource.sqlinjectiontype
				addresource.sqlinjectionchecksqlwildchars = resource.sqlinjectionchecksqlwildchars
				addresource.fieldformataction = resource.fieldformataction
				addresource.defaultfieldformattype = resource.defaultfieldformattype
				addresource.defaultfieldformatminlength = resource.defaultfieldformatminlength
				addresource.defaultfieldformatmaxlength = resource.defaultfieldformatmaxlength
				addresource.bufferoverflowaction = resource.bufferoverflowaction
				addresource.bufferoverflowmaxurllength = resource.bufferoverflowmaxurllength
				addresource.bufferoverflowmaxheaderlength = resource.bufferoverflowmaxheaderlength
				addresource.bufferoverflowmaxcookielength = resource.bufferoverflowmaxcookielength
				addresource.creditcardaction = resource.creditcardaction
				addresource.creditcard = resource.creditcard
				addresource.creditcardmaxallowed = resource.creditcardmaxallowed
				addresource.creditcardxout = resource.creditcardxout
				addresource.dosecurecreditcardlogging = resource.dosecurecreditcardlogging
				addresource.streaming = resource.streaming
				addresource.trace = resource.trace
				addresource.requestcontenttype = resource.requestcontenttype
				addresource.responsecontenttype = resource.responsecontenttype
				addresource.xmldosaction = resource.xmldosaction
				addresource.xmlformataction = resource.xmlformataction
				addresource.xmlsqlinjectionaction = resource.xmlsqlinjectionaction
				addresource.xmlsqlinjectiononlycheckfieldswithsqlchars = resource.xmlsqlinjectiononlycheckfieldswithsqlchars
				addresource.xmlsqlinjectiontype = resource.xmlsqlinjectiontype
				addresource.xmlsqlinjectionchecksqlwildchars = resource.xmlsqlinjectionchecksqlwildchars
				addresource.xmlsqlinjectionparsecomments = resource.xmlsqlinjectionparsecomments
				addresource.xmlxssaction = resource.xmlxssaction
				addresource.xmlwsiaction = resource.xmlwsiaction
				addresource.xmlattachmentaction = resource.xmlattachmentaction
				addresource.xmlvalidationaction = resource.xmlvalidationaction
				addresource.xmlerrorobject = resource.xmlerrorobject
				addresource.customsettings = resource.customsettings
				addresource.signatures = resource.signatures
				addresource.xmlsoapfaultaction = resource.xmlsoapfaultaction
				addresource.usehtmlerrorobject = resource.usehtmlerrorobject
				addresource.errorurl = resource.errorurl
				addresource.htmlerrorobject = resource.htmlerrorobject
				addresource.logeverypolicyhit = resource.logeverypolicyhit
				addresource.stripcomments = resource.stripcomments
				addresource.striphtmlcomments = resource.striphtmlcomments
				addresource.stripxmlcomments = resource.stripxmlcomments
				addresource.exemptclosureurlsfromsecuritychecks = resource.exemptclosureurlsfromsecuritychecks
				addresource.defaultcharset = resource.defaultcharset
				addresource.postbodylimit = resource.postbodylimit
				addresource.fileuploadmaxnum = resource.fileuploadmaxnum
				addresource.canonicalizehtmlresponse = resource.canonicalizehtmlresponse
				addresource.enableformtagging = resource.enableformtagging
				addresource.sessionlessfieldconsistency = resource.sessionlessfieldconsistency
				addresource.sessionlessurlclosure = resource.sessionlessurlclosure
				addresource.semicolonfieldseparator = resource.semicolonfieldseparator
				addresource.excludefileuploadfromchecks = resource.excludefileuploadfromchecks
				addresource.sqlinjectionparsecomments = resource.sqlinjectionparsecomments
				addresource.invalidpercenthandling = resource.invalidpercenthandling
				addresource.type = resource.type
				addresource.checkrequestheaders = resource.checkrequestheaders
				addresource.optimizepartialreqs = resource.optimizepartialreqs
				addresource.urldecoderequestcookies = resource.urldecoderequestcookies
				addresource.comment = resource.comment
				addresource.percentdecoderecursively = resource.percentdecoderecursively
				addresource.multipleheaderaction = resource.multipleheaderaction
				addresource.rfcprofile = resource.rfcprofile
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ appfwprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].defaults = resource[i].defaults
						addresources[i].feature = resource[i].feature
						addresources[i].starturlaction = resource[i].starturlaction
						addresources[i].contenttypeaction = resource[i].contenttypeaction
						addresources[i].inspectcontenttypes = resource[i].inspectcontenttypes
						addresources[i].starturlclosure = resource[i].starturlclosure
						addresources[i].denyurlaction = resource[i].denyurlaction
						addresources[i].refererheadercheck = resource[i].refererheadercheck
						addresources[i].cookieconsistencyaction = resource[i].cookieconsistencyaction
						addresources[i].cookietransforms = resource[i].cookietransforms
						addresources[i].cookieencryption = resource[i].cookieencryption
						addresources[i].cookieproxying = resource[i].cookieproxying
						addresources[i].addcookieflags = resource[i].addcookieflags
						addresources[i].fieldconsistencyaction = resource[i].fieldconsistencyaction
						addresources[i].csrftagaction = resource[i].csrftagaction
						addresources[i].crosssitescriptingaction = resource[i].crosssitescriptingaction
						addresources[i].crosssitescriptingtransformunsafehtml = resource[i].crosssitescriptingtransformunsafehtml
						addresources[i].crosssitescriptingcheckcompleteurls = resource[i].crosssitescriptingcheckcompleteurls
						addresources[i].sqlinjectionaction = resource[i].sqlinjectionaction
						addresources[i].sqlinjectiontransformspecialchars = resource[i].sqlinjectiontransformspecialchars
						addresources[i].sqlinjectiononlycheckfieldswithsqlchars = resource[i].sqlinjectiononlycheckfieldswithsqlchars
						addresources[i].sqlinjectiontype = resource[i].sqlinjectiontype
						addresources[i].sqlinjectionchecksqlwildchars = resource[i].sqlinjectionchecksqlwildchars
						addresources[i].fieldformataction = resource[i].fieldformataction
						addresources[i].defaultfieldformattype = resource[i].defaultfieldformattype
						addresources[i].defaultfieldformatminlength = resource[i].defaultfieldformatminlength
						addresources[i].defaultfieldformatmaxlength = resource[i].defaultfieldformatmaxlength
						addresources[i].bufferoverflowaction = resource[i].bufferoverflowaction
						addresources[i].bufferoverflowmaxurllength = resource[i].bufferoverflowmaxurllength
						addresources[i].bufferoverflowmaxheaderlength = resource[i].bufferoverflowmaxheaderlength
						addresources[i].bufferoverflowmaxcookielength = resource[i].bufferoverflowmaxcookielength
						addresources[i].creditcardaction = resource[i].creditcardaction
						addresources[i].creditcard = resource[i].creditcard
						addresources[i].creditcardmaxallowed = resource[i].creditcardmaxallowed
						addresources[i].creditcardxout = resource[i].creditcardxout
						addresources[i].dosecurecreditcardlogging = resource[i].dosecurecreditcardlogging
						addresources[i].streaming = resource[i].streaming
						addresources[i].trace = resource[i].trace
						addresources[i].requestcontenttype = resource[i].requestcontenttype
						addresources[i].responsecontenttype = resource[i].responsecontenttype
						addresources[i].xmldosaction = resource[i].xmldosaction
						addresources[i].xmlformataction = resource[i].xmlformataction
						addresources[i].xmlsqlinjectionaction = resource[i].xmlsqlinjectionaction
						addresources[i].xmlsqlinjectiononlycheckfieldswithsqlchars = resource[i].xmlsqlinjectiononlycheckfieldswithsqlchars
						addresources[i].xmlsqlinjectiontype = resource[i].xmlsqlinjectiontype
						addresources[i].xmlsqlinjectionchecksqlwildchars = resource[i].xmlsqlinjectionchecksqlwildchars
						addresources[i].xmlsqlinjectionparsecomments = resource[i].xmlsqlinjectionparsecomments
						addresources[i].xmlxssaction = resource[i].xmlxssaction
						addresources[i].xmlwsiaction = resource[i].xmlwsiaction
						addresources[i].xmlattachmentaction = resource[i].xmlattachmentaction
						addresources[i].xmlvalidationaction = resource[i].xmlvalidationaction
						addresources[i].xmlerrorobject = resource[i].xmlerrorobject
						addresources[i].customsettings = resource[i].customsettings
						addresources[i].signatures = resource[i].signatures
						addresources[i].xmlsoapfaultaction = resource[i].xmlsoapfaultaction
						addresources[i].usehtmlerrorobject = resource[i].usehtmlerrorobject
						addresources[i].errorurl = resource[i].errorurl
						addresources[i].htmlerrorobject = resource[i].htmlerrorobject
						addresources[i].logeverypolicyhit = resource[i].logeverypolicyhit
						addresources[i].stripcomments = resource[i].stripcomments
						addresources[i].striphtmlcomments = resource[i].striphtmlcomments
						addresources[i].stripxmlcomments = resource[i].stripxmlcomments
						addresources[i].exemptclosureurlsfromsecuritychecks = resource[i].exemptclosureurlsfromsecuritychecks
						addresources[i].defaultcharset = resource[i].defaultcharset
						addresources[i].postbodylimit = resource[i].postbodylimit
						addresources[i].fileuploadmaxnum = resource[i].fileuploadmaxnum
						addresources[i].canonicalizehtmlresponse = resource[i].canonicalizehtmlresponse
						addresources[i].enableformtagging = resource[i].enableformtagging
						addresources[i].sessionlessfieldconsistency = resource[i].sessionlessfieldconsistency
						addresources[i].sessionlessurlclosure = resource[i].sessionlessurlclosure
						addresources[i].semicolonfieldseparator = resource[i].semicolonfieldseparator
						addresources[i].excludefileuploadfromchecks = resource[i].excludefileuploadfromchecks
						addresources[i].sqlinjectionparsecomments = resource[i].sqlinjectionparsecomments
						addresources[i].invalidpercenthandling = resource[i].invalidpercenthandling
						addresources[i].type = resource[i].type
						addresources[i].checkrequestheaders = resource[i].checkrequestheaders
						addresources[i].optimizepartialreqs = resource[i].optimizepartialreqs
						addresources[i].urldecoderequestcookies = resource[i].urldecoderequestcookies
						addresources[i].comment = resource[i].comment
						addresources[i].percentdecoderecursively = resource[i].percentdecoderecursively
						addresources[i].multipleheaderaction = resource[i].multipleheaderaction
						addresources[i].rfcprofile = resource[i].rfcprofile
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete appfwprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = appfwprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ appfwprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ appfwprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update appfwprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = appfwprofile()
				updateresource.name = resource.name
				updateresource.starturlaction = resource.starturlaction
				updateresource.contenttypeaction = resource.contenttypeaction
				updateresource.inspectcontenttypes = resource.inspectcontenttypes
				updateresource.starturlclosure = resource.starturlclosure
				updateresource.denyurlaction = resource.denyurlaction
				updateresource.refererheadercheck = resource.refererheadercheck
				updateresource.cookieconsistencyaction = resource.cookieconsistencyaction
				updateresource.cookietransforms = resource.cookietransforms
				updateresource.cookieencryption = resource.cookieencryption
				updateresource.cookieproxying = resource.cookieproxying
				updateresource.addcookieflags = resource.addcookieflags
				updateresource.fieldconsistencyaction = resource.fieldconsistencyaction
				updateresource.csrftagaction = resource.csrftagaction
				updateresource.crosssitescriptingaction = resource.crosssitescriptingaction
				updateresource.crosssitescriptingtransformunsafehtml = resource.crosssitescriptingtransformunsafehtml
				updateresource.crosssitescriptingcheckcompleteurls = resource.crosssitescriptingcheckcompleteurls
				updateresource.sqlinjectionaction = resource.sqlinjectionaction
				updateresource.sqlinjectiontransformspecialchars = resource.sqlinjectiontransformspecialchars
				updateresource.sqlinjectiononlycheckfieldswithsqlchars = resource.sqlinjectiononlycheckfieldswithsqlchars
				updateresource.sqlinjectiontype = resource.sqlinjectiontype
				updateresource.sqlinjectionchecksqlwildchars = resource.sqlinjectionchecksqlwildchars
				updateresource.fieldformataction = resource.fieldformataction
				updateresource.defaultfieldformattype = resource.defaultfieldformattype
				updateresource.defaultfieldformatminlength = resource.defaultfieldformatminlength
				updateresource.defaultfieldformatmaxlength = resource.defaultfieldformatmaxlength
				updateresource.bufferoverflowaction = resource.bufferoverflowaction
				updateresource.bufferoverflowmaxurllength = resource.bufferoverflowmaxurllength
				updateresource.bufferoverflowmaxheaderlength = resource.bufferoverflowmaxheaderlength
				updateresource.bufferoverflowmaxcookielength = resource.bufferoverflowmaxcookielength
				updateresource.creditcardaction = resource.creditcardaction
				updateresource.creditcard = resource.creditcard
				updateresource.creditcardmaxallowed = resource.creditcardmaxallowed
				updateresource.creditcardxout = resource.creditcardxout
				updateresource.dosecurecreditcardlogging = resource.dosecurecreditcardlogging
				updateresource.streaming = resource.streaming
				updateresource.trace = resource.trace
				updateresource.requestcontenttype = resource.requestcontenttype
				updateresource.responsecontenttype = resource.responsecontenttype
				updateresource.xmldosaction = resource.xmldosaction
				updateresource.xmlformataction = resource.xmlformataction
				updateresource.xmlsqlinjectionaction = resource.xmlsqlinjectionaction
				updateresource.xmlsqlinjectiononlycheckfieldswithsqlchars = resource.xmlsqlinjectiononlycheckfieldswithsqlchars
				updateresource.xmlsqlinjectiontype = resource.xmlsqlinjectiontype
				updateresource.xmlsqlinjectionchecksqlwildchars = resource.xmlsqlinjectionchecksqlwildchars
				updateresource.xmlsqlinjectionparsecomments = resource.xmlsqlinjectionparsecomments
				updateresource.xmlxssaction = resource.xmlxssaction
				updateresource.xmlwsiaction = resource.xmlwsiaction
				updateresource.xmlattachmentaction = resource.xmlattachmentaction
				updateresource.xmlvalidationaction = resource.xmlvalidationaction
				updateresource.xmlerrorobject = resource.xmlerrorobject
				updateresource.customsettings = resource.customsettings
				updateresource.signatures = resource.signatures
				updateresource.xmlsoapfaultaction = resource.xmlsoapfaultaction
				updateresource.usehtmlerrorobject = resource.usehtmlerrorobject
				updateresource.errorurl = resource.errorurl
				updateresource.htmlerrorobject = resource.htmlerrorobject
				updateresource.logeverypolicyhit = resource.logeverypolicyhit
				updateresource.stripcomments = resource.stripcomments
				updateresource.striphtmlcomments = resource.striphtmlcomments
				updateresource.stripxmlcomments = resource.stripxmlcomments
				updateresource.exemptclosureurlsfromsecuritychecks = resource.exemptclosureurlsfromsecuritychecks
				updateresource.defaultcharset = resource.defaultcharset
				updateresource.postbodylimit = resource.postbodylimit
				updateresource.fileuploadmaxnum = resource.fileuploadmaxnum
				updateresource.canonicalizehtmlresponse = resource.canonicalizehtmlresponse
				updateresource.enableformtagging = resource.enableformtagging
				updateresource.sessionlessfieldconsistency = resource.sessionlessfieldconsistency
				updateresource.sessionlessurlclosure = resource.sessionlessurlclosure
				updateresource.semicolonfieldseparator = resource.semicolonfieldseparator
				updateresource.excludefileuploadfromchecks = resource.excludefileuploadfromchecks
				updateresource.sqlinjectionparsecomments = resource.sqlinjectionparsecomments
				updateresource.invalidpercenthandling = resource.invalidpercenthandling
				updateresource.type = resource.type
				updateresource.checkrequestheaders = resource.checkrequestheaders
				updateresource.optimizepartialreqs = resource.optimizepartialreqs
				updateresource.urldecoderequestcookies = resource.urldecoderequestcookies
				updateresource.comment = resource.comment
				updateresource.percentdecoderecursively = resource.percentdecoderecursively
				updateresource.multipleheaderaction = resource.multipleheaderaction
				updateresource.rfcprofile = resource.rfcprofile
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ appfwprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].starturlaction = resource[i].starturlaction
						updateresources[i].contenttypeaction = resource[i].contenttypeaction
						updateresources[i].inspectcontenttypes = resource[i].inspectcontenttypes
						updateresources[i].starturlclosure = resource[i].starturlclosure
						updateresources[i].denyurlaction = resource[i].denyurlaction
						updateresources[i].refererheadercheck = resource[i].refererheadercheck
						updateresources[i].cookieconsistencyaction = resource[i].cookieconsistencyaction
						updateresources[i].cookietransforms = resource[i].cookietransforms
						updateresources[i].cookieencryption = resource[i].cookieencryption
						updateresources[i].cookieproxying = resource[i].cookieproxying
						updateresources[i].addcookieflags = resource[i].addcookieflags
						updateresources[i].fieldconsistencyaction = resource[i].fieldconsistencyaction
						updateresources[i].csrftagaction = resource[i].csrftagaction
						updateresources[i].crosssitescriptingaction = resource[i].crosssitescriptingaction
						updateresources[i].crosssitescriptingtransformunsafehtml = resource[i].crosssitescriptingtransformunsafehtml
						updateresources[i].crosssitescriptingcheckcompleteurls = resource[i].crosssitescriptingcheckcompleteurls
						updateresources[i].sqlinjectionaction = resource[i].sqlinjectionaction
						updateresources[i].sqlinjectiontransformspecialchars = resource[i].sqlinjectiontransformspecialchars
						updateresources[i].sqlinjectiononlycheckfieldswithsqlchars = resource[i].sqlinjectiononlycheckfieldswithsqlchars
						updateresources[i].sqlinjectiontype = resource[i].sqlinjectiontype
						updateresources[i].sqlinjectionchecksqlwildchars = resource[i].sqlinjectionchecksqlwildchars
						updateresources[i].fieldformataction = resource[i].fieldformataction
						updateresources[i].defaultfieldformattype = resource[i].defaultfieldformattype
						updateresources[i].defaultfieldformatminlength = resource[i].defaultfieldformatminlength
						updateresources[i].defaultfieldformatmaxlength = resource[i].defaultfieldformatmaxlength
						updateresources[i].bufferoverflowaction = resource[i].bufferoverflowaction
						updateresources[i].bufferoverflowmaxurllength = resource[i].bufferoverflowmaxurllength
						updateresources[i].bufferoverflowmaxheaderlength = resource[i].bufferoverflowmaxheaderlength
						updateresources[i].bufferoverflowmaxcookielength = resource[i].bufferoverflowmaxcookielength
						updateresources[i].creditcardaction = resource[i].creditcardaction
						updateresources[i].creditcard = resource[i].creditcard
						updateresources[i].creditcardmaxallowed = resource[i].creditcardmaxallowed
						updateresources[i].creditcardxout = resource[i].creditcardxout
						updateresources[i].dosecurecreditcardlogging = resource[i].dosecurecreditcardlogging
						updateresources[i].streaming = resource[i].streaming
						updateresources[i].trace = resource[i].trace
						updateresources[i].requestcontenttype = resource[i].requestcontenttype
						updateresources[i].responsecontenttype = resource[i].responsecontenttype
						updateresources[i].xmldosaction = resource[i].xmldosaction
						updateresources[i].xmlformataction = resource[i].xmlformataction
						updateresources[i].xmlsqlinjectionaction = resource[i].xmlsqlinjectionaction
						updateresources[i].xmlsqlinjectiononlycheckfieldswithsqlchars = resource[i].xmlsqlinjectiononlycheckfieldswithsqlchars
						updateresources[i].xmlsqlinjectiontype = resource[i].xmlsqlinjectiontype
						updateresources[i].xmlsqlinjectionchecksqlwildchars = resource[i].xmlsqlinjectionchecksqlwildchars
						updateresources[i].xmlsqlinjectionparsecomments = resource[i].xmlsqlinjectionparsecomments
						updateresources[i].xmlxssaction = resource[i].xmlxssaction
						updateresources[i].xmlwsiaction = resource[i].xmlwsiaction
						updateresources[i].xmlattachmentaction = resource[i].xmlattachmentaction
						updateresources[i].xmlvalidationaction = resource[i].xmlvalidationaction
						updateresources[i].xmlerrorobject = resource[i].xmlerrorobject
						updateresources[i].customsettings = resource[i].customsettings
						updateresources[i].signatures = resource[i].signatures
						updateresources[i].xmlsoapfaultaction = resource[i].xmlsoapfaultaction
						updateresources[i].usehtmlerrorobject = resource[i].usehtmlerrorobject
						updateresources[i].errorurl = resource[i].errorurl
						updateresources[i].htmlerrorobject = resource[i].htmlerrorobject
						updateresources[i].logeverypolicyhit = resource[i].logeverypolicyhit
						updateresources[i].stripcomments = resource[i].stripcomments
						updateresources[i].striphtmlcomments = resource[i].striphtmlcomments
						updateresources[i].stripxmlcomments = resource[i].stripxmlcomments
						updateresources[i].exemptclosureurlsfromsecuritychecks = resource[i].exemptclosureurlsfromsecuritychecks
						updateresources[i].defaultcharset = resource[i].defaultcharset
						updateresources[i].postbodylimit = resource[i].postbodylimit
						updateresources[i].fileuploadmaxnum = resource[i].fileuploadmaxnum
						updateresources[i].canonicalizehtmlresponse = resource[i].canonicalizehtmlresponse
						updateresources[i].enableformtagging = resource[i].enableformtagging
						updateresources[i].sessionlessfieldconsistency = resource[i].sessionlessfieldconsistency
						updateresources[i].sessionlessurlclosure = resource[i].sessionlessurlclosure
						updateresources[i].semicolonfieldseparator = resource[i].semicolonfieldseparator
						updateresources[i].excludefileuploadfromchecks = resource[i].excludefileuploadfromchecks
						updateresources[i].sqlinjectionparsecomments = resource[i].sqlinjectionparsecomments
						updateresources[i].invalidpercenthandling = resource[i].invalidpercenthandling
						updateresources[i].type = resource[i].type
						updateresources[i].checkrequestheaders = resource[i].checkrequestheaders
						updateresources[i].optimizepartialreqs = resource[i].optimizepartialreqs
						updateresources[i].urldecoderequestcookies = resource[i].urldecoderequestcookies
						updateresources[i].comment = resource[i].comment
						updateresources[i].percentdecoderecursively = resource[i].percentdecoderecursively
						updateresources[i].multipleheaderaction = resource[i].multipleheaderaction
						updateresources[i].rfcprofile = resource[i].rfcprofile
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of appfwprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = appfwprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ appfwprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ appfwprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def restore(cls, client, resource) :
		r""" Use this API to restore appfwprofile.
		"""
		try :
			if type(resource) is not list :
				restoreresource = appfwprofile()
				restoreresource.archivename = resource.archivename
				return restoreresource.perform_operation(client,"restore")
			else :
				if (resource and len(resource) > 0) :
					restoreresources = [ appfwprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						restoreresources[i].archivename = resource[i].archivename
				result = cls.perform_operation_bulk_request(client, restoreresources,"restore")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the appfwprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appfwprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = appfwprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [appfwprofile() for _ in range(len(name))]
						obj = [appfwprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = appfwprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of appfwprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the appfwprofile resources configured on NetScaler.
		"""
		try :
			obj = appfwprofile()
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
		r""" Use this API to count filtered the set of appfwprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Cookieconsistencyaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Denyurlaction:
		none = "none"
		block = "block"
		log = "log"
		stats = "stats"

	class Urldecoderequestcookies:
		ON = "ON"
		OFF = "OFF"

	class Sessionlessfieldconsistency:
		OFF = "OFF"
		ON = "ON"
		postOnly = "postOnly"

	class Xmlsqlinjectiontype:
		SQLSplChar = "SQLSplChar"
		SQLKeyword = "SQLKeyword"
		SQLSplCharORKeyword = "SQLSplCharORKeyword"
		SQLSplCharANDKeyword = "SQLSplCharANDKeyword"

	class Stripxmlcomments:
		none = "none"
		all = "all"

	class Sqlinjectionchecksqlwildchars:
		ON = "ON"
		OFF = "OFF"

	class Sqlinjectiononlycheckfieldswithsqlchars:
		ON = "ON"
		OFF = "OFF"

	class Trace:
		ON = "ON"
		OFF = "OFF"

	class Enableformtagging:
		ON = "ON"
		OFF = "OFF"

	class Fieldconsistencyaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Dosecurecreditcardlogging:
		ON = "ON"
		OFF = "OFF"

	class Refererheadercheck:
		OFF = "OFF"
		if_present = "if_present"
		AlwaysExceptStartURLs = "AlwaysExceptStartURLs"
		AlwaysExceptFirstRequest = "AlwaysExceptFirstRequest"

	class Exemptclosureurlsfromsecuritychecks:
		ON = "ON"
		OFF = "OFF"

	class Creditcardxout:
		ON = "ON"
		OFF = "OFF"

	class Fieldformataction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Cookietransforms:
		ON = "ON"
		OFF = "OFF"

	class Multipleheaderaction:
		block = "block"
		keepLast = "keepLast"
		log = "log"
		none = "none"

	class Crosssitescriptingtransformunsafehtml:
		ON = "ON"
		OFF = "OFF"

	class Xmlsqlinjectionaction:
		none = "none"
		block = "block"
		log = "log"
		stats = "stats"

	class Defaults:
		basic = "basic"
		advanced = "advanced"

	class Semicolonfieldseparator:
		ON = "ON"
		OFF = "OFF"

	class Xmlvalidationaction:
		none = "none"
		block = "block"
		log = "log"
		stats = "stats"

	class Xmldosaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Crosssitescriptingcheckcompleteurls:
		ON = "ON"
		OFF = "OFF"

	class Xmlformataction:
		none = "none"
		block = "block"
		log = "log"
		stats = "stats"

	class Optimizepartialreqs:
		ON = "ON"
		OFF = "OFF"

	class Creditcard:
		none = "none"
		visa = "visa"
		mastercard = "mastercard"
		discover = "discover"
		amex = "amex"
		jcb = "jcb"
		dinersclub = "dinersclub"

	class Starturlclosure:
		ON = "ON"
		OFF = "OFF"

	class Xmlsqlinjectiononlycheckfieldswithsqlchars:
		ON = "ON"
		OFF = "OFF"

	class Addcookieflags:
		none = "none"
		httpOnly = "httpOnly"
		secure = "secure"
		all = "all"

	class Sqlinjectionparsecomments:
		checkall = "checkall"
		ansi = "ansi"
		nested = "nested"
		ansinested = "ansinested"

	class Invalidpercenthandling:
		apache_mode = "apache_mode"
		asp_mode = "asp_mode"
		secure_mode = "secure_mode"

	class Contenttypeaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Xmlsqlinjectionparsecomments:
		checkall = "checkall"
		ansi = "ansi"
		nested = "nested"
		ansinested = "ansinested"

	class Percentdecoderecursively:
		ON = "ON"
		OFF = "OFF"

	class Checkrequestheaders:
		ON = "ON"
		OFF = "OFF"

	class Creditcardaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class State:
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

	class Starturlaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Striphtmlcomments:
		none = "none"
		all = "all"
		exclude_script_tag = "exclude_script_tag"

	class Sqlinjectiontransformspecialchars:
		ON = "ON"
		OFF = "OFF"

	class Excludefileuploadfromchecks:
		ON = "ON"
		OFF = "OFF"

	class Usehtmlerrorobject:
		ON = "ON"
		OFF = "OFF"

	class Xmlwsiaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Cookieproxying:
		none = "none"
		sessionOnly = "sessionOnly"

	class Csrftagaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Xmlattachmentaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Canonicalizehtmlresponse:
		ON = "ON"
		OFF = "OFF"

	class Logeverypolicyhit:
		ON = "ON"
		OFF = "OFF"

	class Type:
		HTML = "HTML"
		XML = "XML"

	class Stripcomments:
		ON = "ON"
		OFF = "OFF"

	class Inspectcontenttypes:
		none = "none"
		application_x_www_form_urlencoded = "application/x-www-form-urlencoded"
		multipart_form_data = "multipart/form-data"
		text_x_gwt_rpc = "text/x-gwt-rpc"

	class Streaming:
		ON = "ON"
		OFF = "OFF"

	class Xmlxssaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Sqlinjectionaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

	class Bufferoverflowaction:
		none = "none"
		block = "block"
		log = "log"
		stats = "stats"

	class Sessionlessurlclosure:
		ON = "ON"
		OFF = "OFF"

	class Cookieencryption:
		none = "none"
		decryptOnly = "decryptOnly"
		encryptSessionOnly = "encryptSessionOnly"
		encryptAll = "encryptAll"

	class Xmlsoapfaultaction:
		none = "none"
		block = "block"
		log = "log"
		remove = "remove"
		stats = "stats"

	class Sqlinjectiontype:
		SQLSplChar = "SQLSplChar"
		SQLKeyword = "SQLKeyword"
		SQLSplCharORKeyword = "SQLSplCharORKeyword"
		SQLSplCharANDKeyword = "SQLSplCharANDKeyword"

	class Xmlsqlinjectionchecksqlwildchars:
		ON = "ON"
		OFF = "OFF"

	class Crosssitescriptingaction:
		none = "none"
		block = "block"
		learn = "learn"
		log = "log"
		stats = "stats"

class appfwprofile_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile = [appfwprofile() for _ in range(length)]

