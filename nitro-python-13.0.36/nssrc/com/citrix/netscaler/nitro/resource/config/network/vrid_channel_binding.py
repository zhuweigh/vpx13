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

class vrid_channel_binding(base_resource) :
	""" Binding class showing the channel that can be bound to vrid.
	"""
	def __init__(self) :
		self._ifnum = None
		self._vlan = None
		self._flags = None
		self._id = None
		self.___count = None

	@property
	def ifnum(self) :
		r"""Interfaces to bind to the VMAC, specified in (slot/port) notation (for example, 1/2).Use spaces to separate multiple entries.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		r"""Interfaces to bind to the VMAC, specified in (slot/port) notation (for example, 1/2).Use spaces to separate multiple entries.
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def id(self) :
		r"""Integer that uniquely identifies the VMAC address. The generic VMAC address is in the form of 00:00:5e:00:01:<VRID>. For example, if you add a VRID with a value of 60 and bind it to an interface, the resulting VMAC address is 00:00:5e:00:01:3c, where 3c is the hexadecimal representation of 60.<br/>Minimum value =  1<br/>Maximum value =  255.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		r"""Integer that uniquely identifies the VMAC address. The generic VMAC address is in the form of 00:00:5e:00:01:<VRID>. For example, if you add a VRID with a value of 60 and bind it to an interface, the resulting VMAC address is 00:00:5e:00:01:3c, where 3c is the hexadecimal representation of 60.<br/>Minimum value =  1<br/>Maximum value =  255
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""Flags.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""The VLAN in which this VRID resides.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vrid_channel_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vrid_channel_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.id is not None :
				return str(self.id)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = vrid_channel_binding()
				updateresource.id = resource.id
				updateresource.ifnum = resource.ifnum
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [vrid_channel_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].ifnum = resource[i].ifnum
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = vrid_channel_binding()
				deleteresource.id = resource.id
				deleteresource.ifnum = resource.ifnum
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [vrid_channel_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].id = resource[i].id
						deleteresources[i].ifnum = resource[i].ifnum
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, id="", option_="") :
		r""" Use this API to fetch vrid_channel_binding resources.
		"""
		try :
			if not id :
				obj = vrid_channel_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = vrid_channel_binding()
				obj.id = id
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, id, filter_) :
		r""" Use this API to fetch filtered set of vrid_channel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vrid_channel_binding()
			obj.id = id
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, id) :
		r""" Use this API to count vrid_channel_binding resources configued on NetScaler.
		"""
		try :
			obj = vrid_channel_binding()
			obj.id = id
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, id, filter_) :
		r""" Use this API to count the filtered set of vrid_channel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vrid_channel_binding()
			obj.id = id
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class vrid_channel_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vrid_channel_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vrid_channel_binding = [vrid_channel_binding() for _ in range(length)]

