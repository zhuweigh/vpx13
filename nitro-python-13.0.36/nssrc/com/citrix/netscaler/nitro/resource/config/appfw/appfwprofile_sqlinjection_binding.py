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

class appfwprofile_sqlinjection_binding(base_resource) :
	""" Binding class showing the sqlinjection that can be bound to appfwprofile.
	"""
	def __init__(self) :
		self._sqlinjection = None
		self._isregex_sql = None
		self._formactionurl_sql = None
		self._as_scan_location_sql = None
		self._as_value_type_sql = None
		self._as_value_expr_sql = None
		self._isvalueregex_sql = None
		self._state = None
		self._comment = None
		self._name = None
		self.___count = None

	@property
	def as_value_expr_sql(self) :
		r"""The web form value expression.
		"""
		try :
			return self._as_value_expr_sql
		except Exception as e:
			raise e

	@as_value_expr_sql.setter
	def as_value_expr_sql(self, as_value_expr_sql) :
		r"""The web form value expression.
		"""
		try :
			self._as_value_expr_sql = as_value_expr_sql
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Enabled.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Enabled.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def formactionurl_sql(self) :
		r"""The web form action URL.
		"""
		try :
			return self._formactionurl_sql
		except Exception as e:
			raise e

	@formactionurl_sql.setter
	def formactionurl_sql(self, formactionurl_sql) :
		r"""The web form action URL.
		"""
		try :
			self._formactionurl_sql = formactionurl_sql
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def isregex_sql(self) :
		r"""Is the web form field name a regular expression?.<br/>Possible values = REGEX, NOTREGEX.
		"""
		try :
			return self._isregex_sql
		except Exception as e:
			raise e

	@isregex_sql.setter
	def isregex_sql(self, isregex_sql) :
		r"""Is the web form field name a regular expression?.<br/>Possible values = REGEX, NOTREGEX
		"""
		try :
			self._isregex_sql = isregex_sql
		except Exception as e:
			raise e

	@property
	def isvalueregex_sql(self) :
		r"""Is the web form field value a regular expression?.<br/>Possible values = REGEX, NOTREGEX.
		"""
		try :
			return self._isvalueregex_sql
		except Exception as e:
			raise e

	@isvalueregex_sql.setter
	def isvalueregex_sql(self, isvalueregex_sql) :
		r"""Is the web form field value a regular expression?.<br/>Possible values = REGEX, NOTREGEX
		"""
		try :
			self._isvalueregex_sql = isvalueregex_sql
		except Exception as e:
			raise e

	@property
	def as_scan_location_sql(self) :
		r"""Location of SQL injection exception - form field, header or cookie.<br/>Possible values = FORMFIELD, HEADER, COOKIE.
		"""
		try :
			return self._as_scan_location_sql
		except Exception as e:
			raise e

	@as_scan_location_sql.setter
	def as_scan_location_sql(self, as_scan_location_sql) :
		r"""Location of SQL injection exception - form field, header or cookie.<br/>Possible values = FORMFIELD, HEADER, COOKIE
		"""
		try :
			self._as_scan_location_sql = as_scan_location_sql
		except Exception as e:
			raise e

	@property
	def sqlinjection(self) :
		r"""The web form field name.
		"""
		try :
			return self._sqlinjection
		except Exception as e:
			raise e

	@sqlinjection.setter
	def sqlinjection(self, sqlinjection) :
		r"""The web form field name.
		"""
		try :
			self._sqlinjection = sqlinjection
		except Exception as e:
			raise e

	@property
	def as_value_type_sql(self) :
		r"""The web form value type.<br/>Possible values = Keyword, SpecialString, Wildchar.
		"""
		try :
			return self._as_value_type_sql
		except Exception as e:
			raise e

	@as_value_type_sql.setter
	def as_value_type_sql(self, as_value_type_sql) :
		r"""The web form value type.<br/>Possible values = Keyword, SpecialString, Wildchar
		"""
		try :
			self._as_value_type_sql = as_value_type_sql
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_sqlinjection_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile_sqlinjection_binding
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
				updateresource = appfwprofile_sqlinjection_binding()
				updateresource.name = resource.name
				updateresource.sqlinjection = resource.sqlinjection
				updateresource.formactionurl_sql = resource.formactionurl_sql
				updateresource.isregex_sql = resource.isregex_sql
				updateresource.as_scan_location_sql = resource.as_scan_location_sql
				updateresource.as_value_type_sql = resource.as_value_type_sql
				updateresource.as_value_expr_sql = resource.as_value_expr_sql
				updateresource.isvalueregex_sql = resource.isvalueregex_sql
				updateresource.comment = resource.comment
				updateresource.state = resource.state
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [appfwprofile_sqlinjection_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].sqlinjection = resource[i].sqlinjection
						updateresources[i].formactionurl_sql = resource[i].formactionurl_sql
						updateresources[i].isregex_sql = resource[i].isregex_sql
						updateresources[i].as_scan_location_sql = resource[i].as_scan_location_sql
						updateresources[i].as_value_type_sql = resource[i].as_value_type_sql
						updateresources[i].as_value_expr_sql = resource[i].as_value_expr_sql
						updateresources[i].isvalueregex_sql = resource[i].isvalueregex_sql
						updateresources[i].comment = resource[i].comment
						updateresources[i].state = resource[i].state
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = appfwprofile_sqlinjection_binding()
				deleteresource.name = resource.name
				deleteresource.sqlinjection = resource.sqlinjection
				deleteresource.formactionurl_sql = resource.formactionurl_sql
				deleteresource.as_scan_location_sql = resource.as_scan_location_sql
				deleteresource.as_value_type_sql = resource.as_value_type_sql
				deleteresource.as_value_expr_sql = resource.as_value_expr_sql
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [appfwprofile_sqlinjection_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].sqlinjection = resource[i].sqlinjection
						deleteresources[i].formactionurl_sql = resource[i].formactionurl_sql
						deleteresources[i].as_scan_location_sql = resource[i].as_scan_location_sql
						deleteresources[i].as_value_type_sql = resource[i].as_value_type_sql
						deleteresources[i].as_value_expr_sql = resource[i].as_value_expr_sql
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch appfwprofile_sqlinjection_binding resources.
		"""
		try :
			if not name :
				obj = appfwprofile_sqlinjection_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = appfwprofile_sqlinjection_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of appfwprofile_sqlinjection_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_sqlinjection_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count appfwprofile_sqlinjection_binding resources configued on NetScaler.
		"""
		try :
			obj = appfwprofile_sqlinjection_binding()
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
		r""" Use this API to count the filtered set of appfwprofile_sqlinjection_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_sqlinjection_binding()
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

	class As_scan_location_xmlsql:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Xmlmaxelementdepthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattachmentsizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlsoaparraycheck:
		ON = "ON"
		OFF = "OFF"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Xmlmaxelementnamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_ff:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxelementscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlendpointcheck:
		ABSOLUTE = "ABSOLUTE"
		RELATIVE = "RELATIVE"

	class Xmlmaxnamespacescheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattributenamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isvalueregex_xss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlblockdtd:
		ON = "ON"
		OFF = "OFF"

	class Xmlblockpi:
		ON = "ON"
		OFF = "OFF"

	class Isregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlvalidateresponse:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxelementchildrencheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxentityexpansionscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxnamespaceurilengthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xss:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Xmlmaxentityexpansiondepthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xmlxss:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Xmlmaxattributevaluelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_ffc:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Isvalueregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class As_scan_location_sql:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Xmlattachmentcontenttypecheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xmlsql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlvalidatesoapenvelope:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxchardatalengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlminfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class As_value_type_sql:
		Keyword = "Keyword"
		SpecialString = "SpecialString"
		Wildchar = "Wildchar"

	class Isregex_xmlxss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmladditionalsoapheaders:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattributescheck:
		ON = "ON"
		OFF = "OFF"

	class Action:
		none = "none"
		block = "block"
		log = "log"
		remove = "remove"
		stats = "stats"
		xout = "xout"

	class As_value_type_xss:
		Tag = "Tag"
		Attribute = "Attribute"
		Pattern = "Pattern"

	class Xmlblockexternalentities:
		ON = "ON"
		OFF = "OFF"

class appfwprofile_sqlinjection_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile_sqlinjection_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile_sqlinjection_binding = [appfwprofile_sqlinjection_binding() for _ in range(length)]

