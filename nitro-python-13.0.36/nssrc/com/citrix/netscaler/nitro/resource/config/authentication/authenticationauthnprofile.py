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

class authenticationauthnprofile(base_resource) :
	""" Configuration for Authentication profile resource. """
	def __init__(self) :
		self._name = None
		self._authnvsname = None
		self._authenticationhost = None
		self._authenticationdomain = None
		self._authenticationlevel = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the authentication profile. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the RADIUS action is added.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the authentication profile. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the RADIUS action is added.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def authnvsname(self) :
		r"""Name of the authentication vserver at which authentication should be done.<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._authnvsname
		except Exception as e:
			raise e

	@authnvsname.setter
	def authnvsname(self, authnvsname) :
		r"""Name of the authentication vserver at which authentication should be done.<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._authnvsname = authnvsname
		except Exception as e:
			raise e

	@property
	def authenticationhost(self) :
		r"""Hostname of the authentication vserver to which user must be redirected for authentication.<br/>Minimum length =  1<br/>Maximum length =  256.
		"""
		try :
			return self._authenticationhost
		except Exception as e:
			raise e

	@authenticationhost.setter
	def authenticationhost(self, authenticationhost) :
		r"""Hostname of the authentication vserver to which user must be redirected for authentication.<br/>Minimum length =  1<br/>Maximum length =  256
		"""
		try :
			self._authenticationhost = authenticationhost
		except Exception as e:
			raise e

	@property
	def authenticationdomain(self) :
		r"""Domain for which TM cookie must to be set. If unspecified, cookie will be set for FQDN.<br/>Minimum length =  1<br/>Maximum length =  256.
		"""
		try :
			return self._authenticationdomain
		except Exception as e:
			raise e

	@authenticationdomain.setter
	def authenticationdomain(self, authenticationdomain) :
		r"""Domain for which TM cookie must to be set. If unspecified, cookie will be set for FQDN.<br/>Minimum length =  1<br/>Maximum length =  256
		"""
		try :
			self._authenticationdomain = authenticationdomain
		except Exception as e:
			raise e

	@property
	def authenticationlevel(self) :
		r"""Authentication weight or level of the vserver to which this will bound. This is used to order TM vservers based on the protection required. A session that is created by authenticating against TM vserver at given level cannot be used to access TM vserver at a higher level.<br/>Maximum length =  255.
		"""
		try :
			return self._authenticationlevel
		except Exception as e:
			raise e

	@authenticationlevel.setter
	def authenticationlevel(self, authenticationlevel) :
		r"""Authentication weight or level of the vserver to which this will bound. This is used to order TM vservers based on the protection required. A session that is created by authenticating against TM vserver at given level cannot be used to access TM vserver at a higher level.<br/>Maximum length =  255
		"""
		try :
			self._authenticationlevel = authenticationlevel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationauthnprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationauthnprofile
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
		r""" Use this API to add authenticationauthnprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationauthnprofile()
				addresource.name = resource.name
				addresource.authnvsname = resource.authnvsname
				addresource.authenticationhost = resource.authenticationhost
				addresource.authenticationdomain = resource.authenticationdomain
				addresource.authenticationlevel = resource.authenticationlevel
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationauthnprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].authnvsname = resource[i].authnvsname
						addresources[i].authenticationhost = resource[i].authenticationhost
						addresources[i].authenticationdomain = resource[i].authenticationdomain
						addresources[i].authenticationlevel = resource[i].authenticationlevel
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationauthnprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationauthnprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationauthnprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationauthnprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationauthnprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationauthnprofile()
				updateresource.name = resource.name
				updateresource.authnvsname = resource.authnvsname
				updateresource.authenticationhost = resource.authenticationhost
				updateresource.authenticationdomain = resource.authenticationdomain
				updateresource.authenticationlevel = resource.authenticationlevel
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationauthnprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].authnvsname = resource[i].authnvsname
						updateresources[i].authenticationhost = resource[i].authenticationhost
						updateresources[i].authenticationdomain = resource[i].authenticationdomain
						updateresources[i].authenticationlevel = resource[i].authenticationlevel
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationauthnprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationauthnprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationauthnprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationauthnprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationauthnprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationauthnprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationauthnprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationauthnprofile() for _ in range(len(name))]
						obj = [authenticationauthnprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationauthnprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationauthnprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationauthnprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationauthnprofile resources configured on NetScaler.
		"""
		try :
			obj = authenticationauthnprofile()
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
		r""" Use this API to count filtered the set of authenticationauthnprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationauthnprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class authenticationauthnprofile_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationauthnprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationauthnprofile = [authenticationauthnprofile() for _ in range(length)]

