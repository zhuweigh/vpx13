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

class nsaptlicense(base_resource) :
	""" Configuration for aptlicense resource. """
	def __init__(self) :
		self._serialno = None
		self._useproxy = None
		self._id = None
		self._sessionid = None
		self._bindtype = None
		self._countavailable = None
		self._licensedir = None
		self._response = None
		self._counttotal = None
		self._name = None
		self._relevance = None
		self._datepurchased = None
		self._datesa = None
		self._dateexp = None
		self._features = None
		self.___count = None

	@property
	def serialno(self) :
		r"""Hardware Serial Number/License Activation Code(LAC).
		"""
		try :
			return self._serialno
		except Exception as e:
			raise e

	@serialno.setter
	def serialno(self, serialno) :
		r"""Hardware Serial Number/License Activation Code(LAC).
		"""
		try :
			self._serialno = serialno
		except Exception as e:
			raise e

	@property
	def useproxy(self) :
		r"""Specifies whether to use the licenseproxyserver to reach the internet. Make sure to configure licenseproxyserver to use this option.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._useproxy
		except Exception as e:
			raise e

	@useproxy.setter
	def useproxy(self, useproxy) :
		r"""Specifies whether to use the licenseproxyserver to reach the internet. Make sure to configure licenseproxyserver to use this option.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._useproxy = useproxy
		except Exception as e:
			raise e

	@property
	def id(self) :
		r"""License ID.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		r"""License ID.
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def sessionid(self) :
		r"""Session ID.
		"""
		try :
			return self._sessionid
		except Exception as e:
			raise e

	@sessionid.setter
	def sessionid(self, sessionid) :
		r"""Session ID.
		"""
		try :
			self._sessionid = sessionid
		except Exception as e:
			raise e

	@property
	def bindtype(self) :
		r"""Bind type.
		"""
		try :
			return self._bindtype
		except Exception as e:
			raise e

	@bindtype.setter
	def bindtype(self, bindtype) :
		r"""Bind type.
		"""
		try :
			self._bindtype = bindtype
		except Exception as e:
			raise e

	@property
	def countavailable(self) :
		r"""The user can allocate one or more licenses. Ensure the value is less than (for partial allocation) or equal to the total number of available licenses.
		"""
		try :
			return self._countavailable
		except Exception as e:
			raise e

	@countavailable.setter
	def countavailable(self, countavailable) :
		r"""The user can allocate one or more licenses. Ensure the value is less than (for partial allocation) or equal to the total number of available licenses.
		"""
		try :
			self._countavailable = countavailable
		except Exception as e:
			raise e

	@property
	def licensedir(self) :
		r"""License Directory.
		"""
		try :
			return self._licensedir
		except Exception as e:
			raise e

	@licensedir.setter
	def licensedir(self, licensedir) :
		r"""License Directory.
		"""
		try :
			self._licensedir = licensedir
		except Exception as e:
			raise e

	@property
	def response(self) :
		r"""Response data as text blob.
		"""
		try :
			return self._response
		except Exception as e:
			raise e

	@property
	def counttotal(self) :
		r"""Count.
		"""
		try :
			return self._counttotal
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""License name.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@property
	def relevance(self) :
		r"""License relevance.
		"""
		try :
			return self._relevance
		except Exception as e:
			raise e

	@property
	def datepurchased(self) :
		r"""License purchase date.
		"""
		try :
			return self._datepurchased
		except Exception as e:
			raise e

	@property
	def datesa(self) :
		r"""License SA date.
		"""
		try :
			return self._datesa
		except Exception as e:
			raise e

	@property
	def dateexp(self) :
		r"""License expiry date.
		"""
		try :
			return self._dateexp
		except Exception as e:
			raise e

	@property
	def features(self) :
		r"""Features.
		"""
		try :
			return self._features
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsaptlicense_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsaptlicense
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def change(cls, client, resource) :
		r""" Use this API to change nsaptlicense.
		"""
		try :
			if type(resource) is not list :
				changeresource = nsaptlicense()
				changeresource.id = resource.id
				changeresource.sessionid = resource.sessionid
				changeresource.bindtype = resource.bindtype
				changeresource.countavailable = resource.countavailable
				changeresource.licensedir = resource.licensedir
				changeresource.useproxy = resource.useproxy
				return changeresource.perform_operation(client,"update")
			else :
				if (resource and len(resource) > 0) :
					changeresources = [ nsaptlicense() for _ in range(len(resource))]
					for i in range(len(resource)) :
						changeresources[i].id = resource[i].id
						changeresources[i].sessionid = resource[i].sessionid
						changeresources[i].bindtype = resource[i].bindtype
						changeresources[i].countavailable = resource[i].countavailable
						changeresources[i].licensedir = resource[i].licensedir
						changeresources[i].useproxy = resource[i].useproxy
				result = cls.perform_operation_bulk_request(client, changeresources,"update")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsaptlicense resources that are configured on netscaler.
		"""
		try :
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the nsaptlicense resources that are configured on netscaler.
	# This uses nsaptlicense_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nsaptlicense()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client, obj) :
		r""" Use this API to count the nsaptlicense resources configured on NetScaler.
		"""
		try :
			option_ = options()
			option_.count = True
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	class Useproxy:
		YES = "YES"
		NO = "NO"

class nsaptlicense_response(base_response) :
	def __init__(self, length=1) :
		self.nsaptlicense = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsaptlicense = [nsaptlicense() for _ in range(length)]

