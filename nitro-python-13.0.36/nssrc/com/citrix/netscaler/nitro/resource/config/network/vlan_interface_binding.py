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

class vlan_interface_binding(base_resource) :
	""" Binding class showing the interface that can be bound to vlan.
	"""
	def __init__(self) :
		self._ifnum = None
		self._tagged = None
		self._id = None
		self._ownergroup = None
		self.___count = None

	@property
	def ownergroup(self) :
		r"""The owner node group in a Cluster for this vlan.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1.
		"""
		try :
			return self._ownergroup
		except Exception as e:
			raise e

	@ownergroup.setter
	def ownergroup(self, ownergroup) :
		r"""The owner node group in a Cluster for this vlan.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1
		"""
		try :
			self._ownergroup = ownergroup
		except Exception as e:
			raise e

	@property
	def id(self) :
		r"""Specifies the virtual LAN ID.<br/>Minimum value =  1<br/>Maximum value =  4094.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		r"""Specifies the virtual LAN ID.<br/>Minimum value =  1<br/>Maximum value =  4094
		"""
		try :
			self._id = id
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

	@ifnum.setter
	def ifnum(self, ifnum) :
		r"""The interface to be bound to the VLAN, specified in slot/port notation (for example, 1/3).<br/>Minimum length =  1
		"""
		try :
			self._ifnum = ifnum
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

	@tagged.setter
	def tagged(self, tagged) :
		r"""Make the interface an 802.1q tagged interface. Packets sent on this interface on this VLAN have an additional 4-byte 802.1q tag, which identifies the VLAN. To use 802.1q tagging, you must also configure the switch connected to the appliance's interfaces.
		"""
		try :
			self._tagged = tagged
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vlan_interface_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vlan_interface_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = vlan_interface_binding()
				updateresource.id = resource.id
				updateresource.ifnum = resource.ifnum
				updateresource.tagged = resource.tagged
				updateresource.ownergroup = resource.ownergroup
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [vlan_interface_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].ifnum = resource[i].ifnum
						updateresources[i].tagged = resource[i].tagged
						updateresources[i].ownergroup = resource[i].ownergroup
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = vlan_interface_binding()
				deleteresource.id = resource.id
				deleteresource.ifnum = resource.ifnum
				deleteresource.tagged = resource.tagged
				deleteresource.ownergroup = resource.ownergroup
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [vlan_interface_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].id = resource[i].id
						deleteresources[i].ifnum = resource[i].ifnum
						deleteresources[i].tagged = resource[i].tagged
						deleteresources[i].ownergroup = resource[i].ownergroup
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, id="", option_="") :
		r""" Use this API to fetch vlan_interface_binding resources.
		"""
		try :
			if not id :
				obj = vlan_interface_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = vlan_interface_binding()
				obj.id = id
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, id, filter_) :
		r""" Use this API to fetch filtered set of vlan_interface_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vlan_interface_binding()
			obj.id = id
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, id) :
		r""" Use this API to count vlan_interface_binding resources configued on NetScaler.
		"""
		try :
			obj = vlan_interface_binding()
			obj.id = id
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, id, filter_) :
		r""" Use this API to count the filtered set of vlan_interface_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vlan_interface_binding()
			obj.id = id
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class vlan_interface_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vlan_interface_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vlan_interface_binding = [vlan_interface_binding() for _ in range(length)]

