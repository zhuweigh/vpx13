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

class csvserver_binding(base_resource):
	""" Binding class showing the resources that can be bound to csvserver_binding. 
	"""
	def __init__(self) :
		self._name = None
		self.csvserver_spilloverpolicy_binding = []
		self.csvserver_auditnslogpolicy_binding = []
		self.csvserver_domain_binding = []
		self.csvserver_filterpolicy_binding = []
		self.csvserver_cmppolicy_binding = []
		self.csvserver_lbvserver_binding = []
		self.csvserver_appflowpolicy_binding = []
		self.csvserver_responderpolicy_binding = []
		self.csvserver_transformpolicy_binding = []
		self.csvserver_vpnvserver_binding = []
		self.csvserver_contentinspectionpolicy_binding = []
		self.csvserver_feopolicy_binding = []
		self.csvserver_authorizationpolicy_binding = []
		self.csvserver_cachepolicy_binding = []
		self.csvserver_rewritepolicy_binding = []
		self.csvserver_cspolicy_binding = []
		self.csvserver_gslbvserver_binding = []
		self.csvserver_appqoepolicy_binding = []
		self.csvserver_tmtrafficpolicy_binding = []
		self.csvserver_auditsyslogpolicy_binding = []
		self.csvserver_appfwpolicy_binding = []

	@property
	def name(self) :
		r"""Name of a content switching virtual server for which to display information, including the policies bound to the virtual server. To display a list of all configured Content Switching virtual servers, do not specify a value for this parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of a content switching virtual server for which to display information, including the policies bound to the virtual server. To display a list of all configured Content Switching virtual servers, do not specify a value for this parameter.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def csvserver_auditnslogpolicy_bindings(self) :
		r"""auditnslogpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_auditnslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_tmtrafficpolicy_bindings(self) :
		r"""tmtrafficpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_tmtrafficpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_lbvserver_bindings(self) :
		r"""lbvserver that can be bound to csvserver.
		"""
		try :
			return self._csvserver_lbvserver_binding
		except Exception as e:
			raise e

	@property
	def csvserver_responderpolicy_bindings(self) :
		r"""responderpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_responderpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_gslbvserver_bindings(self) :
		r"""gslbvserver that can be bound to csvserver.
		"""
		try :
			return self._csvserver_gslbvserver_binding
		except Exception as e:
			raise e

	@property
	def csvserver_cachepolicy_bindings(self) :
		r"""cachepolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_cachepolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_filterpolicy_bindings(self) :
		r"""filterpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_filterpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_transformpolicy_bindings(self) :
		r"""transformpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_transformpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_appflowpolicy_bindings(self) :
		r"""appflowpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_appflowpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_appfwpolicy_bindings(self) :
		r"""appfwpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_appfwpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_authorizationpolicy_bindings(self) :
		r"""authorizationpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_authorizationpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_auditsyslogpolicy_bindings(self) :
		r"""auditsyslogpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_auditsyslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_cmppolicy_bindings(self) :
		r"""cmppolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_cmppolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_rewritepolicy_bindings(self) :
		r"""rewritepolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_rewritepolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_cspolicy_bindings(self) :
		r"""cspolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_cspolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_contentinspectionpolicy_bindings(self) :
		r"""contentinspectionpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_contentinspectionpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_spilloverpolicy_bindings(self) :
		r"""spilloverpolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_spilloverpolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_appqoepolicy_bindings(self) :
		r"""appqoepolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_appqoepolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_feopolicy_bindings(self) :
		r"""feopolicy that can be bound to csvserver.
		"""
		try :
			return self._csvserver_feopolicy_binding
		except Exception as e:
			raise e

	@property
	def csvserver_vpnvserver_bindings(self) :
		r"""vpnvserver that can be bound to csvserver.
		"""
		try :
			return self._csvserver_vpnvserver_binding
		except Exception as e:
			raise e

	@property
	def csvserver_domain_bindings(self) :
		r"""domain that can be bound to csvserver.
		"""
		try :
			return self._csvserver_domain_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(csvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.csvserver_binding
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
	def get(self, service, name="", option_="") :
		r""" Use this API to fetch csvserver_binding resource.
		"""
		try :
			if not name :
				obj = csvserver_binding()
				response = obj.get_resources(service, option_)
			elif type(name) is not list :
				obj = csvserver_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [csvserver_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class csvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.csvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.csvserver_binding = [csvserver_binding() for _ in range(length)]

