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

class vpnvserver_auditsyslogpolicy_binding(base_resource) :
	""" Binding class showing the auditsyslogpolicy that can be bound to vpnvserver.
	"""
	def __init__(self) :
		self._policy = None
		self._priority = None
		self._acttype = None
		self._name = None
		self._secondary = None
		self._groupextraction = None
		self._gotopriorityexpression = None
		self._bindpoint = None
		self.___count = None

	@property
	def priority(self) :
		r"""Integer specifying the policy's priority. The lower the number, the higher the priority. Policies are evaluated in the order of their priority numbers. Maximum value for default syntax policies is 2147483647 and for classic policies is 64000.<br/>Minimum value =  0<br/>Maximum value =  2147483647.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""Integer specifying the policy's priority. The lower the number, the higher the priority. Policies are evaluated in the order of their priority numbers. Maximum value for default syntax policies is 2147483647 and for classic policies is 64000.<br/>Minimum value =  0<br/>Maximum value =  2147483647
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		r"""Applicable only to advance vpn session policy. Expression or other value specifying the next policy to evaluate if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher priority number.
		* END - End policy evaluation.
		* An expression that evaluates to a number.
		If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
		*  If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
		* If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
		* If the expression evaluates to a number that is larger than the largest numbered priority, policy evaluation ends.
		An UNDEF event is triggered if:
		* The expression is invalid.
		* The expression evaluates to a priority number that is numerically lower than the current policy's priority.
		* The expression evaluates to a priority number that is between the current policy's priority number (say, 30) and the highest priority number (say, 100), but does not match any configured priority number (for example, the expression evaluates to the number 85). This example assumes that the priority number increments by 10 for every successive policy, and therefore a priority number of 85 does not exist in the policy label.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		r"""Applicable only to advance vpn session policy. Expression or other value specifying the next policy to evaluate if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher priority number.
		* END - End policy evaluation.
		* An expression that evaluates to a number.
		If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
		*  If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
		* If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
		* If the expression evaluates to a number that is larger than the largest numbered priority, policy evaluation ends.
		An UNDEF event is triggered if:
		* The expression is invalid.
		* The expression evaluates to a priority number that is numerically lower than the current policy's priority.
		* The expression evaluates to a priority number that is between the current policy's priority number (say, 30) and the highest priority number (say, 100), but does not match any configured priority number (for example, the expression evaluates to the number 85). This example assumes that the priority number increments by 10 for every successive policy, and therefore a priority number of 85 does not exist in the policy label.
		"""
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def policy(self) :
		r"""The name of the policy, if any, bound to the VPN virtual server.
		"""
		try :
			return self._policy
		except Exception as e:
			raise e

	@policy.setter
	def policy(self, policy) :
		r"""The name of the policy, if any, bound to the VPN virtual server.
		"""
		try :
			self._policy = policy
		except Exception as e:
			raise e

	@property
	def groupextraction(self) :
		r"""Binds the authentication policy to a tertiary chain which will be used only for group extraction.  The user will not authenticate against this server, and this will only be called if primary and/or secondary authentication has succeeded.
		"""
		try :
			return self._groupextraction
		except Exception as e:
			raise e

	@groupextraction.setter
	def groupextraction(self, groupextraction) :
		r"""Binds the authentication policy to a tertiary chain which will be used only for group extraction.  The user will not authenticate against this server, and this will only be called if primary and/or secondary authentication has succeeded.
		"""
		try :
			self._groupextraction = groupextraction
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the virtual server.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def secondary(self) :
		r"""Binds the authentication policy as the secondary policy to use in a two-factor configuration. A user must then authenticate not only via a primary authentication method but also via a secondary authentication method. User groups are aggregated across both. The user name must be exactly the same for both authentication methods, but they can require different passwords.
		"""
		try :
			return self._secondary
		except Exception as e:
			raise e

	@secondary.setter
	def secondary(self, secondary) :
		r"""Binds the authentication policy as the secondary policy to use in a two-factor configuration. A user must then authenticate not only via a primary authentication method but also via a secondary authentication method. User groups are aggregated across both. The user name must be exactly the same for both authentication methods, but they can require different passwords.
		"""
		try :
			self._secondary = secondary
		except Exception as e:
			raise e

	@property
	def bindpoint(self) :
		r"""Bind point to which to bind the policy. Applies only to rewrite and cache policies. If you do not set this parameter, the policy is bound to REQ_DEFAULT or RES_DEFAULT, depending on whether the policy rule is a response-time or a request-time expression.
		"""
		try :
			return self._bindpoint
		except Exception as e:
			raise e

	@bindpoint.setter
	def bindpoint(self, bindpoint) :
		r"""Bind point to which to bind the policy. Applies only to rewrite and cache policies. If you do not set this parameter, the policy is bound to REQ_DEFAULT or RES_DEFAULT, depending on whether the policy rule is a response-time or a request-time expression.
		"""
		try :
			self._bindpoint = bindpoint
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
			result = service.payload_formatter.string_to_resource(vpnvserver_auditsyslogpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnvserver_auditsyslogpolicy_binding
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
				updateresource = vpnvserver_auditsyslogpolicy_binding()
				updateresource.name = resource.name
				updateresource.policy = resource.policy
				updateresource.priority = resource.priority
				updateresource.secondary = resource.secondary
				updateresource.groupextraction = resource.groupextraction
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.bindpoint = resource.bindpoint
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [vpnvserver_auditsyslogpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].policy = resource[i].policy
						updateresources[i].priority = resource[i].priority
						updateresources[i].secondary = resource[i].secondary
						updateresources[i].groupextraction = resource[i].groupextraction
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
						updateresources[i].bindpoint = resource[i].bindpoint
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = vpnvserver_auditsyslogpolicy_binding()
				deleteresource.name = resource.name
				deleteresource.policy = resource.policy
				deleteresource.secondary = resource.secondary
				deleteresource.groupextraction = resource.groupextraction
				deleteresource.bindpoint = resource.bindpoint
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [vpnvserver_auditsyslogpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].policy = resource[i].policy
						deleteresources[i].secondary = resource[i].secondary
						deleteresources[i].groupextraction = resource[i].groupextraction
						deleteresources[i].bindpoint = resource[i].bindpoint
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch vpnvserver_auditsyslogpolicy_binding resources.
		"""
		try :
			if not name :
				obj = vpnvserver_auditsyslogpolicy_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = vpnvserver_auditsyslogpolicy_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of vpnvserver_auditsyslogpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnvserver_auditsyslogpolicy_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count vpnvserver_auditsyslogpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = vpnvserver_auditsyslogpolicy_binding()
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
		r""" Use this API to count the filtered set of vpnvserver_auditsyslogpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnvserver_auditsyslogpolicy_binding()
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

	class Staaddresstype:
		IPV4 = "IPV4"
		IPV6 = "IPV6"

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"
		ICA_REQUEST = "ICA_REQUEST"
		OTHERTCP_REQUEST = "OTHERTCP_REQUEST"

class vpnvserver_auditsyslogpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vpnvserver_auditsyslogpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnvserver_auditsyslogpolicy_binding = [vpnvserver_auditsyslogpolicy_binding() for _ in range(length)]

