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

class aaagroup_vpnintranetapplication_binding(base_resource) :
	""" Binding class showing the vpnintranetapplication that can be bound to aaagroup.
	"""
	def __init__(self) :
		self._intranetapplication = None
		self._acttype = None
		self._groupname = None
		self._gotopriorityexpression = None
		self.___count = None

	@property
	def gotopriorityexpression(self) :
		r"""Expression or other value specifying the next policy to evaluate if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher priority number.
		* END - End policy evaluation.
		* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
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
		r"""Expression or other value specifying the next policy to evaluate if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher priority number.
		* END - End policy evaluation.
		* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
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
	def groupname(self) :
		r"""Name of the group that you are binding.<br/>Minimum length =  1.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		r"""Name of the group that you are binding.<br/>Minimum length =  1
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def intranetapplication(self) :
		r"""Bind the group to the specified intranet VPN application.
		"""
		try :
			return self._intranetapplication
		except Exception as e:
			raise e

	@intranetapplication.setter
	def intranetapplication(self, intranetapplication) :
		r"""Bind the group to the specified intranet VPN application.
		"""
		try :
			self._intranetapplication = intranetapplication
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
			result = service.payload_formatter.string_to_resource(aaagroup_vpnintranetapplication_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaagroup_vpnintranetapplication_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.groupname is not None :
				return str(self.groupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = aaagroup_vpnintranetapplication_binding()
				updateresource.groupname = resource.groupname
				updateresource.intranetapplication = resource.intranetapplication
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [aaagroup_vpnintranetapplication_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].groupname = resource[i].groupname
						updateresources[i].intranetapplication = resource[i].intranetapplication
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = aaagroup_vpnintranetapplication_binding()
				deleteresource.groupname = resource.groupname
				deleteresource.intranetapplication = resource.intranetapplication
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [aaagroup_vpnintranetapplication_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].groupname = resource[i].groupname
						deleteresources[i].intranetapplication = resource[i].intranetapplication
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, groupname="", option_="") :
		r""" Use this API to fetch aaagroup_vpnintranetapplication_binding resources.
		"""
		try :
			if not groupname :
				obj = aaagroup_vpnintranetapplication_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = aaagroup_vpnintranetapplication_binding()
				obj.groupname = groupname
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, groupname, filter_) :
		r""" Use this API to fetch filtered set of aaagroup_vpnintranetapplication_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaagroup_vpnintranetapplication_binding()
			obj.groupname = groupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, groupname) :
		r""" Use this API to count aaagroup_vpnintranetapplication_binding resources configued on NetScaler.
		"""
		try :
			obj = aaagroup_vpnintranetapplication_binding()
			obj.groupname = groupname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, groupname, filter_) :
		r""" Use this API to count the filtered set of aaagroup_vpnintranetapplication_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaagroup_vpnintranetapplication_binding()
			obj.groupname = groupname
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

class aaagroup_vpnintranetapplication_binding_response(base_response) :
	def __init__(self, length=1) :
		self.aaagroup_vpnintranetapplication_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaagroup_vpnintranetapplication_binding = [aaagroup_vpnintranetapplication_binding() for _ in range(length)]

