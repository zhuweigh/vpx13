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

class hanode_ci_binding(base_resource) :
	""" Binding class showing the ci that can be bound to hanode.
	"""
	def __init__(self) :
		self._enaifaces = None
		self._id = None
		self._routemonitor = None
		self.___count = None

	@property
	def enaifaces(self) :
		r"""Enabled interfaces.
		"""
		try :
			return self._enaifaces
		except Exception as e:
			raise e

	@enaifaces.setter
	def enaifaces(self, enaifaces) :
		r"""Enabled interfaces.
		"""
		try :
			self._enaifaces = enaifaces
		except Exception as e:
			raise e

	@property
	def routemonitor(self) :
		r"""A route that you want the Citrix ADC to monitor in its internal routing table. You can specify an IPv4 address or network, or an IPv6 address or network prefix. If you specify an IPv4 network address or IPv6 network prefix, the appliance monitors any route that matches the network or prefix.<br/>Minimum length =  1.
		"""
		try :
			return self._routemonitor
		except Exception as e:
			raise e

	@routemonitor.setter
	def routemonitor(self, routemonitor) :
		r"""A route that you want the Citrix ADC to monitor in its internal routing table. You can specify an IPv4 address or network, or an IPv6 address or network prefix. If you specify an IPv4 network address or IPv6 network prefix, the appliance monitors any route that matches the network or prefix.<br/>Minimum length =  1
		"""
		try :
			self._routemonitor = routemonitor
		except Exception as e:
			raise e

	@property
	def id(self) :
		r"""Number that uniquely identifies the local node. The ID of the local node is always 0.<br/>Minimum value =  0<br/>Maximum value =  64.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		r"""Number that uniquely identifies the local node. The ID of the local node is always 0.<br/>Minimum value =  0<br/>Maximum value =  64
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(hanode_ci_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.hanode_ci_binding
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
	def get(cls, service, id="", option_="") :
		r""" Use this API to fetch hanode_ci_binding resources.
		"""
		try :
			if not id :
				obj = hanode_ci_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = hanode_ci_binding()
				obj.id = id
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, id, filter_) :
		r""" Use this API to fetch filtered set of hanode_ci_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = hanode_ci_binding()
			obj.id = id
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, id) :
		r""" Use this API to count hanode_ci_binding resources configued on NetScaler.
		"""
		try :
			obj = hanode_ci_binding()
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
		r""" Use this API to count the filtered set of hanode_ci_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = hanode_ci_binding()
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

class hanode_ci_binding_response(base_response) :
	def __init__(self, length=1) :
		self.hanode_ci_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.hanode_ci_binding = [hanode_ci_binding() for _ in range(length)]

