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

class Interface(base_resource) :
	""" Configuration for interface resource. """
	def __init__(self) :
		self._id = None
		self._speed = None
		self._duplex = None
		self._flowctl = None
		self._autoneg = None
		self._hamonitor = None
		self._haheartbeat = None
		self._mtu = None
		self._tagall = None
		self._trunk = None
		self._trunkmode = None
		self._trunkallowedvlan = None
		self._lacpmode = None
		self._lacpkey = None
		self._lagtype = None
		self._lacppriority = None
		self._lacptimeout = None
		self._ifalias = None
		self._throughput = None
		self._linkredundancy = None
		self._bandwidthhigh = None
		self._bandwidthnormal = None
		self._lldpmode = None
		self._lrsetpriority = None
		self._devicename = None
		self._unit = None
		self._description = None
		self._flags = None
		self._actualmtu = None
		self._vlan = None
		self._mac = None
		self._uptime = None
		self._downtime = None
		self._reqmedia = None
		self._reqspeed = None
		self._reqduplex = None
		self._reqflowcontrol = None
		self._actmedia = None
		self._actspeed = None
		self._actduplex = None
		self._actflowctl = None
		self._mode = None
		self._state = None
		self._autonegresult = None
		self._tagged = None
		self._taggedany = None
		self._taggedautolearn = None
		self._hangdetect = None
		self._hangreset = None
		self._linkstate = None
		self._intfstate = None
		self._rxpackets = None
		self._rxbytes = None
		self._rxerrors = None
		self._rxdrops = None
		self._txpackets = None
		self._txbytes = None
		self._txerrors = None
		self._txdrops = None
		self._indisc = None
		self._outdisc = None
		self._fctls = None
		self._hangs = None
		self._stsstalls = None
		self._txstalls = None
		self._rxstalls = None
		self._bdgmacmoved = None
		self._bdgmuted = None
		self._vmac = None
		self._vmac6 = None
		self._reqthroughput = None
		self._actthroughput = None
		self._backplane = None
		self._ifnum = None
		self._cleartime = None
		self._slavestate = None
		self._slavemedia = None
		self._slavespeed = None
		self._slaveduplex = None
		self._slaveflowctl = None
		self._slavetime = None
		self._intftype = None
		self._svmcmd = None
		self._lacpactormode = None
		self._lacpactortimeout = None
		self._lacpactorpriority = None
		self._lacpactorportno = None
		self._lacppartnerstate = None
		self._lacppartnertimeout = None
		self._lacppartneraggregation = None
		self._lacppartnerinsync = None
		self._lacppartnercollecting = None
		self._lacppartnerdistributing = None
		self._lacppartnerdefaulted = None
		self._lacppartnerexpired = None
		self._lacppartnerpriority = None
		self._lacppartnersystemmac = None
		self._lacppartnersystempriority = None
		self._lacppartnerportno = None
		self._lacppartnerkey = None
		self._lacpactoraggregation = None
		self._lacpactorinsync = None
		self._lacpactorcollecting = None
		self._lacpactordistributing = None
		self._lacpportmuxstate = None
		self._lacpportrxstat = None
		self._lacpportselectstate = None
		self._lractiveintf = None
		self.___count = None

	@property
	def id(self) :
		r"""Interface number, in C/U format, where C can take one of the following values:
		* 0 - Indicates a management interface.
		* 1 - Indicates a 1 Gbps port.
		* 10 - Indicates a 10 Gbps port.
		* LA - Indicates a link aggregation port.
		* LO - Indicates a loop back port.
		U is a unique integer for representing an interface in a particular port group.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		r"""Interface number, in C/U format, where C can take one of the following values:
		* 0 - Indicates a management interface.
		* 1 - Indicates a 1 Gbps port.
		* 10 - Indicates a 10 Gbps port.
		* LA - Indicates a link aggregation port.
		* LO - Indicates a loop back port.
		U is a unique integer for representing an interface in a particular port group.
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def speed(self) :
		r"""Ethernet speed of the interface, in Mbps. 
		Notes:
		* If you set the speed as AUTO, the Citrix ADC attempts to auto-negotiate or auto-sense the link speed of the interface when it is UP. You must enable auto negotiation on the interface.
		* If you set a speed other than AUTO, you must specify the same speed for the peer network device. Mismatched speed and duplex settings between the peer devices of a link lead to link errors, packet loss, and other errors. 
		Some interfaces do not support certain speeds. If you specify an unsupported speed, an error message appears.<br/>Default value: AUTO<br/>Possible values = AUTO, 10, 100, 1000, 10000, 25000, 40000, 50000, 100000.
		"""
		try :
			return self._speed
		except Exception as e:
			raise e

	@speed.setter
	def speed(self, speed) :
		r"""Ethernet speed of the interface, in Mbps. 
		Notes:
		* If you set the speed as AUTO, the Citrix ADC attempts to auto-negotiate or auto-sense the link speed of the interface when it is UP. You must enable auto negotiation on the interface.
		* If you set a speed other than AUTO, you must specify the same speed for the peer network device. Mismatched speed and duplex settings between the peer devices of a link lead to link errors, packet loss, and other errors. 
		Some interfaces do not support certain speeds. If you specify an unsupported speed, an error message appears.<br/>Default value: AUTO<br/>Possible values = AUTO, 10, 100, 1000, 10000, 25000, 40000, 50000, 100000
		"""
		try :
			self._speed = speed
		except Exception as e:
			raise e

	@property
	def duplex(self) :
		r"""The duplex mode for the interface. Notes:* If you set the duplex mode to AUTO, the Citrix ADC attempts to auto-negotiate the duplex mode of the interface when it is UP. You must enable auto negotiation on the interface. If you set a duplex mode other than AUTO, you must specify the same duplex mode for the peer network device. Mismatched speed and duplex settings between the peer devices of a link lead to link errors, packet loss, and other errors.<br/>Default value: AUTO<br/>Possible values = AUTO, HALF, FULL.
		"""
		try :
			return self._duplex
		except Exception as e:
			raise e

	@duplex.setter
	def duplex(self, duplex) :
		r"""The duplex mode for the interface. Notes:* If you set the duplex mode to AUTO, the Citrix ADC attempts to auto-negotiate the duplex mode of the interface when it is UP. You must enable auto negotiation on the interface. If you set a duplex mode other than AUTO, you must specify the same duplex mode for the peer network device. Mismatched speed and duplex settings between the peer devices of a link lead to link errors, packet loss, and other errors.<br/>Default value: AUTO<br/>Possible values = AUTO, HALF, FULL
		"""
		try :
			self._duplex = duplex
		except Exception as e:
			raise e

	@property
	def flowctl(self) :
		r"""802.3x flow control setting for the interface.  The 802.3x specification does not define flow control for 10 Mbps and 100 Mbps speeds, but if a Gigabit Ethernet interface operates at those speeds, the flow control settings can be applied. The flow control setting that is finally applied to an interface depends on auto-negotiation. With the ON option, the peer negotiates the flow control, but the appliance then forces two-way flow control for the interface.<br/>Default value: OFF<br/>Possible values = OFF, RX, TX, RXTX, ON.
		"""
		try :
			return self._flowctl
		except Exception as e:
			raise e

	@flowctl.setter
	def flowctl(self, flowctl) :
		r"""802.3x flow control setting for the interface.  The 802.3x specification does not define flow control for 10 Mbps and 100 Mbps speeds, but if a Gigabit Ethernet interface operates at those speeds, the flow control settings can be applied. The flow control setting that is finally applied to an interface depends on auto-negotiation. With the ON option, the peer negotiates the flow control, but the appliance then forces two-way flow control for the interface.<br/>Default value: OFF<br/>Possible values = OFF, RX, TX, RXTX, ON
		"""
		try :
			self._flowctl = flowctl
		except Exception as e:
			raise e

	@property
	def autoneg(self) :
		r"""Auto-negotiation state of the interface. With the ENABLED setting, the Citrix ADC auto-negotiates the speed and duplex settings with the peer network device on the link. The Citrix ADC appliance auto-negotiates the settings of only those parameters (speed or duplex mode) for which the value is set as AUTO.<br/>Default value: NSA_DVC_AUTONEG_ON<br/>Possible values = DISABLED, ENABLED.
		"""
		try :
			return self._autoneg
		except Exception as e:
			raise e

	@autoneg.setter
	def autoneg(self, autoneg) :
		r"""Auto-negotiation state of the interface. With the ENABLED setting, the Citrix ADC auto-negotiates the speed and duplex settings with the peer network device on the link. The Citrix ADC appliance auto-negotiates the settings of only those parameters (speed or duplex mode) for which the value is set as AUTO.<br/>Default value: NSA_DVC_AUTONEG_ON<br/>Possible values = DISABLED, ENABLED
		"""
		try :
			self._autoneg = autoneg
		except Exception as e:
			raise e

	@property
	def hamonitor(self) :
		r"""In a High Availability (HA) configuration, monitor the interface for failure events. In an HA configuration, an interface that has HA MON enabled and is not bound to any Failover Interface Set (FIS), is a critical interface. Failure or disabling of any critical interface triggers HA failover.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._hamonitor
		except Exception as e:
			raise e

	@hamonitor.setter
	def hamonitor(self, hamonitor) :
		r"""In a High Availability (HA) configuration, monitor the interface for failure events. In an HA configuration, an interface that has HA MON enabled and is not bound to any Failover Interface Set (FIS), is a critical interface. Failure or disabling of any critical interface triggers HA failover.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._hamonitor = hamonitor
		except Exception as e:
			raise e

	@property
	def haheartbeat(self) :
		r"""In a High Availability (HA) or Cluster configuration, configure the interface for sending heartbeats. In an HA or Cluster configuration, an interface that has HA Heartbeat disabled should not send the heartbeats.<br/>Default value: ON<br/>Possible values = OFF, ON.
		"""
		try :
			return self._haheartbeat
		except Exception as e:
			raise e

	@haheartbeat.setter
	def haheartbeat(self, haheartbeat) :
		r"""In a High Availability (HA) or Cluster configuration, configure the interface for sending heartbeats. In an HA or Cluster configuration, an interface that has HA Heartbeat disabled should not send the heartbeats.<br/>Default value: ON<br/>Possible values = OFF, ON
		"""
		try :
			self._haheartbeat = haheartbeat
		except Exception as e:
			raise e

	@property
	def mtu(self) :
		r"""The maximum transmission unit (MTU) is the largest packet size, measured in bytes excluding 14 bytes ethernet header and 4 bytes crc, that can be transmitted and received by this interface. Default value of MTU is 1500 on all the interface of Citrix ADC any value configured more than 1500 on the interface will make the interface as jumbo enabled. In case of cluster backplane interface MTU value will be changed to 1514 by default, user has to change the backplane interface value to maximum mtu configured on any of the interface in cluster system plus 14 bytes more for backplane interface if Jumbo is enabled on any of the interface in a cluster system. Changing the backplane will bring back the MTU of backplane interface to default value of 1500. If a channel is configured as backplane then the same holds true for channel as well as member interfaces.<br/>Default value: 1500<br/>Minimum length =  1500<br/>Maximum length =  9216.
		"""
		try :
			return self._mtu
		except Exception as e:
			raise e

	@mtu.setter
	def mtu(self, mtu) :
		r"""The maximum transmission unit (MTU) is the largest packet size, measured in bytes excluding 14 bytes ethernet header and 4 bytes crc, that can be transmitted and received by this interface. Default value of MTU is 1500 on all the interface of Citrix ADC any value configured more than 1500 on the interface will make the interface as jumbo enabled. In case of cluster backplane interface MTU value will be changed to 1514 by default, user has to change the backplane interface value to maximum mtu configured on any of the interface in cluster system plus 14 bytes more for backplane interface if Jumbo is enabled on any of the interface in a cluster system. Changing the backplane will bring back the MTU of backplane interface to default value of 1500. If a channel is configured as backplane then the same holds true for channel as well as member interfaces.<br/>Default value: 1500<br/>Minimum length =  1500<br/>Maximum length =  9216
		"""
		try :
			self._mtu = mtu
		except Exception as e:
			raise e

	@property
	def tagall(self) :
		r"""Add a four-byte 802.1q tag to every packet sent on this interface.  The ON setting applies the tag for this interface's native VLAN. OFF applies the tag for all VLANs other than the native VLAN.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._tagall
		except Exception as e:
			raise e

	@tagall.setter
	def tagall(self, tagall) :
		r"""Add a four-byte 802.1q tag to every packet sent on this interface.  The ON setting applies the tag for this interface's native VLAN. OFF applies the tag for all VLANs other than the native VLAN.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._tagall = tagall
		except Exception as e:
			raise e

	@property
	def trunk(self) :
		r"""This argument is deprecated by tagall.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._trunk
		except Exception as e:
			raise e

	@trunk.setter
	def trunk(self, trunk) :
		r"""This argument is deprecated by tagall.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._trunk = trunk
		except Exception as e:
			raise e

	@property
	def trunkmode(self) :
		r"""Accept and send 802.1q VLAN tagged packets, based on Allowed Vlan List of this interface.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._trunkmode
		except Exception as e:
			raise e

	@trunkmode.setter
	def trunkmode(self, trunkmode) :
		r"""Accept and send 802.1q VLAN tagged packets, based on Allowed Vlan List of this interface.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._trunkmode = trunkmode
		except Exception as e:
			raise e

	@property
	def trunkallowedvlan(self) :
		r"""VLAN ID or range of VLAN IDs will be allowed on this trunk interface. In the command line interface, separate the range with a hyphen. For example: 40-90.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._trunkallowedvlan
		except Exception as e:
			raise e

	@trunkallowedvlan.setter
	def trunkallowedvlan(self, trunkallowedvlan) :
		r"""VLAN ID or range of VLAN IDs will be allowed on this trunk interface. In the command line interface, separate the range with a hyphen. For example: 40-90.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._trunkallowedvlan = trunkallowedvlan
		except Exception as e:
			raise e

	@property
	def lacpmode(self) :
		r"""Bind the interface to a LA channel created by the Link Aggregation control protocol (LACP).  
		Available settings function as follows:
		* Active - The LA channel port of the Citrix ADC generates LACPDU messages on a regular basis, regardless of any need expressed by its peer device to receive them.
		* Passive - The LA channel port of the Citrix ADC does not transmit LACPDU messages unless the peer device port is in the active mode. That is, the port does not speak unless spoken to.
		* Disabled - Unbinds the interface from the LA channel. If this is the only interface in the LA channel, the LA channel is removed.<br/>Default value: DISABLED<br/>Possible values = DISABLED, ACTIVE, PASSIVE.
		"""
		try :
			return self._lacpmode
		except Exception as e:
			raise e

	@lacpmode.setter
	def lacpmode(self, lacpmode) :
		r"""Bind the interface to a LA channel created by the Link Aggregation control protocol (LACP).  
		Available settings function as follows:
		* Active - The LA channel port of the Citrix ADC generates LACPDU messages on a regular basis, regardless of any need expressed by its peer device to receive them.
		* Passive - The LA channel port of the Citrix ADC does not transmit LACPDU messages unless the peer device port is in the active mode. That is, the port does not speak unless spoken to.
		* Disabled - Unbinds the interface from the LA channel. If this is the only interface in the LA channel, the LA channel is removed.<br/>Default value: DISABLED<br/>Possible values = DISABLED, ACTIVE, PASSIVE
		"""
		try :
			self._lacpmode = lacpmode
		except Exception as e:
			raise e

	@property
	def lacpkey(self) :
		r"""Integer identifying the LACP LA channel to which the interface is to be bound. 
		For an LA channel of the Citrix ADC, this digit specifies the variable x of an LA channel in LA/x notation, where x can range from 1 to 8. For example, if you specify 3 as the LACP key for an LA channel, the interface is bound to the LA channel LA/3.
		For an LA channel of a cluster configuration, this digit specifies the variable y of a cluster LA channel in CLA/(y-4) notation, where y can range from 5 to 8. For example, if you specify 6 as the LACP key for a cluster LA channel, the interface is bound to the cluster LA channel CLA/2.<br/>Minimum length =  1<br/>Maximum length =  8.
		"""
		try :
			return self._lacpkey
		except Exception as e:
			raise e

	@lacpkey.setter
	def lacpkey(self, lacpkey) :
		r"""Integer identifying the LACP LA channel to which the interface is to be bound. 
		For an LA channel of the Citrix ADC, this digit specifies the variable x of an LA channel in LA/x notation, where x can range from 1 to 8. For example, if you specify 3 as the LACP key for an LA channel, the interface is bound to the LA channel LA/3.
		For an LA channel of a cluster configuration, this digit specifies the variable y of a cluster LA channel in CLA/(y-4) notation, where y can range from 5 to 8. For example, if you specify 6 as the LACP key for a cluster LA channel, the interface is bound to the cluster LA channel CLA/2.<br/>Minimum length =  1<br/>Maximum length =  8
		"""
		try :
			self._lacpkey = lacpkey
		except Exception as e:
			raise e

	@property
	def lagtype(self) :
		r"""Type of entity (Citrix ADC or cluster configuration) for which to create the channel.<br/>Default value: NODE<br/>Possible values = NODE, CLUSTER.
		"""
		try :
			return self._lagtype
		except Exception as e:
			raise e

	@lagtype.setter
	def lagtype(self, lagtype) :
		r"""Type of entity (Citrix ADC or cluster configuration) for which to create the channel.<br/>Default value: NODE<br/>Possible values = NODE, CLUSTER
		"""
		try :
			self._lagtype = lagtype
		except Exception as e:
			raise e

	@property
	def lacppriority(self) :
		r"""LACP port priority, expressed as an integer. The lower the number, the higher the priority. The Citrix ADC limits the number of interfaces in an LA channel to sixteen.<br/>Default value: 32768<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._lacppriority
		except Exception as e:
			raise e

	@lacppriority.setter
	def lacppriority(self, lacppriority) :
		r"""LACP port priority, expressed as an integer. The lower the number, the higher the priority. The Citrix ADC limits the number of interfaces in an LA channel to sixteen.<br/>Default value: 32768<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._lacppriority = lacppriority
		except Exception as e:
			raise e

	@property
	def lacptimeout(self) :
		r"""Interval at which the Citrix ADC sends LACPDU messages to the peer device on the LA channel.
		Available settings function as follows:
		LONG - 30 seconds.
		SHORT - 1 second.<br/>Default value: NSA_LACP_TIMEOUT_LONG<br/>Possible values = LONG, SHORT.
		"""
		try :
			return self._lacptimeout
		except Exception as e:
			raise e

	@lacptimeout.setter
	def lacptimeout(self, lacptimeout) :
		r"""Interval at which the Citrix ADC sends LACPDU messages to the peer device on the LA channel.
		Available settings function as follows:
		LONG - 30 seconds.
		SHORT - 1 second.<br/>Default value: NSA_LACP_TIMEOUT_LONG<br/>Possible values = LONG, SHORT
		"""
		try :
			self._lacptimeout = lacptimeout
		except Exception as e:
			raise e

	@property
	def ifalias(self) :
		r"""Alias name for the interface. Used only to enhance readability. To perform any operations, you have to specify the interface ID.<br/>Default value: " "<br/>Maximum length =  31.
		"""
		try :
			return self._ifalias
		except Exception as e:
			raise e

	@ifalias.setter
	def ifalias(self, ifalias) :
		r"""Alias name for the interface. Used only to enhance readability. To perform any operations, you have to specify the interface ID.<br/>Default value: " "<br/>Maximum length =  31
		"""
		try :
			self._ifalias = ifalias
		except Exception as e:
			raise e

	@property
	def throughput(self) :
		r"""Low threshold value for the throughput of the interface, in Mbps. In an HA configuration, failover is triggered if the interface has HA MON enabled and the throughput is below the specified the threshold.<br/>Maximum length =  160000.
		"""
		try :
			return self._throughput
		except Exception as e:
			raise e

	@throughput.setter
	def throughput(self, throughput) :
		r"""Low threshold value for the throughput of the interface, in Mbps. In an HA configuration, failover is triggered if the interface has HA MON enabled and the throughput is below the specified the threshold.<br/>Maximum length =  160000
		"""
		try :
			self._throughput = throughput
		except Exception as e:
			raise e

	@property
	def linkredundancy(self) :
		r"""Link Redundancy for Cluster LAG.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._linkredundancy
		except Exception as e:
			raise e

	@linkredundancy.setter
	def linkredundancy(self, linkredundancy) :
		r"""Link Redundancy for Cluster LAG.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._linkredundancy = linkredundancy
		except Exception as e:
			raise e

	@property
	def bandwidthhigh(self) :
		r"""High threshold value for the bandwidth usage of the interface, in Mbps. The Citrix ADC generates an SNMP trap message when the bandwidth usage of the interface is greater than or equal to the specified high threshold value.<br/>Maximum length =  160000.
		"""
		try :
			return self._bandwidthhigh
		except Exception as e:
			raise e

	@bandwidthhigh.setter
	def bandwidthhigh(self, bandwidthhigh) :
		r"""High threshold value for the bandwidth usage of the interface, in Mbps. The Citrix ADC generates an SNMP trap message when the bandwidth usage of the interface is greater than or equal to the specified high threshold value.<br/>Maximum length =  160000
		"""
		try :
			self._bandwidthhigh = bandwidthhigh
		except Exception as e:
			raise e

	@property
	def bandwidthnormal(self) :
		r"""Normal threshold value for the bandwidth usage of the interface, in Mbps. When the bandwidth usage of the interface becomes less than or equal to the specified normal threshold after exceeding the high threshold, the Citrix ADC generates an SNMP trap message to indicate that the bandwidth usage has returned to normal.<br/>Maximum length =  160000.
		"""
		try :
			return self._bandwidthnormal
		except Exception as e:
			raise e

	@bandwidthnormal.setter
	def bandwidthnormal(self, bandwidthnormal) :
		r"""Normal threshold value for the bandwidth usage of the interface, in Mbps. When the bandwidth usage of the interface becomes less than or equal to the specified normal threshold after exceeding the high threshold, the Citrix ADC generates an SNMP trap message to indicate that the bandwidth usage has returned to normal.<br/>Maximum length =  160000
		"""
		try :
			self._bandwidthnormal = bandwidthnormal
		except Exception as e:
			raise e

	@property
	def lldpmode(self) :
		r"""Link Layer Discovery Protocol (LLDP) mode for an interface. The resultant LLDP mode of an interface depends on the LLDP mode configured at the global and the interface levels.<br/>Possible values = NONE, TRANSMITTER, RECEIVER, TRANSCEIVER.
		"""
		try :
			return self._lldpmode
		except Exception as e:
			raise e

	@lldpmode.setter
	def lldpmode(self, lldpmode) :
		r"""Link Layer Discovery Protocol (LLDP) mode for an interface. The resultant LLDP mode of an interface depends on the LLDP mode configured at the global and the interface levels.<br/>Possible values = NONE, TRANSMITTER, RECEIVER, TRANSCEIVER
		"""
		try :
			self._lldpmode = lldpmode
		except Exception as e:
			raise e

	@property
	def lrsetpriority(self) :
		r"""LRSET port priority, expressed as an integer ranging from 1 to 1024. The highest priority is 1. The Citrix ADC limits the number of interfaces in an LRSET to 8. Within a LRSET the highest LR Priority Interface is considered as the first candidate for the Active interface, if the interface is UP.<br/>Default value: 1024<br/>Minimum length =  1<br/>Maximum length =  1024.
		"""
		try :
			return self._lrsetpriority
		except Exception as e:
			raise e

	@lrsetpriority.setter
	def lrsetpriority(self, lrsetpriority) :
		r"""LRSET port priority, expressed as an integer ranging from 1 to 1024. The highest priority is 1. The Citrix ADC limits the number of interfaces in an LRSET to 8. Within a LRSET the highest LR Priority Interface is considered as the first candidate for the Active interface, if the interface is UP.<br/>Default value: 1024<br/>Minimum length =  1<br/>Maximum length =  1024
		"""
		try :
			self._lrsetpriority = lrsetpriority
		except Exception as e:
			raise e

	@property
	def devicename(self) :
		r"""Name of the interface.
		"""
		try :
			return self._devicename
		except Exception as e:
			raise e

	@property
	def unit(self) :
		r"""Unit number for this interface, signifying the sequence number in which this interface is discovered on this Citrix ADC.
		"""
		try :
			return self._unit
		except Exception as e:
			raise e

	@property
	def description(self) :
		r"""Display the type of interface, the speeds at which this interface can operate, and, if applicable, the type of SFP,.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""Flags for this interface. Used for communicating the device states.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def actualmtu(self) :
		r"""MTU for this interface (the largest frame that can transit this interface).
		"""
		try :
			return self._actualmtu
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""Native VLAN for this interface.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@property
	def mac(self) :
		r"""MAC address for this interface.
		"""
		try :
			return self._mac
		except Exception as e:
			raise e

	@property
	def uptime(self) :
		r"""Duration for which the interface has been UP (Example: 3 hours 1 minute 1 second). This value is reset when the interface state changes to DOWN..
		"""
		try :
			return self._uptime
		except Exception as e:
			raise e

	@property
	def downtime(self) :
		r"""Duration for which the interface has been DOWN.  This value is reset when the interface state changes to UP.(Example: 3 hours 1 minute 1 second).
		"""
		try :
			return self._downtime
		except Exception as e:
			raise e

	@property
	def reqmedia(self) :
		r"""Requested media setting for this interface.<br/>Possible values = AUTO, UTP, FIBER.
		"""
		try :
			return self._reqmedia
		except Exception as e:
			raise e

	@property
	def reqspeed(self) :
		r"""Requested speed setting for this interface.<br/>Possible values = AUTO, 10, 100, 1000, 10000, 25000, 40000, 50000, 100000.
		"""
		try :
			return self._reqspeed
		except Exception as e:
			raise e

	@property
	def reqduplex(self) :
		r"""Requested duplex setting for this interface.<br/>Possible values = AUTO, HALF, FULL.
		"""
		try :
			return self._reqduplex
		except Exception as e:
			raise e

	@property
	def reqflowcontrol(self) :
		r"""Requested flow control setting for this interface.<br/>Possible values = OFF, RX, TX, RXTX, ON.
		"""
		try :
			return self._reqflowcontrol
		except Exception as e:
			raise e

	@property
	def actmedia(self) :
		r"""Actual media setting for this interface.<br/>Possible values = AUTO, UTP, FIBER.
		"""
		try :
			return self._actmedia
		except Exception as e:
			raise e

	@property
	def actspeed(self) :
		r"""Actual speed setting for this interface.<br/>Possible values = AUTO, 10, 100, 1000, 10000, 25000, 40000, 50000, 100000.
		"""
		try :
			return self._actspeed
		except Exception as e:
			raise e

	@property
	def actduplex(self) :
		r"""Actual duplex setting for this interface.<br/>Possible values = AUTO, HALF, FULL.
		"""
		try :
			return self._actduplex
		except Exception as e:
			raise e

	@property
	def actflowctl(self) :
		r"""Actual flow control setting for this interface.<br/>Possible values = OFF, RX, TX, RXTX, ON.
		"""
		try :
			return self._actflowctl
		except Exception as e:
			raise e

	@property
	def mode(self) :
		r"""Interface Link Aggregation mode (Auto/Manual) setting.<br/>Possible values = MANUAL, AUTO.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Link state of the interface (UP/DOWN).<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def autonegresult(self) :
		r"""Actual auto-negotiation setting for this interface.
		"""
		try :
			return self._autonegresult
		except Exception as e:
			raise e

	@property
	def tagged(self) :
		r"""VLAN tags setting on this channel.
		"""
		try :
			return self._tagged
		except Exception as e:
			raise e

	@property
	def taggedany(self) :
		r"""Interface setting to accept/drop all tagged packets.
		"""
		try :
			return self._taggedany
		except Exception as e:
			raise e

	@property
	def taggedautolearn(self) :
		r"""Dynamic VLAN membership autolearning enabled or disabled on this interface.
		"""
		try :
			return self._taggedautolearn
		except Exception as e:
			raise e

	@property
	def hangdetect(self) :
		r"""Hang detection enabled or disabled for this interface.
		"""
		try :
			return self._hangdetect
		except Exception as e:
			raise e

	@property
	def hangreset(self) :
		r"""Hang reset enabled or disabled for this interface.
		"""
		try :
			return self._hangreset
		except Exception as e:
			raise e

	@property
	def linkstate(self) :
		r"""The current state of the link associated with the interface. For logical interfaces (LA), the state of the link is dependent on the state of the slave interfaces. For the link to be UP at least one of the slave interfaces needs to be UP.
		"""
		try :
			return self._linkstate
		except Exception as e:
			raise e

	@property
	def intfstate(self) :
		r"""Current state of the specified interface.  The interface state set to UP only if the link state is UP and administrative state is ENABLED.
		"""
		try :
			return self._intfstate
		except Exception as e:
			raise e

	@property
	def rxpackets(self) :
		r"""Number of packets received by an interface since the Citrix ADC was started or the interface statistics were cleared.
		"""
		try :
			return self._rxpackets
		except Exception as e:
			raise e

	@property
	def rxbytes(self) :
		r"""Number of bytes received by an interface since the Citrix ADC was started or the interface statistics were cleared.
		"""
		try :
			return self._rxbytes
		except Exception as e:
			raise e

	@property
	def rxerrors(self) :
		r"""Number of inbound packets dropped by the hardware on a specified interface since the Citrix ADC was started or the interface statistics were cleared. Packets can be dropped because of CRC, length (undersize or oversize), or alignment errors.
		"""
		try :
			return self._rxerrors
		except Exception as e:
			raise e

	@property
	def rxdrops(self) :
		r"""Number of inbound packets dropped by the specified interface. Commonly dropped packets are multicast frames, spanning tree BPDUs, packets destined to a MAC not owned by the Citrix ADC when L2 mode is disabled, or packets tagged for a VLAN that is not bound to the interface.  In most healthy networks, this statistic increments at a steady rate regardless of traffic load.  A sharp spike in dropped packets generally indicates an issue with connected L2 switches, such as a forwarding database overflow resulting in packets being broadcast on all ports.
		"""
		try :
			return self._rxdrops
		except Exception as e:
			raise e

	@property
	def txpackets(self) :
		r"""Number of packets transmitted by an interface since the Citrix ADC was started or the interface statistics were cleared.
		"""
		try :
			return self._txpackets
		except Exception as e:
			raise e

	@property
	def txbytes(self) :
		r"""Number of bytes transmitted by an interface since the Citrix ADC was started or the interface statistics were cleared.
		"""
		try :
			return self._txbytes
		except Exception as e:
			raise e

	@property
	def txerrors(self) :
		r"""Number of outbound packets dropped by the hardware on a specified interface since the Citrix ADC was started or the interface statistics were cleared. Packets can be dropped because of length (undersize or oversize) errors or a lack of resources. This statistic is available only for:
		(1) Loop back interface (LO) of all platforms.
		(2) All data ports on the Citrix ADC 12000 platform.
		(3) Management ports on the Citrix ADC MPX 15000 and 17000 platforms.
		.
		"""
		try :
			return self._txerrors
		except Exception as e:
			raise e

	@property
	def txdrops(self) :
		r"""Number of packets dropped in transmission by the specified interface for one of the following reasons.
		(1) VLAN mismatch.
		(2) Oversized packets.
		(3) Interface congestion.
		(4) Loopback packets sent on non loop back interface.
		.
		"""
		try :
			return self._txdrops
		except Exception as e:
			raise e

	@property
	def indisc(self) :
		r"""Number of error-free inbound packets discarded by the specified interface because of a lack of resources (for example, insufficient receive buffers).
		"""
		try :
			return self._indisc
		except Exception as e:
			raise e

	@property
	def outdisc(self) :
		r"""Number of error-free outbound packets discarded by the specified interface because of a lack of resources. This statistic is not available on:
		(1) 10G ports of Citrix ADC MPX 12500/12500/15500-10G  platforms.
		(2) 10G data ports on Citrix ADC MPX 17500/19500/21500 platforms.
		.
		"""
		try :
			return self._outdisc
		except Exception as e:
			raise e

	@property
	def fctls(self) :
		r"""Number of times flow control is performed on the specified interface because of received pause frames.
		"""
		try :
			return self._fctls
		except Exception as e:
			raise e

	@property
	def hangs(self) :
		r"""Number of times the specified interface detected hangs in the transmit and receive paths since the Citrix ADC was started or the interface statistics were cleared.
		"""
		try :
			return self._hangs
		except Exception as e:
			raise e

	@property
	def stsstalls(self) :
		r"""Number of times the status updates for a specified interface were stalled since the Citrix ADC was started or the interface statistics were cleared. A status stall is detected when the status of the interface is not updated by the NIC hardware within 0.8 seconds of the last update.
		"""
		try :
			return self._stsstalls
		except Exception as e:
			raise e

	@property
	def txstalls(self) :
		r"""Number of times the interface stalled, when transmitting packets, since the Citrix ADC was started or the interface statistics were cleared. Transmit (Tx) stalls are detected when a packet posted for transmission is not transmitted in 4 seconds.
		"""
		try :
			return self._txstalls
		except Exception as e:
			raise e

	@property
	def rxstalls(self) :
		r"""Number of times the interface stalled, when receiving packets, since the Citrix ADC was started or the interface statistics were cleared. Receive (Rx) stalls are detected when the following conditions are met:
		(1)The link is up for more than 10 minutes.
		(2)Packets are transmitted, but no packets are received for 16 seconds.
		.
		"""
		try :
			return self._rxstalls
		except Exception as e:
			raise e

	@property
	def bdgmacmoved(self) :
		r"""Number of MAC moves between ports. A high rate of MAC moves typically indicates a bridge loop between two interfaces.
		"""
		try :
			return self._bdgmacmoved
		except Exception as e:
			raise e

	@property
	def bdgmuted(self) :
		r"""Number of times the specified interface stopped transmitting and receiving packets because of MAC moves between ports.
		"""
		try :
			return self._bdgmuted
		except Exception as e:
			raise e

	@property
	def vmac(self) :
		r"""Virtual MAC of this interface.
		"""
		try :
			return self._vmac
		except Exception as e:
			raise e

	@property
	def vmac6(self) :
		r"""Virtual MAC for IPv6 of this interface.
		"""
		try :
			return self._vmac6
		except Exception as e:
			raise e

	@property
	def reqthroughput(self) :
		r"""Minimum required throughput for an interface. Failover is triggered if the operating throughput of a Link Aggregation (LA) channel for which HAMON is ON falls below this value. The possible values are:
		1. 1000Mbps for 1G interfaces.
		2. 10000Mbps for 10G interfaces.
		3. 160000Mbps for Link Aggregation channels.<br/>Minimum value =  0<br/>Maximum value =  160000.
		"""
		try :
			return self._reqthroughput
		except Exception as e:
			raise e

	@property
	def actthroughput(self) :
		r"""Actual throughput for the interface.
		"""
		try :
			return self._actthroughput
		except Exception as e:
			raise e

	@property
	def backplane(self) :
		r"""The cluster backplane status of the interface. If the status is enabled, the interface is part of the cluster backplane. By default, the backplane status is disabled.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._backplane
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		r"""Contains the LA Master, if the interface is part of LA channel.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@property
	def cleartime(self) :
		r"""Time since the interface stats are cleared last time.
		"""
		try :
			return self._cleartime
		except Exception as e:
			raise e

	@property
	def slavestate(self) :
		r"""State of the member interfaces.
		"""
		try :
			return self._slavestate
		except Exception as e:
			raise e

	@property
	def slavemedia(self) :
		r"""Media type of the member interfaces.
		"""
		try :
			return self._slavemedia
		except Exception as e:
			raise e

	@property
	def slavespeed(self) :
		r"""Speed of the member interfaces.
		"""
		try :
			return self._slavespeed
		except Exception as e:
			raise e

	@property
	def slaveduplex(self) :
		r"""Duplex of the member interfaces.
		"""
		try :
			return self._slaveduplex
		except Exception as e:
			raise e

	@property
	def slaveflowctl(self) :
		r"""Flowcontrol of the member interfaces.
		"""
		try :
			return self._slaveflowctl
		except Exception as e:
			raise e

	@property
	def slavetime(self) :
		r"""UP time of the member interfaces.
		"""
		try :
			return self._slavetime
		except Exception as e:
			raise e

	@property
	def intftype(self) :
		r"""Interface Type, this field will have the interface type either it is virtual, physical or loopback. .<br/>Possible values = BROADCOM 5700/5701, TIGON1/TIGON2, INTEL 82546, INTEL 8255X(PRO), Link Aggregate, Loopback, Intel 82541/47, Broadcom 5704, Chelsio 1G, Intel 8247X, Intel 82576 VF, Xen Virtual, Intel 10G, Intel 82599 VF, Mellanox 100G, Mellanox 50G, Mellanox 25G, Intel FVL 40G, Intel FVL 25G, Intel FVL 10G, Intel FVL 40G VF, Mellanox VF, Hyper v, Cluster LAG, Intel 8247X SFP, XEN Interface, Chelsio 10G, KVM Virtio, VMXNET3.
		"""
		try :
			return self._intftype
		except Exception as e:
			raise e

	@property
	def svmcmd(self) :
		r"""New attribute added to identify the source of cmd, when SVM fires the nitro cmd, it will set the value of SVMCMD to be 1. .<br/>Default value: 0.
		"""
		try :
			return self._svmcmd
		except Exception as e:
			raise e

	@property
	def lacpactormode(self) :
		r"""
		* Active - The LA channel port of the Citrix ADC generates LACPDU messages on a regular basis, regardless of any need expressed by its peer device to receive them.
		* Passive - The LA channel port of the Citrix ADC does not transmit LACPDU messages unless the peer device port is in the active mode. That is, the port does not speak unless spoken to.
		* Disabled - Unbinds the interface from the LA channel. If this is the only interface in the LA channel, the LA channel is removed.<br/>Possible values = DISABLED, ACTIVE, PASSIVE.
		"""
		try :
			return self._lacpactormode
		except Exception as e:
			raise e

	@property
	def lacpactortimeout(self) :
		r"""Interval at which the Citrix ADC sends LACPDU messages to the peer device on the LA channel.
		Available settings function as follows:
		LONG - 30 seconds.
		SHORT - 1 second.<br/>Possible values = LONG, SHORT.
		"""
		try :
			return self._lacpactortimeout
		except Exception as e:
			raise e

	@property
	def lacpactorpriority(self) :
		r"""LACP Actor Priority. A LACP port priority is configured on each port using LACP. LACP uses the port priority with the port number to form the port identifier. The port priority determines which ports should be put in standby mode when there is a hardware limitation that prevents all compatible ports from aggregating.
		"""
		try :
			return self._lacpactorpriority
		except Exception as e:
			raise e

	@property
	def lacpactorportno(self) :
		r"""LACP Actor port number. LACP uses the port priority with the port number to form the port identifier.
		"""
		try :
			return self._lacpactorportno
		except Exception as e:
			raise e

	@property
	def lacppartnerstate(self) :
		r"""LACP Partner State. Whether the port is in Active or Passive negotiating state.<br/>Possible values = MANUAL, AUTO.
		"""
		try :
			return self._lacppartnerstate
		except Exception as e:
			raise e

	@property
	def lacppartnertimeout(self) :
		r"""The timeout value for the information revieved in LACPDUs. It can have values as SHORT or LONG. The SHORT timeout is 3s and the LONG timeout is 90s.<br/>Possible values = LONG, SHORT.
		"""
		try :
			return self._lacppartnertimeout
		except Exception as e:
			raise e

	@property
	def lacppartneraggregation(self) :
		r"""The Aggregation flag indicates that the participant will allow the link to be used as part of an aggregate. Otherwise the link is to be used as an individual link, i.e. not aggregated with any other.<br/>Possible values = NS_EMPTY_STR, AGG.
		"""
		try :
			return self._lacppartneraggregation
		except Exception as e:
			raise e

	@property
	def lacppartnerinsync(self) :
		r"""The Synchronization flag indicates that the transmitting participant.s mux component is in sync with the system id and key information transmitted.<br/>Possible values = NS_EMPTY_STR, SYNC.
		"""
		try :
			return self._lacppartnerinsync
		except Exception as e:
			raise e

	@property
	def lacppartnercollecting(self) :
		r"""The Collecting flag indicates that the participant.s collector, i.e. the reception component of the mux, is definitely on. If set the flag communicates collecting.<br/>Possible values = NS_EMPTY_STR, COLLECTING.
		"""
		try :
			return self._lacppartnercollecting
		except Exception as e:
			raise e

	@property
	def lacppartnerdistributing(self) :
		r"""The Distributing flag indicates that the participant.s distributor is not definitely off. If reset the flag indicates not distributing.<br/>Possible values = NS_EMPTY_STR, DISTRIBUTING.
		"""
		try :
			return self._lacppartnerdistributing
		except Exception as e:
			raise e

	@property
	def lacppartnerdefaulted(self) :
		r"""If the timer expires in the Expired state, the Receive Machine enters the Defaulted state.<br/>Possible values = NS_EMPTY_STR, DEFAULTED.
		"""
		try :
			return self._lacppartnerdefaulted
		except Exception as e:
			raise e

	@property
	def lacppartnerexpired(self) :
		r"""If the LACPDUs are received for timeout period, the Receive Machine enters the Expired state and the timer is restarted with the timeout value of SHORT timeout.<br/>Possible values = NS_EMPTY_STR, EXPIRED.
		"""
		try :
			return self._lacppartnerexpired
		except Exception as e:
			raise e

	@property
	def lacppartnerpriority(self) :
		r"""LACP Partner Priority. A LACP port priority is configured on each port using LACP. LACP uses the port priority with the port number to form the port identifier. 
		The port priority determines which ports should be put in standby mode when there is a hardware limitation that prevents all compatible ports from aggregating.
		"""
		try :
			return self._lacppartnerpriority
		except Exception as e:
			raise e

	@property
	def lacppartnersystemmac(self) :
		r"""LACP Partner System MAC.
		"""
		try :
			return self._lacppartnersystemmac
		except Exception as e:
			raise e

	@property
	def lacppartnersystempriority(self) :
		r"""LACP Partner System Priority. The LACP partner's system priority. The values for the priority range from 0 to 65535. The lower the value, the higher the system priority. The switch with the lower system priority value determines which links between LACP partner are active and which are in the standby for each LACP Channel.
		"""
		try :
			return self._lacppartnersystempriority
		except Exception as e:
			raise e

	@property
	def lacppartnerportno(self) :
		r"""LACP Partner Port number. LACP uses the port priority with the port number to form the port identifier.
		"""
		try :
			return self._lacppartnerportno
		except Exception as e:
			raise e

	@property
	def lacppartnerkey(self) :
		r"""LACP Partner Key. The LACP key used by the partner port.
		"""
		try :
			return self._lacppartnerkey
		except Exception as e:
			raise e

	@property
	def lacpactoraggregation(self) :
		r"""The Aggregation flag indicates that the participant will allow the link to be used as part of an aggregate. Otherwise the link is to be used as an individual link, i.e. not aggregated with any other.<br/>Possible values = NS_EMPTY_STR, AGG.
		"""
		try :
			return self._lacpactoraggregation
		except Exception as e:
			raise e

	@property
	def lacpactorinsync(self) :
		r"""The Synchronization flag indicates that the transmitting participant.s mux component is in sync with the system id and key information transmitted.<br/>Possible values = NS_EMPTY_STR, SYNC.
		"""
		try :
			return self._lacpactorinsync
		except Exception as e:
			raise e

	@property
	def lacpactorcollecting(self) :
		r"""The Collecting flag indicates that the participant.s collector, i.e. the reception component of the mux, is definitely on. If set the flag communicates collecting.<br/>Possible values = NS_EMPTY_STR, COLLECTING.
		"""
		try :
			return self._lacpactorcollecting
		except Exception as e:
			raise e

	@property
	def lacpactordistributing(self) :
		r"""The Distributing flag indicates that the participant.s distributor is not definitely off. If reset the flag indicates not distributing.<br/>Possible values = NS_EMPTY_STR, DISTRIBUTING.
		"""
		try :
			return self._lacpactordistributing
		except Exception as e:
			raise e

	@property
	def lacpportmuxstate(self) :
		r"""LACP Port MUX state. The state of the MUX control machine. The  Mux Control Machine attaches the physical port to an aggregate port, using the Selection Logic to choose an appropriate port, and turns the distributor and collector for the physical port on or off as required by protocol	information.<br/>Possible values = DETACHED, WAITING, ATTACHED, COLLECTING, DISTRIBUTING.
		"""
		try :
			return self._lacpportmuxstate
		except Exception as e:
			raise e

	@property
	def lacpportrxstat(self) :
		r"""LACP Port RX state. The state of the Receive machine. The Receive Machine maintains partner information, recording protocol information from LACPDUs sent by remote partner(s). Received information is subject to a timeout, and if sufficient time elapses the receive machine will revert to using default partner information.<br/>Possible values = INIT, PORT_DISABLED, LACP_DISABLED, EXPIRED, DEFAULTED, CURRENT.
		"""
		try :
			return self._lacpportrxstat
		except Exception as e:
			raise e

	@property
	def lacpportselectstate(self) :
		r"""LACP Port SELECT state. The state of the SELECT state machine, It could be SELECTED or UNSELECTED.<br/>Possible values = UNSELECTED, SELECTED, STANDBY.
		"""
		try :
			return self._lacpportselectstate
		except Exception as e:
			raise e

	@property
	def lractiveintf(self) :
		r"""LR set member interface state(active/inactive).
		"""
		try :
			return self._lractiveintf
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(Interface_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.Interface
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.id is not None :
				return str(self.id)
			return None
		except Exception as e :
			raise e



	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear Interface.
		"""
		try :
			if type(resource) is not list :
				clearresource = Interface()
				clearresource.id = resource.id
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ Interface() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].id = resource[i].id
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update Interface.
		"""
		try :
			if type(resource) is not list :
				updateresource = Interface()
				updateresource.id = resource.id
				updateresource.speed = resource.speed
				updateresource.duplex = resource.duplex
				updateresource.flowctl = resource.flowctl
				updateresource.autoneg = resource.autoneg
				updateresource.hamonitor = resource.hamonitor
				updateresource.haheartbeat = resource.haheartbeat
				updateresource.mtu = resource.mtu
				updateresource.tagall = resource.tagall
				updateresource.trunk = resource.trunk
				updateresource.trunkmode = resource.trunkmode
				updateresource.trunkallowedvlan = resource.trunkallowedvlan
				updateresource.lacpmode = resource.lacpmode
				updateresource.lacpkey = resource.lacpkey
				updateresource.lagtype = resource.lagtype
				updateresource.lacppriority = resource.lacppriority
				updateresource.lacptimeout = resource.lacptimeout
				updateresource.ifalias = resource.ifalias
				updateresource.throughput = resource.throughput
				updateresource.linkredundancy = resource.linkredundancy
				updateresource.bandwidthhigh = resource.bandwidthhigh
				updateresource.bandwidthnormal = resource.bandwidthnormal
				updateresource.lldpmode = resource.lldpmode
				updateresource.lrsetpriority = resource.lrsetpriority
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ Interface() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].speed = resource[i].speed
						updateresources[i].duplex = resource[i].duplex
						updateresources[i].flowctl = resource[i].flowctl
						updateresources[i].autoneg = resource[i].autoneg
						updateresources[i].hamonitor = resource[i].hamonitor
						updateresources[i].haheartbeat = resource[i].haheartbeat
						updateresources[i].mtu = resource[i].mtu
						updateresources[i].tagall = resource[i].tagall
						updateresources[i].trunk = resource[i].trunk
						updateresources[i].trunkmode = resource[i].trunkmode
						updateresources[i].trunkallowedvlan = resource[i].trunkallowedvlan
						updateresources[i].lacpmode = resource[i].lacpmode
						updateresources[i].lacpkey = resource[i].lacpkey
						updateresources[i].lagtype = resource[i].lagtype
						updateresources[i].lacppriority = resource[i].lacppriority
						updateresources[i].lacptimeout = resource[i].lacptimeout
						updateresources[i].ifalias = resource[i].ifalias
						updateresources[i].throughput = resource[i].throughput
						updateresources[i].linkredundancy = resource[i].linkredundancy
						updateresources[i].bandwidthhigh = resource[i].bandwidthhigh
						updateresources[i].bandwidthnormal = resource[i].bandwidthnormal
						updateresources[i].lldpmode = resource[i].lldpmode
						updateresources[i].lrsetpriority = resource[i].lrsetpriority
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of Interface resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = Interface()
				if type(resource) !=  type(unsetresource):
					unsetresource.id = resource
				else :
					unsetresource.id = resource.id
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ Interface() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ Interface() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i].id
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable Interface.
		"""
		try :
			if type(resource) is not list :
				enableresource = Interface()
				if type(resource) !=  type(enableresource):
					enableresource.id = resource
				else :
					enableresource.id = resource.id
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ Interface() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ Interface() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].id = resource[i].id
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable Interface.
		"""
		try :
			if type(resource) is not list :
				disableresource = Interface()
				if type(resource) !=  type(disableresource):
					disableresource.id = resource
				else :
					disableresource.id = resource.id
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ Interface() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ Interface() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].id = resource[i].id
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def reset(cls, client, resource) :
		r""" Use this API to reset Interface.
		"""
		try :
			if type(resource) is not list :
				resetresource = Interface()
				resetresource.id = resource.id
				return resetresource.perform_operation(client,"reset")
			else :
				if (resource and len(resource) > 0) :
					resetresources = [ Interface() for _ in range(len(resource))]
					for i in range(len(resource)) :
						resetresources[i].id = resource[i].id
				result = cls.perform_operation_bulk_request(client, resetresources,"reset")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the Interface resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = Interface()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = Interface()
					obj.id = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [Interface() for _ in range(len(name))]
						obj = [Interface() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = Interface()
							obj[i].id = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of Interface resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = Interface()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the Interface resources configured on NetScaler.
		"""
		try :
			obj = Interface()
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
		r""" Use this API to count filtered the set of Interface resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = Interface()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Lacpportselectstate:
		UNSELECTED = "UNSELECTED"
		SELECTED = "SELECTED"
		STANDBY = "STANDBY"

	class Reqduplex:
		AUTO = "AUTO"
		HALF = "HALF"
		FULL = "FULL"

	class Backplane:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mode:
		MANUAL = "MANUAL"
		AUTO = "AUTO"

	class Lacpportrxstat:
		INIT = "INIT"
		PORT_DISABLED = "PORT_DISABLED"
		LACP_DISABLED = "LACP_DISABLED"
		EXPIRED = "EXPIRED"
		DEFAULTED = "DEFAULTED"
		CURRENT = "CURRENT"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Lacppartnerinsync:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		SYNC = "SYNC"

	class Actduplex:
		AUTO = "AUTO"
		HALF = "HALF"
		FULL = "FULL"

	class Hamonitor:
		ON = "ON"
		OFF = "OFF"

	class Lacppartnerdistributing:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		DISTRIBUTING = "DISTRIBUTING"

	class Lacppartnercollecting:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		COLLECTING = "COLLECTING"

	class Reqspeed:
		AUTO = "AUTO"
		_10 = "10"
		_100 = "100"
		_1000 = "1000"
		_10000 = "10000"
		_25000 = "25000"
		_40000 = "40000"
		_50000 = "50000"
		_100000 = "100000"

	class Duplex:
		AUTO = "AUTO"
		HALF = "HALF"
		FULL = "FULL"

	class Actspeed:
		AUTO = "AUTO"
		_10 = "10"
		_100 = "100"
		_1000 = "1000"
		_10000 = "10000"
		_25000 = "25000"
		_40000 = "40000"
		_50000 = "50000"
		_100000 = "100000"

	class Reqmedia:
		AUTO = "AUTO"
		UTP = "UTP"
		FIBER = "FIBER"

	class Lacppartnertimeout:
		LONG = "LONG"
		SHORT = "SHORT"

	class Intftype:
		BROADCOM_5700_5701 = "BROADCOM 5700/5701"
		TIGON1_TIGON2 = "TIGON1/TIGON2"
		INTEL_82546 = "INTEL 82546"
		INTEL_8255X_PRO_ = "INTEL 8255X(PRO)"
		Link_Aggregate = "Link Aggregate"
		Loopback = "Loopback"
		Intel_82541_47 = "Intel 82541/47"
		Broadcom_5704 = "Broadcom 5704"
		Chelsio_1G = "Chelsio 1G"
		Intel_8247X = "Intel 8247X"
		Intel_82576_VF = "Intel 82576 VF"
		Xen_Virtual = "Xen Virtual"
		Intel_10G = "Intel 10G"
		Intel_82599_VF = "Intel 82599 VF"
		Mellanox_100G = "Mellanox 100G"
		Mellanox_50G = "Mellanox 50G"
		Mellanox_25G = "Mellanox 25G"
		Intel_FVL_40G = "Intel FVL 40G"
		Intel_FVL_25G = "Intel FVL 25G"
		Intel_FVL_10G = "Intel FVL 10G"
		Intel_FVL_40G_VF = "Intel FVL 40G VF"
		Mellanox_VF = "Mellanox VF"
		Hyper_v = "Hyper v"
		Cluster_LAG = "Cluster LAG"
		Intel_8247X_SFP = "Intel 8247X SFP"
		XEN_Interface = "XEN Interface"
		Chelsio_10G = "Chelsio 10G"
		KVM_Virtio = "KVM Virtio"
		VMXNET3 = "VMXNET3"

	class Lldpmode:
		NONE = "NONE"
		TRANSMITTER = "TRANSMITTER"
		RECEIVER = "RECEIVER"
		TRANSCEIVER = "TRANSCEIVER"

	class Autoneg:
		DISABLED = "DISABLED"
		ENABLED = "ENABLED"

	class Lacppartnerexpired:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		EXPIRED = "EXPIRED"

	class Lacppartnerstate:
		MANUAL = "MANUAL"
		AUTO = "AUTO"

	class Lacpportmuxstate:
		DETACHED = "DETACHED"
		WAITING = "WAITING"
		ATTACHED = "ATTACHED"
		COLLECTING = "COLLECTING"
		DISTRIBUTING = "DISTRIBUTING"

	class Lacpactordistributing:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		DISTRIBUTING = "DISTRIBUTING"

	class Lacpactorinsync:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		SYNC = "SYNC"

	class Trunkmode:
		ON = "ON"
		OFF = "OFF"

	class Lacppartnerdefaulted:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		DEFAULTED = "DEFAULTED"

	class Actmedia:
		AUTO = "AUTO"
		UTP = "UTP"
		FIBER = "FIBER"

	class Actflowctl:
		OFF = "OFF"
		RX = "RX"
		TX = "TX"
		RXTX = "RXTX"
		ON = "ON"

	class Lacpactormode:
		DISABLED = "DISABLED"
		ACTIVE = "ACTIVE"
		PASSIVE = "PASSIVE"

	class Speed:
		AUTO = "AUTO"
		_10 = "10"
		_100 = "100"
		_1000 = "1000"
		_10000 = "10000"
		_25000 = "25000"
		_40000 = "40000"
		_50000 = "50000"
		_100000 = "100000"

	class Haheartbeat:
		OFF = "OFF"
		ON = "ON"

	class Lacptimeout:
		LONG = "LONG"
		SHORT = "SHORT"

	class Tagall:
		ON = "ON"
		OFF = "OFF"

	class Lacppartneraggregation:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		AGG = "AGG"

	class Lacpactortimeout:
		LONG = "LONG"
		SHORT = "SHORT"

	class Trunk:
		ON = "ON"
		OFF = "OFF"

	class Lacpmode:
		DISABLED = "DISABLED"
		ACTIVE = "ACTIVE"
		PASSIVE = "PASSIVE"

	class Reqflowcontrol:
		OFF = "OFF"
		RX = "RX"
		TX = "TX"
		RXTX = "RXTX"
		ON = "ON"

	class Lacpactorcollecting:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		COLLECTING = "COLLECTING"

	class Lacpactoraggregation:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		AGG = "AGG"

	class Linkredundancy:
		ON = "ON"
		OFF = "OFF"

	class Flowctl:
		OFF = "OFF"
		RX = "RX"
		TX = "TX"
		RXTX = "RXTX"
		ON = "ON"

	class Lagtype:
		NODE = "NODE"
		CLUSTER = "CLUSTER"

class Interface_response(base_response) :
	def __init__(self, length=1) :
		self.Interface = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.Interface = [Interface() for _ in range(length)]

