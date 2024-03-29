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

class dnsnameserver(base_resource) :
	""" Configuration for name server resource. """
	def __init__(self) :
		self._ip = None
		self._dnsvservername = None
		self._local = None
		self._state = None
		self._type = None
		self._dnsprofilename = None
		self._servicename = None
		self._port = None
		self._nameserverstate = None
		self._clmonowner = None
		self._clmonview = None
		self.___count = None

	@property
	def ip(self) :
		r"""IP address of an external name server or, if the Local parameter is set, IP address of a local DNS server (LDNS).<br/>Minimum length =  1.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@ip.setter
	def ip(self, ip) :
		r"""IP address of an external name server or, if the Local parameter is set, IP address of a local DNS server (LDNS).<br/>Minimum length =  1
		"""
		try :
			self._ip = ip
		except Exception as e:
			raise e

	@property
	def dnsvservername(self) :
		r"""Name of a DNS virtual server. Overrides any IP address-based name servers configured on the Citrix ADC.<br/>Minimum length =  1.
		"""
		try :
			return self._dnsvservername
		except Exception as e:
			raise e

	@dnsvservername.setter
	def dnsvservername(self, dnsvservername) :
		r"""Name of a DNS virtual server. Overrides any IP address-based name servers configured on the Citrix ADC.<br/>Minimum length =  1
		"""
		try :
			self._dnsvservername = dnsvservername
		except Exception as e:
			raise e

	@property
	def local(self) :
		r"""Mark the IP address as one that belongs to a local recursive DNS server on the Citrix ADC. The appliance recursively resolves queries received on an IP address that is marked as being local. For recursive resolution to work, the global DNS parameter, Recursion, must also be set. 
		If no name server is marked as being local, the appliance functions as a stub resolver and load balances the name servers.
		"""
		try :
			return self._local
		except Exception as e:
			raise e

	@local.setter
	def local(self, local) :
		r"""Mark the IP address as one that belongs to a local recursive DNS server on the Citrix ADC. The appliance recursively resolves queries received on an IP address that is marked as being local. For recursive resolution to work, the global DNS parameter, Recursion, must also be set. 
		If no name server is marked as being local, the appliance functions as a stub resolver and load balances the name servers.
		"""
		try :
			self._local = local
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Administrative state of the name server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Administrative state of the name server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Protocol used by the name server. UDP_TCP is not valid if the name server is a DNS virtual server configured on the appliance.<br/>Default value: UDP<br/>Possible values = UDP, TCP, UDP_TCP.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Protocol used by the name server. UDP_TCP is not valid if the name server is a DNS virtual server configured on the appliance.<br/>Default value: UDP<br/>Possible values = UDP, TCP, UDP_TCP
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def dnsprofilename(self) :
		r"""Name of the DNS profile to be associated with the name server.<br/>Minimum length =  1.
		"""
		try :
			return self._dnsprofilename
		except Exception as e:
			raise e

	@dnsprofilename.setter
	def dnsprofilename(self, dnsprofilename) :
		r"""Name of the DNS profile to be associated with the name server.<br/>Minimum length =  1
		"""
		try :
			self._dnsprofilename = dnsprofilename
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		r"""The name of the dns vserver.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Port of the service.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@property
	def nameserverstate(self) :
		r"""State of the server.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._nameserverstate
		except Exception as e:
			raise e

	@property
	def clmonowner(self) :
		r"""Tells the mon owner of the service.
		"""
		try :
			return self._clmonowner
		except Exception as e:
			raise e

	@property
	def clmonview(self) :
		r"""Tells the view id by which state of the service is updated.
		"""
		try :
			return self._clmonview
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsnameserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsnameserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ip is not None :
				return str(self.ip)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add dnsnameserver.
		"""
		try :
			if type(resource) is not list :
				addresource = dnsnameserver()
				addresource.ip = resource.ip
				addresource.dnsvservername = resource.dnsvservername
				addresource.local = resource.local
				addresource.state = resource.state
				addresource.type = resource.type
				addresource.dnsprofilename = resource.dnsprofilename
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnsnameserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].ip = resource[i].ip
						addresources[i].dnsvservername = resource[i].dnsvservername
						addresources[i].local = resource[i].local
						addresources[i].state = resource[i].state
						addresources[i].type = resource[i].type
						addresources[i].dnsprofilename = resource[i].dnsprofilename
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update dnsnameserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnsnameserver()
				updateresource.ip = resource.ip
				updateresource.dnsprofilename = resource.dnsprofilename
				updateresource.type = resource.type
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnsnameserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].ip = resource[i].ip
						updateresources[i].dnsprofilename = resource[i].dnsprofilename
						updateresources[i].type = resource[i].type
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of dnsnameserver resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnsnameserver()
				if type(resource) !=  type(unsetresource):
					unsetresource.ip = resource
				else :
					unsetresource.ip = resource.ip
					unsetresource.type = resource.type
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnsnameserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ip = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnsnameserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ip = resource[i].ip
							unsetresources[i].type = resource[i].type
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete dnsnameserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnsnameserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.ip = resource
				else :
					deleteresource.ip = resource.ip
					deleteresource.dnsvservername = resource.dnsvservername
					deleteresource.type = resource.type
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsnameserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ip = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsnameserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ip = resource[i].ip
							deleteresources[i].dnsvservername = resource[i].dnsvservername
							deleteresources[i].type = resource[i].type
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable dnsnameserver.
		"""
		try :
			if type(resource) is not list :
				enableresource = dnsnameserver()
				if type(resource) !=  type(enableresource):
					enableresource.ip = resource
				else :
					enableresource.ip = resource.ip
					enableresource.dnsvservername = resource.dnsvservername
					enableresource.type = resource.type
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ dnsnameserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].ip = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ dnsnameserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].ip = resource[i].ip
							enableresources[i].dnsvservername = resource[i].dnsvservername
							enableresources[i].type = resource[i].type
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable dnsnameserver.
		"""
		try :
			if type(resource) is not list :
				disableresource = dnsnameserver()
				if type(resource) !=  type(disableresource):
					disableresource.ip = resource
				else :
					disableresource.ip = resource.ip
					disableresource.dnsvservername = resource.dnsvservername
					disableresource.type = resource.type
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ dnsnameserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].ip = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ dnsnameserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].ip = resource[i].ip
							disableresources[i].dnsvservername = resource[i].dnsvservername
							disableresources[i].type = resource[i].type
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the dnsnameserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsnameserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) != cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) != cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [dnsnameserver() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of dnsnameserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsnameserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the dnsnameserver resources configured on NetScaler.
		"""
		try :
			obj = dnsnameserver()
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
		r""" Use this API to count filtered the set of dnsnameserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsnameserver()
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

	class Type:
		UDP = "UDP"
		TCP = "TCP"
		UDP_TCP = "UDP_TCP"

	class Nameserverstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

class dnsnameserver_response(base_response) :
	def __init__(self, length=1) :
		self.dnsnameserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsnameserver = [dnsnameserver() for _ in range(length)]

