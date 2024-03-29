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

class authenticationvserver_cspolicy_binding(base_resource) :
	""" Binding class showing the cspolicy that can be bound to authenticationvserver.
	"""
	def __init__(self) :
		self._policy = None
		self._priority = None
		self._gotopriorityexpression = None
		self._name = None
		self._secondary = None
		self._groupextraction = None
		self._nextfactor = None
		self.___count = None

	@property
	def priority(self) :
		r"""The priority, if any, of the vpn vserver policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""The priority, if any, of the vpn vserver policy.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the authentication virtual server to which to bind the policy.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the authentication virtual server to which to bind the policy.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def nextfactor(self) :
		r"""Applicable only while binding advance authentication policy as classic authentication policy does not support nFactor.
		"""
		try :
			return self._nextfactor
		except Exception as e:
			raise e

	@nextfactor.setter
	def nextfactor(self, nextfactor) :
		r"""Applicable only while binding advance authentication policy as classic authentication policy does not support nFactor
		"""
		try :
			self._nextfactor = nextfactor
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
	def secondary(self) :
		r"""Applicable only while bindind classic authentication policy as advance authentication policy use nFactor.
		"""
		try :
			return self._secondary
		except Exception as e:
			raise e

	@secondary.setter
	def secondary(self, secondary) :
		r"""Applicable only while bindind classic authentication policy as advance authentication policy use nFactor
		"""
		try :
			self._secondary = secondary
		except Exception as e:
			raise e

	@property
	def policy(self) :
		r"""The name of the policy, if any, bound to the authentication vserver.
		"""
		try :
			return self._policy
		except Exception as e:
			raise e

	@policy.setter
	def policy(self, policy) :
		r"""The name of the policy, if any, bound to the authentication vserver.
		"""
		try :
			self._policy = policy
		except Exception as e:
			raise e

	@property
	def groupextraction(self) :
		r"""Applicable only while bindind classic authentication policy as advance authentication policy use nFactor.
		"""
		try :
			return self._groupextraction
		except Exception as e:
			raise e

	@groupextraction.setter
	def groupextraction(self, groupextraction) :
		r"""Applicable only while bindind classic authentication policy as advance authentication policy use nFactor
		"""
		try :
			self._groupextraction = groupextraction
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationvserver_cspolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationvserver_cspolicy_binding
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
				updateresource = authenticationvserver_cspolicy_binding()
				updateresource.name = resource.name
				updateresource.policy = resource.policy
				updateresource.priority = resource.priority
				updateresource.secondary = resource.secondary
				updateresource.groupextraction = resource.groupextraction
				updateresource.nextfactor = resource.nextfactor
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [authenticationvserver_cspolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].policy = resource[i].policy
						updateresources[i].priority = resource[i].priority
						updateresources[i].secondary = resource[i].secondary
						updateresources[i].groupextraction = resource[i].groupextraction
						updateresources[i].nextfactor = resource[i].nextfactor
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = authenticationvserver_cspolicy_binding()
				deleteresource.name = resource.name
				deleteresource.policy = resource.policy
				deleteresource.secondary = resource.secondary
				deleteresource.groupextraction = resource.groupextraction
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [authenticationvserver_cspolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].policy = resource[i].policy
						deleteresources[i].secondary = resource[i].secondary
						deleteresources[i].groupextraction = resource[i].groupextraction
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch authenticationvserver_cspolicy_binding resources.
		"""
		try :
			if not name :
				obj = authenticationvserver_cspolicy_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = authenticationvserver_cspolicy_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of authenticationvserver_cspolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationvserver_cspolicy_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count authenticationvserver_cspolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = authenticationvserver_cspolicy_binding()
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
		r""" Use this API to count the filtered set of authenticationvserver_cspolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationvserver_cspolicy_binding()
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

class authenticationvserver_cspolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationvserver_cspolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationvserver_cspolicy_binding = [authenticationvserver_cspolicy_binding() for _ in range(length)]

