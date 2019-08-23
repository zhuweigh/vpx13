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

class lacp(base_resource) :
	""" Configuration for Link aggregation control protocol resource. """
	def __init__(self) :
		self._syspriority = None
		self._ownernode = None
		self._devicename = None
		self._mac = None
		self._flags = None
		self._lacpkey = None
		self._clustersyspriority = None
		self._clustermac = None
		self.___count = None

	@property
	def syspriority(self) :
		r"""Priority number that determines which peer device of an LACP LA channel can have control over the LA channel. This parameter is globally applied to all LACP channels on the Citrix ADC. The lower the number, the higher the priority.<br/>Default value: 32768<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._syspriority
		except Exception as e:
			raise e

	@syspriority.setter
	def syspriority(self, syspriority) :
		r"""Priority number that determines which peer device of an LACP LA channel can have control over the LA channel. This parameter is globally applied to all LACP channels on the Citrix ADC. The lower the number, the higher the priority.<br/>Default value: 32768<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._syspriority = syspriority
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		r"""The owner node in a cluster for which we want to set the lacp priority. Owner node can vary from 0 to 31. Ownernode value of 254 is used for Cluster.<br/>Default value: 255.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		r"""The owner node in a cluster for which we want to set the lacp priority. Owner node can vary from 0 to 31. Ownernode value of 254 is used for Cluster.<br/>Default value: 255
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	@property
	def devicename(self) :
		r"""Name of the channel.
		"""
		try :
			return self._devicename
		except Exception as e:
			raise e

	@property
	def mac(self) :
		r"""LACP system MAC.
		"""
		try :
			return self._mac
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""Flags of this channel.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def lacpkey(self) :
		r"""LACP key of this channel.
		"""
		try :
			return self._lacpkey
		except Exception as e:
			raise e

	@property
	def clustersyspriority(self) :
		r"""LACP system (Cluster) priority.
		"""
		try :
			return self._clustersyspriority
		except Exception as e:
			raise e

	@property
	def clustermac(self) :
		r"""LACP system (Cluster) mac.
		"""
		try :
			return self._clustermac
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lacp_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lacp
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ownernode is not None :
				return str(self.ownernode)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update lacp.
		"""
		try :
			if type(resource) is not list :
				updateresource = lacp()
				updateresource.syspriority = resource.syspriority
				updateresource.ownernode = resource.ownernode
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lacp() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].syspriority = resource[i].syspriority
						updateresources[i].ownernode = resource[i].ownernode
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lacp resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lacp()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = lacp()
					obj.ownernode = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [lacp() for _ in range(len(name))]
						obj = [lacp() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = lacp()
							obj[i].ownernode = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of lacp resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lacp()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the lacp resources configured on NetScaler.
		"""
		try :
			obj = lacp()
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
		r""" Use this API to count filtered the set of lacp resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lacp()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class lacp_response(base_response) :
	def __init__(self, length=1) :
		self.lacp = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lacp = [lacp() for _ in range(length)]

