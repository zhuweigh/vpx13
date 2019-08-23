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

class vpnvserver_binding(base_resource):
	""" Binding class showing the resources that can be bound to vpnvserver_binding. 
	"""
	def __init__(self) :
		self._name = None
		self.vpnvserver_intranetip6_binding = []
		self.vpnvserver_authenticationradiuspolicy_binding = []
		self.vpnvserver_vpnsessionpolicy_binding = []
		self.vpnvserver_vpnurlpolicy_binding = []
		self.vpnvserver_vpnnexthopserver_binding = []
		self.vpnvserver_authenticationldappolicy_binding = []
		self.vpnvserver_authenticationsamlidppolicy_binding = []
		self.vpnvserver_authenticationwebauthpolicy_binding = []
		self.vpnvserver_sharefileserver_binding = []
		self.vpnvserver_authenticationlocalpolicy_binding = []
		self.vpnvserver_vpnintranetapplication_binding = []
		self.vpnvserver_appcontroller_binding = []
		self.vpnvserver_rewritepolicy_binding = []
		self.vpnvserver_vpnportaltheme_binding = []
		self.vpnvserver_cspolicy_binding = []
		self.vpnvserver_auditsyslogpolicy_binding = []
		self.vpnvserver_authenticationcertpolicy_binding = []
		self.vpnvserver_vpnepaprofile_binding = []
		self.vpnvserver_vpnurl_binding = []
		self.vpnvserver_authenticationoauthidppolicy_binding = []
		self.vpnvserver_auditnslogpolicy_binding = []
		self.vpnvserver_authenticationpolicy_binding = []
		self.vpnvserver_vpneula_binding = []
		self.vpnvserver_icapolicy_binding = []
		self.vpnvserver_vpnclientlessaccesspolicy_binding = []
		self.vpnvserver_intranetip_binding = []
		self.vpnvserver_appflowpolicy_binding = []
		self.vpnvserver_responderpolicy_binding = []
		self.vpnvserver_vpntrafficpolicy_binding = []
		self.vpnvserver_authenticationnegotiatepolicy_binding = []
		self.vpnvserver_feopolicy_binding = []
		self.vpnvserver_aaapreauthenticationpolicy_binding = []
		self.vpnvserver_cachepolicy_binding = []
		self.vpnvserver_authenticationtacacspolicy_binding = []
		self.vpnvserver_authenticationsamlpolicy_binding = []
		self.vpnvserver_authenticationdfapolicy_binding = []
		self.vpnvserver_staserver_binding = []
		self.vpnvserver_authenticationloginschemapolicy_binding = []

	@property
	def name(self) :
		r"""Name of the Citrix Gateway virtual server for which to show detailed information.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the Citrix Gateway virtual server for which to show detailed information.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpnurlpolicy_bindings(self) :
		r"""vpnurlpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpnurlpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationoauthidppolicy_bindings(self) :
		r"""authenticationoauthidppolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationoauthidppolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationloginschemapolicy_bindings(self) :
		r"""authenticationloginschemapolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationloginschemapolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationsamlpolicy_bindings(self) :
		r"""authenticationsamlpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationsamlpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_cspolicy_bindings(self) :
		r"""cspolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_cspolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_icapolicy_bindings(self) :
		r"""icapolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_icapolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpnportaltheme_bindings(self) :
		r"""vpnportaltheme that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpnportaltheme_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_appflowpolicy_bindings(self) :
		r"""appflowpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_appflowpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_intranetip_bindings(self) :
		r"""intranetip that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_intranetip_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpntrafficpolicy_bindings(self) :
		r"""vpntrafficpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpntrafficpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpnepaprofile_bindings(self) :
		r"""vpnepaprofile that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpnepaprofile_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationtacacspolicy_bindings(self) :
		r"""authenticationtacacspolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationtacacspolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpnintranetapplication_bindings(self) :
		r"""vpnintranetapplication that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpnintranetapplication_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationradiuspolicy_bindings(self) :
		r"""authenticationradiuspolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationradiuspolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationpolicy_bindings(self) :
		r"""authenticationpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_aaapreauthenticationpolicy_bindings(self) :
		r"""aaapreauthenticationpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_aaapreauthenticationpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_feopolicy_bindings(self) :
		r"""feopolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_feopolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationlocalpolicy_bindings(self) :
		r"""authenticationlocalpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationlocalpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_intranetip6_bindings(self) :
		r"""intranetip6 that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_intranetip6_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpnsessionpolicy_bindings(self) :
		r"""vpnsessionpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpnsessionpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_staserver_bindings(self) :
		r"""staserver that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_staserver_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationcertpolicy_bindings(self) :
		r"""authenticationcertpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationcertpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationsamlidppolicy_bindings(self) :
		r"""authenticationsamlidppolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationsamlidppolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpnnexthopserver_bindings(self) :
		r"""vpnnexthopserver that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpnnexthopserver_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_auditnslogpolicy_bindings(self) :
		r"""auditnslogpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_auditnslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_auditsyslogpolicy_bindings(self) :
		r"""auditsyslogpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_auditsyslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_sharefileserver_bindings(self) :
		r"""sharefileserver that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_sharefileserver_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_responderpolicy_bindings(self) :
		r"""responderpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_responderpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpnurl_bindings(self) :
		r"""vpnurl that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpnurl_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_cachepolicy_bindings(self) :
		r"""cachepolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_cachepolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationldappolicy_bindings(self) :
		r"""authenticationldappolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationldappolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationwebauthpolicy_bindings(self) :
		r"""authenticationwebauthpolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationwebauthpolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_rewritepolicy_bindings(self) :
		r"""rewritepolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_rewritepolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationnegotiatepolicy_bindings(self) :
		r"""authenticationnegotiatepolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationnegotiatepolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_appcontroller_bindings(self) :
		r"""appcontroller that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_appcontroller_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpnclientlessaccesspolicy_bindings(self) :
		r"""vpnclientlessaccesspolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpnclientlessaccesspolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_authenticationdfapolicy_bindings(self) :
		r"""authenticationdfapolicy that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_authenticationdfapolicy_binding
		except Exception as e:
			raise e

	@property
	def vpnvserver_vpneula_bindings(self) :
		r"""vpneula that can be bound to vpnvserver.
		"""
		try :
			return self._vpnvserver_vpneula_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnvserver_binding
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
		r""" Use this API to fetch vpnvserver_binding resource.
		"""
		try :
			if not name :
				obj = vpnvserver_binding()
				response = obj.get_resources(service, option_)
			elif type(name) is not list :
				obj = vpnvserver_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [vpnvserver_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class vpnvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vpnvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnvserver_binding = [vpnvserver_binding() for _ in range(length)]

