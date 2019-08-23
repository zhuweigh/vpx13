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

class cacheobject(base_resource) :
	""" Configuration for cache object resource. """
	def __init__(self) :
		self._url = None
		self._locator = None
		self._httpstatus = None
		self._host = None
		self._port = None
		self._groupname = None
		self._httpmethod = None
		self._group = None
		self._ignoremarkerobjects = None
		self._includenotreadyobjects = None
		self._nodeid = None
		self._tosecondary = None
		self._cacheressize = None
		self._cachereshdrsize = None
		self._cacheetag = None
		self._httpstatusoutput = None
		self._cachereslastmod = None
		self._cachecontrol = None
		self._cacheresdate = None
		self._contentgroup = None
		self._destipv46 = None
		self._destport = None
		self._cachecellcomplex = None
		self._hitparams = None
		self._hitvalues = None
		self._cachecellreqtime = None
		self._cachecellrestime = None
		self._cachecurage = None
		self._cachecellexpires = None
		self._cachecellexpiresmillisec = None
		self._flushed = None
		self._prefetch = None
		self._prefetchperiod = None
		self._prefetchperiodmillisec = None
		self._cachecellcurreaders = None
		self._cachecellcurmisses = None
		self._cachecellhits = None
		self._cachecellmisses = None
		self._cachecelldhits = None
		self._cachecellcompressionformat = None
		self._cachecellappfwmetadataexists = None
		self._cachecellhttp11 = None
		self._cachecellweaketag = None
		self._cachecellresbadsize = None
		self._markerreason = None
		self._cachecellpolleverytime = None
		self._cachecelletaginserted = None
		self._cachecellreadywithlastbyte = None
		self._cacheinmemory = None
		self._cacheindisk = None
		self._cacheinsecondary = None
		self._cachedirname = None
		self._cachefilename = None
		self._cachecelldestipverified = None
		self._cachecellfwpxyobj = None
		self._cachecellbasefile = None
		self._cachecellminhitflag = None
		self._cachecellminhit = None
		self._policy = None
		self._policyname = None
		self._selectorname = None
		self._rule = None
		self._selectorvalue = None
		self._cacheurls = None
		self._warnbucketskip = None
		self._totalobjs = None
		self._httpcalloutcell = None
		self._httpcalloutname = None
		self._returntype = None
		self._httpcalloutresult = None
		self._locatorshow = None
		self._ceflags = None
		self.___count = None

	@property
	def url(self) :
		r"""URL of the particular object whose details is required. Parameter "host" must be specified along with the URL.<br/>Minimum length =  1.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		r"""URL of the particular object whose details is required. Parameter "host" must be specified along with the URL.<br/>Minimum length =  1
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def locator(self) :
		r"""ID of the cached object.
		"""
		try :
			return self._locator
		except Exception as e:
			raise e

	@locator.setter
	def locator(self, locator) :
		r"""ID of the cached object.
		"""
		try :
			self._locator = locator
		except Exception as e:
			raise e

	@property
	def httpstatus(self) :
		r"""HTTP status of the object.
		"""
		try :
			return self._httpstatus
		except Exception as e:
			raise e

	@httpstatus.setter
	def httpstatus(self, httpstatus) :
		r"""HTTP status of the object.
		"""
		try :
			self._httpstatus = httpstatus
		except Exception as e:
			raise e

	@property
	def host(self) :
		r"""Host name of the object. Parameter "url" must be specified.<br/>Minimum length =  1.
		"""
		try :
			return self._host
		except Exception as e:
			raise e

	@host.setter
	def host(self, host) :
		r"""Host name of the object. Parameter "url" must be specified.<br/>Minimum length =  1
		"""
		try :
			self._host = host
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Host port of the object. You must also set the Host parameter.<br/>Default value: 80<br/>Minimum length =  1.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Host port of the object. You must also set the Host parameter.<br/>Default value: 80<br/>Minimum length =  1
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def groupname(self) :
		r"""Name of the content group to which the object belongs. It will display only the objects belonging to the specified content group. You must also set the Host parameter.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		r"""Name of the content group to which the object belongs. It will display only the objects belonging to the specified content group. You must also set the Host parameter.
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def httpmethod(self) :
		r"""HTTP request method that caused the object to be stored.<br/>Default value: GET<br/>Possible values = GET, POST.
		"""
		try :
			return self._httpmethod
		except Exception as e:
			raise e

	@httpmethod.setter
	def httpmethod(self, httpmethod) :
		r"""HTTP request method that caused the object to be stored.<br/>Default value: GET<br/>Possible values = GET, POST
		"""
		try :
			self._httpmethod = httpmethod
		except Exception as e:
			raise e

	@property
	def group(self) :
		r"""Name of the content group whose objects should be listed.
		"""
		try :
			return self._group
		except Exception as e:
			raise e

	@group.setter
	def group(self, group) :
		r"""Name of the content group whose objects should be listed.
		"""
		try :
			self._group = group
		except Exception as e:
			raise e

	@property
	def ignoremarkerobjects(self) :
		r"""Ignore marker objects. Marker objects are created when a response exceeds the maximum or minimum response size for the content group or has not yet received the minimum number of hits for the content group.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._ignoremarkerobjects
		except Exception as e:
			raise e

	@ignoremarkerobjects.setter
	def ignoremarkerobjects(self, ignoremarkerobjects) :
		r"""Ignore marker objects. Marker objects are created when a response exceeds the maximum or minimum response size for the content group or has not yet received the minimum number of hits for the content group.<br/>Possible values = ON, OFF
		"""
		try :
			self._ignoremarkerobjects = ignoremarkerobjects
		except Exception as e:
			raise e

	@property
	def includenotreadyobjects(self) :
		r"""Include responses that have not yet reached a minimum number of hits before being cached.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._includenotreadyobjects
		except Exception as e:
			raise e

	@includenotreadyobjects.setter
	def includenotreadyobjects(self, includenotreadyobjects) :
		r"""Include responses that have not yet reached a minimum number of hits before being cached.<br/>Possible values = ON, OFF
		"""
		try :
			self._includenotreadyobjects = includenotreadyobjects
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def tosecondary(self) :
		r"""Object will be saved onto Secondary.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._tosecondary
		except Exception as e:
			raise e

	@tosecondary.setter
	def tosecondary(self, tosecondary) :
		r"""Object will be saved onto Secondary.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._tosecondary = tosecondary
		except Exception as e:
			raise e

	@property
	def cacheressize(self) :
		r"""Cache response size of the object.
		"""
		try :
			return self._cacheressize
		except Exception as e:
			raise e

	@property
	def cachereshdrsize(self) :
		r"""Cache response header size of the object.
		"""
		try :
			return self._cachereshdrsize
		except Exception as e:
			raise e

	@property
	def cacheetag(self) :
		r"""Cache ETag of the object.
		"""
		try :
			return self._cacheetag
		except Exception as e:
			raise e

	@property
	def httpstatusoutput(self) :
		r"""HTTP status of the object.
		"""
		try :
			return self._httpstatusoutput
		except Exception as e:
			raise e

	@property
	def cachereslastmod(self) :
		r"""Value of "Last-modified" header.
		"""
		try :
			return self._cachereslastmod
		except Exception as e:
			raise e

	@property
	def cachecontrol(self) :
		r"""Cache-Control header of the object.
		"""
		try :
			return self._cachecontrol
		except Exception as e:
			raise e

	@property
	def cacheresdate(self) :
		r"""Value of "Date" header.
		"""
		try :
			return self._cacheresdate
		except Exception as e:
			raise e

	@property
	def contentgroup(self) :
		r"""Name of the contentgroup in which it is stored.
		"""
		try :
			return self._contentgroup
		except Exception as e:
			raise e

	@property
	def destipv46(self) :
		r"""Destination IP.
		"""
		try :
			return self._destipv46
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""Destination Port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@property
	def cachecellcomplex(self) :
		r"""The state of the parameterized caching on this cell.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellcomplex
		except Exception as e:
			raise e

	@property
	def hitparams(self) :
		r"""Parameterized hit evaluation of an object.
		"""
		try :
			return self._hitparams
		except Exception as e:
			raise e

	@property
	def hitvalues(self) :
		r"""Values of hitparams for this object.
		"""
		try :
			return self._hitvalues
		except Exception as e:
			raise e

	@property
	def cachecellreqtime(self) :
		r"""Required time of the cache cell object.
		"""
		try :
			return self._cachecellreqtime
		except Exception as e:
			raise e

	@property
	def cachecellrestime(self) :
		r"""Response time to the cache cell object.
		"""
		try :
			return self._cachecellrestime
		except Exception as e:
			raise e

	@property
	def cachecurage(self) :
		r"""Current age of the cache object.
		"""
		try :
			return self._cachecurage
		except Exception as e:
			raise e

	@property
	def cachecellexpires(self) :
		r"""Expiry time of the cache cell object in seconds.
		"""
		try :
			return self._cachecellexpires
		except Exception as e:
			raise e

	@property
	def cachecellexpiresmillisec(self) :
		r"""Expiry time of the cache cell object in milliseconds.
		"""
		try :
			return self._cachecellexpiresmillisec
		except Exception as e:
			raise e

	@property
	def flushed(self) :
		r"""Specifies whether the object is flushed.<br/>Possible values = YES, NO.
		"""
		try :
			return self._flushed
		except Exception as e:
			raise e

	@property
	def prefetch(self) :
		r"""Specifies whether Integrated Cache should attempt to refresh an object immediately before it goes stale.<br/>Possible values = YES, NO.
		"""
		try :
			return self._prefetch
		except Exception as e:
			raise e

	@property
	def prefetchperiod(self) :
		r"""The duration in seconds of the period during which prefetch should be attempted, immediately before the object's calculated expiry time.
		"""
		try :
			return self._prefetchperiod
		except Exception as e:
			raise e

	@property
	def prefetchperiodmillisec(self) :
		r"""The duration in milliseconds of the period during which prefetch should be attempted, immediately before the object's calculated expiry time.
		"""
		try :
			return self._prefetchperiodmillisec
		except Exception as e:
			raise e

	@property
	def cachecellcurreaders(self) :
		r"""Current readers of the cache cell object.
		"""
		try :
			return self._cachecellcurreaders
		except Exception as e:
			raise e

	@property
	def cachecellcurmisses(self) :
		r"""Current misses of the cache cell object.
		"""
		try :
			return self._cachecellcurmisses
		except Exception as e:
			raise e

	@property
	def cachecellhits(self) :
		r"""Cache cell hits.
		"""
		try :
			return self._cachecellhits
		except Exception as e:
			raise e

	@property
	def cachecellmisses(self) :
		r"""Cache cell misses.
		"""
		try :
			return self._cachecellmisses
		except Exception as e:
			raise e

	@property
	def cachecelldhits(self) :
		r"""Cache cell disk hits.
		"""
		try :
			return self._cachecelldhits
		except Exception as e:
			raise e

	@property
	def cachecellcompressionformat(self) :
		r"""Compression format of this object. Identity means not compressed.
		"""
		try :
			return self._cachecellcompressionformat
		except Exception as e:
			raise e

	@property
	def cachecellappfwmetadataexists(self) :
		r"""AppFirewall cache object.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellappfwmetadataexists
		except Exception as e:
			raise e

	@property
	def cachecellhttp11(self) :
		r"""The state of the response to be HTTP/1.1.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellhttp11
		except Exception as e:
			raise e

	@property
	def cachecellweaketag(self) :
		r"""The state of the weak HTTP Entity Tag in the cell.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellweaketag
		except Exception as e:
			raise e

	@property
	def cachecellresbadsize(self) :
		r"""The marked state of the cell.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellresbadsize
		except Exception as e:
			raise e

	@property
	def markerreason(self) :
		r"""Reason for marking the cell.<br/>Possible values = Waiting for min hit, Response header is too big, Content-length header said response size is not in group size limit, Content-length response received more data, Content-length response received less data, Content-length response data is not in group size limit, Chunk response received more data, Chunk response data is not in group size limit, Bad chunk format, Fin terminated response data is not in group size limit.
		"""
		try :
			return self._markerreason
		except Exception as e:
			raise e

	@property
	def cachecellpolleverytime(self) :
		r"""The state to poll every time on object.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellpolleverytime
		except Exception as e:
			raise e

	@property
	def cachecelletaginserted(self) :
		r"""The state of the ETag to be inserted by IC for this object.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecelletaginserted
		except Exception as e:
			raise e

	@property
	def cachecellreadywithlastbyte(self) :
		r"""The state of the complete arrived response.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellreadywithlastbyte
		except Exception as e:
			raise e

	@property
	def cacheinmemory(self) :
		r"""The cache data is available in memory.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheinmemory
		except Exception as e:
			raise e

	@property
	def cacheindisk(self) :
		r"""The cache data is available in disk.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheindisk
		except Exception as e:
			raise e

	@property
	def cacheinsecondary(self) :
		r"""The cache data is available in secondary in HA deployment.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheinsecondary
		except Exception as e:
			raise e

	@property
	def cachedirname(self) :
		r"""The directory name used if saved.
		"""
		try :
			return self._cachedirname
		except Exception as e:
			raise e

	@property
	def cachefilename(self) :
		r"""The filename used if saved.
		"""
		try :
			return self._cachefilename
		except Exception as e:
			raise e

	@property
	def cachecelldestipverified(self) :
		r"""The state of DNS verification.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecelldestipverified
		except Exception as e:
			raise e

	@property
	def cachecellfwpxyobj(self) :
		r"""The state of the object to be stored on a request to a forward proxy.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellfwpxyobj
		except Exception as e:
			raise e

	@property
	def cachecellbasefile(self) :
		r"""The state of delta being used as a basefile.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellbasefile
		except Exception as e:
			raise e

	@property
	def cachecellminhitflag(self) :
		r"""The state of the minhit feature on this cell.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachecellminhitflag
		except Exception as e:
			raise e

	@property
	def cachecellminhit(self) :
		r"""Min hit value for the object.
		"""
		try :
			return self._cachecellminhit
		except Exception as e:
			raise e

	@property
	def policy(self) :
		r"""Policy info for the object.
		"""
		try :
			return self._policy
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		r"""Policy which created the object.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@property
	def selectorname(self) :
		r"""The hit selector for the object.
		"""
		try :
			return self._selectorname
		except Exception as e:
			raise e

	@property
	def rule(self) :
		r"""Selectors for this object.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@property
	def selectorvalue(self) :
		r"""The HTTP request method that caused the object to be stored.
		"""
		try :
			return self._selectorvalue
		except Exception as e:
			raise e

	@property
	def cacheurls(self) :
		r"""List of cache object URLs.
		"""
		try :
			return self._cacheurls
		except Exception as e:
			raise e

	@property
	def warnbucketskip(self) :
		r"""Bucket skipped warning.
		"""
		try :
			return self._warnbucketskip
		except Exception as e:
			raise e

	@property
	def totalobjs(self) :
		r"""Total objects.
		"""
		try :
			return self._totalobjs
		except Exception as e:
			raise e

	@property
	def httpcalloutcell(self) :
		r"""Is it a http callout cell ?.<br/>Possible values = YES, NO.
		"""
		try :
			return self._httpcalloutcell
		except Exception as e:
			raise e

	@property
	def httpcalloutname(self) :
		r"""Name of the http callout.
		"""
		try :
			return self._httpcalloutname
		except Exception as e:
			raise e

	@property
	def returntype(self) :
		r"""Return type of the http callout.<br/>Possible values = BOOL, NUM, TEXT.
		"""
		try :
			return self._returntype
		except Exception as e:
			raise e

	@property
	def httpcalloutresult(self) :
		r"""First few bytes of http callout response.
		"""
		try :
			return self._httpcalloutresult
		except Exception as e:
			raise e

	@property
	def locatorshow(self) :
		r"""ID of the cached object.
		"""
		try :
			return self._locatorshow
		except Exception as e:
			raise e

	@property
	def ceflags(self) :
		r"""Indicates state and type of cached cell.
		"""
		try :
			return self._ceflags
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cacheobject_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cacheobject
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
	def expire(cls, client, resource) :
		r""" Use this API to expire cacheobject.
		"""
		try :
			if type(resource) is not list :
				expireresource = cacheobject()
				expireresource.locator = resource.locator
				expireresource.url = resource.url
				expireresource.host = resource.host
				expireresource.port = resource.port
				expireresource.groupname = resource.groupname
				expireresource.httpmethod = resource.httpmethod
				return expireresource.perform_operation(client,"expire")
			else :
				if (resource and len(resource) > 0) :
					expireresources = [ cacheobject() for _ in range(len(resource))]
					for i in range(len(resource)) :
						expireresources[i].locator = resource[i].locator
						expireresources[i].url = resource[i].url
						expireresources[i].host = resource[i].host
						expireresources[i].port = resource[i].port
						expireresources[i].groupname = resource[i].groupname
						expireresources[i].httpmethod = resource[i].httpmethod
				result = cls.perform_operation_bulk_request(client, expireresources,"expire")
			return result
		except Exception as e :
			raise e

	@classmethod
	def flush(cls, client, resource) :
		r""" Use this API to flush cacheobject.
		"""
		try :
			if type(resource) is not list :
				flushresource = cacheobject()
				flushresource.locator = resource.locator
				flushresource.url = resource.url
				flushresource.host = resource.host
				flushresource.port = resource.port
				flushresource.groupname = resource.groupname
				flushresource.httpmethod = resource.httpmethod
				return flushresource.perform_operation(client,"flush")
			else :
				if (resource and len(resource) > 0) :
					flushresources = [ cacheobject() for _ in range(len(resource))]
					for i in range(len(resource)) :
						flushresources[i].locator = resource[i].locator
						flushresources[i].url = resource[i].url
						flushresources[i].host = resource[i].host
						flushresources[i].port = resource[i].port
						flushresources[i].groupname = resource[i].groupname
						flushresources[i].httpmethod = resource[i].httpmethod
				result = cls.perform_operation_bulk_request(client, flushresources,"flush")
			return result
		except Exception as e :
			raise e

	@classmethod
	def save(cls, client, resource) :
		r""" Use this API to save cacheobject.
		"""
		try :
			if type(resource) is not list :
				saveresource = cacheobject()
				saveresource.locator = resource.locator
				saveresource.tosecondary = resource.tosecondary
				return saveresource.perform_operation(client,"save")
			else :
				if (resource and len(resource) > 0) :
					saveresources = [ cacheobject() for _ in range(len(resource))]
					for i in range(len(resource)) :
						saveresources[i].locator = resource[i].locator
						saveresources[i].tosecondary = resource[i].tosecondary
				result = cls.perform_operation_bulk_request(client, saveresources,"save")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the cacheobject resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cacheobject()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the cacheobject resources that are configured on netscaler.
	# This uses cacheobject_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = cacheobject()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of cacheobject resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cacheobject()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the cacheobject resources configured on NetScaler.
		"""
		try :
			obj = cacheobject()
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
		r""" Use this API to count filtered the set of cacheobject resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cacheobject()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Cachecellfwpxyobj:
		YES = "YES"
		NO = "NO"

	class Tosecondary:
		YES = "YES"
		NO = "NO"

	class Cachecellbasefile:
		YES = "YES"
		NO = "NO"

	class Cachecellcomplex:
		YES = "YES"
		NO = "NO"

	class Cachecellweaketag:
		YES = "YES"
		NO = "NO"

	class Ignoremarkerobjects:
		ON = "ON"
		OFF = "OFF"

	class Cachecellreadywithlastbyte:
		YES = "YES"
		NO = "NO"

	class Flushed:
		YES = "YES"
		NO = "NO"

	class Cachecelldestipverified:
		YES = "YES"
		NO = "NO"

	class Cachecellhttp11:
		YES = "YES"
		NO = "NO"

	class Includenotreadyobjects:
		ON = "ON"
		OFF = "OFF"

	class Cachecellminhitflag:
		YES = "YES"
		NO = "NO"

	class Cacheindisk:
		YES = "YES"
		NO = "NO"

	class Markerreason:
		Waiting_for_min_hit = "Waiting for min hit"
		Response_header_is_too_big = "Response header is too big"
		Content_length_header_said_response_size_is_not_in_group_size_limit = "Content-length header said response size is not in group size limit"
		Content_length_response_received_more_data = "Content-length response received more data"
		Content_length_response_received_less_data = "Content-length response received less data"
		Content_length_response_data_is_not_in_group_size_limit = "Content-length response data is not in group size limit"
		Chunk_response_received_more_data = "Chunk response received more data"
		Chunk_response_data_is_not_in_group_size_limit = "Chunk response data is not in group size limit"
		Bad_chunk_format = "Bad chunk format"
		Fin_terminated_response_data_is_not_in_group_size_limit = "Fin terminated response data is not in group size limit"

	class Cachecellpolleverytime:
		YES = "YES"
		NO = "NO"

	class Httpmethod:
		GET = "GET"
		POST = "POST"

	class Returntype:
		BOOL = "BOOL"
		NUM = "NUM"
		TEXT = "TEXT"

	class Httpcalloutcell:
		YES = "YES"
		NO = "NO"

	class Cachecelletaginserted:
		YES = "YES"
		NO = "NO"

	class Cacheinmemory:
		YES = "YES"
		NO = "NO"

	class Cachecellappfwmetadataexists:
		YES = "YES"
		NO = "NO"

	class Cachecellresbadsize:
		YES = "YES"
		NO = "NO"

	class Prefetch:
		YES = "YES"
		NO = "NO"

	class Cacheinsecondary:
		YES = "YES"
		NO = "NO"

class cacheobject_response(base_response) :
	def __init__(self, length=1) :
		self.cacheobject = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cacheobject = [cacheobject() for _ in range(length)]

