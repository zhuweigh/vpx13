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

class icaaccessprofile(base_resource) :
	""" Configuration for ica accessprofile resource. """
	def __init__(self) :
		self._name = None
		self._connectclientlptports = None
		self._clientaudioredirection = None
		self._localremotedatasharing = None
		self._clientclipboardredirection = None
		self._clientcomportredirection = None
		self._clientdriveredirection = None
		self._clientprinterredirection = None
		self._multistream = None
		self._clientusbdriveredirection = None
		self._feature = None
		self._refcnt = None
		self._isdefault = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the ICA accessprofile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and
		the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the ICA accessprofile is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ica accessprofile" or 'my ica accessprofile').
		Each of the features can be configured as DEFAULT/DISABLED.
		Here, DISABLED means that the policy settings on the backend XenApp/XenDesktop server are overridden and the Citrix ADC makes the decision to deny access. Whereas DEFAULT means that the Citrix ADC allows the request to reach the XenApp/XenDesktop that takes the decision to allow/deny access based on the policy configured on it. For example, if ClientAudioRedirection is enabled on the backend XenApp/XenDesktop server, and the configured profile has ClientAudioRedirection as DISABLED, the Citrix ADC makes the decision to deny the request irrespective of the configuration on the backend. If the configured profile has ClientAudioRedirection as DEFAULT, then the Citrix ADC forwards the requests to the backend XenApp/XenDesktop server.It then makes the decision to allow/deny access based on the policy configured on it.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the ICA accessprofile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and
		the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the ICA accessprofile is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ica accessprofile" or 'my ica accessprofile').
		Each of the features can be configured as DEFAULT/DISABLED.
		Here, DISABLED means that the policy settings on the backend XenApp/XenDesktop server are overridden and the Citrix ADC makes the decision to deny access. Whereas DEFAULT means that the Citrix ADC allows the request to reach the XenApp/XenDesktop that takes the decision to allow/deny access based on the policy configured on it. For example, if ClientAudioRedirection is enabled on the backend XenApp/XenDesktop server, and the configured profile has ClientAudioRedirection as DISABLED, the Citrix ADC makes the decision to deny the request irrespective of the configuration on the backend. If the configured profile has ClientAudioRedirection as DEFAULT, then the Citrix ADC forwards the requests to the backend XenApp/XenDesktop server.It then makes the decision to allow/deny access based on the policy configured on it.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def connectclientlptports(self) :
		r"""Allow Default access/Disable automatic connection of LPT ports from the client when the user logs on.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED.
		"""
		try :
			return self._connectclientlptports
		except Exception as e:
			raise e

	@connectclientlptports.setter
	def connectclientlptports(self, connectclientlptports) :
		r"""Allow Default access/Disable automatic connection of LPT ports from the client when the user logs on.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED
		"""
		try :
			self._connectclientlptports = connectclientlptports
		except Exception as e:
			raise e

	@property
	def clientaudioredirection(self) :
		r"""Allow Default access/Disable applications hosted on the server to play sounds through a sound device installed on the client computer, also allows or prevents users to record audio input.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED.
		"""
		try :
			return self._clientaudioredirection
		except Exception as e:
			raise e

	@clientaudioredirection.setter
	def clientaudioredirection(self, clientaudioredirection) :
		r"""Allow Default access/Disable applications hosted on the server to play sounds through a sound device installed on the client computer, also allows or prevents users to record audio input.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED
		"""
		try :
			self._clientaudioredirection = clientaudioredirection
		except Exception as e:
			raise e

	@property
	def localremotedatasharing(self) :
		r"""Allow Default access/Disable file/data sharing via the Receiver for HTML5.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED.
		"""
		try :
			return self._localremotedatasharing
		except Exception as e:
			raise e

	@localremotedatasharing.setter
	def localremotedatasharing(self, localremotedatasharing) :
		r"""Allow Default access/Disable file/data sharing via the Receiver for HTML5.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED
		"""
		try :
			self._localremotedatasharing = localremotedatasharing
		except Exception as e:
			raise e

	@property
	def clientclipboardredirection(self) :
		r"""Allow Default access/Disable the clipboard on the client device to be mapped to the clipboard on the server.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED.
		"""
		try :
			return self._clientclipboardredirection
		except Exception as e:
			raise e

	@clientclipboardredirection.setter
	def clientclipboardredirection(self, clientclipboardredirection) :
		r"""Allow Default access/Disable the clipboard on the client device to be mapped to the clipboard on the server.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED
		"""
		try :
			self._clientclipboardredirection = clientclipboardredirection
		except Exception as e:
			raise e

	@property
	def clientcomportredirection(self) :
		r"""Allow Default access/Disable COM port redirection to and from the client.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED.
		"""
		try :
			return self._clientcomportredirection
		except Exception as e:
			raise e

	@clientcomportredirection.setter
	def clientcomportredirection(self, clientcomportredirection) :
		r"""Allow Default access/Disable COM port redirection to and from the client.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED
		"""
		try :
			self._clientcomportredirection = clientcomportredirection
		except Exception as e:
			raise e

	@property
	def clientdriveredirection(self) :
		r"""Allow Default access/Disables drive redirection to and from the client.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED.
		"""
		try :
			return self._clientdriveredirection
		except Exception as e:
			raise e

	@clientdriveredirection.setter
	def clientdriveredirection(self, clientdriveredirection) :
		r"""Allow Default access/Disables drive redirection to and from the client.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED
		"""
		try :
			self._clientdriveredirection = clientdriveredirection
		except Exception as e:
			raise e

	@property
	def clientprinterredirection(self) :
		r"""Allow Default access/Disable client printers to be mapped to a server when a user logs on to a session.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED.
		"""
		try :
			return self._clientprinterredirection
		except Exception as e:
			raise e

	@clientprinterredirection.setter
	def clientprinterredirection(self, clientprinterredirection) :
		r"""Allow Default access/Disable client printers to be mapped to a server when a user logs on to a session.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED
		"""
		try :
			self._clientprinterredirection = clientprinterredirection
		except Exception as e:
			raise e

	@property
	def multistream(self) :
		r"""Allow Default access/Disable the multistream feature for the specified users.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED.
		"""
		try :
			return self._multistream
		except Exception as e:
			raise e

	@multistream.setter
	def multistream(self, multistream) :
		r"""Allow Default access/Disable the multistream feature for the specified users.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED
		"""
		try :
			self._multistream = multistream
		except Exception as e:
			raise e

	@property
	def clientusbdriveredirection(self) :
		r"""Allow Default access/Disable the redirection of USB devices to and from the client.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED.
		"""
		try :
			return self._clientusbdriveredirection
		except Exception as e:
			raise e

	@clientusbdriveredirection.setter
	def clientusbdriveredirection(self, clientusbdriveredirection) :
		r"""Allow Default access/Disable the redirection of USB devices to and from the client.<br/>Default value: DISABLED<br/>Possible values = DEFAULT, DISABLED
		"""
		try :
			self._clientusbdriveredirection = clientusbdriveredirection
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	@feature.setter
	def feature(self, feature) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			self._feature = feature
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		r"""Number of entities using this accessprofile.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		r"""A value of true is returned if it is a default accessprofile.
		"""
		try :
			return self._isdefault
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(icaaccessprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.icaaccessprofile
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
		r""" Use this API to add icaaccessprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = icaaccessprofile()
				addresource.name = resource.name
				addresource.connectclientlptports = resource.connectclientlptports
				addresource.clientaudioredirection = resource.clientaudioredirection
				addresource.localremotedatasharing = resource.localremotedatasharing
				addresource.clientclipboardredirection = resource.clientclipboardredirection
				addresource.clientcomportredirection = resource.clientcomportredirection
				addresource.clientdriveredirection = resource.clientdriveredirection
				addresource.clientprinterredirection = resource.clientprinterredirection
				addresource.multistream = resource.multistream
				addresource.clientusbdriveredirection = resource.clientusbdriveredirection
				addresource.feature = resource.feature
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ icaaccessprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].connectclientlptports = resource[i].connectclientlptports
						addresources[i].clientaudioredirection = resource[i].clientaudioredirection
						addresources[i].localremotedatasharing = resource[i].localremotedatasharing
						addresources[i].clientclipboardredirection = resource[i].clientclipboardredirection
						addresources[i].clientcomportredirection = resource[i].clientcomportredirection
						addresources[i].clientdriveredirection = resource[i].clientdriveredirection
						addresources[i].clientprinterredirection = resource[i].clientprinterredirection
						addresources[i].multistream = resource[i].multistream
						addresources[i].clientusbdriveredirection = resource[i].clientusbdriveredirection
						addresources[i].feature = resource[i].feature
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete icaaccessprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = icaaccessprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ icaaccessprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ icaaccessprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update icaaccessprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = icaaccessprofile()
				updateresource.name = resource.name
				updateresource.connectclientlptports = resource.connectclientlptports
				updateresource.clientaudioredirection = resource.clientaudioredirection
				updateresource.localremotedatasharing = resource.localremotedatasharing
				updateresource.clientclipboardredirection = resource.clientclipboardredirection
				updateresource.clientcomportredirection = resource.clientcomportredirection
				updateresource.clientdriveredirection = resource.clientdriveredirection
				updateresource.clientprinterredirection = resource.clientprinterredirection
				updateresource.multistream = resource.multistream
				updateresource.clientusbdriveredirection = resource.clientusbdriveredirection
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ icaaccessprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].connectclientlptports = resource[i].connectclientlptports
						updateresources[i].clientaudioredirection = resource[i].clientaudioredirection
						updateresources[i].localremotedatasharing = resource[i].localremotedatasharing
						updateresources[i].clientclipboardredirection = resource[i].clientclipboardredirection
						updateresources[i].clientcomportredirection = resource[i].clientcomportredirection
						updateresources[i].clientdriveredirection = resource[i].clientdriveredirection
						updateresources[i].clientprinterredirection = resource[i].clientprinterredirection
						updateresources[i].multistream = resource[i].multistream
						updateresources[i].clientusbdriveredirection = resource[i].clientusbdriveredirection
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of icaaccessprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = icaaccessprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ icaaccessprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ icaaccessprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the icaaccessprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = icaaccessprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = icaaccessprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [icaaccessprofile() for _ in range(len(name))]
						obj = [icaaccessprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = icaaccessprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of icaaccessprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = icaaccessprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the icaaccessprofile resources configured on NetScaler.
		"""
		try :
			obj = icaaccessprofile()
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
		r""" Use this API to count filtered the set of icaaccessprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = icaaccessprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Localremotedatasharing:
		DEFAULT = "DEFAULT"
		DISABLED = "DISABLED"

	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"

	class Clientprinterredirection:
		DEFAULT = "DEFAULT"
		DISABLED = "DISABLED"

	class Clientclipboardredirection:
		DEFAULT = "DEFAULT"
		DISABLED = "DISABLED"

	class Clientcomportredirection:
		DEFAULT = "DEFAULT"
		DISABLED = "DISABLED"

	class Clientusbdriveredirection:
		DEFAULT = "DEFAULT"
		DISABLED = "DISABLED"

	class Connectclientlptports:
		DEFAULT = "DEFAULT"
		DISABLED = "DISABLED"

	class Clientaudioredirection:
		DEFAULT = "DEFAULT"
		DISABLED = "DISABLED"

	class Multistream:
		DEFAULT = "DEFAULT"
		DISABLED = "DISABLED"

	class Clientdriveredirection:
		DEFAULT = "DEFAULT"
		DISABLED = "DISABLED"

class icaaccessprofile_response(base_response) :
	def __init__(self, length=1) :
		self.icaaccessprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.icaaccessprofile = [icaaccessprofile() for _ in range(length)]

