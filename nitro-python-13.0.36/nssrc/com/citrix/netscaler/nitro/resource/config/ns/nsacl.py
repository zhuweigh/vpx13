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

class nsacl(base_resource) :
	""" Configuration for ACL entry resource. """
	def __init__(self) :
		self._aclname = None
		self._aclaction = None
		self._td = None
		self._srcip = None
		self._srcipop = None
		self._srcipval = None
		self._srcport = None
		self._srcportop = None
		self._srcportval = None
		self._destip = None
		self._destipop = None
		self._destipval = None
		self._destport = None
		self._destportop = None
		self._destportval = None
		self._ttl = None
		self._srcmac = None
		self._srcmacmask = None
		self._protocol = None
		self._protocolnumber = None
		self._vlan = None
		self._vxlan = None
		self._Interface = None
		self._established = None
		self._icmptype = None
		self._icmpcode = None
		self._priority = None
		self._state = None
		self._logstate = None
		self._ratelimit = None
		self._type = None
		self._dfdhash = None
		self._stateful = None
		self._newname = None
		self._hits = None
		self._kernelstate = None
		self._aclassociate = None
		self.___count = None

	@property
	def aclname(self) :
		r"""Name for the extended ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._aclname
		except Exception as e:
			raise e

	@aclname.setter
	def aclname(self, aclname) :
		r"""Name for the extended ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1
		"""
		try :
			self._aclname = aclname
		except Exception as e:
			raise e

	@property
	def aclaction(self) :
		r"""Action to perform on incoming IPv4 packets that match the extended ACL rule.
		Available settings function as follows:
		* ALLOW - The Citrix ADC processes the packet.
		* BRIDGE - The Citrix ADC bridges the packet to the destination without processing it.
		* DENY - The Citrix ADC drops the packet.<br/>Possible values = BRIDGE, DENY, ALLOW.
		"""
		try :
			return self._aclaction
		except Exception as e:
			raise e

	@aclaction.setter
	def aclaction(self, aclaction) :
		r"""Action to perform on incoming IPv4 packets that match the extended ACL rule.
		Available settings function as follows:
		* ALLOW - The Citrix ADC processes the packet.
		* BRIDGE - The Citrix ADC bridges the packet to the destination without processing it.
		* DENY - The Citrix ADC drops the packet.<br/>Possible values = BRIDGE, DENY, ALLOW
		"""
		try :
			self._aclaction = aclaction
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
	def srcip(self) :
		r"""IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@srcip.setter
	def srcip(self, srcip) :
		r"""IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			self._srcip = srcip
		except Exception as e:
			raise e

	@property
	def srcipop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._srcipop
		except Exception as e:
			raise e

	@srcipop.setter
	def srcipop(self, srcipop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._srcipop = srcipop
		except Exception as e:
			raise e

	@property
	def srcipval(self) :
		r"""IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example:10.102.29.30-10.102.29.189.
		"""
		try :
			return self._srcipval
		except Exception as e:
			raise e

	@srcipval.setter
	def srcipval(self, srcipval) :
		r"""IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example:10.102.29.30-10.102.29.189.
		"""
		try :
			self._srcipval = srcipval
		except Exception as e:
			raise e

	@property
	def srcport(self) :
		r"""Port number or range of port numbers to match against the source port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		"""
		try :
			return self._srcport
		except Exception as e:
			raise e

	@srcport.setter
	def srcport(self, srcport) :
		r"""Port number or range of port numbers to match against the source port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		"""
		try :
			self._srcport = srcport
		except Exception as e:
			raise e

	@property
	def srcportop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._srcportop
		except Exception as e:
			raise e

	@srcportop.setter
	def srcportop(self, srcportop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._srcportop = srcportop
		except Exception as e:
			raise e

	@property
	def srcportval(self) :
		r"""Port number or range of port numbers to match against the source port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.<br/>Maximum length =  65535.
		"""
		try :
			return self._srcportval
		except Exception as e:
			raise e

	@srcportval.setter
	def srcportval(self, srcportval) :
		r"""Port number or range of port numbers to match against the source port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.<br/>Maximum length =  65535
		"""
		try :
			self._srcportval = srcportval
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet.  In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		r"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet.  In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def destipop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destipop
		except Exception as e:
			raise e

	@destipop.setter
	def destipop(self, destipop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destipop = destipop
		except Exception as e:
			raise e

	@property
	def destipval(self) :
		r"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet.  In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			return self._destipval
		except Exception as e:
			raise e

	@destipval.setter
	def destipval(self, destipval) :
		r"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet.  In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			self._destipval = destipval
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""Port number or range of port numbers to match against the destination port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		r"""Port number or range of port numbers to match against the destination port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def destportop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destportop
		except Exception as e:
			raise e

	@destportop.setter
	def destportop(self, destportop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destportop = destportop
		except Exception as e:
			raise e

	@property
	def destportval(self) :
		r"""Port number or range of port numbers to match against the destination port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535.
		"""
		try :
			return self._destportval
		except Exception as e:
			raise e

	@destportval.setter
	def destportval(self, destportval) :
		r"""Port number or range of port numbers to match against the destination port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535
		"""
		try :
			self._destportval = destportval
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r"""Number of seconds, in multiples of four, after which the extended ACL rule expires. If you do not want the extended ACL rule to expire, do not specify a TTL value.<br/>Minimum length =  1<br/>Maximum length =  0x7FFFFFFF.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		r"""Number of seconds, in multiples of four, after which the extended ACL rule expires. If you do not want the extended ACL rule to expire, do not specify a TTL value.<br/>Minimum length =  1<br/>Maximum length =  0x7FFFFFFF
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def srcmac(self) :
		r"""MAC address to match against the source MAC address of an incoming IPv4 packet.
		"""
		try :
			return self._srcmac
		except Exception as e:
			raise e

	@srcmac.setter
	def srcmac(self, srcmac) :
		r"""MAC address to match against the source MAC address of an incoming IPv4 packet.
		"""
		try :
			self._srcmac = srcmac
		except Exception as e:
			raise e

	@property
	def srcmacmask(self) :
		r""" Used to define range of Source MAC address. It takes string of 0 and 1, 0s are for exact match and 1s for wildcard. For matching first 3 bytes of MAC address, srcMacMask value "000000111111". .<br/>Default value: "000000000000".
		"""
		try :
			return self._srcmacmask
		except Exception as e:
			raise e

	@srcmacmask.setter
	def srcmacmask(self, srcmacmask) :
		r""" Used to define range of Source MAC address. It takes string of 0 and 1, 0s are for exact match and 1s for wildcard. For matching first 3 bytes of MAC address, srcMacMask value "000000111111". .<br/>Default value: "000000000000"
		"""
		try :
			self._srcmacmask = srcmacmask
		except Exception as e:
			raise e

	@property
	def protocol(self) :
		r"""Protocol to match against the protocol of an incoming IPv4 packet.<br/>Possible values = ICMP, IGMP, TCP, EGP, IGP, ARGUS, UDP, RDP, RSVP, EIGRP, L2TP, ISIS, GGP, IPoverIP, ST, CBT, BBN-RCC-M, NVP-II, PUP, EMCON, XNET, CHAOS, MUX, DCN-MEAS, HMP, PRM, XNS-IDP, TRUNK-1, TRUNK-2, LEAF-1, LEAF-2, IRTP, ISO-TP4, NETBLT, MFE-NSP, MERIT-INP, SEP, 3PC, IDPR, XTP, DDP, IDPR-CMTP, TP++, IL, IPv6, SDRP, IPv6-Route, IPv6-Frag, IDRP, GRE, MHRP, BNA, ESP, AH, I-NLSP, SWIPE, NARP, MOBILE, TLSP, SKIP, ICMPV6, IPv6-NoNx, IPv6-Opts, Any-Host-Internal-Protocol, CFTP, Any-Local-Network, SAT-EXPAK, KRYPTOLAN, RVD, IPPC, Any-Distributed-File-System, TFTP, VISA, IPCV, CPNX, CPHB, WSN, PVP, BR-SAT-MO, SUN-ND, WB-MON, WB-EXPAK, ISO-IP, VMTP, SECURE-VM, VINES, TTP, NSFNET-IG, DGP, TCF, OSPFIGP, Sprite-RP, LARP, MTP, AX.25, IPIP, MICP, SCC-SP, ETHERIP, Any-Private-Encryption-Scheme, GMTP, IFMP, PNNI, PIM, ARIS, SCPS, QNX, A/N, IPComp, SNP, Compaq-Pe, IPX-in-IP, VRRP, PGM, Any-0-Hop-Protocol, ENCAP, DDX, IATP, STP, SRP, UTI, SMP, SM, PTP, FIRE, CRTP, CRUDP, SSCOPMCE, IPLT, SPS, PIPE, SCTP, FC, RSVP-E2E-IGNORE, Mobility-Header, UDPLite.
		"""
		try :
			return self._protocol
		except Exception as e:
			raise e

	@protocol.setter
	def protocol(self, protocol) :
		r"""Protocol to match against the protocol of an incoming IPv4 packet.<br/>Possible values = ICMP, IGMP, TCP, EGP, IGP, ARGUS, UDP, RDP, RSVP, EIGRP, L2TP, ISIS, GGP, IPoverIP, ST, CBT, BBN-RCC-M, NVP-II, PUP, EMCON, XNET, CHAOS, MUX, DCN-MEAS, HMP, PRM, XNS-IDP, TRUNK-1, TRUNK-2, LEAF-1, LEAF-2, IRTP, ISO-TP4, NETBLT, MFE-NSP, MERIT-INP, SEP, 3PC, IDPR, XTP, DDP, IDPR-CMTP, TP++, IL, IPv6, SDRP, IPv6-Route, IPv6-Frag, IDRP, GRE, MHRP, BNA, ESP, AH, I-NLSP, SWIPE, NARP, MOBILE, TLSP, SKIP, ICMPV6, IPv6-NoNx, IPv6-Opts, Any-Host-Internal-Protocol, CFTP, Any-Local-Network, SAT-EXPAK, KRYPTOLAN, RVD, IPPC, Any-Distributed-File-System, TFTP, VISA, IPCV, CPNX, CPHB, WSN, PVP, BR-SAT-MO, SUN-ND, WB-MON, WB-EXPAK, ISO-IP, VMTP, SECURE-VM, VINES, TTP, NSFNET-IG, DGP, TCF, OSPFIGP, Sprite-RP, LARP, MTP, AX.25, IPIP, MICP, SCC-SP, ETHERIP, Any-Private-Encryption-Scheme, GMTP, IFMP, PNNI, PIM, ARIS, SCPS, QNX, A/N, IPComp, SNP, Compaq-Pe, IPX-in-IP, VRRP, PGM, Any-0-Hop-Protocol, ENCAP, DDX, IATP, STP, SRP, UTI, SMP, SM, PTP, FIRE, CRTP, CRUDP, SSCOPMCE, IPLT, SPS, PIPE, SCTP, FC, RSVP-E2E-IGNORE, Mobility-Header, UDPLite
		"""
		try :
			self._protocol = protocol
		except Exception as e:
			raise e

	@property
	def protocolnumber(self) :
		r"""Protocol to match against the protocol of an incoming IPv4 packet.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._protocolnumber
		except Exception as e:
			raise e

	@protocolnumber.setter
	def protocolnumber(self, protocolnumber) :
		r"""Protocol to match against the protocol of an incoming IPv4 packet.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._protocolnumber = protocolnumber
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""ID of the VLAN. The Citrix ADC applies the ACL rule only to the incoming packets of the specified VLAN. If you do not specify a VLAN ID, the appliance applies the ACL rule to the incoming packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""ID of the VLAN. The Citrix ADC applies the ACL rule only to the incoming packets of the specified VLAN. If you do not specify a VLAN ID, the appliance applies the ACL rule to the incoming packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		r"""ID of the VXLAN. The Citrix ADC applies the ACL rule only to the incoming packets of the specified VXLAN. If you do not specify a VXLAN ID, the appliance applies the ACL rule to the incoming packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		r"""ID of the VXLAN. The Citrix ADC applies the ACL rule only to the incoming packets of the specified VXLAN. If you do not specify a VXLAN ID, the appliance applies the ACL rule to the incoming packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def Interface(self) :
		r"""ID of an interface. The Citrix ADC applies the ACL rule only to the incoming packets from the specified interface. If you do not specify any value, the appliance applies the ACL rule to the incoming packets of all interfaces.
		"""
		try :
			return self._Interface
		except Exception as e:
			raise e

	@Interface.setter
	def Interface(self, Interface) :
		r"""ID of an interface. The Citrix ADC applies the ACL rule only to the incoming packets from the specified interface. If you do not specify any value, the appliance applies the ACL rule to the incoming packets of all interfaces.
		"""
		try :
			self._Interface = Interface
		except Exception as e:
			raise e

	@property
	def established(self) :
		r"""Allow only incoming TCP packets that have the ACK or RST bit set, if the action set for the ACL rule is ALLOW and these packets match the other conditions in the ACL rule.
		"""
		try :
			return self._established
		except Exception as e:
			raise e

	@established.setter
	def established(self, established) :
		r"""Allow only incoming TCP packets that have the ACK or RST bit set, if the action set for the ACL rule is ALLOW and these packets match the other conditions in the ACL rule.
		"""
		try :
			self._established = established
		except Exception as e:
			raise e

	@property
	def icmptype(self) :
		r"""ICMP Message type to match against the message type of an incoming ICMP packet. For example, to block DESTINATION UNREACHABLE messages, you must specify 3 as the ICMP type.
		Note: This parameter can be specified only for the ICMP protocol.<br/>Maximum length =  65536.
		"""
		try :
			return self._icmptype
		except Exception as e:
			raise e

	@icmptype.setter
	def icmptype(self, icmptype) :
		r"""ICMP Message type to match against the message type of an incoming ICMP packet. For example, to block DESTINATION UNREACHABLE messages, you must specify 3 as the ICMP type.
		Note: This parameter can be specified only for the ICMP protocol.<br/>Maximum length =  65536
		"""
		try :
			self._icmptype = icmptype
		except Exception as e:
			raise e

	@property
	def icmpcode(self) :
		r"""Code of a particular ICMP message type to match against the ICMP code of an incoming ICMP packet.  For example, to block DESTINATION HOST UNREACHABLE messages, specify 3 as the ICMP type and 1 as the ICMP code.
		If you set this parameter, you must set the ICMP Type parameter.<br/>Maximum length =  65536.
		"""
		try :
			return self._icmpcode
		except Exception as e:
			raise e

	@icmpcode.setter
	def icmpcode(self, icmpcode) :
		r"""Code of a particular ICMP message type to match against the ICMP code of an incoming ICMP packet.  For example, to block DESTINATION HOST UNREACHABLE messages, specify 3 as the ICMP type and 1 as the ICMP code.
		If you set this parameter, you must set the ICMP Type parameter.<br/>Maximum length =  65536
		"""
		try :
			self._icmpcode = icmpcode
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""Priority for the extended ACL rule that determines the order in which it is evaluated relative to the other extended ACL rules. If you do not specify priorities while creating extended ACL rules, the ACL rules are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  100000.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""Priority for the extended ACL rule that determines the order in which it is evaluated relative to the other extended ACL rules. If you do not specify priorities while creating extended ACL rules, the ACL rules are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  100000
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Enable or disable the extended ACL rule. After you apply the extended ACL rules, the Citrix ADC compares incoming packets against the enabled extended ACL rules.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Enable or disable the extended ACL rule. After you apply the extended ACL rules, the Citrix ADC compares incoming packets against the enabled extended ACL rules.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def logstate(self) :
		r"""Enable or disable logging of events related to the extended ACL rule. The log messages are stored in the configured syslog or auditlog server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logstate
		except Exception as e:
			raise e

	@logstate.setter
	def logstate(self, logstate) :
		r"""Enable or disable logging of events related to the extended ACL rule. The log messages are stored in the configured syslog or auditlog server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logstate = logstate
		except Exception as e:
			raise e

	@property
	def ratelimit(self) :
		r"""Maximum number of log messages to be generated per second. If you set this parameter, you must enable the Log State parameter.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  10000.
		"""
		try :
			return self._ratelimit
		except Exception as e:
			raise e

	@ratelimit.setter
	def ratelimit(self, ratelimit) :
		r"""Maximum number of log messages to be generated per second. If you set this parameter, you must enable the Log State parameter.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  10000
		"""
		try :
			self._ratelimit = ratelimit
		except Exception as e:
			raise e

	@property
	def type(self) :
		r""" Type of the acl ,default will be CLASSIC.
		Available options as follows:
		* CLASSIC - specifies the regular extended acls.
		* DFD - cluster specific acls,specifies hashmethod for steering of the packet in cluster .<br/>Default value: CLASSIC<br/>Possible values = CLASSIC, DFD.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r""" Type of the acl ,default will be CLASSIC.
		Available options as follows:
		* CLASSIC - specifies the regular extended acls.
		* DFD - cluster specific acls,specifies hashmethod for steering of the packet in cluster .<br/>Default value: CLASSIC<br/>Possible values = CLASSIC, DFD
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def dfdhash(self) :
		r"""Specifies the type hashmethod to be applied, to steer the packet to the FP of the packet.<br/>Possible values = SIP-SPORT-DIP-DPORT, SIP, DIP, SIP-DIP, SIP-SPORT, DIP-DPORT.
		"""
		try :
			return self._dfdhash
		except Exception as e:
			raise e

	@dfdhash.setter
	def dfdhash(self, dfdhash) :
		r"""Specifies the type hashmethod to be applied, to steer the packet to the FP of the packet.<br/>Possible values = SIP-SPORT-DIP-DPORT, SIP, DIP, SIP-DIP, SIP-SPORT, DIP-DPORT
		"""
		try :
			self._dfdhash = dfdhash
		except Exception as e:
			raise e

	@property
	def stateful(self) :
		r"""If stateful option is enabled, transparent sessions are created for the traffic hitting this ACL and not hitting any other features like LB, INAT etc. .<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._stateful
		except Exception as e:
			raise e

	@stateful.setter
	def stateful(self, stateful) :
		r"""If stateful option is enabled, transparent sessions are created for the traffic hitting this ACL and not hitting any other features like LB, INAT etc. .<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._stateful = stateful
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the extended ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the extended ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""The hits of this ACL.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def kernelstate(self) :
		r"""The commit status of the ACL.<br/>Default value: NOTAPPLIED<br/>Possible values = APPLIED, NOTAPPLIED, RE-APPLY, SFAPPLIED, SFNOTAPPLIED, SFAPPLIED61, SFNOTAPPLIED61.
		"""
		try :
			return self._kernelstate
		except Exception as e:
			raise e

	@property
	def aclassociate(self) :
		r"""ACL linked.<br/>Possible values = NAT, FORWARDINGSESSION, NAT64, LSN.
		"""
		try :
			return self._aclassociate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsacl_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsacl
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.aclname is not None :
				return str(self.aclname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nsacl.
		"""
		try :
			if type(resource) is not list :
				addresource = nsacl()
				addresource.aclname = resource.aclname
				addresource.aclaction = resource.aclaction
				addresource.td = resource.td
				addresource.srcip = resource.srcip
				addresource.srcipop = resource.srcipop
				addresource.srcipval = resource.srcipval
				addresource.srcport = resource.srcport
				addresource.srcportop = resource.srcportop
				addresource.srcportval = resource.srcportval
				addresource.destip = resource.destip
				addresource.destipop = resource.destipop
				addresource.destipval = resource.destipval
				addresource.destport = resource.destport
				addresource.destportop = resource.destportop
				addresource.destportval = resource.destportval
				addresource.ttl = resource.ttl
				addresource.srcmac = resource.srcmac
				addresource.srcmacmask = resource.srcmacmask
				addresource.protocol = resource.protocol
				addresource.protocolnumber = resource.protocolnumber
				addresource.vlan = resource.vlan
				addresource.vxlan = resource.vxlan
				addresource.Interface = resource.Interface
				addresource.established = resource.established
				addresource.icmptype = resource.icmptype
				addresource.icmpcode = resource.icmpcode
				addresource.priority = resource.priority
				addresource.state = resource.state
				addresource.logstate = resource.logstate
				addresource.ratelimit = resource.ratelimit
				addresource.type = resource.type
				addresource.dfdhash = resource.dfdhash
				addresource.stateful = resource.stateful
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsacl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].aclname = resource[i].aclname
						addresources[i].aclaction = resource[i].aclaction
						addresources[i].td = resource[i].td
						addresources[i].srcip = resource[i].srcip
						addresources[i].srcipop = resource[i].srcipop
						addresources[i].srcipval = resource[i].srcipval
						addresources[i].srcport = resource[i].srcport
						addresources[i].srcportop = resource[i].srcportop
						addresources[i].srcportval = resource[i].srcportval
						addresources[i].destip = resource[i].destip
						addresources[i].destipop = resource[i].destipop
						addresources[i].destipval = resource[i].destipval
						addresources[i].destport = resource[i].destport
						addresources[i].destportop = resource[i].destportop
						addresources[i].destportval = resource[i].destportval
						addresources[i].ttl = resource[i].ttl
						addresources[i].srcmac = resource[i].srcmac
						addresources[i].srcmacmask = resource[i].srcmacmask
						addresources[i].protocol = resource[i].protocol
						addresources[i].protocolnumber = resource[i].protocolnumber
						addresources[i].vlan = resource[i].vlan
						addresources[i].vxlan = resource[i].vxlan
						addresources[i].Interface = resource[i].Interface
						addresources[i].established = resource[i].established
						addresources[i].icmptype = resource[i].icmptype
						addresources[i].icmpcode = resource[i].icmpcode
						addresources[i].priority = resource[i].priority
						addresources[i].state = resource[i].state
						addresources[i].logstate = resource[i].logstate
						addresources[i].ratelimit = resource[i].ratelimit
						addresources[i].type = resource[i].type
						addresources[i].dfdhash = resource[i].dfdhash
						addresources[i].stateful = resource[i].stateful
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nsacl.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsacl()
				if type(resource) !=  type(deleteresource):
					deleteresource.aclname = resource
				else :
					deleteresource.aclname = resource.aclname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].aclname = resource[i].aclname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsacl.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsacl()
				updateresource.aclname = resource.aclname
				updateresource.aclaction = resource.aclaction
				updateresource.srcip = resource.srcip
				updateresource.srcipop = resource.srcipop
				updateresource.srcipval = resource.srcipval
				updateresource.srcport = resource.srcport
				updateresource.srcportop = resource.srcportop
				updateresource.srcportval = resource.srcportval
				updateresource.destip = resource.destip
				updateresource.destipop = resource.destipop
				updateresource.destipval = resource.destipval
				updateresource.destport = resource.destport
				updateresource.destportop = resource.destportop
				updateresource.destportval = resource.destportval
				updateresource.srcmac = resource.srcmac
				updateresource.srcmacmask = resource.srcmacmask
				updateresource.protocol = resource.protocol
				updateresource.protocolnumber = resource.protocolnumber
				updateresource.icmptype = resource.icmptype
				updateresource.icmpcode = resource.icmpcode
				updateresource.vlan = resource.vlan
				updateresource.vxlan = resource.vxlan
				updateresource.Interface = resource.Interface
				updateresource.priority = resource.priority
				updateresource.logstate = resource.logstate
				updateresource.ratelimit = resource.ratelimit
				updateresource.established = resource.established
				updateresource.dfdhash = resource.dfdhash
				updateresource.stateful = resource.stateful
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsacl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].aclname = resource[i].aclname
						updateresources[i].aclaction = resource[i].aclaction
						updateresources[i].srcip = resource[i].srcip
						updateresources[i].srcipop = resource[i].srcipop
						updateresources[i].srcipval = resource[i].srcipval
						updateresources[i].srcport = resource[i].srcport
						updateresources[i].srcportop = resource[i].srcportop
						updateresources[i].srcportval = resource[i].srcportval
						updateresources[i].destip = resource[i].destip
						updateresources[i].destipop = resource[i].destipop
						updateresources[i].destipval = resource[i].destipval
						updateresources[i].destport = resource[i].destport
						updateresources[i].destportop = resource[i].destportop
						updateresources[i].destportval = resource[i].destportval
						updateresources[i].srcmac = resource[i].srcmac
						updateresources[i].srcmacmask = resource[i].srcmacmask
						updateresources[i].protocol = resource[i].protocol
						updateresources[i].protocolnumber = resource[i].protocolnumber
						updateresources[i].icmptype = resource[i].icmptype
						updateresources[i].icmpcode = resource[i].icmpcode
						updateresources[i].vlan = resource[i].vlan
						updateresources[i].vxlan = resource[i].vxlan
						updateresources[i].Interface = resource[i].Interface
						updateresources[i].priority = resource[i].priority
						updateresources[i].logstate = resource[i].logstate
						updateresources[i].ratelimit = resource[i].ratelimit
						updateresources[i].established = resource[i].established
						updateresources[i].dfdhash = resource[i].dfdhash
						updateresources[i].stateful = resource[i].stateful
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsacl resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsacl()
				if type(resource) !=  type(unsetresource):
					unsetresource.aclname = resource
				else :
					unsetresource.aclname = resource.aclname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].aclname = resource[i].aclname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable nsacl.
		"""
		try :
			if type(resource) is not list :
				enableresource = nsacl()
				if type(resource) !=  type(enableresource):
					enableresource.aclname = resource
				else :
					enableresource.aclname = resource.aclname
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].aclname = resource[i].aclname
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable nsacl.
		"""
		try :
			if type(resource) is not list :
				disableresource = nsacl()
				if type(resource) !=  type(disableresource):
					disableresource.aclname = resource
				else :
					disableresource.aclname = resource.aclname
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].aclname = resource[i].aclname
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_aclname) :
		r""" Use this API to rename a nsacl resource.
		"""
		try :
			renameresource = nsacl()
			if type(resource) == cls :
				renameresource.aclname = resource.aclname
			else :
				renameresource.aclname = resource
			return renameresource.rename_resource(client,new_aclname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsacl resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsacl()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nsacl()
					obj.aclname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nsacl() for _ in range(len(name))]
						obj = [nsacl() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nsacl()
							obj[i].aclname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the nsacl resources that are configured on netscaler.
	# This uses nsacl_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nsacl()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nsacl resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsacl()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nsacl resources configured on NetScaler.
		"""
		try :
			obj = nsacl()
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
		r""" Use this API to count filtered the set of nsacl resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsacl()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Protocol:
		ICMP = "ICMP"
		IGMP = "IGMP"
		TCP = "TCP"
		EGP = "EGP"
		IGP = "IGP"
		ARGUS = "ARGUS"
		UDP = "UDP"
		RDP = "RDP"
		RSVP = "RSVP"
		EIGRP = "EIGRP"
		L2TP = "L2TP"
		ISIS = "ISIS"
		GGP = "GGP"
		IPoverIP = "IPoverIP"
		ST = "ST"
		CBT = "CBT"
		BBN_RCC_M = "BBN-RCC-M"
		NVP_II = "NVP-II"
		PUP = "PUP"
		EMCON = "EMCON"
		XNET = "XNET"
		CHAOS = "CHAOS"
		MUX = "MUX"
		DCN_MEAS = "DCN-MEAS"
		HMP = "HMP"
		PRM = "PRM"
		XNS_IDP = "XNS-IDP"
		TRUNK_1 = "TRUNK-1"
		TRUNK_2 = "TRUNK-2"
		LEAF_1 = "LEAF-1"
		LEAF_2 = "LEAF-2"
		IRTP = "IRTP"
		ISO_TP4 = "ISO-TP4"
		NETBLT = "NETBLT"
		MFE_NSP = "MFE-NSP"
		MERIT_INP = "MERIT-INP"
		SEP = "SEP"
		_3PC = "3PC"
		IDPR = "IDPR"
		XTP = "XTP"
		DDP = "DDP"
		IDPR_CMTP = "IDPR-CMTP"
		TP__ = "TP++"
		IL = "IL"
		IPv6 = "IPv6"
		SDRP = "SDRP"
		IPv6_Route = "IPv6-Route"
		IPv6_Frag = "IPv6-Frag"
		IDRP = "IDRP"
		GRE = "GRE"
		MHRP = "MHRP"
		BNA = "BNA"
		ESP = "ESP"
		AH = "AH"
		I_NLSP = "I-NLSP"
		SWIPE = "SWIPE"
		NARP = "NARP"
		MOBILE = "MOBILE"
		TLSP = "TLSP"
		SKIP = "SKIP"
		ICMPV6 = "ICMPV6"
		IPv6_NoNx = "IPv6-NoNx"
		IPv6_Opts = "IPv6-Opts"
		Any_Host_Internal_Protocol = "Any-Host-Internal-Protocol"
		CFTP = "CFTP"
		Any_Local_Network = "Any-Local-Network"
		SAT_EXPAK = "SAT-EXPAK"
		KRYPTOLAN = "KRYPTOLAN"
		RVD = "RVD"
		IPPC = "IPPC"
		Any_Distributed_File_System = "Any-Distributed-File-System"
		TFTP = "TFTP"
		VISA = "VISA"
		IPCV = "IPCV"
		CPNX = "CPNX"
		CPHB = "CPHB"
		WSN = "WSN"
		PVP = "PVP"
		BR_SAT_MO = "BR-SAT-MO"
		SUN_ND = "SUN-ND"
		WB_MON = "WB-MON"
		WB_EXPAK = "WB-EXPAK"
		ISO_IP = "ISO-IP"
		VMTP = "VMTP"
		SECURE_VM = "SECURE-VM"
		VINES = "VINES"
		TTP = "TTP"
		NSFNET_IG = "NSFNET-IG"
		DGP = "DGP"
		TCF = "TCF"
		OSPFIGP = "OSPFIGP"
		Sprite_RP = "Sprite-RP"
		LARP = "LARP"
		MTP = "MTP"
		AX_25 = "AX.25"
		IPIP = "IPIP"
		MICP = "MICP"
		SCC_SP = "SCC-SP"
		ETHERIP = "ETHERIP"
		Any_Private_Encryption_Scheme = "Any-Private-Encryption-Scheme"
		GMTP = "GMTP"
		IFMP = "IFMP"
		PNNI = "PNNI"
		PIM = "PIM"
		ARIS = "ARIS"
		SCPS = "SCPS"
		QNX = "QNX"
		A_N = "A/N"
		IPComp = "IPComp"
		SNP = "SNP"
		Compaq_Pe = "Compaq-Pe"
		IPX_in_IP = "IPX-in-IP"
		VRRP = "VRRP"
		PGM = "PGM"
		Any_0_Hop_Protocol = "Any-0-Hop-Protocol"
		ENCAP = "ENCAP"
		DDX = "DDX"
		IATP = "IATP"
		STP = "STP"
		SRP = "SRP"
		UTI = "UTI"
		SMP = "SMP"
		SM = "SM"
		PTP = "PTP"
		FIRE = "FIRE"
		CRTP = "CRTP"
		CRUDP = "CRUDP"
		SSCOPMCE = "SSCOPMCE"
		IPLT = "IPLT"
		SPS = "SPS"
		PIPE = "PIPE"
		SCTP = "SCTP"
		FC = "FC"
		RSVP_E2E_IGNORE = "RSVP-E2E-IGNORE"
		Mobility_Header = "Mobility-Header"
		UDPLite = "UDPLite"

	class Aclassociate:
		NAT = "NAT"
		FORWARDINGSESSION = "FORWARDINGSESSION"
		NAT64 = "NAT64"
		LSN = "LSN"

	class Destipop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Kernelstate:
		APPLIED = "APPLIED"
		NOTAPPLIED = "NOTAPPLIED"
		RE_APPLY = "RE-APPLY"
		SFAPPLIED = "SFAPPLIED"
		SFNOTAPPLIED = "SFNOTAPPLIED"
		SFAPPLIED61 = "SFAPPLIED61"
		SFNOTAPPLIED61 = "SFNOTAPPLIED61"

	class Aclaction:
		BRIDGE = "BRIDGE"
		DENY = "DENY"
		ALLOW = "ALLOW"

	class Type:
		CLASSIC = "CLASSIC"
		DFD = "DFD"

	class Srcportop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class Srcipop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class Dfdhash:
		SIP_SPORT_DIP_DPORT = "SIP-SPORT-DIP-DPORT"
		SIP = "SIP"
		DIP = "DIP"
		SIP_DIP = "SIP-DIP"
		SIP_SPORT = "SIP-SPORT"
		DIP_DPORT = "DIP-DPORT"

	class Logstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Stateful:
		YES = "YES"
		NO = "NO"

	class Destportop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

class nsacl_response(base_response) :
	def __init__(self, length=1) :
		self.nsacl = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsacl = [nsacl() for _ in range(length)]

