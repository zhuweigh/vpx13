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

class appfwprofile_binding(base_resource):
	""" Binding class showing the resources that can be bound to appfwprofile_binding. 
	"""
	def __init__(self) :
		self._name = None
		self.appfwprofile_xmlattachmenturl_binding = []
		self.appfwprofile_excluderescontenttype_binding = []
		self.appfwprofile_crosssitescripting_binding = []
		self.appfwprofile_xmlwsiurl_binding = []
		self.appfwprofile_xmldosurl_binding = []
		self.appfwprofile_fieldconsistency_binding = []
		self.appfwprofile_sqlinjection_binding = []
		self.appfwprofile_safeobject_binding = []
		self.appfwprofile_logexpression_binding = []
		self.appfwprofile_denyurl_binding = []
		self.appfwprofile_trustedlearningclients_binding = []
		self.appfwprofile_csrftag_binding = []
		self.appfwprofile_starturl_binding = []
		self.appfwprofile_cookieconsistency_binding = []
		self.appfwprofile_xmlsqlinjection_binding = []
		self.appfwprofile_creditcardnumber_binding = []
		self.appfwprofile_xmlxss_binding = []
		self.appfwprofile_fieldformat_binding = []
		self.appfwprofile_contenttype_binding = []
		self.appfwprofile_xmlvalidationurl_binding = []

	@property
	def name(self) :
		r"""Name of the application firewall profile.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the application firewall profile.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def appfwprofile_csrftag_bindings(self) :
		r"""csrftag that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_csrftag_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_starturl_bindings(self) :
		r"""starturl that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_starturl_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_xmlvalidationurl_bindings(self) :
		r"""xmlvalidationurl that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_xmlvalidationurl_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_logexpression_bindings(self) :
		r"""logexpression that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_logexpression_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_xmlattachmenturl_bindings(self) :
		r"""xmlattachmenturl that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_xmlattachmenturl_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_safeobject_bindings(self) :
		r"""safeobject that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_safeobject_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_cookieconsistency_bindings(self) :
		r"""cookieconsistency that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_cookieconsistency_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_fieldconsistency_bindings(self) :
		r"""fieldconsistency that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_fieldconsistency_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_xmlwsiurl_bindings(self) :
		r"""xmlwsiurl that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_xmlwsiurl_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_xmlsqlinjection_bindings(self) :
		r"""xmlsqlinjection that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_xmlsqlinjection_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_sqlinjection_bindings(self) :
		r"""sqlinjection that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_sqlinjection_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_trustedlearningclients_bindings(self) :
		r"""trustedlearningclients that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_trustedlearningclients_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_crosssitescripting_bindings(self) :
		r"""crosssitescripting that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_crosssitescripting_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_excluderescontenttype_bindings(self) :
		r"""excluderescontenttype that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_excluderescontenttype_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_contenttype_bindings(self) :
		r"""contenttype that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_contenttype_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_denyurl_bindings(self) :
		r"""denyurl that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_denyurl_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_xmlxss_bindings(self) :
		r"""xmlxss that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_xmlxss_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_fieldformat_bindings(self) :
		r"""fieldformat that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_fieldformat_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_creditcardnumber_bindings(self) :
		r"""creditcardnumber that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_creditcardnumber_binding
		except Exception as e:
			raise e

	@property
	def appfwprofile_xmldosurl_bindings(self) :
		r"""xmldosurl that can be bound to appfwprofile.
		"""
		try :
			return self._appfwprofile_xmldosurl_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile_binding
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
		r""" Use this API to fetch appfwprofile_binding resource.
		"""
		try :
			if not name :
				obj = appfwprofile_binding()
				response = obj.get_resources(service, option_)
			elif type(name) is not list :
				obj = appfwprofile_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [appfwprofile_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class appfwprofile_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile_binding = [appfwprofile_binding() for _ in range(length)]

