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

class sslprofile_sslcipher_binding(base_resource) :
	""" Binding class showing the sslcipher that can be bound to sslprofile.
	"""
	def __init__(self) :
		self._cipheraliasname = None
		self._cipherpriority = None
		self._description = None
		self._name = None
		self._ciphername = None
		self.___count = None

	@property
	def ciphername(self) :
		try :
			return self._ciphername
		except Exception as e:
			raise e

	@ciphername.setter
	def ciphername(self, ciphername) :
		try :
			self._ciphername = ciphername
		except Exception as e:
			raise e

	@property
	def cipheraliasname(self) :
		r"""The name of the cipher group/alias/individual cipheri bindings.
		"""
		try :
			return self._cipheraliasname
		except Exception as e:
			raise e

	@cipheraliasname.setter
	def cipheraliasname(self, cipheraliasname) :
		r"""The name of the cipher group/alias/individual cipheri bindings.
		"""
		try :
			self._cipheraliasname = cipheraliasname
		except Exception as e:
			raise e

	@property
	def cipherpriority(self) :
		r"""cipher priority.<br/>Minimum value =  1.
		"""
		try :
			return self._cipherpriority
		except Exception as e:
			raise e

	@cipherpriority.setter
	def cipherpriority(self, cipherpriority) :
		r"""cipher priority.<br/>Minimum value =  1
		"""
		try :
			self._cipherpriority = cipherpriority
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the SSL profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the SSL profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def description(self) :
		r"""The cipher suite description.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@description.setter
	def description(self, description) :
		r"""The cipher suite description.
		"""
		try :
			self._description = description
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslprofile_sslcipher_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslprofile_sslcipher_binding
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
				updateresource = sslprofile_sslcipher_binding()
				updateresource.name = resource.name
				updateresource.ciphername = resource.ciphername
				updateresource.cipherpriority = resource.cipherpriority
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslprofile_sslcipher_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ciphername = resource[i].ciphername
						updateresources[i].cipherpriority = resource[i].cipherpriority
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = sslprofile_sslcipher_binding()
				deleteresource.name = resource.name
				deleteresource.ciphername = resource.ciphername
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslprofile_sslcipher_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].ciphername = resource[i].ciphername
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch sslprofile_sslcipher_binding resources.
		"""
		try :
			if not name :
				obj = sslprofile_sslcipher_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = sslprofile_sslcipher_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of sslprofile_sslcipher_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslprofile_sslcipher_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count sslprofile_sslcipher_binding resources configued on NetScaler.
		"""
		try :
			obj = sslprofile_sslcipher_binding()
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
		r""" Use this API to count the filtered set of sslprofile_sslcipher_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslprofile_sslcipher_binding()
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

	class Ecccurvename:
		ALL = "ALL"
		P_224 = "P_224"
		P_256 = "P_256"
		P_384 = "P_384"
		P_521 = "P_521"

class sslprofile_sslcipher_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslprofile_sslcipher_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslprofile_sslcipher_binding = [sslprofile_sslcipher_binding() for _ in range(length)]

