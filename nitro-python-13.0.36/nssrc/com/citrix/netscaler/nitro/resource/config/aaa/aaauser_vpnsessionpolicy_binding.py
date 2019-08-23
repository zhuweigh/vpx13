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

class aaauser_vpnsessionpolicy_binding(base_resource) :
	""" Binding class showing the vpnsessionpolicy that can be bound to aaauser.
	"""
	def __init__(self) :
		self._policy = None
		self._priority = None
		self._acttype = None
		self._gotopriorityexpression = None
		self._username = None
		self._type = None
		self.___count = None

	@property
	def priority(self) :
		r"""Integer specifying the priority of the policy.  A lower number indicates a higher priority. Policies are evaluated in the order of their priority numbers. Maximum value for default syntax policies is 2147483647 and for classic policies max priority is 64000. .<br/>Minimum value =  0<br/>Maximum value =  2147483647.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""Integer specifying the priority of the policy.  A lower number indicates a higher priority. Policies are evaluated in the order of their priority numbers. Maximum value for default syntax policies is 2147483647 and for classic policies max priority is 64000. .<br/>Minimum value =  0<br/>Maximum value =  2147483647
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def username(self) :
		r"""User account to which to bind the policy.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		r"""User account to which to bind the policy.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		r"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		r"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def policy(self) :
		r"""The policy Name.
		"""
		try :
			return self._policy
		except Exception as e:
			raise e

	@policy.setter
	def policy(self, policy) :
		r"""The policy Name.
		"""
		try :
			self._policy = policy
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Bindpoint to which the policy is bound.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Bindpoint to which the policy is bound.
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def acttype(self) :
		try :
			return self._acttype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaauser_vpnsessionpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaauser_vpnsessionpolicy_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.username is not None :
				return str(self.username)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = aaauser_vpnsessionpolicy_binding()
				updateresource.username = resource.username
				updateresource.policy = resource.policy
				updateresource.priority = resource.priority
				updateresource.type = resource.type
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [aaauser_vpnsessionpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].username = resource[i].username
						updateresources[i].policy = resource[i].policy
						updateresources[i].priority = resource[i].priority
						updateresources[i].type = resource[i].type
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = aaauser_vpnsessionpolicy_binding()
				deleteresource.username = resource.username
				deleteresource.policy = resource.policy
				deleteresource.type = resource.type
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [aaauser_vpnsessionpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].username = resource[i].username
						deleteresources[i].policy = resource[i].policy
						deleteresources[i].type = resource[i].type
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, username="", option_="") :
		r""" Use this API to fetch aaauser_vpnsessionpolicy_binding resources.
		"""
		try :
			if not username :
				obj = aaauser_vpnsessionpolicy_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = aaauser_vpnsessionpolicy_binding()
				obj.username = username
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, username, filter_) :
		r""" Use this API to fetch filtered set of aaauser_vpnsessionpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaauser_vpnsessionpolicy_binding()
			obj.username = username
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, username) :
		r""" Use this API to count aaauser_vpnsessionpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = aaauser_vpnsessionpolicy_binding()
			obj.username = username
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, username, filter_) :
		r""" Use this API to count the filtered set of aaauser_vpnsessionpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaauser_vpnsessionpolicy_binding()
			obj.username = username
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Type:
		REQUEST = "REQUEST"
		UDP_REQUEST = "UDP_REQUEST"
		DNS_REQUEST = "DNS_REQUEST"
		ICMP_REQUEST = "ICMP_REQUEST"

class aaauser_vpnsessionpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.aaauser_vpnsessionpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaauser_vpnsessionpolicy_binding = [aaauser_vpnsessionpolicy_binding() for _ in range(length)]

