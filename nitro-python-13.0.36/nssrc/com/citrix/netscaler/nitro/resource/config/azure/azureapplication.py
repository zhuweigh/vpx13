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

class azureapplication(base_resource) :
	""" Configuration for Azure Application resource. """
	def __init__(self) :
		self._name = None
		self._clientid = None
		self._clientsecret = None
		self._tenantid = None
		self._tokenendpoint = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of application object in netscaler.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of application object in netscaler.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clientid(self) :
		r"""client id of the application.<br/>Minimum length =  1.
		"""
		try :
			return self._clientid
		except Exception as e:
			raise e

	@clientid.setter
	def clientid(self, clientid) :
		r"""client id of the application.<br/>Minimum length =  1
		"""
		try :
			self._clientid = clientid
		except Exception as e:
			raise e

	@property
	def clientsecret(self) :
		r"""Client secret for this application configured in Azure.<br/>Minimum length =  1.
		"""
		try :
			return self._clientsecret
		except Exception as e:
			raise e

	@clientsecret.setter
	def clientsecret(self, clientsecret) :
		r"""Client secret for this application configured in Azure.<br/>Minimum length =  1
		"""
		try :
			self._clientsecret = clientsecret
		except Exception as e:
			raise e

	@property
	def tenantid(self) :
		r"""Azure active directory tenant id on which this application was created.<br/>Minimum length =  1.
		"""
		try :
			return self._tenantid
		except Exception as e:
			raise e

	@tenantid.setter
	def tenantid(self, tenantid) :
		r"""Azure active directory tenant id on which this application was created.<br/>Minimum length =  1
		"""
		try :
			self._tenantid = tenantid
		except Exception as e:
			raise e

	@property
	def tokenendpoint(self) :
		r"""URL from where access token has to be obtained by submitting credentials.<br/>Minimum length =  1.
		"""
		try :
			return self._tokenendpoint
		except Exception as e:
			raise e

	@tokenendpoint.setter
	def tokenendpoint(self, tokenendpoint) :
		r"""URL from where access token has to be obtained by submitting credentials.<br/>Minimum length =  1
		"""
		try :
			self._tokenendpoint = tokenendpoint
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(azureapplication_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.azureapplication
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
		r""" Use this API to add azureapplication.
		"""
		try :
			if type(resource) is not list :
				addresource = azureapplication()
				addresource.name = resource.name
				addresource.clientid = resource.clientid
				addresource.clientsecret = resource.clientsecret
				addresource.tenantid = resource.tenantid
				addresource.tokenendpoint = resource.tokenendpoint
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ azureapplication() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].clientid = resource[i].clientid
						addresources[i].clientsecret = resource[i].clientsecret
						addresources[i].tenantid = resource[i].tenantid
						addresources[i].tokenendpoint = resource[i].tokenendpoint
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete azureapplication.
		"""
		try :
			if type(resource) is not list :
				deleteresource = azureapplication()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ azureapplication() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ azureapplication() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the azureapplication resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = azureapplication()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = azureapplication()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [azureapplication() for _ in range(len(name))]
						obj = [azureapplication() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = azureapplication()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of azureapplication resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = azureapplication()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the azureapplication resources configured on NetScaler.
		"""
		try :
			obj = azureapplication()
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
		r""" Use this API to count filtered the set of azureapplication resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = azureapplication()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class azureapplication_response(base_response) :
	def __init__(self, length=1) :
		self.azureapplication = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.azureapplication = [azureapplication() for _ in range(length)]

