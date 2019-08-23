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

class ipv6(base_resource) :
	""" Configuration for ip v6 resource. """
	def __init__(self) :
		self._ralearning = None
		self._routerredirection = None
		self._ndbasereachtime = None
		self._ndretransmissiontime = None
		self._natprefix = None
		self._td = None
		self._dodad = None
		self._usipnatprefix = None
		self._basereachtime = None
		self._reachtime = None
		self._ndreachtime = None
		self._retransmissiontime = None
		self.___count = None

	@property
	def ralearning(self) :
		r"""Enable the Citrix ADC to learn about various routes from Router Advertisement (RA) and Router Solicitation (RS) messages sent by the routers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ralearning
		except Exception as e:
			raise e

	@ralearning.setter
	def ralearning(self, ralearning) :
		r"""Enable the Citrix ADC to learn about various routes from Router Advertisement (RA) and Router Solicitation (RS) messages sent by the routers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ralearning = ralearning
		except Exception as e:
			raise e

	@property
	def routerredirection(self) :
		r"""Enable the Citrix ADC to do Router Redirection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._routerredirection
		except Exception as e:
			raise e

	@routerredirection.setter
	def routerredirection(self, routerredirection) :
		r"""Enable the Citrix ADC to do Router Redirection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._routerredirection = routerredirection
		except Exception as e:
			raise e

	@property
	def ndbasereachtime(self) :
		r"""Base reachable time of the Neighbor Discovery (ND6) protocol. The time, in milliseconds, that the Citrix ADC assumes an adjacent device is reachable after receiving a reachability confirmation.<br/>Default value: 30000<br/>Minimum length =  1.
		"""
		try :
			return self._ndbasereachtime
		except Exception as e:
			raise e

	@ndbasereachtime.setter
	def ndbasereachtime(self, ndbasereachtime) :
		r"""Base reachable time of the Neighbor Discovery (ND6) protocol. The time, in milliseconds, that the Citrix ADC assumes an adjacent device is reachable after receiving a reachability confirmation.<br/>Default value: 30000<br/>Minimum length =  1
		"""
		try :
			self._ndbasereachtime = ndbasereachtime
		except Exception as e:
			raise e

	@property
	def ndretransmissiontime(self) :
		r"""Retransmission time of the Neighbor Discovery (ND6) protocol. The time, in milliseconds, between retransmitted Neighbor Solicitation (NS) messages, to an adjacent device.<br/>Default value: 1000<br/>Minimum length =  1.
		"""
		try :
			return self._ndretransmissiontime
		except Exception as e:
			raise e

	@ndretransmissiontime.setter
	def ndretransmissiontime(self, ndretransmissiontime) :
		r"""Retransmission time of the Neighbor Discovery (ND6) protocol. The time, in milliseconds, between retransmitted Neighbor Solicitation (NS) messages, to an adjacent device.<br/>Default value: 1000<br/>Minimum length =  1
		"""
		try :
			self._ndretransmissiontime = ndretransmissiontime
		except Exception as e:
			raise e

	@property
	def natprefix(self) :
		r"""Prefix used for translating packets from private IPv6 servers to IPv4 packets. This prefix has a length of 96 bits (128-32 = 96). The IPv6 servers embed the destination IP address of the IPv4 servers or hosts in the last 32 bits of the destination IP address field of the IPv6 packets. The first 96 bits of the destination IP address field are set as the IPv6 NAT prefix. IPv6 packets addressed to this prefix have to be routed to the Citrix ADC to ensure that the IPv6-IPv4 translation is done by the appliance.
		"""
		try :
			return self._natprefix
		except Exception as e:
			raise e

	@natprefix.setter
	def natprefix(self, natprefix) :
		r"""Prefix used for translating packets from private IPv6 servers to IPv4 packets. This prefix has a length of 96 bits (128-32 = 96). The IPv6 servers embed the destination IP address of the IPv4 servers or hosts in the last 32 bits of the destination IP address field of the IPv6 packets. The first 96 bits of the destination IP address field are set as the IPv6 NAT prefix. IPv6 packets addressed to this prefix have to be routed to the Citrix ADC to ensure that the IPv6-IPv4 translation is done by the appliance.
		"""
		try :
			self._natprefix = natprefix
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Default value: 0<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Default value: 0<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def dodad(self) :
		r"""Enable the Citrix ADC to do Duplicate Address
		Detection (DAD) for all the Citrix ADC owned IPv6 addresses regardless of whether they are obtained through stateless auto configuration, DHCPv6, or manual configuration.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dodad
		except Exception as e:
			raise e

	@dodad.setter
	def dodad(self, dodad) :
		r"""Enable the Citrix ADC to do Duplicate Address
		Detection (DAD) for all the Citrix ADC owned IPv6 addresses regardless of whether they are obtained through stateless auto configuration, DHCPv6, or manual configuration.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dodad = dodad
		except Exception as e:
			raise e

	@property
	def usipnatprefix(self) :
		r"""IPV6 NATPREFIX used in NAT46 scenario when USIP is turned on.
		"""
		try :
			return self._usipnatprefix
		except Exception as e:
			raise e

	@usipnatprefix.setter
	def usipnatprefix(self, usipnatprefix) :
		r"""IPV6 NATPREFIX used in NAT46 scenario when USIP is turned on.
		"""
		try :
			self._usipnatprefix = usipnatprefix
		except Exception as e:
			raise e

	@property
	def basereachtime(self) :
		r"""ND6 base reachable time (ms).
		"""
		try :
			return self._basereachtime
		except Exception as e:
			raise e

	@property
	def reachtime(self) :
		r"""ND6 computed reachable time (ms).
		"""
		try :
			return self._reachtime
		except Exception as e:
			raise e

	@property
	def ndreachtime(self) :
		r"""ND6 computed reachable time (ms).
		"""
		try :
			return self._ndreachtime
		except Exception as e:
			raise e

	@property
	def retransmissiontime(self) :
		r"""ND6 retransmission time (ms).
		"""
		try :
			return self._retransmissiontime
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ipv6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ipv6
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.td is not None :
				return str(self.td)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update ipv6.
		"""
		try :
			if type(resource) is not list :
				updateresource = ipv6()
				updateresource.ralearning = resource.ralearning
				updateresource.routerredirection = resource.routerredirection
				updateresource.ndbasereachtime = resource.ndbasereachtime
				updateresource.ndretransmissiontime = resource.ndretransmissiontime
				updateresource.natprefix = resource.natprefix
				updateresource.td = resource.td
				updateresource.dodad = resource.dodad
				updateresource.usipnatprefix = resource.usipnatprefix
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ ipv6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].ralearning = resource[i].ralearning
						updateresources[i].routerredirection = resource[i].routerredirection
						updateresources[i].ndbasereachtime = resource[i].ndbasereachtime
						updateresources[i].ndretransmissiontime = resource[i].ndretransmissiontime
						updateresources[i].natprefix = resource[i].natprefix
						updateresources[i].td = resource[i].td
						updateresources[i].dodad = resource[i].dodad
						updateresources[i].usipnatprefix = resource[i].usipnatprefix
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of ipv6 resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = ipv6()
				if type(resource) !=  type(unsetresource):
					unsetresource.td = resource
				else :
					unsetresource.td = resource.td
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ ipv6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].td = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ ipv6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].td = resource[i].td
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the ipv6 resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ipv6()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = ipv6()
					obj.td = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [ipv6() for _ in range(len(name))]
						obj = [ipv6() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = ipv6()
							obj[i].td = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of ipv6 resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ipv6()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the ipv6 resources configured on NetScaler.
		"""
		try :
			obj = ipv6()
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
		r""" Use this API to count filtered the set of ipv6 resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ipv6()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Routerredirection:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ralearning:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dodad:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class ipv6_response(base_response) :
	def __init__(self, length=1) :
		self.ipv6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ipv6 = [ipv6() for _ in range(length)]

