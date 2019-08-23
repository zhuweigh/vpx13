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

class lsnlogprofile(base_resource) :
	""" Configuration for LSN logging Profile resource. """
	def __init__(self) :
		self._logprofilename = None
		self._logsubscrinfo = None
		self._logcompact = None
		self._logipfix = None
		self._analyticsprofile = None
		self._logsessdeletion = None
		self.___count = None

	@property
	def logprofilename(self) :
		r"""The name of the logging Profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._logprofilename
		except Exception as e:
			raise e

	@logprofilename.setter
	def logprofilename(self, logprofilename) :
		r"""The name of the logging Profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._logprofilename = logprofilename
		except Exception as e:
			raise e

	@property
	def logsubscrinfo(self) :
		r"""Subscriber ID information is logged if option is enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logsubscrinfo
		except Exception as e:
			raise e

	@logsubscrinfo.setter
	def logsubscrinfo(self, logsubscrinfo) :
		r"""Subscriber ID information is logged if option is enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logsubscrinfo = logsubscrinfo
		except Exception as e:
			raise e

	@property
	def logcompact(self) :
		r"""Logs in Compact Logging format if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logcompact
		except Exception as e:
			raise e

	@logcompact.setter
	def logcompact(self, logcompact) :
		r"""Logs in Compact Logging format if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logcompact = logcompact
		except Exception as e:
			raise e

	@property
	def logipfix(self) :
		r"""Logs in IPFIX  format if option is enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logipfix
		except Exception as e:
			raise e

	@logipfix.setter
	def logipfix(self, logipfix) :
		r"""Logs in IPFIX  format if option is enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logipfix = logipfix
		except Exception as e:
			raise e

	@property
	def analyticsprofile(self) :
		r"""Name of the Analytics Profile attached to this lsn profile.
		"""
		try :
			return self._analyticsprofile
		except Exception as e:
			raise e

	@analyticsprofile.setter
	def analyticsprofile(self, analyticsprofile) :
		r"""Name of the Analytics Profile attached to this lsn profile.
		"""
		try :
			self._analyticsprofile = analyticsprofile
		except Exception as e:
			raise e

	@property
	def logsessdeletion(self) :
		r"""LSN Session deletion will not be logged if disabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logsessdeletion
		except Exception as e:
			raise e

	@logsessdeletion.setter
	def logsessdeletion(self, logsessdeletion) :
		r"""LSN Session deletion will not be logged if disabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logsessdeletion = logsessdeletion
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnlogprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnlogprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.logprofilename is not None :
				return str(self.logprofilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add lsnlogprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = lsnlogprofile()
				addresource.logprofilename = resource.logprofilename
				addresource.logsubscrinfo = resource.logsubscrinfo
				addresource.logcompact = resource.logcompact
				addresource.logipfix = resource.logipfix
				addresource.analyticsprofile = resource.analyticsprofile
				addresource.logsessdeletion = resource.logsessdeletion
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lsnlogprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].logprofilename = resource[i].logprofilename
						addresources[i].logsubscrinfo = resource[i].logsubscrinfo
						addresources[i].logcompact = resource[i].logcompact
						addresources[i].logipfix = resource[i].logipfix
						addresources[i].analyticsprofile = resource[i].analyticsprofile
						addresources[i].logsessdeletion = resource[i].logsessdeletion
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete lsnlogprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lsnlogprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.logprofilename = resource
				else :
					deleteresource.logprofilename = resource.logprofilename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnlogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].logprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnlogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].logprofilename = resource[i].logprofilename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update lsnlogprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = lsnlogprofile()
				updateresource.logprofilename = resource.logprofilename
				updateresource.logsubscrinfo = resource.logsubscrinfo
				updateresource.logcompact = resource.logcompact
				updateresource.logipfix = resource.logipfix
				updateresource.analyticsprofile = resource.analyticsprofile
				updateresource.logsessdeletion = resource.logsessdeletion
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lsnlogprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].logprofilename = resource[i].logprofilename
						updateresources[i].logsubscrinfo = resource[i].logsubscrinfo
						updateresources[i].logcompact = resource[i].logcompact
						updateresources[i].logipfix = resource[i].logipfix
						updateresources[i].analyticsprofile = resource[i].analyticsprofile
						updateresources[i].logsessdeletion = resource[i].logsessdeletion
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of lsnlogprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lsnlogprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.logprofilename = resource
				else :
					unsetresource.logprofilename = resource.logprofilename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnlogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].logprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnlogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].logprofilename = resource[i].logprofilename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lsnlogprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsnlogprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = lsnlogprofile()
					obj.logprofilename = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [lsnlogprofile() for _ in range(len(name))]
						obj = [lsnlogprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = lsnlogprofile()
							obj[i].logprofilename = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of lsnlogprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnlogprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the lsnlogprofile resources configured on NetScaler.
		"""
		try :
			obj = lsnlogprofile()
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
		r""" Use this API to count filtered the set of lsnlogprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnlogprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Logcompact:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Logipfix:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Logsubscrinfo:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Logsessdeletion:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lsnlogprofile_response(base_response) :
	def __init__(self, length=1) :
		self.lsnlogprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnlogprofile = [lsnlogprofile() for _ in range(length)]

