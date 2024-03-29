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

class route6(base_resource) :
	""" Configuration for route 6 resource. """
	def __init__(self) :
		self._network = None
		self._gateway = None
		self._vlan = None
		self._vxlan = None
		self._weight = None
		self._distance = None
		self._cost = None
		self._advertise = None
		self._msr = None
		self._monitor = None
		self._td = None
		self._ownergroup = None
		self._routetype = None
		self._detail = None
		self._gatewayname = None
		self._type = None
		self._dynamic = None
		self._data = None
		self._flags = None
		self._state = None
		self._totalprobes = None
		self._totalfailedprobes = None
		self._failedprobes = None
		self._monstatcode = None
		self._monstatparam1 = None
		self._monstatparam2 = None
		self._monstatparam3 = None
		self._data1 = None
		self._routeowners = None
		self._retain = None
		self._Static = None
		self._permanent = None
		self._connected = None
		self._ospfv3 = None
		self._isis = None
		self._active = None
		self._bgp = None
		self._rip = None
		self._raroute = None
		self.___count = None

	@property
	def network(self) :
		r"""IPv6 network address for which to add a route entry to the routing table of the Citrix ADC.
		"""
		try :
			return self._network
		except Exception as e:
			raise e

	@network.setter
	def network(self, network) :
		r"""IPv6 network address for which to add a route entry to the routing table of the Citrix ADC.
		"""
		try :
			self._network = network
		except Exception as e:
			raise e

	@property
	def gateway(self) :
		r"""The gateway for this route. The value for this parameter is either an IPv6 address or null.<br/>Default value: 0.
		"""
		try :
			return self._gateway
		except Exception as e:
			raise e

	@gateway.setter
	def gateway(self, gateway) :
		r"""The gateway for this route. The value for this parameter is either an IPv6 address or null.<br/>Default value: 0
		"""
		try :
			self._gateway = gateway
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""Integer value that uniquely identifies a VLAN through which the Citrix ADC forwards the packets for this route.<br/>Default value: 0<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""Integer value that uniquely identifies a VLAN through which the Citrix ADC forwards the packets for this route.<br/>Default value: 0<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		r"""Integer value that uniquely identifies a VXLAN through which the Citrix ADC forwards the packets for this route.<br/>Minimum length =  1<br/>Maximum length =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		r"""Integer value that uniquely identifies a VXLAN through which the Citrix ADC forwards the packets for this route.<br/>Minimum length =  1<br/>Maximum length =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Positive integer used by the routing algorithms to determine preference for this route over others of equal cost. The lower the weight, the higher the preference.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""Positive integer used by the routing algorithms to determine preference for this route over others of equal cost. The lower the weight, the higher the preference.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def distance(self) :
		r"""Administrative distance of this route from the appliance.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  254.
		"""
		try :
			return self._distance
		except Exception as e:
			raise e

	@distance.setter
	def distance(self, distance) :
		r"""Administrative distance of this route from the appliance.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  254
		"""
		try :
			self._distance = distance
		except Exception as e:
			raise e

	@property
	def cost(self) :
		r"""Positive integer used by the routing algorithms to determine preference for this route. The lower the cost, the higher the preference.<br/>Default value: 1<br/>Maximum length =  65535.
		"""
		try :
			return self._cost
		except Exception as e:
			raise e

	@cost.setter
	def cost(self, cost) :
		r"""Positive integer used by the routing algorithms to determine preference for this route. The lower the cost, the higher the preference.<br/>Default value: 1<br/>Maximum length =  65535
		"""
		try :
			self._cost = cost
		except Exception as e:
			raise e

	@property
	def advertise(self) :
		r"""Advertise this route.<br/>Possible values = DISABLED, ENABLED.
		"""
		try :
			return self._advertise
		except Exception as e:
			raise e

	@advertise.setter
	def advertise(self, advertise) :
		r"""Advertise this route.<br/>Possible values = DISABLED, ENABLED
		"""
		try :
			self._advertise = advertise
		except Exception as e:
			raise e

	@property
	def msr(self) :
		r"""Monitor this route with a monitor of type ND6 or PING.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._msr
		except Exception as e:
			raise e

	@msr.setter
	def msr(self, msr) :
		r"""Monitor this route with a monitor of type ND6 or PING.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._msr = msr
		except Exception as e:
			raise e

	@property
	def monitor(self) :
		r"""Name of the monitor, of type ND6 or PING, configured on the Citrix ADC to monitor this route.<br/>Minimum length =  1.
		"""
		try :
			return self._monitor
		except Exception as e:
			raise e

	@monitor.setter
	def monitor(self, monitor) :
		r"""Name of the monitor, of type ND6 or PING, configured on the Citrix ADC to monitor this route.<br/>Minimum length =  1
		"""
		try :
			self._monitor = monitor
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
	def ownergroup(self) :
		r"""The owner node group in a Cluster for this route6. If owner node group is not specified then the route is treated as Striped route.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1.
		"""
		try :
			return self._ownergroup
		except Exception as e:
			raise e

	@ownergroup.setter
	def ownergroup(self, ownergroup) :
		r"""The owner node group in a Cluster for this route6. If owner node group is not specified then the route is treated as Striped route.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1
		"""
		try :
			self._ownergroup = ownergroup
		except Exception as e:
			raise e

	@property
	def routetype(self) :
		r"""Type of IPv6 routes to remove from the routing table of the Citrix ADC.<br/>Possible values = CONNECTED, STATIC, DYNAMIC, OSPF, ISIS, BGP, RIP, ND-RA-ROUTE, FIB6.
		"""
		try :
			return self._routetype
		except Exception as e:
			raise e

	@routetype.setter
	def routetype(self, routetype) :
		r"""Type of IPv6 routes to remove from the routing table of the Citrix ADC.<br/>Possible values = CONNECTED, STATIC, DYNAMIC, OSPF, ISIS, BGP, RIP, ND-RA-ROUTE, FIB6
		"""
		try :
			self._routetype = routetype
		except Exception as e:
			raise e

	@property
	def detail(self) :
		r"""To get a detailed view.
		"""
		try :
			return self._detail
		except Exception as e:
			raise e

	@detail.setter
	def detail(self, detail) :
		r"""To get a detailed view.
		"""
		try :
			self._detail = detail
		except Exception as e:
			raise e

	@property
	def gatewayname(self) :
		r"""The name of the gateway for this route.
		"""
		try :
			return self._gatewayname
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""State of the RNAT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def dynamic(self) :
		r"""Whether this route is dynamically learned or not.
		"""
		try :
			return self._dynamic
		except Exception as e:
			raise e

	@property
	def data(self) :
		r"""Internal data of this route.
		"""
		try :
			return self._data
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""For a dynamic route, the routing protocol from which the route was learned.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Whether this route is UP or DOWN.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def totalprobes(self) :
		r"""The total number of probes sent.
		"""
		try :
			return self._totalprobes
		except Exception as e:
			raise e

	@property
	def totalfailedprobes(self) :
		r"""The total number of failed probes.
		"""
		try :
			return self._totalfailedprobes
		except Exception as e:
			raise e

	@property
	def failedprobes(self) :
		r"""Current number of failed monitoring probes.
		"""
		try :
			return self._failedprobes
		except Exception as e:
			raise e

	@property
	def monstatcode(self) :
		r"""The code indicating the monitor response.
		"""
		try :
			return self._monstatcode
		except Exception as e:
			raise e

	@property
	def monstatparam1(self) :
		r"""First parameter for use with message code.
		"""
		try :
			return self._monstatparam1
		except Exception as e:
			raise e

	@property
	def monstatparam2(self) :
		r"""Second parameter for use with message code.
		"""
		try :
			return self._monstatparam2
		except Exception as e:
			raise e

	@property
	def monstatparam3(self) :
		r"""Third parameter for use with message code.
		"""
		try :
			return self._monstatparam3
		except Exception as e:
			raise e

	@property
	def data1(self) :
		r"""Internal data of this route.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._data1
		except Exception as e:
			raise e

	@property
	def routeowners(self) :
		r"""Use this option with -dynamic and in a cluster only to specify the set of nodes from which this dynamic route has been learnt.<br/>Possible values = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31.
		"""
		try :
			return self._routeowners
		except Exception as e:
			raise e

	@property
	def retain(self) :
		try :
			return self._retain
		except Exception as e:
			raise e

	@property
	def Static(self) :
		r"""Static route.
		"""
		try :
			return self._Static
		except Exception as e:
			raise e

	@property
	def permanent(self) :
		r"""Permanent Route.
		"""
		try :
			return self._permanent
		except Exception as e:
			raise e

	@property
	def connected(self) :
		r"""Connected Route.
		"""
		try :
			return self._connected
		except Exception as e:
			raise e

	@property
	def ospfv3(self) :
		r"""For a dynamic route, the routing protocol from which the route was learned.
		"""
		try :
			return self._ospfv3
		except Exception as e:
			raise e

	@property
	def isis(self) :
		r"""If this route is dynamic then which routing protocol was it learnt from.
		"""
		try :
			return self._isis
		except Exception as e:
			raise e

	@property
	def active(self) :
		r"""For a dynamic route, the routing protocol from which the route was learned.
		"""
		try :
			return self._active
		except Exception as e:
			raise e

	@property
	def bgp(self) :
		r"""For a dynamic route, the routing protocol from which the route was learned.
		"""
		try :
			return self._bgp
		except Exception as e:
			raise e

	@property
	def rip(self) :
		r""" For a dynamic route, the routing protocol from which the route was learned.
		"""
		try :
			return self._rip
		except Exception as e:
			raise e

	@property
	def raroute(self) :
		r""" For a dynamic route, the routing protocol from which the route was learned.
		"""
		try :
			return self._raroute
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(route6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.route6
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.network is not None :
				return str(self.network)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add route6.
		"""
		try :
			if type(resource) is not list :
				addresource = route6()
				addresource.network = resource.network
				addresource.gateway = resource.gateway
				addresource.vlan = resource.vlan
				addresource.vxlan = resource.vxlan
				addresource.weight = resource.weight
				addresource.distance = resource.distance
				addresource.cost = resource.cost
				addresource.advertise = resource.advertise
				addresource.msr = resource.msr
				addresource.monitor = resource.monitor
				addresource.td = resource.td
				addresource.ownergroup = resource.ownergroup
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ route6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].network = resource[i].network
						addresources[i].gateway = resource[i].gateway
						addresources[i].vlan = resource[i].vlan
						addresources[i].vxlan = resource[i].vxlan
						addresources[i].weight = resource[i].weight
						addresources[i].distance = resource[i].distance
						addresources[i].cost = resource[i].cost
						addresources[i].advertise = resource[i].advertise
						addresources[i].msr = resource[i].msr
						addresources[i].monitor = resource[i].monitor
						addresources[i].td = resource[i].td
						addresources[i].ownergroup = resource[i].ownergroup
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear route6.
		"""
		try :
			if type(resource) is not list :
				clearresource = route6()
				clearresource.routetype = resource.routetype
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ route6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].routetype = resource[i].routetype
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete route6.
		"""
		try :
			if type(resource) is not list :
				deleteresource = route6()
				if type(resource) !=  type(deleteresource):
					deleteresource.network = resource
				else :
					deleteresource.network = resource.network
					deleteresource.gateway = resource.gateway
					deleteresource.vlan = resource.vlan
					deleteresource.vxlan = resource.vxlan
					deleteresource.td = resource.td
					deleteresource.ownergroup = resource.ownergroup
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ route6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].network = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ route6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].network = resource[i].network
							deleteresources[i].gateway = resource[i].gateway
							deleteresources[i].vlan = resource[i].vlan
							deleteresources[i].vxlan = resource[i].vxlan
							deleteresources[i].td = resource[i].td
							deleteresources[i].ownergroup = resource[i].ownergroup
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update route6.
		"""
		try :
			if type(resource) is not list :
				updateresource = route6()
				updateresource.network = resource.network
				updateresource.gateway = resource.gateway
				updateresource.vlan = resource.vlan
				updateresource.vxlan = resource.vxlan
				updateresource.weight = resource.weight
				updateresource.distance = resource.distance
				updateresource.cost = resource.cost
				updateresource.advertise = resource.advertise
				updateresource.msr = resource.msr
				updateresource.monitor = resource.monitor
				updateresource.td = resource.td
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ route6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].network = resource[i].network
						updateresources[i].gateway = resource[i].gateway
						updateresources[i].vlan = resource[i].vlan
						updateresources[i].vxlan = resource[i].vxlan
						updateresources[i].weight = resource[i].weight
						updateresources[i].distance = resource[i].distance
						updateresources[i].cost = resource[i].cost
						updateresources[i].advertise = resource[i].advertise
						updateresources[i].msr = resource[i].msr
						updateresources[i].monitor = resource[i].monitor
						updateresources[i].td = resource[i].td
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of route6 resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = route6()
				if type(resource) !=  type(unsetresource):
					unsetresource.network = resource
				else :
					unsetresource.network = resource.network
					unsetresource.gateway = resource.gateway
					unsetresource.vlan = resource.vlan
					unsetresource.vxlan = resource.vxlan
					unsetresource.td = resource.td
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ route6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].network = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ route6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].network = resource[i].network
							unsetresources[i].gateway = resource[i].gateway
							unsetresources[i].vlan = resource[i].vlan
							unsetresources[i].vxlan = resource[i].vxlan
							unsetresources[i].td = resource[i].td
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the route6 resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = route6()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) != cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) != cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [route6() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the route6 resources that are configured on netscaler.
	# This uses route6_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = route6()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of route6 resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = route6()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the route6 resources configured on NetScaler.
		"""
		try :
			obj = route6()
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
		r""" Use this API to count filtered the set of route6 resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = route6()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Advertise:
		DISABLED = "DISABLED"
		ENABLED = "ENABLED"

	class Routetype:
		CONNECTED = "CONNECTED"
		STATIC = "STATIC"
		DYNAMIC = "DYNAMIC"
		OSPF = "OSPF"
		ISIS = "ISIS"
		BGP = "BGP"
		RIP = "RIP"
		ND_RA_ROUTE = "ND-RA-ROUTE"
		FIB6 = "FIB6"

	class Msr:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Data1:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Routeowners:
		_0 = "0"
		_1 = "1"
		_2 = "2"
		_3 = "3"
		_4 = "4"
		_5 = "5"
		_6 = "6"
		_7 = "7"
		_8 = "8"
		_9 = "9"
		_10 = "10"
		_11 = "11"
		_12 = "12"
		_13 = "13"
		_14 = "14"
		_15 = "15"
		_16 = "16"
		_17 = "17"
		_18 = "18"
		_19 = "19"
		_20 = "20"
		_21 = "21"
		_22 = "22"
		_23 = "23"
		_24 = "24"
		_25 = "25"
		_26 = "26"
		_27 = "27"
		_28 = "28"
		_29 = "29"
		_30 = "30"
		_31 = "31"

class route6_response(base_response) :
	def __init__(self, length=1) :
		self.route6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.route6 = [route6() for _ in range(length)]

