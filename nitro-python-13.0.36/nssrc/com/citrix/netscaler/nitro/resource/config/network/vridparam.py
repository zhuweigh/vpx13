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

class vridparam(base_resource) :
	""" Configuration for VR ID parameter resource. """
	def __init__(self) :
		self._sendtomaster = None
		self._hellointerval = None
		self._deadinterval = None

	@property
	def sendtomaster(self) :
		r"""Forward packets to the master node, in an active-active mode configuration, if the virtual server is in the backup state and sharing is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sendtomaster
		except Exception as e:
			raise e

	@sendtomaster.setter
	def sendtomaster(self, sendtomaster) :
		r"""Forward packets to the master node, in an active-active mode configuration, if the virtual server is in the backup state and sharing is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sendtomaster = sendtomaster
		except Exception as e:
			raise e

	@property
	def hellointerval(self) :
		r"""Interval, in milliseconds, between vrrp advertisement messages sent to the peer node in active-active mode.<br/>Default value: 1000<br/>Minimum length =  200<br/>Maximum length =  1000.
		"""
		try :
			return self._hellointerval
		except Exception as e:
			raise e

	@hellointerval.setter
	def hellointerval(self, hellointerval) :
		r"""Interval, in milliseconds, between vrrp advertisement messages sent to the peer node in active-active mode.<br/>Default value: 1000<br/>Minimum length =  200<br/>Maximum length =  1000
		"""
		try :
			self._hellointerval = hellointerval
		except Exception as e:
			raise e

	@property
	def deadinterval(self) :
		r"""Number of seconds after which a peer node in active-active mode is marked down if vrrp advertisements are not received from the peer node.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  60.
		"""
		try :
			return self._deadinterval
		except Exception as e:
			raise e

	@deadinterval.setter
	def deadinterval(self, deadinterval) :
		r"""Number of seconds after which a peer node in active-active mode is marked down if vrrp advertisements are not received from the peer node.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  60
		"""
		try :
			self._deadinterval = deadinterval
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vridparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vridparam
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
	def update(cls, client, resource) :
		r""" Use this API to update vridparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = vridparam()
				updateresource.sendtomaster = resource.sendtomaster
				updateresource.hellointerval = resource.hellointerval
				updateresource.deadinterval = resource.deadinterval
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of vridparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vridparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vridparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vridparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Sendtomaster:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class vridparam_response(base_response) :
	def __init__(self, length=1) :
		self.vridparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vridparam = [vridparam() for _ in range(length)]

