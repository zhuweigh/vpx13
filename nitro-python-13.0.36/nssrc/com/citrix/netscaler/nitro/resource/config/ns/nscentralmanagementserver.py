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

class nscentralmanagementserver(base_resource) :
	""" Configuration for centralmanagementserver resource. """
	def __init__(self) :
		self._type = None
		self._username = None
		self._password = None
		self._ipaddress = None
		self._servername = None
		self.___count = None

	@property
	def type(self) :
		r"""Type of the central management server. Must be either CLOUD or ONPREM depending on whether the server is on the cloud or on premise.<br/>Possible values = CLOUD, ONPREM.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of the central management server. Must be either CLOUD or ONPREM depending on whether the server is on the cloud or on premise.<br/>Possible values = CLOUD, ONPREM
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def username(self) :
		r"""Username for access to central management server. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or
		single quotation marks (for example, "my ns centralmgmtserver" or "my ns centralmgmtserver").<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		r"""Username for access to central management server. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or
		single quotation marks (for example, "my ns centralmgmtserver" or "my ns centralmgmtserver").<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def password(self) :
		r"""Password for access to central management server. Required for any user account.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		r"""Password for access to central management server. Required for any user account.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""Ip Address of central management server.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""Ip Address of central management server.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""Fully qualified domain name of the central management server.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""Fully qualified domain name of the central management server.
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nscentralmanagementserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nscentralmanagementserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.type is not None :
				return str(self.type)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nscentralmanagementserver.
		"""
		try :
			if type(resource) is not list :
				addresource = nscentralmanagementserver()
				addresource.type = resource.type
				addresource.username = resource.username
				addresource.password = resource.password
				addresource.ipaddress = resource.ipaddress
				addresource.servername = resource.servername
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nscentralmanagementserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].type = resource[i].type
						addresources[i].username = resource[i].username
						addresources[i].password = resource[i].password
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].servername = resource[i].servername
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nscentralmanagementserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nscentralmanagementserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.type = resource
				else :
					deleteresource.type = resource.type
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nscentralmanagementserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].type = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nscentralmanagementserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].type = resource[i].type
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nscentralmanagementserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nscentralmanagementserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nscentralmanagementserver()
					obj.type = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nscentralmanagementserver() for _ in range(len(name))]
						obj = [nscentralmanagementserver() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nscentralmanagementserver()
							obj[i].type = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nscentralmanagementserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nscentralmanagementserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nscentralmanagementserver resources configured on NetScaler.
		"""
		try :
			obj = nscentralmanagementserver()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of nscentralmanagementserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nscentralmanagementserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Type:
		CLOUD = "CLOUD"
		ONPREM = "ONPREM"

class nscentralmanagementserver_response(base_response) :
	def __init__(self, length=1) :
		self.nscentralmanagementserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nscentralmanagementserver = [nscentralmanagementserver() for _ in range(length)]

