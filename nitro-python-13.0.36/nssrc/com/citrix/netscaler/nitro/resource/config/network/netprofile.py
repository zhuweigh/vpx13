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

class netprofile(base_resource) :
	""" Configuration for Network profile resource. """
	def __init__(self) :
		self._name = None
		self._td = None
		self._srcip = None
		self._srcippersistency = None
		self._overridelsn = None
		self._mbf = None
		self._proxyprotocol = None
		self._proxyprotocoltxversion = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the net profile. Must begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created. Choose a name that helps identify the net profile.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the net profile. Must begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created. Choose a name that helps identify the net profile.<br/>Minimum length =  1
		"""
		try :
			self._name = name
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
	def srcip(self) :
		r"""IP address or the name of an IP set.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@srcip.setter
	def srcip(self, srcip) :
		r"""IP address or the name of an IP set.
		"""
		try :
			self._srcip = srcip
		except Exception as e:
			raise e

	@property
	def srcippersistency(self) :
		r"""When the net profile is associated with a virtual server or its bound services, this option enables the Citrix ADC to use the same  address, specified in the net profile, to communicate to servers for all sessions initiated from a particular client to the virtual server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._srcippersistency
		except Exception as e:
			raise e

	@srcippersistency.setter
	def srcippersistency(self, srcippersistency) :
		r"""When the net profile is associated with a virtual server or its bound services, this option enables the Citrix ADC to use the same  address, specified in the net profile, to communicate to servers for all sessions initiated from a particular client to the virtual server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._srcippersistency = srcippersistency
		except Exception as e:
			raise e

	@property
	def overridelsn(self) :
		r"""USNIP/USIP settings override LSN settings for configured
		service/virtual server traffic.. .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._overridelsn
		except Exception as e:
			raise e

	@overridelsn.setter
	def overridelsn(self, overridelsn) :
		r"""USNIP/USIP settings override LSN settings for configured
		service/virtual server traffic.. .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._overridelsn = overridelsn
		except Exception as e:
			raise e

	@property
	def mbf(self) :
		r"""Response will be sent using learnt info if enabled. When creating a netprofile, if you do not set this parameter, the netprofile inherits the global MBF setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the netprofile.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mbf
		except Exception as e:
			raise e

	@mbf.setter
	def mbf(self, mbf) :
		r"""Response will be sent using learnt info if enabled. When creating a netprofile, if you do not set this parameter, the netprofile inherits the global MBF setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the netprofile.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mbf = mbf
		except Exception as e:
			raise e

	@property
	def proxyprotocol(self) :
		r"""Proxy Protocol Action (Enabled/Disabled).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._proxyprotocol
		except Exception as e:
			raise e

	@proxyprotocol.setter
	def proxyprotocol(self, proxyprotocol) :
		r"""Proxy Protocol Action (Enabled/Disabled).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._proxyprotocol = proxyprotocol
		except Exception as e:
			raise e

	@property
	def proxyprotocoltxversion(self) :
		r"""Proxy Protocol Version (V1/V2).<br/>Default value: V1<br/>Possible values = V1, V2.
		"""
		try :
			return self._proxyprotocoltxversion
		except Exception as e:
			raise e

	@proxyprotocoltxversion.setter
	def proxyprotocoltxversion(self, proxyprotocoltxversion) :
		r"""Proxy Protocol Version (V1/V2).<br/>Default value: V1<br/>Possible values = V1, V2
		"""
		try :
			self._proxyprotocoltxversion = proxyprotocoltxversion
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(netprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.netprofile
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
		r""" Use this API to add netprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = netprofile()
				addresource.name = resource.name
				addresource.td = resource.td
				addresource.srcip = resource.srcip
				addresource.srcippersistency = resource.srcippersistency
				addresource.overridelsn = resource.overridelsn
				addresource.mbf = resource.mbf
				addresource.proxyprotocol = resource.proxyprotocol
				addresource.proxyprotocoltxversion = resource.proxyprotocoltxversion
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ netprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].td = resource[i].td
						addresources[i].srcip = resource[i].srcip
						addresources[i].srcippersistency = resource[i].srcippersistency
						addresources[i].overridelsn = resource[i].overridelsn
						addresources[i].mbf = resource[i].mbf
						addresources[i].proxyprotocol = resource[i].proxyprotocol
						addresources[i].proxyprotocoltxversion = resource[i].proxyprotocoltxversion
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete netprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = netprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ netprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ netprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update netprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = netprofile()
				updateresource.name = resource.name
				updateresource.srcip = resource.srcip
				updateresource.srcippersistency = resource.srcippersistency
				updateresource.overridelsn = resource.overridelsn
				updateresource.mbf = resource.mbf
				updateresource.proxyprotocol = resource.proxyprotocol
				updateresource.proxyprotocoltxversion = resource.proxyprotocoltxversion
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ netprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].srcip = resource[i].srcip
						updateresources[i].srcippersistency = resource[i].srcippersistency
						updateresources[i].overridelsn = resource[i].overridelsn
						updateresources[i].mbf = resource[i].mbf
						updateresources[i].proxyprotocol = resource[i].proxyprotocol
						updateresources[i].proxyprotocoltxversion = resource[i].proxyprotocoltxversion
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of netprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = netprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ netprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ netprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the netprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = netprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = netprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [netprofile() for _ in range(len(name))]
						obj = [netprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = netprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of netprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = netprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the netprofile resources configured on NetScaler.
		"""
		try :
			obj = netprofile()
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
		r""" Use this API to count filtered the set of netprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = netprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Srcippersistency:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Proxyprotocol:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mbf:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Proxyprotocoltxversion:
		V1 = "V1"
		V2 = "V2"

	class Overridelsn:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class netprofile_response(base_response) :
	def __init__(self, length=1) :
		self.netprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.netprofile = [netprofile() for _ in range(length)]

