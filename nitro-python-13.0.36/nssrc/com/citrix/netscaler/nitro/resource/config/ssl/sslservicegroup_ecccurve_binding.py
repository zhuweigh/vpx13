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

class sslservicegroup_ecccurve_binding(base_resource) :
	""" Binding class showing the ecccurve that can be bound to sslservicegroup.
	"""
	def __init__(self) :
		self._ecccurvename = None
		self._servicegroupname = None
		self.___count = None

	@property
	def servicegroupname(self) :
		r"""The name of the SSL service to which the SSL policy needs to be bound.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""The name of the SSL service to which the SSL policy needs to be bound.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def ecccurvename(self) :
		r"""Named ECC curve bound to servicegroup.<br/>Possible values = ALL, P_224, P_256, P_384, P_521.
		"""
		try :
			return self._ecccurvename
		except Exception as e:
			raise e

	@ecccurvename.setter
	def ecccurvename(self, ecccurvename) :
		r"""Named ECC curve bound to servicegroup.<br/>Possible values = ALL, P_224, P_256, P_384, P_521
		"""
		try :
			self._ecccurvename = ecccurvename
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslservicegroup_ecccurve_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslservicegroup_ecccurve_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = sslservicegroup_ecccurve_binding()
				updateresource.servicegroupname = resource.servicegroupname
				updateresource.ecccurvename = resource.ecccurvename
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslservicegroup_ecccurve_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].servicegroupname = resource[i].servicegroupname
						updateresources[i].ecccurvename = resource[i].ecccurvename
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = sslservicegroup_ecccurve_binding()
				deleteresource.servicegroupname = resource.servicegroupname
				deleteresource.ecccurvename = resource.ecccurvename
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslservicegroup_ecccurve_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].servicegroupname = resource[i].servicegroupname
						deleteresources[i].ecccurvename = resource[i].ecccurvename
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, servicegroupname="", option_="") :
		r""" Use this API to fetch sslservicegroup_ecccurve_binding resources.
		"""
		try :
			if not servicegroupname :
				obj = sslservicegroup_ecccurve_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = sslservicegroup_ecccurve_binding()
				obj.servicegroupname = servicegroupname
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, servicegroupname, filter_) :
		r""" Use this API to fetch filtered set of sslservicegroup_ecccurve_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservicegroup_ecccurve_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, servicegroupname) :
		r""" Use this API to count sslservicegroup_ecccurve_binding resources configued on NetScaler.
		"""
		try :
			obj = sslservicegroup_ecccurve_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, servicegroupname, filter_) :
		r""" Use this API to count the filtered set of sslservicegroup_ecccurve_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservicegroup_ecccurve_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Ecccurvename:
		ALL = "ALL"
		P_224 = "P_224"
		P_256 = "P_256"
		P_384 = "P_384"
		P_521 = "P_521"

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

class sslservicegroup_ecccurve_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslservicegroup_ecccurve_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslservicegroup_ecccurve_binding = [sslservicegroup_ecccurve_binding() for _ in range(length)]

