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

class crvserver_rewritepolicy_binding(base_resource) :
	""" Binding class showing the rewritepolicy that can be bound to crvserver.
	"""
	def __init__(self) :
		self._policyname = None
		self._priority = None
		self._gotopriorityexpression = None
		self._bindpoint = None
		self._invoke = None
		self._labeltype = None
		self._labelname = None
		self._name = None
		self._targetvserver = None
		self.___count = None

	@property
	def priority(self) :
		r"""The priority for the policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""The priority for the policy.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def bindpoint(self) :
		r"""The bindpoint to which the policy is bound.<br/>Possible values = REQUEST, RESPONSE, ICA_REQUEST.
		"""
		try :
			return self._bindpoint
		except Exception as e:
			raise e

	@bindpoint.setter
	def bindpoint(self, bindpoint) :
		r"""The bindpoint to which the policy is bound.<br/>Possible values = REQUEST, RESPONSE, ICA_REQUEST
		"""
		try :
			self._bindpoint = bindpoint
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		r"""Policies bound to this vserver.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		r"""Policies bound to this vserver.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		r"""Name of the label invoked.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		r"""Name of the label invoked.
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the cache redirection virtual server to which to bind the cache redirection policy.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the cache redirection virtual server to which to bind the cache redirection policy.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def targetvserver(self) :
		r"""Name of the virtual server to which content is forwarded. Applicable only if the policy is a map policy and the cache redirection virtual server is of type REVERSE.
		"""
		try :
			return self._targetvserver
		except Exception as e:
			raise e

	@targetvserver.setter
	def targetvserver(self, targetvserver) :
		r"""Name of the virtual server to which content is forwarded. Applicable only if the policy is a map policy and the cache redirection virtual server is of type REVERSE.
		"""
		try :
			self._targetvserver = targetvserver
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
	def invoke(self) :
		r"""Invoke flag.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@invoke.setter
	def invoke(self, invoke) :
		r"""Invoke flag.
		"""
		try :
			self._invoke = invoke
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		r"""The invocation type.<br/>Possible values = reqvserver, resvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@labeltype.setter
	def labeltype(self, labeltype) :
		r"""The invocation type.<br/>Possible values = reqvserver, resvserver, policylabel
		"""
		try :
			self._labeltype = labeltype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(crvserver_rewritepolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.crvserver_rewritepolicy_binding
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
				updateresource = crvserver_rewritepolicy_binding()
				updateresource.name = resource.name
				updateresource.policyname = resource.policyname
				updateresource.targetvserver = resource.targetvserver
				updateresource.priority = resource.priority
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.bindpoint = resource.bindpoint
				updateresource.invoke = resource.invoke
				updateresource.labeltype = resource.labeltype
				updateresource.labelname = resource.labelname
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [crvserver_rewritepolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].targetvserver = resource[i].targetvserver
						updateresources[i].priority = resource[i].priority
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
						updateresources[i].bindpoint = resource[i].bindpoint
						updateresources[i].invoke = resource[i].invoke
						updateresources[i].labeltype = resource[i].labeltype
						updateresources[i].labelname = resource[i].labelname
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = crvserver_rewritepolicy_binding()
				deleteresource.name = resource.name
				deleteresource.policyname = resource.policyname
				deleteresource.bindpoint = resource.bindpoint
				deleteresource.priority = resource.priority
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [crvserver_rewritepolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].policyname = resource[i].policyname
						deleteresources[i].bindpoint = resource[i].bindpoint
						deleteresources[i].priority = resource[i].priority
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch crvserver_rewritepolicy_binding resources.
		"""
		try :
			if not name :
				obj = crvserver_rewritepolicy_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = crvserver_rewritepolicy_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of crvserver_rewritepolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = crvserver_rewritepolicy_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count crvserver_rewritepolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = crvserver_rewritepolicy_binding()
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
		r""" Use this API to count the filtered set of crvserver_rewritepolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = crvserver_rewritepolicy_binding()
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

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"
		ICA_REQUEST = "ICA_REQUEST"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

class crvserver_rewritepolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.crvserver_rewritepolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.crvserver_rewritepolicy_binding = [crvserver_rewritepolicy_binding() for _ in range(length)]

