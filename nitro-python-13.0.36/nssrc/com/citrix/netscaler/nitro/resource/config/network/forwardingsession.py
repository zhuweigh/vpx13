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

class forwardingsession(base_resource) :
	""" Configuration for session forward resource. """
	def __init__(self) :
		self._name = None
		self._network = None
		self._netmask = None
		self._acl6name = None
		self._aclname = None
		self._td = None
		self._connfailover = None
		self._sourceroutecache = None
		self._processlocal = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the forwarding session rule. Can begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the rule is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my rule" or 'my rule').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the forwarding session rule. Can begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the rule is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my rule" or 'my rule').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def network(self) :
		r"""An IPv4 network address or IPv6 prefix of a network from which the forwarded traffic originates or to which it is destined.<br/>Minimum length =  1.
		"""
		try :
			return self._network
		except Exception as e:
			raise e

	@network.setter
	def network(self, network) :
		r"""An IPv4 network address or IPv6 prefix of a network from which the forwarded traffic originates or to which it is destined.<br/>Minimum length =  1
		"""
		try :
			self._network = network
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		r"""Subnet mask associated with the network.<br/>Minimum length =  1.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		r"""Subnet mask associated with the network.<br/>Minimum length =  1
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def acl6name(self) :
		r"""Name of any configured ACL6 whose action is ALLOW. The rule of the ACL6 is used as a forwarding session rule.<br/>Minimum length =  1.
		"""
		try :
			return self._acl6name
		except Exception as e:
			raise e

	@acl6name.setter
	def acl6name(self, acl6name) :
		r"""Name of any configured ACL6 whose action is ALLOW. The rule of the ACL6 is used as a forwarding session rule.<br/>Minimum length =  1
		"""
		try :
			self._acl6name = acl6name
		except Exception as e:
			raise e

	@property
	def aclname(self) :
		r"""Name of any configured ACL whose action is ALLOW. The rule of the ACL is used as a forwarding session rule.<br/>Minimum length =  1.
		"""
		try :
			return self._aclname
		except Exception as e:
			raise e

	@aclname.setter
	def aclname(self, aclname) :
		r"""Name of any configured ACL whose action is ALLOW. The rule of the ACL is used as a forwarding session rule.<br/>Minimum length =  1
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
	def connfailover(self) :
		r"""Synchronize connection information with the secondary appliance in a high availability (HA) pair. That is, synchronize all connection-related information for the forwarding session.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._connfailover
		except Exception as e:
			raise e

	@connfailover.setter
	def connfailover(self, connfailover) :
		r"""Synchronize connection information with the secondary appliance in a high availability (HA) pair. That is, synchronize all connection-related information for the forwarding session.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._connfailover = connfailover
		except Exception as e:
			raise e

	@property
	def sourceroutecache(self) :
		r"""Cache the source ip address and mac address of the DA servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sourceroutecache
		except Exception as e:
			raise e

	@sourceroutecache.setter
	def sourceroutecache(self, sourceroutecache) :
		r"""Cache the source ip address and mac address of the DA servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sourceroutecache = sourceroutecache
		except Exception as e:
			raise e

	@property
	def processlocal(self) :
		r"""Enabling this option on forwarding session will not steer the packet to flow processor. Instead, packet will be routed.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._processlocal
		except Exception as e:
			raise e

	@processlocal.setter
	def processlocal(self, processlocal) :
		r"""Enabling this option on forwarding session will not steer the packet to flow processor. Instead, packet will be routed.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._processlocal = processlocal
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(forwardingsession_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.forwardingsession
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
		r""" Use this API to add forwardingsession.
		"""
		try :
			if type(resource) is not list :
				addresource = forwardingsession()
				addresource.name = resource.name
				addresource.network = resource.network
				addresource.netmask = resource.netmask
				addresource.acl6name = resource.acl6name
				addresource.aclname = resource.aclname
				addresource.td = resource.td
				addresource.connfailover = resource.connfailover
				addresource.sourceroutecache = resource.sourceroutecache
				addresource.processlocal = resource.processlocal
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ forwardingsession() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].network = resource[i].network
						addresources[i].netmask = resource[i].netmask
						addresources[i].acl6name = resource[i].acl6name
						addresources[i].aclname = resource[i].aclname
						addresources[i].td = resource[i].td
						addresources[i].connfailover = resource[i].connfailover
						addresources[i].sourceroutecache = resource[i].sourceroutecache
						addresources[i].processlocal = resource[i].processlocal
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update forwardingsession.
		"""
		try :
			if type(resource) is not list :
				updateresource = forwardingsession()
				updateresource.name = resource.name
				updateresource.connfailover = resource.connfailover
				updateresource.sourceroutecache = resource.sourceroutecache
				updateresource.processlocal = resource.processlocal
				updateresource.acl6name = resource.acl6name
				updateresource.aclname = resource.aclname
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ forwardingsession() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].connfailover = resource[i].connfailover
						updateresources[i].sourceroutecache = resource[i].sourceroutecache
						updateresources[i].processlocal = resource[i].processlocal
						updateresources[i].acl6name = resource[i].acl6name
						updateresources[i].aclname = resource[i].aclname
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete forwardingsession.
		"""
		try :
			if type(resource) is not list :
				deleteresource = forwardingsession()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ forwardingsession() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ forwardingsession() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the forwardingsession resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = forwardingsession()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = forwardingsession()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [forwardingsession() for _ in range(len(name))]
						obj = [forwardingsession() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = forwardingsession()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of forwardingsession resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = forwardingsession()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the forwardingsession resources configured on NetScaler.
		"""
		try :
			obj = forwardingsession()
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
		r""" Use this API to count filtered the set of forwardingsession resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = forwardingsession()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Processlocal:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Connfailover:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sourceroutecache:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class forwardingsession_response(base_response) :
	def __init__(self, length=1) :
		self.forwardingsession = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.forwardingsession = [forwardingsession() for _ in range(length)]

