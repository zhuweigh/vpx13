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

class systemsession(base_resource) :
	""" Configuration for system session resource. """
	def __init__(self) :
		self._sid = None
		self._all = None
		self._username = None
		self._logintime = None
		self._logintimelocal = None
		self._lastactivitytime = None
		self._lastactivitytimelocal = None
		self._expirytime = None
		self._numofconnections = None
		self._currentconn = None
		self._clienttype = None
		self._partitionname = None
		self.___count = None

	@property
	def sid(self) :
		r"""ID of the system session about which to display information.<br/>Minimum length =  1.
		"""
		try :
			return self._sid
		except Exception as e:
			raise e

	@sid.setter
	def sid(self, sid) :
		r"""ID of the system session about which to display information.<br/>Minimum length =  1
		"""
		try :
			self._sid = sid
		except Exception as e:
			raise e

	@property
	def all(self) :
		r"""Terminate all the system sessions except the current session.
		"""
		try :
			return self._all
		except Exception as e:
			raise e

	@all.setter
	def all(self, all) :
		r"""Terminate all the system sessions except the current session.
		"""
		try :
			self._all = all
		except Exception as e:
			raise e

	@property
	def username(self) :
		r"""user name of the session.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@property
	def logintime(self) :
		r"""logged-in time of this session.
		"""
		try :
			return self._logintime
		except Exception as e:
			raise e

	@property
	def logintimelocal(self) :
		r"""logged-in time (in local ADC timezone) of this session.
		"""
		try :
			return self._logintimelocal
		except Exception as e:
			raise e

	@property
	def lastactivitytime(self) :
		r"""last activity time of this session.
		"""
		try :
			return self._lastactivitytime
		except Exception as e:
			raise e

	@property
	def lastactivitytimelocal(self) :
		r"""last activity time (in local ADC timezone) of this session.
		"""
		try :
			return self._lastactivitytimelocal
		except Exception as e:
			raise e

	@property
	def expirytime(self) :
		r"""Time left in expire the session in seconds.
		"""
		try :
			return self._expirytime
		except Exception as e:
			raise e

	@property
	def numofconnections(self) :
		r"""number of connection using this token.
		"""
		try :
			return self._numofconnections
		except Exception as e:
			raise e

	@property
	def currentconn(self) :
		r"""True if the token is used for current session.
		"""
		try :
			return self._currentconn
		except Exception as e:
			raise e

	@property
	def clienttype(self) :
		r"""client type of the session.<br/>Possible values = CLI, API, GUI.
		"""
		try :
			return self._clienttype
		except Exception as e:
			raise e

	@property
	def partitionname(self) :
		r"""Name of the partition where the user is currently present.
		"""
		try :
			return self._partitionname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemsession_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemsession
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.sid is not None :
				return str(self.sid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def kill(cls, client, resource) :
		r""" Use this API to kill systemsession.
		"""
		try :
			if type(resource) is not list :
				killresource = systemsession()
				killresource.sid = resource.sid
				killresource.all = resource.all
				return killresource.perform_operation(client,"kill")
			else :
				if (resource and len(resource) > 0) :
					killresources = [ systemsession() for _ in range(len(resource))]
					for i in range(len(resource)) :
						killresources[i].sid = resource[i].sid
						killresources[i].all = resource[i].all
				result = cls.perform_operation_bulk_request(client, killresources,"kill")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the systemsession resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemsession()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = systemsession()
					obj.sid = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [systemsession() for _ in range(len(name))]
						obj = [systemsession() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = systemsession()
							obj[i].sid = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of systemsession resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemsession()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the systemsession resources configured on NetScaler.
		"""
		try :
			obj = systemsession()
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
		r""" Use this API to count filtered the set of systemsession resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemsession()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Clienttype:
		CLI = "CLI"
		API = "API"
		GUI = "GUI"

class systemsession_response(base_response) :
	def __init__(self, length=1) :
		self.systemsession = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemsession = [systemsession() for _ in range(length)]

