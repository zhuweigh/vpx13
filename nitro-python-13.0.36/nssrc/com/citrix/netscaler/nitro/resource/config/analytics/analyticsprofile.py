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

class analyticsprofile(base_resource) :
	""" Configuration for Analytics profile resource. """
	def __init__(self) :
		self._name = None
		self._collectors = None
		self._type = None
		self._httpclientsidemeasurements = None
		self._httppagetracking = None
		self._httpurl = None
		self._httphost = None
		self._httpmethod = None
		self._httpreferer = None
		self._httpuseragent = None
		self._httpcookie = None
		self._httplocation = None
		self._urlcategory = None
		self._httpcontenttype = None
		self._httpauthentication = None
		self._httpvia = None
		self._httpxforwardedforheader = None
		self._httpsetcookie = None
		self._httpsetcookie2 = None
		self._httpdomainname = None
		self._httpurlquery = None
		self._tcpburstreporting = None
		self._cqareporting = None
		self._integratedcache = None
		self._feature = None
		self._refcnt = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the analytics profile. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at
		(@), equals (=), and hyphen (-) characters.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my appflow profile" or 'my appflow profile').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the analytics profile. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at
		(@), equals (=), and hyphen (-) characters.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my appflow profile" or 'my appflow profile').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def collectors(self) :
		r"""The collector can be an IP, an appflow collector name, a service or a vserver. If IP is specified, the transport is considered as logstream and default port of 5557 is taken. If collector name is specified, the collector properties are taken from the configured collector. If service is specified, the configured service is assumed as the collector. If vserver is specified, the services bound to it are considered as collectors and the records are load balanced.<br/>Minimum length =  1.
		"""
		try :
			return self._collectors
		except Exception as e:
			raise e

	@collectors.setter
	def collectors(self, collectors) :
		r"""The collector can be an IP, an appflow collector name, a service or a vserver. If IP is specified, the transport is considered as logstream and default port of 5557 is taken. If collector name is specified, the collector properties are taken from the configured collector. If service is specified, the configured service is assumed as the collector. If vserver is specified, the services bound to it are considered as collectors and the records are load balanced.<br/>Minimum length =  1
		"""
		try :
			self._collectors = collectors
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""This option indicates what information needs to be collected and exported.<br/>Possible values = global, webinsight, tcpinsight, securityinsight, videoinsight, hdxinsight, gatewayinsight, httpstream, lsninsight.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""This option indicates what information needs to be collected and exported.<br/>Possible values = global, webinsight, tcpinsight, securityinsight, videoinsight, hdxinsight, gatewayinsight, httpstream, lsninsight
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def httpclientsidemeasurements(self) :
		r"""On enabling this option, the Citrix ADC will insert a javascript into the HTTP response to collect the client side page-timings and will send the same to the configured collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpclientsidemeasurements
		except Exception as e:
			raise e

	@httpclientsidemeasurements.setter
	def httpclientsidemeasurements(self, httpclientsidemeasurements) :
		r"""On enabling this option, the Citrix ADC will insert a javascript into the HTTP response to collect the client side page-timings and will send the same to the configured collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpclientsidemeasurements = httpclientsidemeasurements
		except Exception as e:
			raise e

	@property
	def httppagetracking(self) :
		r"""On enabling this option, the Citrix ADC will link the embedded objects of a page together.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httppagetracking
		except Exception as e:
			raise e

	@httppagetracking.setter
	def httppagetracking(self, httppagetracking) :
		r"""On enabling this option, the Citrix ADC will link the embedded objects of a page together.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httppagetracking = httppagetracking
		except Exception as e:
			raise e

	@property
	def httpurl(self) :
		r"""On enabling this option, the Citrix ADC will log the URL in appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpurl
		except Exception as e:
			raise e

	@httpurl.setter
	def httpurl(self, httpurl) :
		r"""On enabling this option, the Citrix ADC will log the URL in appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpurl = httpurl
		except Exception as e:
			raise e

	@property
	def httphost(self) :
		r"""On enabling this option, the Citrix ADC will log the Host header in appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httphost
		except Exception as e:
			raise e

	@httphost.setter
	def httphost(self, httphost) :
		r"""On enabling this option, the Citrix ADC will log the Host header in appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httphost = httphost
		except Exception as e:
			raise e

	@property
	def httpmethod(self) :
		r"""On enabling this option, the Citrix ADC will log the method header in appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpmethod
		except Exception as e:
			raise e

	@httpmethod.setter
	def httpmethod(self, httpmethod) :
		r"""On enabling this option, the Citrix ADC will log the method header in appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpmethod = httpmethod
		except Exception as e:
			raise e

	@property
	def httpreferer(self) :
		r"""On enabling this option, the Citrix ADC will log the referer header in appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpreferer
		except Exception as e:
			raise e

	@httpreferer.setter
	def httpreferer(self, httpreferer) :
		r"""On enabling this option, the Citrix ADC will log the referer header in appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpreferer = httpreferer
		except Exception as e:
			raise e

	@property
	def httpuseragent(self) :
		r"""On enabling this option, the Citrix ADC will log User-Agent header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpuseragent
		except Exception as e:
			raise e

	@httpuseragent.setter
	def httpuseragent(self, httpuseragent) :
		r"""On enabling this option, the Citrix ADC will log User-Agent header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpuseragent = httpuseragent
		except Exception as e:
			raise e

	@property
	def httpcookie(self) :
		r"""On enabling this option, the Citrix ADC will log cookie header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpcookie
		except Exception as e:
			raise e

	@httpcookie.setter
	def httpcookie(self, httpcookie) :
		r"""On enabling this option, the Citrix ADC will log cookie header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpcookie = httpcookie
		except Exception as e:
			raise e

	@property
	def httplocation(self) :
		r"""On enabling this option, the Citrix ADC will log location header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httplocation
		except Exception as e:
			raise e

	@httplocation.setter
	def httplocation(self, httplocation) :
		r"""On enabling this option, the Citrix ADC will log location header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httplocation = httplocation
		except Exception as e:
			raise e

	@property
	def urlcategory(self) :
		r"""On enabling this option, the Citrix ADC will send the URL category record.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._urlcategory
		except Exception as e:
			raise e

	@urlcategory.setter
	def urlcategory(self, urlcategory) :
		r"""On enabling this option, the Citrix ADC will send the URL category record.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._urlcategory = urlcategory
		except Exception as e:
			raise e

	@property
	def httpcontenttype(self) :
		r"""On enabling this option, the Citrix ADC will log content-length header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpcontenttype
		except Exception as e:
			raise e

	@httpcontenttype.setter
	def httpcontenttype(self, httpcontenttype) :
		r"""On enabling this option, the Citrix ADC will log content-length header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpcontenttype = httpcontenttype
		except Exception as e:
			raise e

	@property
	def httpauthentication(self) :
		r"""On enabling this option, the Citrix ADC will log Authentication header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpauthentication
		except Exception as e:
			raise e

	@httpauthentication.setter
	def httpauthentication(self, httpauthentication) :
		r"""On enabling this option, the Citrix ADC will log Authentication header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpauthentication = httpauthentication
		except Exception as e:
			raise e

	@property
	def httpvia(self) :
		r"""On enabling this option, the Citrix ADC will Via header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpvia
		except Exception as e:
			raise e

	@httpvia.setter
	def httpvia(self, httpvia) :
		r"""On enabling this option, the Citrix ADC will Via header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpvia = httpvia
		except Exception as e:
			raise e

	@property
	def httpxforwardedforheader(self) :
		r"""On enabling this option, the Citrix ADC will log X-Forwarded-For header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpxforwardedforheader
		except Exception as e:
			raise e

	@httpxforwardedforheader.setter
	def httpxforwardedforheader(self, httpxforwardedforheader) :
		r"""On enabling this option, the Citrix ADC will log X-Forwarded-For header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpxforwardedforheader = httpxforwardedforheader
		except Exception as e:
			raise e

	@property
	def httpsetcookie(self) :
		r"""On enabling this option, the Citrix ADC will log set-cookie header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpsetcookie
		except Exception as e:
			raise e

	@httpsetcookie.setter
	def httpsetcookie(self, httpsetcookie) :
		r"""On enabling this option, the Citrix ADC will log set-cookie header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpsetcookie = httpsetcookie
		except Exception as e:
			raise e

	@property
	def httpsetcookie2(self) :
		r"""On enabling this option, the Citrix ADC will log set-cookie2 header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpsetcookie2
		except Exception as e:
			raise e

	@httpsetcookie2.setter
	def httpsetcookie2(self, httpsetcookie2) :
		r"""On enabling this option, the Citrix ADC will log set-cookie2 header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpsetcookie2 = httpsetcookie2
		except Exception as e:
			raise e

	@property
	def httpdomainname(self) :
		r"""On enabling this option, the Citrix ADC will log domain name.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpdomainname
		except Exception as e:
			raise e

	@httpdomainname.setter
	def httpdomainname(self, httpdomainname) :
		r"""On enabling this option, the Citrix ADC will log domain name.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpdomainname = httpdomainname
		except Exception as e:
			raise e

	@property
	def httpurlquery(self) :
		r"""On enabling this option, the Citrix ADC will log URL Query.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpurlquery
		except Exception as e:
			raise e

	@httpurlquery.setter
	def httpurlquery(self, httpurlquery) :
		r"""On enabling this option, the Citrix ADC will log URL Query.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpurlquery = httpurlquery
		except Exception as e:
			raise e

	@property
	def tcpburstreporting(self) :
		r"""On enabling this option, the Citrix ADC will log TCP burst parameters.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tcpburstreporting
		except Exception as e:
			raise e

	@tcpburstreporting.setter
	def tcpburstreporting(self, tcpburstreporting) :
		r"""On enabling this option, the Citrix ADC will log TCP burst parameters.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tcpburstreporting = tcpburstreporting
		except Exception as e:
			raise e

	@property
	def cqareporting(self) :
		r"""On enabling this option, the Citrix ADC will log TCP CQA parameters.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cqareporting
		except Exception as e:
			raise e

	@cqareporting.setter
	def cqareporting(self, cqareporting) :
		r"""On enabling this option, the Citrix ADC will log TCP CQA parameters.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cqareporting = cqareporting
		except Exception as e:
			raise e

	@property
	def integratedcache(self) :
		r"""On enabling this option, the Citrix ADC will log the Integrated Caching appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._integratedcache
		except Exception as e:
			raise e

	@integratedcache.setter
	def integratedcache(self, integratedcache) :
		r"""On enabling this option, the Citrix ADC will log the Integrated Caching appflow records.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._integratedcache = integratedcache
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
	def refcnt(self) :
		r"""The number of references to the profile.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(analyticsprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.analyticsprofile
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
		r""" Use this API to add analyticsprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = analyticsprofile()
				addresource.name = resource.name
				addresource.collectors = resource.collectors
				addresource.type = resource.type
				addresource.httpclientsidemeasurements = resource.httpclientsidemeasurements
				addresource.httppagetracking = resource.httppagetracking
				addresource.httpurl = resource.httpurl
				addresource.httphost = resource.httphost
				addresource.httpmethod = resource.httpmethod
				addresource.httpreferer = resource.httpreferer
				addresource.httpuseragent = resource.httpuseragent
				addresource.httpcookie = resource.httpcookie
				addresource.httplocation = resource.httplocation
				addresource.urlcategory = resource.urlcategory
				addresource.httpcontenttype = resource.httpcontenttype
				addresource.httpauthentication = resource.httpauthentication
				addresource.httpvia = resource.httpvia
				addresource.httpxforwardedforheader = resource.httpxforwardedforheader
				addresource.httpsetcookie = resource.httpsetcookie
				addresource.httpsetcookie2 = resource.httpsetcookie2
				addresource.httpdomainname = resource.httpdomainname
				addresource.httpurlquery = resource.httpurlquery
				addresource.tcpburstreporting = resource.tcpburstreporting
				addresource.cqareporting = resource.cqareporting
				addresource.integratedcache = resource.integratedcache
				addresource.feature = resource.feature
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ analyticsprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].collectors = resource[i].collectors
						addresources[i].type = resource[i].type
						addresources[i].httpclientsidemeasurements = resource[i].httpclientsidemeasurements
						addresources[i].httppagetracking = resource[i].httppagetracking
						addresources[i].httpurl = resource[i].httpurl
						addresources[i].httphost = resource[i].httphost
						addresources[i].httpmethod = resource[i].httpmethod
						addresources[i].httpreferer = resource[i].httpreferer
						addresources[i].httpuseragent = resource[i].httpuseragent
						addresources[i].httpcookie = resource[i].httpcookie
						addresources[i].httplocation = resource[i].httplocation
						addresources[i].urlcategory = resource[i].urlcategory
						addresources[i].httpcontenttype = resource[i].httpcontenttype
						addresources[i].httpauthentication = resource[i].httpauthentication
						addresources[i].httpvia = resource[i].httpvia
						addresources[i].httpxforwardedforheader = resource[i].httpxforwardedforheader
						addresources[i].httpsetcookie = resource[i].httpsetcookie
						addresources[i].httpsetcookie2 = resource[i].httpsetcookie2
						addresources[i].httpdomainname = resource[i].httpdomainname
						addresources[i].httpurlquery = resource[i].httpurlquery
						addresources[i].tcpburstreporting = resource[i].tcpburstreporting
						addresources[i].cqareporting = resource[i].cqareporting
						addresources[i].integratedcache = resource[i].integratedcache
						addresources[i].feature = resource[i].feature
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update analyticsprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = analyticsprofile()
				updateresource.name = resource.name
				updateresource.collectors = resource.collectors
				updateresource.httpclientsidemeasurements = resource.httpclientsidemeasurements
				updateresource.httppagetracking = resource.httppagetracking
				updateresource.httpurl = resource.httpurl
				updateresource.httphost = resource.httphost
				updateresource.httpmethod = resource.httpmethod
				updateresource.httpreferer = resource.httpreferer
				updateresource.httpuseragent = resource.httpuseragent
				updateresource.httpcookie = resource.httpcookie
				updateresource.httplocation = resource.httplocation
				updateresource.urlcategory = resource.urlcategory
				updateresource.httpcontenttype = resource.httpcontenttype
				updateresource.httpauthentication = resource.httpauthentication
				updateresource.httpvia = resource.httpvia
				updateresource.httpxforwardedforheader = resource.httpxforwardedforheader
				updateresource.httpsetcookie = resource.httpsetcookie
				updateresource.httpsetcookie2 = resource.httpsetcookie2
				updateresource.httpdomainname = resource.httpdomainname
				updateresource.httpurlquery = resource.httpurlquery
				updateresource.tcpburstreporting = resource.tcpburstreporting
				updateresource.cqareporting = resource.cqareporting
				updateresource.integratedcache = resource.integratedcache
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ analyticsprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].collectors = resource[i].collectors
						updateresources[i].httpclientsidemeasurements = resource[i].httpclientsidemeasurements
						updateresources[i].httppagetracking = resource[i].httppagetracking
						updateresources[i].httpurl = resource[i].httpurl
						updateresources[i].httphost = resource[i].httphost
						updateresources[i].httpmethod = resource[i].httpmethod
						updateresources[i].httpreferer = resource[i].httpreferer
						updateresources[i].httpuseragent = resource[i].httpuseragent
						updateresources[i].httpcookie = resource[i].httpcookie
						updateresources[i].httplocation = resource[i].httplocation
						updateresources[i].urlcategory = resource[i].urlcategory
						updateresources[i].httpcontenttype = resource[i].httpcontenttype
						updateresources[i].httpauthentication = resource[i].httpauthentication
						updateresources[i].httpvia = resource[i].httpvia
						updateresources[i].httpxforwardedforheader = resource[i].httpxforwardedforheader
						updateresources[i].httpsetcookie = resource[i].httpsetcookie
						updateresources[i].httpsetcookie2 = resource[i].httpsetcookie2
						updateresources[i].httpdomainname = resource[i].httpdomainname
						updateresources[i].httpurlquery = resource[i].httpurlquery
						updateresources[i].tcpburstreporting = resource[i].tcpburstreporting
						updateresources[i].cqareporting = resource[i].cqareporting
						updateresources[i].integratedcache = resource[i].integratedcache
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of analyticsprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = analyticsprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ analyticsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ analyticsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete analyticsprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = analyticsprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ analyticsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ analyticsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the analyticsprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = analyticsprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = analyticsprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [analyticsprofile() for _ in range(len(name))]
						obj = [analyticsprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = analyticsprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of analyticsprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = analyticsprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the analyticsprofile resources configured on NetScaler.
		"""
		try :
			obj = analyticsprofile()
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
		r""" Use this API to count filtered the set of analyticsprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = analyticsprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Httpurlquery:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpreferer:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpmethod:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httplocation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cqareporting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httppagetracking:
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

	class Tcpburstreporting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpsetcookie2:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Integratedcache:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpauthentication:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Urlcategory:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpdomainname:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpxforwardedforheader:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpcontenttype:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpurl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpcookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpclientsidemeasurements:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Type:
		GLOBAL = "global"
		webinsight = "webinsight"
		tcpinsight = "tcpinsight"
		securityinsight = "securityinsight"
		videoinsight = "videoinsight"
		hdxinsight = "hdxinsight"
		gatewayinsight = "gatewayinsight"
		httpstream = "httpstream"
		lsninsight = "lsninsight"

	class Httpuseragent:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httphost:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class analyticsprofile_response(base_response) :
	def __init__(self, length=1) :
		self.analyticsprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.analyticsprofile = [analyticsprofile() for _ in range(length)]

