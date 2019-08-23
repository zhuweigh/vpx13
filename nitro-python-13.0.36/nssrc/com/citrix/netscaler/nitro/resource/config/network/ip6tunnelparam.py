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

class ip6tunnelparam(base_resource) :
	""" Configuration for ip6 tunnel parameter resource. """
	def __init__(self) :
		self._srcip = None
		self._dropfrag = None
		self._dropfragcputhreshold = None
		self._srciproundrobin = None
		self._useclientsourceipv6 = None

	@property
	def srcip(self) :
		r"""Common source IPv6 address for all IPv6 tunnels. Must be a SNIP6 or VIP6 address.<br/>Minimum length =  1.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@srcip.setter
	def srcip(self, srcip) :
		r"""Common source IPv6 address for all IPv6 tunnels. Must be a SNIP6 or VIP6 address.<br/>Minimum length =  1
		"""
		try :
			self._srcip = srcip
		except Exception as e:
			raise e

	@property
	def dropfrag(self) :
		r"""Drop any packet that requires fragmentation.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._dropfrag
		except Exception as e:
			raise e

	@dropfrag.setter
	def dropfrag(self, dropfrag) :
		r"""Drop any packet that requires fragmentation.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._dropfrag = dropfrag
		except Exception as e:
			raise e

	@property
	def dropfragcputhreshold(self) :
		r"""Threshold value, as a percentage of CPU usage, at which to drop packets that require fragmentation. Applies only if dropFragparameter is set to NO.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._dropfragcputhreshold
		except Exception as e:
			raise e

	@dropfragcputhreshold.setter
	def dropfragcputhreshold(self, dropfragcputhreshold) :
		r"""Threshold value, as a percentage of CPU usage, at which to drop packets that require fragmentation. Applies only if dropFragparameter is set to NO.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._dropfragcputhreshold = dropfragcputhreshold
		except Exception as e:
			raise e

	@property
	def srciproundrobin(self) :
		r"""Use a different source IPv6 address for each new session through a particular IPv6 tunnel, as determined by round robin selection of one of the SNIP6 addresses. This setting is ignored if a common global source IPv6 address has been specified for all the IPv6 tunnels. This setting does not apply to a tunnel for which a source IPv6 address has been specified.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._srciproundrobin
		except Exception as e:
			raise e

	@srciproundrobin.setter
	def srciproundrobin(self, srciproundrobin) :
		r"""Use a different source IPv6 address for each new session through a particular IPv6 tunnel, as determined by round robin selection of one of the SNIP6 addresses. This setting is ignored if a common global source IPv6 address has been specified for all the IPv6 tunnels. This setting does not apply to a tunnel for which a source IPv6 address has been specified.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._srciproundrobin = srciproundrobin
		except Exception as e:
			raise e

	@property
	def useclientsourceipv6(self) :
		r"""Use client source IPv6 address as source IPv6 address for outer tunnel IPv6 header.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._useclientsourceipv6
		except Exception as e:
			raise e

	@useclientsourceipv6.setter
	def useclientsourceipv6(self, useclientsourceipv6) :
		r"""Use client source IPv6 address as source IPv6 address for outer tunnel IPv6 header.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._useclientsourceipv6 = useclientsourceipv6
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ip6tunnelparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ip6tunnelparam
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
		r""" Use this API to update ip6tunnelparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = ip6tunnelparam()
				updateresource.srcip = resource.srcip
				updateresource.dropfrag = resource.dropfrag
				updateresource.dropfragcputhreshold = resource.dropfragcputhreshold
				updateresource.srciproundrobin = resource.srciproundrobin
				updateresource.useclientsourceipv6 = resource.useclientsourceipv6
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of ip6tunnelparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = ip6tunnelparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the ip6tunnelparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ip6tunnelparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Useclientsourceipv6:
		YES = "YES"
		NO = "NO"

	class Dropfrag:
		YES = "YES"
		NO = "NO"

	class Srciproundrobin:
		YES = "YES"
		NO = "NO"

class ip6tunnelparam_response(base_response) :
	def __init__(self, length=1) :
		self.ip6tunnelparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ip6tunnelparam = [ip6tunnelparam() for _ in range(length)]

