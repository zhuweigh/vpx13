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

class nssimpleacl6(base_resource) :
	""" Configuration for simple ACL6 resource. """
	def __init__(self) :
		self._aclname = None
		self._td = None
		self._aclaction = None
		self._srcipv6 = None
		self._destport = None
		self._protocol = None
		self._ttl = None
		self._estsessions = None
		self._hits = None
		self.___count = None

	@property
	def aclname(self) :
		r"""Name for the simple ACL6 rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the simple ACL6 rule is created.<br/>Minimum length =  1.
		"""
		try :
			return self._aclname
		except Exception as e:
			raise e

	@aclname.setter
	def aclname(self, aclname) :
		r"""Name for the simple ACL6 rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the simple ACL6 rule is created.<br/>Minimum length =  1
		"""
		try :
			self._aclname = aclname
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def aclaction(self) :
		r"""Drop incoming IPv6 packets that match the simple ACL6 rule.<br/>Possible values = DENY.
		"""
		try :
			return self._aclaction
		except Exception as e:
			raise e

	@aclaction.setter
	def aclaction(self, aclaction) :
		r"""Drop incoming IPv6 packets that match the simple ACL6 rule.<br/>Possible values = DENY
		"""
		try :
			self._aclaction = aclaction
		except Exception as e:
			raise e

	@property
	def srcipv6(self) :
		r"""IP address to match against the source IP address of an incoming IPv6 packet.
		"""
		try :
			return self._srcipv6
		except Exception as e:
			raise e

	@srcipv6.setter
	def srcipv6(self, srcipv6) :
		r"""IP address to match against the source IP address of an incoming IPv6 packet.
		"""
		try :
			self._srcipv6 = srcipv6
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""Port number to match against the destination port number of an incoming IPv6 packet.
		DestPort is mandatory while setting Protocol. Omitting the port number and protocol creates an all-ports  and all protocol simple ACL6 rule, which matches any port and any protocol. In that case, you cannot create another simple ACL6 rule specifying a specific port and the same source IPv6 address.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		r"""Port number to match against the destination port number of an incoming IPv6 packet.
		DestPort is mandatory while setting Protocol. Omitting the port number and protocol creates an all-ports  and all protocol simple ACL6 rule, which matches any port and any protocol. In that case, you cannot create another simple ACL6 rule specifying a specific port and the same source IPv6 address.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def protocol(self) :
		r"""Protocol to match against the protocol of an incoming IPv6 packet. You must set this parameter if you set the Destination Port parameter.<br/>Possible values = TCP, UDP.
		"""
		try :
			return self._protocol
		except Exception as e:
			raise e

	@protocol.setter
	def protocol(self, protocol) :
		r"""Protocol to match against the protocol of an incoming IPv6 packet. You must set this parameter if you set the Destination Port parameter.<br/>Possible values = TCP, UDP
		"""
		try :
			self._protocol = protocol
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r"""Number of seconds, in multiples of four, after which the simple ACL6 rule expires. If you do not want the simple ACL6 rule to expire, do not specify a TTL value.<br/>Minimum length =  4<br/>Maximum length =  0x7FFFFFFF.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		r"""Number of seconds, in multiples of four, after which the simple ACL6 rule expires. If you do not want the simple ACL6 rule to expire, do not specify a TTL value.<br/>Minimum length =  4<br/>Maximum length =  0x7FFFFFFF
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def estsessions(self) :
		try :
			return self._estsessions
		except Exception as e:
			raise e

	@estsessions.setter
	def estsessions(self, estsessions) :
		try :
			self._estsessions = estsessions
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""Number of hits for this SACL6 rule.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nssimpleacl6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nssimpleacl6
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.aclname is not None :
				return str(self.aclname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nssimpleacl6.
		"""
		try :
			if type(resource) is not list :
				addresource = nssimpleacl6()
				addresource.aclname = resource.aclname
				addresource.td = resource.td
				addresource.aclaction = resource.aclaction
				addresource.srcipv6 = resource.srcipv6
				addresource.destport = resource.destport
				addresource.protocol = resource.protocol
				addresource.ttl = resource.ttl
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nssimpleacl6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].aclname = resource[i].aclname
						addresources[i].td = resource[i].td
						addresources[i].aclaction = resource[i].aclaction
						addresources[i].srcipv6 = resource[i].srcipv6
						addresources[i].destport = resource[i].destport
						addresources[i].protocol = resource[i].protocol
						addresources[i].ttl = resource[i].ttl
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource="") :
		r""" Use this API to clear nssimpleacl6.
		"""
		try :
			if type(resource) is not list :
				clearresource = nssimpleacl6()
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ nssimpleacl6() for _ in range(len(resource))]
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def flush(cls, client, resource) :
		r""" Use this API to flush nssimpleacl6.
		"""
		try :
			if type(resource) is not list :
				flushresource = nssimpleacl6()
				flushresource.estsessions = resource.estsessions
				return flushresource.perform_operation(client,"flush")
			else :
				if (resource and len(resource) > 0) :
					flushresources = [ nssimpleacl6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						flushresources[i].estsessions = resource[i].estsessions
				result = cls.perform_operation_bulk_request(client, flushresources,"flush")
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nssimpleacl6.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nssimpleacl6()
				if type(resource) !=  type(deleteresource):
					deleteresource.aclname = resource
				else :
					deleteresource.aclname = resource.aclname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nssimpleacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nssimpleacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].aclname = resource[i].aclname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nssimpleacl6 resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nssimpleacl6()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nssimpleacl6()
					obj.aclname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nssimpleacl6() for _ in range(len(name))]
						obj = [nssimpleacl6() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nssimpleacl6()
							obj[i].aclname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nssimpleacl6 resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nssimpleacl6()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nssimpleacl6 resources configured on NetScaler.
		"""
		try :
			obj = nssimpleacl6()
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
		r""" Use this API to count filtered the set of nssimpleacl6 resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nssimpleacl6()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Protocol:
		TCP = "TCP"
		UDP = "UDP"

	class Aclaction:
		DENY = "DENY"

class nssimpleacl6_response(base_response) :
	def __init__(self, length=1) :
		self.nssimpleacl6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nssimpleacl6 = [nssimpleacl6() for _ in range(length)]

