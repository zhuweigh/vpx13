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

class authenticationlocalpolicy_authenticationvserver_binding(base_resource) :
	""" Binding class showing the authenticationvserver that can be bound to authenticationlocalpolicy.
	"""
	def __init__(self) :
		self._boundto = None
		self._priority = None
		self._activepolicy = None
		self._name = None
		self.___count = None

	@property
	def boundto(self) :
		r"""The entity name to which policy is bound.
		"""
		try :
			return self._boundto
		except Exception as e:
			raise e

	@boundto.setter
	def boundto(self, boundto) :
		r"""The entity name to which policy is bound.
		"""
		try :
			self._boundto = boundto
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the local authentication policy.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the local authentication policy.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def priority(self) :
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def activepolicy(self) :
		try :
			return self._activepolicy
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationlocalpolicy_authenticationvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationlocalpolicy_authenticationvserver_binding
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
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch authenticationlocalpolicy_authenticationvserver_binding resources.
		"""
		try :
			if not name :
				obj = authenticationlocalpolicy_authenticationvserver_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = authenticationlocalpolicy_authenticationvserver_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of authenticationlocalpolicy_authenticationvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationlocalpolicy_authenticationvserver_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count authenticationlocalpolicy_authenticationvserver_binding resources configued on NetScaler.
		"""
		try :
			obj = authenticationlocalpolicy_authenticationvserver_binding()
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
		r""" Use this API to count the filtered set of authenticationlocalpolicy_authenticationvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationlocalpolicy_authenticationvserver_binding()
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

class authenticationlocalpolicy_authenticationvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationlocalpolicy_authenticationvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationlocalpolicy_authenticationvserver_binding = [authenticationlocalpolicy_authenticationvserver_binding() for _ in range(length)]

