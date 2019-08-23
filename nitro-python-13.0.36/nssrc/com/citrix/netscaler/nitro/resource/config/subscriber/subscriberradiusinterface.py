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

class subscriberradiusinterface(base_resource) :
	""" Configuration for RADIUS interface Parameters resource. """
	def __init__(self) :
		self._listeningservice = None
		self._radiusinterimasstart = None
		self._svrstate = None

	@property
	def listeningservice(self) :
		r"""Name of RADIUS LISTENING service that will process RADIUS accounting requests.<br/>Minimum length =  1.
		"""
		try :
			return self._listeningservice
		except Exception as e:
			raise e

	@listeningservice.setter
	def listeningservice(self, listeningservice) :
		r"""Name of RADIUS LISTENING service that will process RADIUS accounting requests.<br/>Minimum length =  1
		"""
		try :
			self._listeningservice = listeningservice
		except Exception as e:
			raise e

	@property
	def radiusinterimasstart(self) :
		r"""Treat radius interim message as start radius messages.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._radiusinterimasstart
		except Exception as e:
			raise e

	@radiusinterimasstart.setter
	def radiusinterimasstart(self, radiusinterimasstart) :
		r"""Treat radius interim message as start radius messages.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._radiusinterimasstart = radiusinterimasstart
		except Exception as e:
			raise e

	@property
	def svrstate(self) :
		r"""The state of the radius service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svrstate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(subscriberradiusinterface_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.subscriberradiusinterface
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
		r""" Use this API to update subscriberradiusinterface.
		"""
		try :
			if type(resource) is not list :
				updateresource = subscriberradiusinterface()
				updateresource.listeningservice = resource.listeningservice
				updateresource.radiusinterimasstart = resource.radiusinterimasstart
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of subscriberradiusinterface resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = subscriberradiusinterface()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the subscriberradiusinterface resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = subscriberradiusinterface()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Svrstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Radiusinterimasstart:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class subscriberradiusinterface_response(base_response) :
	def __init__(self, length=1) :
		self.subscriberradiusinterface = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.subscriberradiusinterface = [subscriberradiusinterface() for _ in range(length)]

