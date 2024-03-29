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

class cspolicy_csvserver_binding(base_resource) :
	""" Binding class showing the csvserver that can be bound to cspolicy.
	"""
	def __init__(self) :
		self._domain = None
		self._action = None
		self._url = None
		self._priority = None
		self._hits = None
		self._pihits = None
		self._pipolicyhits = None
		self._labeltype = None
		self._labelname = None
		self._policyname = None
		self.___count = None

	@property
	def policyname(self) :
		r"""Name of the content switching policy to display. If this parameter is omitted, details of all the policies are displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		r"""Name of the content switching policy to display. If this parameter is omitted, details of all the policies are displayed.<br/>Minimum length =  1
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def domain(self) :
		r"""The domain name. The string value can range to 63 characters.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		r"""The domain name. The string value can range to 63 characters.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""priority of bound policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""Total number of hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def url(self) :
		r"""URL string that is matched with the URL of a request. Can contain a wildcard character. Specify the string value in the following format: [[prefix] [*]] [.suffix].<br/>Minimum length =  1<br/>Maximum length =  208.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@property
	def pipolicyhits(self) :
		r"""bind hits for PI CS Policy.
		"""
		try :
			return self._pipolicyhits
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		r"""The invocation type.<br/>Possible values = reqvserver, resvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		r"""Name of the label invoked.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@property
	def pihits(self) :
		r"""Total number of hits.
		"""
		try :
			return self._pihits
		except Exception as e:
			raise e

	@property
	def action(self) :
		r"""Content switching action that names the target load balancing virtual server to which the traffic is switched.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cspolicy_csvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cspolicy_csvserver_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.policyname is not None :
				return str(self.policyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, policyname="", option_="") :
		r""" Use this API to fetch cspolicy_csvserver_binding resources.
		"""
		try :
			if not policyname :
				obj = cspolicy_csvserver_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = cspolicy_csvserver_binding()
				obj.policyname = policyname
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, policyname, filter_) :
		r""" Use this API to fetch filtered set of cspolicy_csvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cspolicy_csvserver_binding()
			obj.policyname = policyname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, policyname) :
		r""" Use this API to count cspolicy_csvserver_binding resources configued on NetScaler.
		"""
		try :
			obj = cspolicy_csvserver_binding()
			obj.policyname = policyname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, policyname, filter_) :
		r""" Use this API to count the filtered set of cspolicy_csvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cspolicy_csvserver_binding()
			obj.policyname = policyname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

class cspolicy_csvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.cspolicy_csvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cspolicy_csvserver_binding = [cspolicy_csvserver_binding() for _ in range(length)]

