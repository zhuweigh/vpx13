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

class netbridge_iptunnel_binding(base_resource) :
	""" Binding class showing the iptunnel that can be bound to netbridge.
	"""
	def __init__(self) :
		self._tunnel = None
		self._name = None
		self.___count = None

	@property
	def name(self) :
		r"""The name of the network bridge.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""The name of the network bridge.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def tunnel(self) :
		r"""The name of the tunnel that is a part of this bridge.
		"""
		try :
			return self._tunnel
		except Exception as e:
			raise e

	@tunnel.setter
	def tunnel(self, tunnel) :
		r"""The name of the tunnel that is a part of this bridge.
		"""
		try :
			self._tunnel = tunnel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(netbridge_iptunnel_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.netbridge_iptunnel_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = netbridge_iptunnel_binding()
				updateresource.name = resource.name
				updateresource.tunnel = resource.tunnel
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [netbridge_iptunnel_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].tunnel = resource[i].tunnel
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = netbridge_iptunnel_binding()
				deleteresource.name = resource.name
				deleteresource.tunnel = resource.tunnel
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [netbridge_iptunnel_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].tunnel = resource[i].tunnel
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch netbridge_iptunnel_binding resources.
		"""
		try :
			if not name :
				obj = netbridge_iptunnel_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = netbridge_iptunnel_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of netbridge_iptunnel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = netbridge_iptunnel_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count netbridge_iptunnel_binding resources configued on NetScaler.
		"""
		try :
			obj = netbridge_iptunnel_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		r""" Use this API to count the filtered set of netbridge_iptunnel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = netbridge_iptunnel_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class netbridge_iptunnel_binding_response(base_response) :
	def __init__(self, length=1) :
		self.netbridge_iptunnel_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.netbridge_iptunnel_binding = [netbridge_iptunnel_binding() for _ in range(length)]

