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

class sslcertkey_sslocspresponder_binding(base_resource) :
	""" Binding class showing the sslocspresponder that can be bound to sslcertkey.
	"""
	def __init__(self) :
		self._ocspresponder = None
		self._priority = None
		self._certkey = None
		self._ca = None
		self.___count = None

	@property
	def priority(self) :
		r"""ocsp priority.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""ocsp priority.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def ca(self) :
		r"""The certificate-key pair being unbound is a Certificate Authority (CA) certificate. If you choose this option, the certificate-key pair is unbound from the list of CA certificates that were bound to the specified SSL virtual server or SSL service.
		"""
		try :
			return self._ca
		except Exception as e:
			raise e

	@ca.setter
	def ca(self, ca) :
		r"""The certificate-key pair being unbound is a Certificate Authority (CA) certificate. If you choose this option, the certificate-key pair is unbound from the list of CA certificates that were bound to the specified SSL virtual server or SSL service.
		"""
		try :
			self._ca = ca
		except Exception as e:
			raise e

	@property
	def certkey(self) :
		r"""Name of the certificate-key pair.<br/>Minimum length =  1.
		"""
		try :
			return self._certkey
		except Exception as e:
			raise e

	@certkey.setter
	def certkey(self, certkey) :
		r"""Name of the certificate-key pair.<br/>Minimum length =  1
		"""
		try :
			self._certkey = certkey
		except Exception as e:
			raise e

	@property
	def ocspresponder(self) :
		r"""OCSP responders bound to this certkey.
		"""
		try :
			return self._ocspresponder
		except Exception as e:
			raise e

	@ocspresponder.setter
	def ocspresponder(self, ocspresponder) :
		r"""OCSP responders bound to this certkey.
		"""
		try :
			self._ocspresponder = ocspresponder
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcertkey_sslocspresponder_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcertkey_sslocspresponder_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.certkey is not None :
				return str(self.certkey)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = sslcertkey_sslocspresponder_binding()
				updateresource.certkey = resource.certkey
				updateresource.ocspresponder = resource.ocspresponder
				updateresource.priority = resource.priority
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslcertkey_sslocspresponder_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].certkey = resource[i].certkey
						updateresources[i].ocspresponder = resource[i].ocspresponder
						updateresources[i].priority = resource[i].priority
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = sslcertkey_sslocspresponder_binding()
				deleteresource.certkey = resource.certkey
				deleteresource.ocspresponder = resource.ocspresponder
				deleteresource.ca = resource.ca
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslcertkey_sslocspresponder_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].certkey = resource[i].certkey
						deleteresources[i].ocspresponder = resource[i].ocspresponder
						deleteresources[i].ca = resource[i].ca
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, certkey="", option_="") :
		r""" Use this API to fetch sslcertkey_sslocspresponder_binding resources.
		"""
		try :
			if not certkey :
				obj = sslcertkey_sslocspresponder_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = sslcertkey_sslocspresponder_binding()
				obj.certkey = certkey
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, certkey, filter_) :
		r""" Use this API to fetch filtered set of sslcertkey_sslocspresponder_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertkey_sslocspresponder_binding()
			obj.certkey = certkey
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, certkey) :
		r""" Use this API to count sslcertkey_sslocspresponder_binding resources configued on NetScaler.
		"""
		try :
			obj = sslcertkey_sslocspresponder_binding()
			obj.certkey = certkey
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, certkey, filter_) :
		r""" Use this API to count the filtered set of sslcertkey_sslocspresponder_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertkey_sslocspresponder_binding()
			obj.certkey = certkey
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class sslcertkey_sslocspresponder_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcertkey_sslocspresponder_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcertkey_sslocspresponder_binding = [sslcertkey_sslocspresponder_binding() for _ in range(length)]

