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

class vpnnexthopserver(base_resource) :
	""" Configuration for Next Hop Server resource. """
	def __init__(self) :
		self._name = None
		self._nexthopip = None
		self._nexthopfqdn = None
		self._resaddresstype = None
		self._nexthopport = None
		self._secure = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the Citrix Gateway appliance in the first DMZ.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the Citrix Gateway appliance in the first DMZ.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def nexthopip(self) :
		r"""IP address of the Citrix Gateway proxy in the second DMZ.
		"""
		try :
			return self._nexthopip
		except Exception as e:
			raise e

	@nexthopip.setter
	def nexthopip(self, nexthopip) :
		r"""IP address of the Citrix Gateway proxy in the second DMZ.
		"""
		try :
			self._nexthopip = nexthopip
		except Exception as e:
			raise e

	@property
	def nexthopfqdn(self) :
		r"""FQDN of the Citrix Gateway proxy in the second DMZ.<br/>Minimum length =  1.
		"""
		try :
			return self._nexthopfqdn
		except Exception as e:
			raise e

	@nexthopfqdn.setter
	def nexthopfqdn(self, nexthopfqdn) :
		r"""FQDN of the Citrix Gateway proxy in the second DMZ.<br/>Minimum length =  1
		"""
		try :
			self._nexthopfqdn = nexthopfqdn
		except Exception as e:
			raise e

	@property
	def resaddresstype(self) :
		r"""Address Type (IPV4/IPv6) of DNS name of nextHopServer FQDN.<br/>Minimum length =  1<br/>Possible values = IPV4, IPV6.
		"""
		try :
			return self._resaddresstype
		except Exception as e:
			raise e

	@resaddresstype.setter
	def resaddresstype(self, resaddresstype) :
		r"""Address Type (IPV4/IPv6) of DNS name of nextHopServer FQDN.<br/>Minimum length =  1<br/>Possible values = IPV4, IPV6
		"""
		try :
			self._resaddresstype = resaddresstype
		except Exception as e:
			raise e

	@property
	def nexthopport(self) :
		r"""Port number of the Citrix Gateway proxy in the second DMZ.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._nexthopport
		except Exception as e:
			raise e

	@nexthopport.setter
	def nexthopport(self, nexthopport) :
		r"""Port number of the Citrix Gateway proxy in the second DMZ.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._nexthopport = nexthopport
		except Exception as e:
			raise e

	@property
	def secure(self) :
		r"""Use of a secure port, such as 443, for the double-hop configuration.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._secure
		except Exception as e:
			raise e

	@secure.setter
	def secure(self, secure) :
		r"""Use of a secure port, such as 443, for the double-hop configuration.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._secure = secure
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnnexthopserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnnexthopserver
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
		r""" Use this API to add vpnnexthopserver.
		"""
		try :
			if type(resource) is not list :
				addresource = vpnnexthopserver()
				addresource.name = resource.name
				addresource.nexthopip = resource.nexthopip
				addresource.nexthopfqdn = resource.nexthopfqdn
				addresource.resaddresstype = resource.resaddresstype
				addresource.nexthopport = resource.nexthopport
				addresource.secure = resource.secure
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnnexthopserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].nexthopip = resource[i].nexthopip
						addresources[i].nexthopfqdn = resource[i].nexthopfqdn
						addresources[i].resaddresstype = resource[i].resaddresstype
						addresources[i].nexthopport = resource[i].nexthopport
						addresources[i].secure = resource[i].secure
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete vpnnexthopserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnnexthopserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnnexthopserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnnexthopserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vpnnexthopserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnnexthopserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = vpnnexthopserver()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [vpnnexthopserver() for _ in range(len(name))]
						obj = [vpnnexthopserver() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = vpnnexthopserver()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of vpnnexthopserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnnexthopserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the vpnnexthopserver resources configured on NetScaler.
		"""
		try :
			obj = vpnnexthopserver()
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
		r""" Use this API to count filtered the set of vpnnexthopserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnnexthopserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Secure:
		ON = "ON"
		OFF = "OFF"

	class Resaddresstype:
		IPV4 = "IPV4"
		IPV6 = "IPV6"

class vpnnexthopserver_response(base_response) :
	def __init__(self, length=1) :
		self.vpnnexthopserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnnexthopserver = [vpnnexthopserver() for _ in range(length)]

