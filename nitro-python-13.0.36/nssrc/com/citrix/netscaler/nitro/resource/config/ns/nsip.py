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

class nsip(base_resource) :
	""" Configuration for ip resource. """
	def __init__(self) :
		self._ipaddress = None
		self._netmask = None
		self._type = None
		self._arp = None
		self._icmp = None
		self._vserver = None
		self._telnet = None
		self._ftp = None
		self._gui = None
		self._ssh = None
		self._snmp = None
		self._mgmtaccess = None
		self._restrictaccess = None
		self._dynamicrouting = None
		self._decrementttl = None
		self._ospf = None
		self._bgp = None
		self._rip = None
		self._hostroute = None
		self._advertiseondefaultpartition = None
		self._networkroute = None
		self._tag = None
		self._hostrtgw = None
		self._metric = None
		self._vserverrhilevel = None
		self._vserverrhimode = None
		self._ospflsatype = None
		self._ospfarea = None
		self._state = None
		self._vrid = None
		self._icmpresponse = None
		self._ownernode = None
		self._arpresponse = None
		self._ownerdownresponse = None
		self._td = None
		self._flags = None
		self._hostrtgwact = None
		self._ospfareaval = None
		self._viprtadv2bsd = None
		self._vipvsercount = None
		self._vipvserdowncount = None
		self._vipvsrvrrhiactivecount = None
		self._vipvsrvrrhiactiveupcount = None
		self._freeports = None
		self._riserhimsgcode = None
		self._iptype = None
		self.___count = None

	@property
	def ipaddress(self) :
		r"""IPv4 address to create on the Citrix ADC. Cannot be changed after the IP address is created.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""IPv4 address to create on the Citrix ADC. Cannot be changed after the IP address is created.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		r"""Subnet mask associated with the IP address.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		r"""Subnet mask associated with the IP address.
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of the IP address to create on the Citrix ADC. Cannot be changed after the IP address is created. The following are the different types of Citrix ADC owned IP addresses:
		* A Subnet IP (SNIP) address is used by the Citrix ADC to communicate with the servers. The Citrix ADC also uses the subnet IP address when generating its own packets, such as packets related to dynamic routing protocols, or to send monitor probes to check the health of the servers.
		* A Virtual IP (VIP) address is the IP address associated with a virtual server. It is the IP address to which clients connect. An appliance managing a wide range of traffic may have many VIPs configured. Some of the attributes of the VIP address are customized to meet the requirements of the virtual server.
		* A GSLB site IP (GSLBIP) address is associated with a GSLB site. It is not mandatory to specify a GSLBIP address when you initially configure the Citrix ADC. A GSLBIP address is used only when you create a GSLB site.
		* A Cluster IP (CLIP) address is the management address of the cluster. All cluster configurations must be performed by accessing the cluster through this IP address.<br/>Default value: SNIP<br/>Possible values = SNIP, VIP, NSIP, GSLBsiteIP, CLIP.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of the IP address to create on the Citrix ADC. Cannot be changed after the IP address is created. The following are the different types of Citrix ADC owned IP addresses:
		* A Subnet IP (SNIP) address is used by the Citrix ADC to communicate with the servers. The Citrix ADC also uses the subnet IP address when generating its own packets, such as packets related to dynamic routing protocols, or to send monitor probes to check the health of the servers.
		* A Virtual IP (VIP) address is the IP address associated with a virtual server. It is the IP address to which clients connect. An appliance managing a wide range of traffic may have many VIPs configured. Some of the attributes of the VIP address are customized to meet the requirements of the virtual server.
		* A GSLB site IP (GSLBIP) address is associated with a GSLB site. It is not mandatory to specify a GSLBIP address when you initially configure the Citrix ADC. A GSLBIP address is used only when you create a GSLB site.
		* A Cluster IP (CLIP) address is the management address of the cluster. All cluster configurations must be performed by accessing the cluster through this IP address.<br/>Default value: SNIP<br/>Possible values = SNIP, VIP, NSIP, GSLBsiteIP, CLIP
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def arp(self) :
		r"""Respond to ARP requests for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._arp
		except Exception as e:
			raise e

	@arp.setter
	def arp(self, arp) :
		r"""Respond to ARP requests for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._arp = arp
		except Exception as e:
			raise e

	@property
	def icmp(self) :
		r"""Respond to ICMP requests for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._icmp
		except Exception as e:
			raise e

	@icmp.setter
	def icmp(self, icmp) :
		r"""Respond to ICMP requests for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._icmp = icmp
		except Exception as e:
			raise e

	@property
	def vserver(self) :
		r"""Use this option to set (enable or disable) the virtual server attribute for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		r"""Use this option to set (enable or disable) the virtual server attribute for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._vserver = vserver
		except Exception as e:
			raise e

	@property
	def telnet(self) :
		r"""Allow Telnet access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._telnet
		except Exception as e:
			raise e

	@telnet.setter
	def telnet(self, telnet) :
		r"""Allow Telnet access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._telnet = telnet
		except Exception as e:
			raise e

	@property
	def ftp(self) :
		r"""Allow File Transfer Protocol (FTP) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ftp
		except Exception as e:
			raise e

	@ftp.setter
	def ftp(self, ftp) :
		r"""Allow File Transfer Protocol (FTP) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ftp = ftp
		except Exception as e:
			raise e

	@property
	def gui(self) :
		r"""Allow graphical user interface (GUI) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, SECUREONLY, DISABLED.
		"""
		try :
			return self._gui
		except Exception as e:
			raise e

	@gui.setter
	def gui(self, gui) :
		r"""Allow graphical user interface (GUI) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, SECUREONLY, DISABLED
		"""
		try :
			self._gui = gui
		except Exception as e:
			raise e

	@property
	def ssh(self) :
		r"""Allow secure shell (SSH) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssh
		except Exception as e:
			raise e

	@ssh.setter
	def ssh(self, ssh) :
		r"""Allow secure shell (SSH) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssh = ssh
		except Exception as e:
			raise e

	@property
	def snmp(self) :
		r"""Allow Simple Network Management Protocol (SNMP) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._snmp
		except Exception as e:
			raise e

	@snmp.setter
	def snmp(self, snmp) :
		r"""Allow Simple Network Management Protocol (SNMP) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._snmp = snmp
		except Exception as e:
			raise e

	@property
	def mgmtaccess(self) :
		r"""Allow access to management applications on this IP address.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mgmtaccess
		except Exception as e:
			raise e

	@mgmtaccess.setter
	def mgmtaccess(self, mgmtaccess) :
		r"""Allow access to management applications on this IP address.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mgmtaccess = mgmtaccess
		except Exception as e:
			raise e

	@property
	def restrictaccess(self) :
		r"""Block access to nonmanagement applications on this IP. This option is applicable for MIPs, SNIPs, and NSIP, and is disabled by default. Nonmanagement applications can run on the underlying Citrix ADC Free BSD operating system.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._restrictaccess
		except Exception as e:
			raise e

	@restrictaccess.setter
	def restrictaccess(self, restrictaccess) :
		r"""Block access to nonmanagement applications on this IP. This option is applicable for MIPs, SNIPs, and NSIP, and is disabled by default. Nonmanagement applications can run on the underlying Citrix ADC Free BSD operating system.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._restrictaccess = restrictaccess
		except Exception as e:
			raise e

	@property
	def dynamicrouting(self) :
		r"""Allow dynamic routing on this IP address. Specific to Subnet IP (SNIP) address.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dynamicrouting
		except Exception as e:
			raise e

	@dynamicrouting.setter
	def dynamicrouting(self, dynamicrouting) :
		r"""Allow dynamic routing on this IP address. Specific to Subnet IP (SNIP) address.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dynamicrouting = dynamicrouting
		except Exception as e:
			raise e

	@property
	def decrementttl(self) :
		r"""Decrement TTL by 1 when ENABLED.This setting is applicable only for UDP traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._decrementttl
		except Exception as e:
			raise e

	@decrementttl.setter
	def decrementttl(self, decrementttl) :
		r"""Decrement TTL by 1 when ENABLED.This setting is applicable only for UDP traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._decrementttl = decrementttl
		except Exception as e:
			raise e

	@property
	def ospf(self) :
		r"""Use this option to enable or disable OSPF on this IP address for the entity.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ospf
		except Exception as e:
			raise e

	@ospf.setter
	def ospf(self, ospf) :
		r"""Use this option to enable or disable OSPF on this IP address for the entity.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ospf = ospf
		except Exception as e:
			raise e

	@property
	def bgp(self) :
		r"""Use this option to enable or disable BGP on this IP address for the entity.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._bgp
		except Exception as e:
			raise e

	@bgp.setter
	def bgp(self, bgp) :
		r"""Use this option to enable or disable BGP on this IP address for the entity.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._bgp = bgp
		except Exception as e:
			raise e

	@property
	def rip(self) :
		r"""Use this option to enable or disable RIP on this IP address for the entity.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rip
		except Exception as e:
			raise e

	@rip.setter
	def rip(self, rip) :
		r"""Use this option to enable or disable RIP on this IP address for the entity.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rip = rip
		except Exception as e:
			raise e

	@property
	def hostroute(self) :
		r"""Option to push the VIP to ZebOS routing table for Kernel route redistribution through dynamic routing protocols.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._hostroute
		except Exception as e:
			raise e

	@hostroute.setter
	def hostroute(self, hostroute) :
		r"""Option to push the VIP to ZebOS routing table for Kernel route redistribution through dynamic routing protocols.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._hostroute = hostroute
		except Exception as e:
			raise e

	@property
	def advertiseondefaultpartition(self) :
		r"""Advertise VIPs from Shared VLAN on Default Partition.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._advertiseondefaultpartition
		except Exception as e:
			raise e

	@advertiseondefaultpartition.setter
	def advertiseondefaultpartition(self, advertiseondefaultpartition) :
		r"""Advertise VIPs from Shared VLAN on Default Partition.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._advertiseondefaultpartition = advertiseondefaultpartition
		except Exception as e:
			raise e

	@property
	def networkroute(self) :
		r"""Option to push the SNIP subnet to ZebOS routing table for Kernel route redistribution through dynamic routing protocol.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._networkroute
		except Exception as e:
			raise e

	@networkroute.setter
	def networkroute(self, networkroute) :
		r"""Option to push the SNIP subnet to ZebOS routing table for Kernel route redistribution through dynamic routing protocol.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._networkroute = networkroute
		except Exception as e:
			raise e

	@property
	def tag(self) :
		r"""Tag value for the network/host route associated with this IP.<br/>Default value: 0.
		"""
		try :
			return self._tag
		except Exception as e:
			raise e

	@tag.setter
	def tag(self, tag) :
		r"""Tag value for the network/host route associated with this IP.<br/>Default value: 0
		"""
		try :
			self._tag = tag
		except Exception as e:
			raise e

	@property
	def hostrtgw(self) :
		r"""IP address of the gateway of the route for this VIP address.<br/>Default value: -1.
		"""
		try :
			return self._hostrtgw
		except Exception as e:
			raise e

	@hostrtgw.setter
	def hostrtgw(self, hostrtgw) :
		r"""IP address of the gateway of the route for this VIP address.<br/>Default value: -1
		"""
		try :
			self._hostrtgw = hostrtgw
		except Exception as e:
			raise e

	@property
	def metric(self) :
		r"""Integer value to add to or subtract from the cost of the route advertised for the VIP address.<br/>Minimum length =  -16777215.
		"""
		try :
			return self._metric
		except Exception as e:
			raise e

	@metric.setter
	def metric(self, metric) :
		r"""Integer value to add to or subtract from the cost of the route advertised for the VIP address.<br/>Minimum length =  -16777215
		"""
		try :
			self._metric = metric
		except Exception as e:
			raise e

	@property
	def vserverrhilevel(self) :
		r"""Advertise the route for the Virtual IP (VIP) address on the basis of the state of the virtual servers associated with that VIP.
		* NONE - Advertise the route for the VIP address, regardless of the state of the virtual servers associated with the address.
		* ONE VSERVER - Advertise the route for the VIP address if at least one of the associated virtual servers is in UP state.
		* ALL VSERVER - Advertise the route for the VIP address if all of the associated virtual servers are in UP state.
		* VSVR_CNTRLD - Advertise the route for the VIP address according to the  RHIstate (RHI STATE) parameter setting on all the associated virtual servers of the VIP address along with their states.
		When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated with the VIP address:
		* If you set RHI STATE to PASSIVE on all virtual servers, the Citrix ADC always advertises the route for the VIP address.
		* If you set RHI STATE to ACTIVE on all virtual servers, the Citrix ADC advertises the route for the VIP address if at least one of the associated virtual servers is in UP state.
		*If you set RHI STATE to ACTIVE on some and PASSIVE on others, the Citrix ADC advertises the route for the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is in UP state.
		<br/>Default value: ONE_VSERVER<br/>Possible values = ONE_VSERVER, ALL_VSERVERS, NONE, VSVR_CNTRLD.
		"""
		try :
			return self._vserverrhilevel
		except Exception as e:
			raise e

	@vserverrhilevel.setter
	def vserverrhilevel(self, vserverrhilevel) :
		r"""Advertise the route for the Virtual IP (VIP) address on the basis of the state of the virtual servers associated with that VIP.
		* NONE - Advertise the route for the VIP address, regardless of the state of the virtual servers associated with the address.
		* ONE VSERVER - Advertise the route for the VIP address if at least one of the associated virtual servers is in UP state.
		* ALL VSERVER - Advertise the route for the VIP address if all of the associated virtual servers are in UP state.
		* VSVR_CNTRLD - Advertise the route for the VIP address according to the  RHIstate (RHI STATE) parameter setting on all the associated virtual servers of the VIP address along with their states.
		When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated with the VIP address:
		* If you set RHI STATE to PASSIVE on all virtual servers, the Citrix ADC always advertises the route for the VIP address.
		* If you set RHI STATE to ACTIVE on all virtual servers, the Citrix ADC advertises the route for the VIP address if at least one of the associated virtual servers is in UP state.
		*If you set RHI STATE to ACTIVE on some and PASSIVE on others, the Citrix ADC advertises the route for the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is in UP state.
		<br/>Default value: ONE_VSERVER<br/>Possible values = ONE_VSERVER, ALL_VSERVERS, NONE, VSVR_CNTRLD
		"""
		try :
			self._vserverrhilevel = vserverrhilevel
		except Exception as e:
			raise e

	@property
	def vserverrhimode(self) :
		r"""Advertise the route for the Virtual IP (VIP) address using dynamic routing protocols or using RISE
		* DYNMAIC_ROUTING - Advertise the route for the VIP address using dynamic routing protocols (default)
		* RISE - Advertise the route for the VIP address using RISE.<br/>Default value: DYNAMIC_ROUTING<br/>Possible values = DYNAMIC_ROUTING, RISE.
		"""
		try :
			return self._vserverrhimode
		except Exception as e:
			raise e

	@vserverrhimode.setter
	def vserverrhimode(self, vserverrhimode) :
		r"""Advertise the route for the Virtual IP (VIP) address using dynamic routing protocols or using RISE
		* DYNMAIC_ROUTING - Advertise the route for the VIP address using dynamic routing protocols (default)
		* RISE - Advertise the route for the VIP address using RISE.<br/>Default value: DYNAMIC_ROUTING<br/>Possible values = DYNAMIC_ROUTING, RISE
		"""
		try :
			self._vserverrhimode = vserverrhimode
		except Exception as e:
			raise e

	@property
	def ospflsatype(self) :
		r"""Type of LSAs to be used by the OSPF protocol, running on the Citrix ADC, for advertising the route for this VIP address.<br/>Default value: TYPE5<br/>Possible values = TYPE1, TYPE5.
		"""
		try :
			return self._ospflsatype
		except Exception as e:
			raise e

	@ospflsatype.setter
	def ospflsatype(self, ospflsatype) :
		r"""Type of LSAs to be used by the OSPF protocol, running on the Citrix ADC, for advertising the route for this VIP address.<br/>Default value: TYPE5<br/>Possible values = TYPE1, TYPE5
		"""
		try :
			self._ospflsatype = ospflsatype
		except Exception as e:
			raise e

	@property
	def ospfarea(self) :
		r"""ID of the area in which the type1 link-state advertisements (LSAs) are to be advertised for this virtual IP (VIP)  address by the OSPF protocol running on the Citrix ADC.  When this parameter is not set, the VIP is advertised on all areas.<br/>Default value: -1<br/>Maximum length =  4294967294LU.
		"""
		try :
			return self._ospfarea
		except Exception as e:
			raise e

	@ospfarea.setter
	def ospfarea(self, ospfarea) :
		r"""ID of the area in which the type1 link-state advertisements (LSAs) are to be advertised for this virtual IP (VIP)  address by the OSPF protocol running on the Citrix ADC.  When this parameter is not set, the VIP is advertised on all areas.<br/>Default value: -1<br/>Maximum length =  4294967294LU
		"""
		try :
			self._ospfarea = ospfarea
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Enable or disable the IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Enable or disable the IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def vrid(self) :
		r"""A positive integer that uniquely identifies a VMAC address for binding to this VIP address. This binding is used to set up Citrix ADCs in an active-active configuration using VRRP.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._vrid
		except Exception as e:
			raise e

	@vrid.setter
	def vrid(self, vrid) :
		r"""A positive integer that uniquely identifies a VMAC address for binding to this VIP address. This binding is used to set up Citrix ADCs in an active-active configuration using VRRP.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._vrid = vrid
		except Exception as e:
			raise e

	@property
	def icmpresponse(self) :
		r"""Respond to ICMP requests for a Virtual IP (VIP) address on the basis of the states of the virtual servers associated with that VIP. Available settings function as follows:
		* NONE - The Citrix ADC responds to any ICMP request for the VIP address, irrespective of the states of the virtual servers associated with the address.
		* ONE VSERVER - The Citrix ADC responds to any ICMP request for the VIP address if at least one of the associated virtual servers is in UP state.
		* ALL VSERVER - The Citrix ADC responds to any ICMP request for the VIP address if all of the associated virtual servers are in UP state.
		* VSVR_CNTRLD - The behavior depends on the ICMP VSERVER RESPONSE setting on all the associated virtual servers.
		The following settings can be made for the ICMP VSERVER RESPONSE parameter on a virtual server:
		* If you set ICMP VSERVER RESPONSE to PASSIVE on all virtual servers, Citrix ADC always responds.
		* If you set ICMP VSERVER RESPONSE to ACTIVE on all virtual servers, Citrix ADC responds if even one virtual server is UP.
		* When you set ICMP VSERVER RESPONSE to ACTIVE on some and PASSIVE on others, Citrix ADC responds if even one virtual server set to ACTIVE is UP.<br/>Default value: 5<br/>Possible values = NONE, ONE_VSERVER, ALL_VSERVERS, VSVR_CNTRLD.
		"""
		try :
			return self._icmpresponse
		except Exception as e:
			raise e

	@icmpresponse.setter
	def icmpresponse(self, icmpresponse) :
		r"""Respond to ICMP requests for a Virtual IP (VIP) address on the basis of the states of the virtual servers associated with that VIP. Available settings function as follows:
		* NONE - The Citrix ADC responds to any ICMP request for the VIP address, irrespective of the states of the virtual servers associated with the address.
		* ONE VSERVER - The Citrix ADC responds to any ICMP request for the VIP address if at least one of the associated virtual servers is in UP state.
		* ALL VSERVER - The Citrix ADC responds to any ICMP request for the VIP address if all of the associated virtual servers are in UP state.
		* VSVR_CNTRLD - The behavior depends on the ICMP VSERVER RESPONSE setting on all the associated virtual servers.
		The following settings can be made for the ICMP VSERVER RESPONSE parameter on a virtual server:
		* If you set ICMP VSERVER RESPONSE to PASSIVE on all virtual servers, Citrix ADC always responds.
		* If you set ICMP VSERVER RESPONSE to ACTIVE on all virtual servers, Citrix ADC responds if even one virtual server is UP.
		* When you set ICMP VSERVER RESPONSE to ACTIVE on some and PASSIVE on others, Citrix ADC responds if even one virtual server set to ACTIVE is UP.<br/>Default value: 5<br/>Possible values = NONE, ONE_VSERVER, ALL_VSERVERS, VSVR_CNTRLD
		"""
		try :
			self._icmpresponse = icmpresponse
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		r"""The owner node in a Cluster for this IP address. Owner node can vary from 0 to 31. If ownernode is not specified then the IP is treated as Striped IP.<br/>Default value: 255.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		r"""The owner node in a Cluster for this IP address. Owner node can vary from 0 to 31. If ownernode is not specified then the IP is treated as Striped IP.<br/>Default value: 255
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	@property
	def arpresponse(self) :
		r"""Respond to ARP requests for a Virtual IP (VIP) address on the basis of the states of the virtual servers associated with that VIP. Available settings function as follows:
		* NONE - The Citrix ADC responds to any ARP request for the VIP address, irrespective of the states of the virtual servers associated with the address.
		* ONE VSERVER - The Citrix ADC responds to any ARP request for the VIP address if at least one of the associated virtual servers is in UP state.
		* ALL VSERVER - The Citrix ADC responds to any ARP request for the VIP address if all of the associated virtual servers are in UP state.<br/>Default value: 5<br/>Possible values = NONE, ONE_VSERVER, ALL_VSERVERS.
		"""
		try :
			return self._arpresponse
		except Exception as e:
			raise e

	@arpresponse.setter
	def arpresponse(self, arpresponse) :
		r"""Respond to ARP requests for a Virtual IP (VIP) address on the basis of the states of the virtual servers associated with that VIP. Available settings function as follows:
		* NONE - The Citrix ADC responds to any ARP request for the VIP address, irrespective of the states of the virtual servers associated with the address.
		* ONE VSERVER - The Citrix ADC responds to any ARP request for the VIP address if at least one of the associated virtual servers is in UP state.
		* ALL VSERVER - The Citrix ADC responds to any ARP request for the VIP address if all of the associated virtual servers are in UP state.<br/>Default value: 5<br/>Possible values = NONE, ONE_VSERVER, ALL_VSERVERS
		"""
		try :
			self._arpresponse = arpresponse
		except Exception as e:
			raise e

	@property
	def ownerdownresponse(self) :
		r"""in cluster system, if the owner node is down, whether should it respond to icmp/arp.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._ownerdownresponse
		except Exception as e:
			raise e

	@ownerdownresponse.setter
	def ownerdownresponse(self, ownerdownresponse) :
		r"""in cluster system, if the owner node is down, whether should it respond to icmp/arp.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._ownerdownresponse = ownerdownresponse
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0. TD id 4095 is used reserved for  LSN use  .<br/>Maximum length =  4095.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0. TD id 4095 is used reserved for  LSN use  .<br/>Maximum length =  4095
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""The flags for this entry.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def hostrtgwact(self) :
		r"""Actual Gateway used for advertising host route.
		"""
		try :
			return self._hostrtgwact
		except Exception as e:
			raise e

	@property
	def ospfareaval(self) :
		r"""The area ID of the area in which OSPF Type1 LSAs are advertised.
		"""
		try :
			return self._ospfareaval
		except Exception as e:
			raise e

	@property
	def viprtadv2bsd(self) :
		r"""Whether this route is advertised to FreeBSD.
		"""
		try :
			return self._viprtadv2bsd
		except Exception as e:
			raise e

	@property
	def vipvsercount(self) :
		r"""Number of vservers bound to this VIP.
		"""
		try :
			return self._vipvsercount
		except Exception as e:
			raise e

	@property
	def vipvserdowncount(self) :
		r"""Number of vservers bound to this VIP, which are down.
		"""
		try :
			return self._vipvserdowncount
		except Exception as e:
			raise e

	@property
	def vipvsrvrrhiactivecount(self) :
		r"""Number of vservers that have RHI state ACTIVE.
		"""
		try :
			return self._vipvsrvrrhiactivecount
		except Exception as e:
			raise e

	@property
	def vipvsrvrrhiactiveupcount(self) :
		r"""Number of vservers that have RHI state ACTIVE, which are UP.
		"""
		try :
			return self._vipvsrvrrhiactiveupcount
		except Exception as e:
			raise e

	@property
	def freeports(self) :
		r"""Number of free Ports available on this IP.
		"""
		try :
			return self._freeports
		except Exception as e:
			raise e

	@property
	def riserhimsgcode(self) :
		r"""The code indicating the rise rhi status.
		"""
		try :
			return self._riserhimsgcode
		except Exception as e:
			raise e

	@property
	def iptype(self) :
		r""".<br/>Possible values = SNIP, VIP, NSIP, GSLBsiteIP, CLIP.
		"""
		try :
			return self._iptype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsip_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsip
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ipaddress is not None :
				return str(self.ipaddress)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nsip.
		"""
		try :
			if type(resource) is not list :
				addresource = nsip()
				addresource.ipaddress = resource.ipaddress
				addresource.netmask = resource.netmask
				addresource.type = resource.type
				addresource.arp = resource.arp
				addresource.icmp = resource.icmp
				addresource.vserver = resource.vserver
				addresource.telnet = resource.telnet
				addresource.ftp = resource.ftp
				addresource.gui = resource.gui
				addresource.ssh = resource.ssh
				addresource.snmp = resource.snmp
				addresource.mgmtaccess = resource.mgmtaccess
				addresource.restrictaccess = resource.restrictaccess
				addresource.dynamicrouting = resource.dynamicrouting
				addresource.decrementttl = resource.decrementttl
				addresource.ospf = resource.ospf
				addresource.bgp = resource.bgp
				addresource.rip = resource.rip
				addresource.hostroute = resource.hostroute
				addresource.advertiseondefaultpartition = resource.advertiseondefaultpartition
				addresource.networkroute = resource.networkroute
				addresource.tag = resource.tag
				addresource.hostrtgw = resource.hostrtgw
				addresource.metric = resource.metric
				addresource.vserverrhilevel = resource.vserverrhilevel
				addresource.vserverrhimode = resource.vserverrhimode
				addresource.ospflsatype = resource.ospflsatype
				addresource.ospfarea = resource.ospfarea
				addresource.state = resource.state
				addresource.vrid = resource.vrid
				addresource.icmpresponse = resource.icmpresponse
				addresource.ownernode = resource.ownernode
				addresource.arpresponse = resource.arpresponse
				addresource.ownerdownresponse = resource.ownerdownresponse
				addresource.td = resource.td
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsip() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].netmask = resource[i].netmask
						addresources[i].type = resource[i].type
						addresources[i].arp = resource[i].arp
						addresources[i].icmp = resource[i].icmp
						addresources[i].vserver = resource[i].vserver
						addresources[i].telnet = resource[i].telnet
						addresources[i].ftp = resource[i].ftp
						addresources[i].gui = resource[i].gui
						addresources[i].ssh = resource[i].ssh
						addresources[i].snmp = resource[i].snmp
						addresources[i].mgmtaccess = resource[i].mgmtaccess
						addresources[i].restrictaccess = resource[i].restrictaccess
						addresources[i].dynamicrouting = resource[i].dynamicrouting
						addresources[i].decrementttl = resource[i].decrementttl
						addresources[i].ospf = resource[i].ospf
						addresources[i].bgp = resource[i].bgp
						addresources[i].rip = resource[i].rip
						addresources[i].hostroute = resource[i].hostroute
						addresources[i].advertiseondefaultpartition = resource[i].advertiseondefaultpartition
						addresources[i].networkroute = resource[i].networkroute
						addresources[i].tag = resource[i].tag
						addresources[i].hostrtgw = resource[i].hostrtgw
						addresources[i].metric = resource[i].metric
						addresources[i].vserverrhilevel = resource[i].vserverrhilevel
						addresources[i].vserverrhimode = resource[i].vserverrhimode
						addresources[i].ospflsatype = resource[i].ospflsatype
						addresources[i].ospfarea = resource[i].ospfarea
						addresources[i].state = resource[i].state
						addresources[i].vrid = resource[i].vrid
						addresources[i].icmpresponse = resource[i].icmpresponse
						addresources[i].ownernode = resource[i].ownernode
						addresources[i].arpresponse = resource[i].arpresponse
						addresources[i].ownerdownresponse = resource[i].ownerdownresponse
						addresources[i].td = resource[i].td
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nsip.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsip()
				if type(resource) !=  type(deleteresource):
					deleteresource.ipaddress = resource
				else :
					deleteresource.ipaddress = resource.ipaddress
					deleteresource.td = resource.td
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsip() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipaddress = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsip() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipaddress = resource[i].ipaddress
							deleteresources[i].td = resource[i].td
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsip.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsip()
				updateresource.ipaddress = resource.ipaddress
				updateresource.td = resource.td
				updateresource.netmask = resource.netmask
				updateresource.arp = resource.arp
				updateresource.icmp = resource.icmp
				updateresource.vserver = resource.vserver
				updateresource.telnet = resource.telnet
				updateresource.ftp = resource.ftp
				updateresource.gui = resource.gui
				updateresource.ssh = resource.ssh
				updateresource.snmp = resource.snmp
				updateresource.mgmtaccess = resource.mgmtaccess
				updateresource.restrictaccess = resource.restrictaccess
				updateresource.decrementttl = resource.decrementttl
				updateresource.dynamicrouting = resource.dynamicrouting
				updateresource.ospf = resource.ospf
				updateresource.bgp = resource.bgp
				updateresource.rip = resource.rip
				updateresource.hostroute = resource.hostroute
				updateresource.advertiseondefaultpartition = resource.advertiseondefaultpartition
				updateresource.networkroute = resource.networkroute
				updateresource.hostrtgw = resource.hostrtgw
				updateresource.metric = resource.metric
				updateresource.vserverrhilevel = resource.vserverrhilevel
				updateresource.vserverrhimode = resource.vserverrhimode
				updateresource.ospflsatype = resource.ospflsatype
				updateresource.ospfarea = resource.ospfarea
				updateresource.tag = resource.tag
				updateresource.vrid = resource.vrid
				updateresource.icmpresponse = resource.icmpresponse
				updateresource.arpresponse = resource.arpresponse
				updateresource.ownerdownresponse = resource.ownerdownresponse
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsip() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].ipaddress = resource[i].ipaddress
						updateresources[i].td = resource[i].td
						updateresources[i].netmask = resource[i].netmask
						updateresources[i].arp = resource[i].arp
						updateresources[i].icmp = resource[i].icmp
						updateresources[i].vserver = resource[i].vserver
						updateresources[i].telnet = resource[i].telnet
						updateresources[i].ftp = resource[i].ftp
						updateresources[i].gui = resource[i].gui
						updateresources[i].ssh = resource[i].ssh
						updateresources[i].snmp = resource[i].snmp
						updateresources[i].mgmtaccess = resource[i].mgmtaccess
						updateresources[i].restrictaccess = resource[i].restrictaccess
						updateresources[i].decrementttl = resource[i].decrementttl
						updateresources[i].dynamicrouting = resource[i].dynamicrouting
						updateresources[i].ospf = resource[i].ospf
						updateresources[i].bgp = resource[i].bgp
						updateresources[i].rip = resource[i].rip
						updateresources[i].hostroute = resource[i].hostroute
						updateresources[i].advertiseondefaultpartition = resource[i].advertiseondefaultpartition
						updateresources[i].networkroute = resource[i].networkroute
						updateresources[i].hostrtgw = resource[i].hostrtgw
						updateresources[i].metric = resource[i].metric
						updateresources[i].vserverrhilevel = resource[i].vserverrhilevel
						updateresources[i].vserverrhimode = resource[i].vserverrhimode
						updateresources[i].ospflsatype = resource[i].ospflsatype
						updateresources[i].ospfarea = resource[i].ospfarea
						updateresources[i].tag = resource[i].tag
						updateresources[i].vrid = resource[i].vrid
						updateresources[i].icmpresponse = resource[i].icmpresponse
						updateresources[i].arpresponse = resource[i].arpresponse
						updateresources[i].ownerdownresponse = resource[i].ownerdownresponse
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsip resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsip()
				if type(resource) !=  type(unsetresource):
					unsetresource.ipaddress = resource
				else :
					unsetresource.ipaddress = resource.ipaddress
					unsetresource.td = resource.td
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsip() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ipaddress = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsip() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ipaddress = resource[i].ipaddress
							unsetresources[i].td = resource[i].td
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable nsip.
		"""
		try :
			if type(resource) is not list :
				enableresource = nsip()
				if type(resource) !=  type(enableresource):
					enableresource.ipaddress = resource
				else :
					enableresource.ipaddress = resource.ipaddress
					enableresource.td = resource.td
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ nsip() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].ipaddress = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ nsip() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].ipaddress = resource[i].ipaddress
							enableresources[i].td = resource[i].td
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable nsip.
		"""
		try :
			if type(resource) is not list :
				disableresource = nsip()
				if type(resource) !=  type(disableresource):
					disableresource.ipaddress = resource
				else :
					disableresource.ipaddress = resource.ipaddress
					disableresource.td = resource.td
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ nsip() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].ipaddress = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ nsip() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].ipaddress = resource[i].ipaddress
							disableresources[i].td = resource[i].td
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsip resources that are configured on netscaler.
		"""
		response = None
		try :
			if not name :
				obj = nsip()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nsip()
					obj.ipaddress = name
					# option_ = options()
					# option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) != cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nsip() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the nsip resources that are configured on netscaler.
	# This uses nsip_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nsip()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nsip resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsip()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nsip resources configured on NetScaler.
		"""
		try :
			obj = nsip()
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
		r""" Use this API to count filtered the set of nsip resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsip()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Arpresponse:
		NONE = "NONE"
		ONE_VSERVER = "ONE_VSERVER"
		ALL_VSERVERS = "ALL_VSERVERS"

	class Networkroute:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ospf:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ospflsatype:
		TYPE1 = "TYPE1"
		TYPE5 = "TYPE5"

	class Bgp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mgmtaccess:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Hostroute:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Icmp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Icmpresponse:
		NONE = "NONE"
		ONE_VSERVER = "ONE_VSERVER"
		ALL_VSERVERS = "ALL_VSERVERS"
		VSVR_CNTRLD = "VSVR_CNTRLD"

	class Advertiseondefaultpartition:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Iptype:
		SNIP = "SNIP"
		VIP = "VIP"
		NSIP = "NSIP"
		GSLBsiteIP = "GSLBsiteIP"
		CLIP = "CLIP"

	class Decrementttl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ssh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Gui:
		ENABLED = "ENABLED"
		SECUREONLY = "SECUREONLY"
		DISABLED = "DISABLED"

	class Dynamicrouting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Type:
		SNIP = "SNIP"
		VIP = "VIP"
		NSIP = "NSIP"
		GSLBsiteIP = "GSLBsiteIP"
		CLIP = "CLIP"

	class Arp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ftp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ownerdownresponse:
		YES = "YES"
		NO = "NO"

	class Vserverrhilevel:
		ONE_VSERVER = "ONE_VSERVER"
		ALL_VSERVERS = "ALL_VSERVERS"
		NONE = "NONE"
		VSVR_CNTRLD = "VSVR_CNTRLD"

	class Vserver:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Snmp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Restrictaccess:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Vserverrhimode:
		DYNAMIC_ROUTING = "DYNAMIC_ROUTING"
		RISE = "RISE"

	class Telnet:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nsip_response(base_response) :
	def __init__(self, length=1) :
		self.nsip = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsip = [nsip() for _ in range(length)]

