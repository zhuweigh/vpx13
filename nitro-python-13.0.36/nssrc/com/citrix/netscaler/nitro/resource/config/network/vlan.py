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

class vlan(base_resource) :
	""" Configuration for "VLAN" resource. """
	def __init__(self) :
		self._id = None
		self._aliasname = None
		self._dynamicrouting = None
		self._ipv6dynamicrouting = None
		self._mtu = None
		self._sharing = None
		self._linklocalipv6addr = None
		self._rnat = None
		self._portbitmap = None
		self._lsbitmap = None
		self._tagbitmap = None
		self._lstagbitmap = None
		self._ifaces = None
		self._tagifaces = None
		self._ifnum = None
		self._tagged = None
		self._vlantd = None
		self._sdxvlan = None
		self._partitionname = None
		self._vxlan = None
		self.___count = None

	@property
	def id(self) :
		r"""A positive integer that uniquely identifies a VLAN.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		r"""A positive integer that uniquely identifies a VLAN.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def aliasname(self) :
		r"""A name for the VLAN. Must begin with a letter, a number, or the underscore symbol, and can consist of from 1 to 31 letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters. You should choose a name that helps identify the VLAN. However, you cannot perform any VLAN operation by specifying this name instead of the VLAN ID.<br/>Maximum length =  31.
		"""
		try :
			return self._aliasname
		except Exception as e:
			raise e

	@aliasname.setter
	def aliasname(self, aliasname) :
		r"""A name for the VLAN. Must begin with a letter, a number, or the underscore symbol, and can consist of from 1 to 31 letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters. You should choose a name that helps identify the VLAN. However, you cannot perform any VLAN operation by specifying this name instead of the VLAN ID.<br/>Maximum length =  31
		"""
		try :
			self._aliasname = aliasname
		except Exception as e:
			raise e

	@property
	def dynamicrouting(self) :
		r"""Enable dynamic routing on this VLAN.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dynamicrouting
		except Exception as e:
			raise e

	@dynamicrouting.setter
	def dynamicrouting(self, dynamicrouting) :
		r"""Enable dynamic routing on this VLAN.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dynamicrouting = dynamicrouting
		except Exception as e:
			raise e

	@property
	def ipv6dynamicrouting(self) :
		r"""Enable all IPv6 dynamic routing protocols on this VLAN. Note: For the ENABLED setting to work, you must configure IPv6 dynamic routing protocols from the VTYSH command line.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ipv6dynamicrouting
		except Exception as e:
			raise e

	@ipv6dynamicrouting.setter
	def ipv6dynamicrouting(self, ipv6dynamicrouting) :
		r"""Enable all IPv6 dynamic routing protocols on this VLAN. Note: For the ENABLED setting to work, you must configure IPv6 dynamic routing protocols from the VTYSH command line.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ipv6dynamicrouting = ipv6dynamicrouting
		except Exception as e:
			raise e

	@property
	def mtu(self) :
		r"""Specifies the maximum transmission unit (MTU), in bytes. The MTU is the largest packet size, excluding 14 bytes of ethernet header and 4 bytes of crc, that can be transmitted and received over this VLAN.<br/>Default value: 0<br/>Minimum length =  500<br/>Maximum length =  9216.
		"""
		try :
			return self._mtu
		except Exception as e:
			raise e

	@mtu.setter
	def mtu(self, mtu) :
		r"""Specifies the maximum transmission unit (MTU), in bytes. The MTU is the largest packet size, excluding 14 bytes of ethernet header and 4 bytes of crc, that can be transmitted and received over this VLAN.<br/>Default value: 0<br/>Minimum length =  500<br/>Maximum length =  9216
		"""
		try :
			self._mtu = mtu
		except Exception as e:
			raise e

	@property
	def sharing(self) :
		r"""If sharing is enabled, then this vlan can be shared across multiple partitions by binding it to all those partitions. If sharing is disabled, then this vlan can be bound to only one of the partitions.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sharing
		except Exception as e:
			raise e

	@sharing.setter
	def sharing(self, sharing) :
		r"""If sharing is enabled, then this vlan can be shared across multiple partitions by binding it to all those partitions. If sharing is disabled, then this vlan can be bound to only one of the partitions.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sharing = sharing
		except Exception as e:
			raise e

	@property
	def linklocalipv6addr(self) :
		r"""The link-local IP address assigned to the VLAN.
		"""
		try :
			return self._linklocalipv6addr
		except Exception as e:
			raise e

	@property
	def rnat(self) :
		r"""Temporary flag used for internal purpose.
		"""
		try :
			return self._rnat
		except Exception as e:
			raise e

	@property
	def portbitmap(self) :
		r"""Member interfaces of this vlan.
		"""
		try :
			return self._portbitmap
		except Exception as e:
			raise e

	@property
	def lsbitmap(self) :
		r"""Member linksets of this vlan.
		"""
		try :
			return self._lsbitmap
		except Exception as e:
			raise e

	@property
	def tagbitmap(self) :
		r"""Tagged members of this vlan.
		"""
		try :
			return self._tagbitmap
		except Exception as e:
			raise e

	@property
	def lstagbitmap(self) :
		r"""Tagged linksets of this vlan.
		"""
		try :
			return self._lstagbitmap
		except Exception as e:
			raise e

	@property
	def ifaces(self) :
		r"""Names of all member interfaces of this vlan.
		"""
		try :
			return self._ifaces
		except Exception as e:
			raise e

	@property
	def tagifaces(self) :
		r"""Names of all tagged member interfaces of this vlan.
		"""
		try :
			return self._tagifaces
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		r"""The interface to be bound to the VLAN, specified in slot/port notation (for example, 1/3).<br/>Minimum length =  1.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@property
	def tagged(self) :
		r"""Make the interface an 802.1q tagged interface. Packets sent on this interface on this VLAN have an additional 4-byte 802.1q tag, which identifies the VLAN. To use 802.1q tagging, you must also configure the switch connected to the appliance's interfaces.
		"""
		try :
			return self._tagged
		except Exception as e:
			raise e

	@property
	def vlantd(self) :
		r"""Traffic domain associated with vlan.<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._vlantd
		except Exception as e:
			raise e

	@property
	def sdxvlan(self) :
		r"""SDX vlan.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._sdxvlan
		except Exception as e:
			raise e

	@property
	def partitionname(self) :
		r"""Name of the Partition to which this vlan bound to.<br/>Minimum length =  1.
		"""
		try :
			return self._partitionname
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		r"""The VXLAN that extends this vlan.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vlan_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vlan
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.id is not None :
				return str(self.id)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add vlan.
		"""
		try :
			if type(resource) is not list :
				addresource = vlan()
				addresource.id = resource.id
				addresource.aliasname = resource.aliasname
				addresource.dynamicrouting = resource.dynamicrouting
				addresource.ipv6dynamicrouting = resource.ipv6dynamicrouting
				addresource.mtu = resource.mtu
				addresource.sharing = resource.sharing
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vlan() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].id = resource[i].id
						addresources[i].aliasname = resource[i].aliasname
						addresources[i].dynamicrouting = resource[i].dynamicrouting
						addresources[i].ipv6dynamicrouting = resource[i].ipv6dynamicrouting
						addresources[i].mtu = resource[i].mtu
						addresources[i].sharing = resource[i].sharing
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete vlan.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vlan()
				if type(resource) !=  type(deleteresource):
					deleteresource.id = resource
				else :
					deleteresource.id = resource.id
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vlan() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vlan() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i].id
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update vlan.
		"""
		try :
			if type(resource) is not list :
				updateresource = vlan()
				updateresource.id = resource.id
				updateresource.aliasname = resource.aliasname
				updateresource.dynamicrouting = resource.dynamicrouting
				updateresource.ipv6dynamicrouting = resource.ipv6dynamicrouting
				updateresource.mtu = resource.mtu
				updateresource.sharing = resource.sharing
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vlan() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].aliasname = resource[i].aliasname
						updateresources[i].dynamicrouting = resource[i].dynamicrouting
						updateresources[i].ipv6dynamicrouting = resource[i].ipv6dynamicrouting
						updateresources[i].mtu = resource[i].mtu
						updateresources[i].sharing = resource[i].sharing
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of vlan resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vlan()
				if type(resource) !=  type(unsetresource):
					unsetresource.id = resource
				else :
					unsetresource.id = resource.id
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vlan() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vlan() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i].id
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vlan resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vlan()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = vlan()
					obj.id = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [vlan() for _ in range(len(name))]
						obj = [vlan() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = vlan()
							obj[i].id = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of vlan resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vlan()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the vlan resources configured on NetScaler.
		"""
		try :
			obj = vlan()
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
		r""" Use this API to count filtered the set of vlan resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vlan()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Ipv6dynamicrouting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sdxvlan:
		YES = "YES"
		NO = "NO"

	class Sharing:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dynamicrouting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class vlan_response(base_response) :
	def __init__(self, length=1) :
		self.vlan = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vlan = [vlan() for _ in range(length)]

