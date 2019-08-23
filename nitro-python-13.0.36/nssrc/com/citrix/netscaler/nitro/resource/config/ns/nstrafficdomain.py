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

class nstrafficdomain(base_resource) :
	""" Configuration for Traffic Domain resource. """
	def __init__(self) :
		self._td = None
		self._aliasname = None
		self._vmac = None
		self._state = None
		self.___count = None

	@property
	def td(self) :
		r"""Integer value that uniquely identifies a traffic domain.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies a traffic domain.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def aliasname(self) :
		r"""Name of traffic domain  being added.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._aliasname
		except Exception as e:
			raise e

	@aliasname.setter
	def aliasname(self, aliasname) :
		r"""Name of traffic domain  being added.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._aliasname = aliasname
		except Exception as e:
			raise e

	@property
	def vmac(self) :
		r"""Associate the traffic domain with a VMAC address instead of with VLANs. The Citrix ADC then sends the VMAC address of the traffic domain in all responses to ARP queries for network entities in that domain. As a result, the ADC can segregate subsequent incoming traffic for this traffic domain on the basis of the destination MAC address, because the destination MAC address is the VMAC address of the traffic domain. After creating entities on a traffic domain, you can easily manage and monitor them by performing traffic domain level operations.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._vmac
		except Exception as e:
			raise e

	@vmac.setter
	def vmac(self, vmac) :
		r"""Associate the traffic domain with a VMAC address instead of with VLANs. The Citrix ADC then sends the VMAC address of the traffic domain in all responses to ARP queries for network entities in that domain. As a result, the ADC can segregate subsequent incoming traffic for this traffic domain on the basis of the destination MAC address, because the destination MAC address is the VMAC address of the traffic domain. After creating entities on a traffic domain, you can easily manage and monitor them by performing traffic domain level operations.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._vmac = vmac
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""The state of TrafficDmain.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstrafficdomain_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstrafficdomain
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.td is not None :
				return str(self.td)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nstrafficdomain.
		"""
		try :
			if type(resource) is not list :
				addresource = nstrafficdomain()
				addresource.td = resource.td
				addresource.aliasname = resource.aliasname
				addresource.vmac = resource.vmac
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nstrafficdomain() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].td = resource[i].td
						addresources[i].aliasname = resource[i].aliasname
						addresources[i].vmac = resource[i].vmac
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nstrafficdomain.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nstrafficdomain()
				if type(resource) !=  type(deleteresource):
					deleteresource.td = resource
				else :
					deleteresource.td = resource.td
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nstrafficdomain() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].td = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nstrafficdomain() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].td = resource[i].td
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear nstrafficdomain.
		"""
		try :
			if type(resource) is not list :
				clearresource = nstrafficdomain()
				clearresource.td = resource.td
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ nstrafficdomain() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].td = resource[i].td
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable nstrafficdomain.
		"""
		try :
			if type(resource) is not list :
				enableresource = nstrafficdomain()
				if type(resource) !=  type(enableresource):
					enableresource.td = resource
				else :
					enableresource.td = resource.td
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ nstrafficdomain() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].td = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ nstrafficdomain() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].td = resource[i].td
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable nstrafficdomain.
		"""
		try :
			if type(resource) is not list :
				disableresource = nstrafficdomain()
				if type(resource) !=  type(disableresource):
					disableresource.td = resource
				else :
					disableresource.td = resource.td
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ nstrafficdomain() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].td = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ nstrafficdomain() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].td = resource[i].td
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nstrafficdomain resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nstrafficdomain()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nstrafficdomain()
					obj.td = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nstrafficdomain() for _ in range(len(name))]
						obj = [nstrafficdomain() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nstrafficdomain()
							obj[i].td = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nstrafficdomain resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nstrafficdomain()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nstrafficdomain resources configured on NetScaler.
		"""
		try :
			obj = nstrafficdomain()
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
		r""" Use this API to count filtered the set of nstrafficdomain resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nstrafficdomain()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Vmac:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nstrafficdomain_response(base_response) :
	def __init__(self, length=1) :
		self.nstrafficdomain = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstrafficdomain = [nstrafficdomain() for _ in range(length)]

