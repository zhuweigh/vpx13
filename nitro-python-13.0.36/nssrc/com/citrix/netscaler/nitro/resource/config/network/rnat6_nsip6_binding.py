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

class rnat6_nsip6_binding(base_resource) :
	""" Binding class showing the nsip6 that can be bound to rnat6.
	"""
	def __init__(self) :
		self._natip6 = None
		self._td = None
		self._ownergroup = None
		self._name = None
		self.___count = None

	@property
	def natip6(self) :
		r"""Nat IP Address.<br/>Minimum length =  1.
		"""
		try :
			return self._natip6
		except Exception as e:
			raise e

	@natip6.setter
	def natip6(self, natip6) :
		r"""Nat IP Address.<br/>Minimum length =  1
		"""
		try :
			self._natip6 = natip6
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the RNAT6 rule to which to bind NAT IPs.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the RNAT6 rule to which to bind NAT IPs.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ownergroup(self) :
		r"""The owner node group in a Cluster for this rnat rule.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1.
		"""
		try :
			return self._ownergroup
		except Exception as e:
			raise e

	@ownergroup.setter
	def ownergroup(self, ownergroup) :
		r"""The owner node group in a Cluster for this rnat rule.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1
		"""
		try :
			self._ownergroup = ownergroup
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rnat6_nsip6_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rnat6_nsip6_binding
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
				updateresource = rnat6_nsip6_binding()
				updateresource.name = resource.name
				updateresource.natip6 = resource.natip6
				updateresource.ownergroup = resource.ownergroup
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [rnat6_nsip6_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].natip6 = resource[i].natip6
						updateresources[i].ownergroup = resource[i].ownergroup
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = rnat6_nsip6_binding()
				deleteresource.name = resource.name
				deleteresource.natip6 = resource.natip6
				deleteresource.ownergroup = resource.ownergroup
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [rnat6_nsip6_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].natip6 = resource[i].natip6
						deleteresources[i].ownergroup = resource[i].ownergroup
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch rnat6_nsip6_binding resources.
		"""
		try :
			if not name :
				obj = rnat6_nsip6_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = rnat6_nsip6_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of rnat6_nsip6_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rnat6_nsip6_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count rnat6_nsip6_binding resources configued on NetScaler.
		"""
		try :
			obj = rnat6_nsip6_binding()
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
		r""" Use this API to count the filtered set of rnat6_nsip6_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rnat6_nsip6_binding()
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

class rnat6_nsip6_binding_response(base_response) :
	def __init__(self, length=1) :
		self.rnat6_nsip6_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rnat6_nsip6_binding = [rnat6_nsip6_binding() for _ in range(length)]

