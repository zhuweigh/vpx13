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

class protocolip_stats(base_resource) :
	r""" Statistics for protocolip resource.
	"""
	def __init__(self) :
		self._clearstats = None
		self._iptotrxpkts = 0
		self._iprxpktsrate = 0
		self._iptotrxbytes = 0
		self._iprxbytesrate = 0
		self._iptottxpkts = 0
		self._iptxpktsrate = 0
		self._iptottxbytes = 0
		self._iptxbytesrate = 0
		self._iptotrxmbits = 0
		self._iprxmbitsrate = 0
		self._iptottxmbits = 0
		self._iptxmbitsrate = 0
		self._iptotroutedpkts = 0
		self._iproutedpktsrate = 0
		self._iptotroutedmbits = 0
		self._iproutedmbitsrate = 0
		self._iptotfragments = 0
		self._iptotsuccreassembly = 0
		self._iptotreassemblyattempt = 0
		self._iptotaddrlookup = 0
		self._iptotaddrlookupfail = 0
		self._iptotudpfragmentsfwd = 0
		self._iptottcpfragmentsfwd = 0
		self._iptotfragpktsgen = 0
		self._iptotbadchecksums = 0
		self._iptotunsuccreassembly = 0
		self._iptottoobig = 0
		self._iptotzerofragmentlen = 0
		self._iptotdupfragments = 0
		self._iptotoutoforderfrag = 0
		self._iptotunknowndstrcvd = 0
		self._iptotbadtransport = 0
		self._iptotvipdown = 0
		self._iptotfixheaderfail = 0
		self._iptotttlexpired = 0
		self._iptotmaxclients = 0
		self._iptotunknownsvcs = 0
		self._iptotlandattacks = 0
		self._iptotinvalidheadersz = 0
		self._iptotinvalidpacketsize = 0
		self._iptottruncatedpackets = 0
		self._noniptottruncatedpackets = 0
		self._iptotzeronexthop = 0
		self._iptotbadlens = 0
		self._iptotbadmacaddrs = 0

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def iproutedpktsrate(self) :
		r"""Rate (/s) counter for iptotroutedpkts.
		"""
		try :
			return self._iproutedpktsrate
		except Exception as e:
			raise e

	@property
	def iptotoutoforderfrag(self) :
		r"""Fragments received that are out of order.
		"""
		try :
			return self._iptotoutoforderfrag
		except Exception as e:
			raise e

	@property
	def noniptottruncatedpackets(self) :
		r"""Truncated non-IP packets received.
		"""
		try :
			return self._noniptottruncatedpackets
		except Exception as e:
			raise e

	@property
	def iptotmaxclients(self) :
		r"""Attempts to open a new connection to a service for which the maximum limit has been exceeded. Default value, 0, applies no limit.
		"""
		try :
			return self._iptotmaxclients
		except Exception as e:
			raise e

	@property
	def iptotzerofragmentlen(self) :
		r"""Packets received with a fragment length of 0 bytes.
		"""
		try :
			return self._iptotzerofragmentlen
		except Exception as e:
			raise e

	@property
	def iptxbytesrate(self) :
		r"""Rate (/s) counter for iptottxbytes.
		"""
		try :
			return self._iptxbytesrate
		except Exception as e:
			raise e

	@property
	def iptotvipdown(self) :
		r"""Packets received for which the VIP is down. This can occur when all the services bound to the VIP are down or the VIP is manually disabled.
		"""
		try :
			return self._iptotvipdown
		except Exception as e:
			raise e

	@property
	def iptotroutedpkts(self) :
		r"""Total routed packets.
		"""
		try :
			return self._iptotroutedpkts
		except Exception as e:
			raise e

	@property
	def iprxmbitsrate(self) :
		r"""Rate (/s) counter for iptotrxmbits.
		"""
		try :
			return self._iprxmbitsrate
		except Exception as e:
			raise e

	@property
	def iprxpktsrate(self) :
		r"""Rate (/s) counter for iptotrxpkts.
		"""
		try :
			return self._iprxpktsrate
		except Exception as e:
			raise e

	@property
	def iptxmbitsrate(self) :
		r"""Rate (/s) counter for iptottxmbits.
		"""
		try :
			return self._iptxmbitsrate
		except Exception as e:
			raise e

	@property
	def iptotroutedmbits(self) :
		r"""Total routed Mbits.
		"""
		try :
			return self._iptotroutedmbits
		except Exception as e:
			raise e

	@property
	def iptotinvalidheadersz(self) :
		r"""Packets received in which an invalid data length is specified, or the value in the length field and the actual data length do not match. The range for the Ethernet packet data length is 0-1500 bytes.
		"""
		try :
			return self._iptotinvalidheadersz
		except Exception as e:
			raise e

	@property
	def iptotaddrlookupfail(self) :
		r"""IP address lookups performed by the Citrix ADC that have failed because the destination IP address of the packet does not match any of the Citrix ADC owned IP addresses.
		"""
		try :
			return self._iptotaddrlookupfail
		except Exception as e:
			raise e

	@property
	def iptotbadtransport(self) :
		r"""Packets received in which the protocol specified in the IP header is unknown to the Citrix ADC.
		"""
		try :
			return self._iptotbadtransport
		except Exception as e:
			raise e

	@property
	def iptotfragpktsgen(self) :
		r"""Fragmented packets created by the Citrix ADC.
		"""
		try :
			return self._iptotfragpktsgen
		except Exception as e:
			raise e

	@property
	def iptotsuccreassembly(self) :
		r"""Fragmented IP packets successfully reassembled on the Citrix ADC.
		"""
		try :
			return self._iptotsuccreassembly
		except Exception as e:
			raise e

	@property
	def iptotrxmbits(self) :
		r"""Megabits of IP data received.
		"""
		try :
			return self._iptotrxmbits
		except Exception as e:
			raise e

	@property
	def iptottxbytes(self) :
		r"""Bytes of IP data transmitted.
		"""
		try :
			return self._iptottxbytes
		except Exception as e:
			raise e

	@property
	def iptotbadmacaddrs(self) :
		r"""IP packets transmitted with a bad MAC address.
		"""
		try :
			return self._iptotbadmacaddrs
		except Exception as e:
			raise e

	@property
	def iptottcpfragmentsfwd(self) :
		r"""TCP fragments forwarded to the client or the server.
		"""
		try :
			return self._iptottcpfragmentsfwd
		except Exception as e:
			raise e

	@property
	def iptotrxpkts(self) :
		r"""IP packets received.
		"""
		try :
			return self._iptotrxpkts
		except Exception as e:
			raise e

	@property
	def iptotrxbytes(self) :
		r"""Bytes of IP data received.
		"""
		try :
			return self._iptotrxbytes
		except Exception as e:
			raise e

	@property
	def iptotlandattacks(self) :
		r"""Land-attack packets received. The source and destination addresses are the same.
		"""
		try :
			return self._iptotlandattacks
		except Exception as e:
			raise e

	@property
	def iptotunknowndstrcvd(self) :
		r"""Packets received in which the destination IP address was not reachable or not owned by the Citrix ADC.
		"""
		try :
			return self._iptotunknowndstrcvd
		except Exception as e:
			raise e

	@property
	def iptottruncatedpackets(self) :
		r"""Truncated IP packets received. An overflow in the routers along the path can truncate IP packets.
		"""
		try :
			return self._iptottruncatedpackets
		except Exception as e:
			raise e

	@property
	def iptotttlexpired(self) :
		r"""Packets for which the time-to-live (TTL) expired during transit. These packets are dropped.
		"""
		try :
			return self._iptotttlexpired
		except Exception as e:
			raise e

	@property
	def iprxbytesrate(self) :
		r"""Rate (/s) counter for iptotrxbytes.
		"""
		try :
			return self._iprxbytesrate
		except Exception as e:
			raise e

	@property
	def iptottxmbits(self) :
		r"""Megabits of IP data transmitted.
		"""
		try :
			return self._iptottxmbits
		except Exception as e:
			raise e

	@property
	def iptotbadlens(self) :
		r"""Packets received with a length greater than the normal maximum transmission unit of 1514 bytes.
		"""
		try :
			return self._iptotbadlens
		except Exception as e:
			raise e

	@property
	def iptotunknownsvcs(self) :
		r"""Packets received on a port or service that is not configured.
		"""
		try :
			return self._iptotunknownsvcs
		except Exception as e:
			raise e

	@property
	def iptotdupfragments(self) :
		r"""Duplicate IP fragments received. This can occur when the acknowledgement was not received within the expected time.
		"""
		try :
			return self._iptotdupfragments
		except Exception as e:
			raise e

	@property
	def iptottoobig(self) :
		r"""Packets received for which the reassembled data exceeds the Ethernet packet data length of 1500 bytes.
		"""
		try :
			return self._iptottoobig
		except Exception as e:
			raise e

	@property
	def iptotzeronexthop(self) :
		r"""Packets received that contain a 0 value in the next hop field. These packets are dropped.
		"""
		try :
			return self._iptotzeronexthop
		except Exception as e:
			raise e

	@property
	def iptotaddrlookup(self) :
		r"""IP address lookups performed by the Citrix ADC. When a packet is received on a non-established session, the Citrix ADC checks if the destination IP address is one of the Citrix ADC owned IP addresses.
		"""
		try :
			return self._iptotaddrlookup
		except Exception as e:
			raise e

	@property
	def iptotfragments(self) :
		r"""IP fragments received.
		"""
		try :
			return self._iptotfragments
		except Exception as e:
			raise e

	@property
	def iptotinvalidpacketsize(self) :
		r"""Total number of packets received by Citrix ADC with invalid IP packet size.
		"""
		try :
			return self._iptotinvalidpacketsize
		except Exception as e:
			raise e

	@property
	def iptotunsuccreassembly(self) :
		r"""Packets received that could not be reassembled. This can occur when there is a checksum failure, an identification field mismatch, or when one of the fragments is missing.
		"""
		try :
			return self._iptotunsuccreassembly
		except Exception as e:
			raise e

	@property
	def iptotreassemblyattempt(self) :
		r"""IP packets that the Citrix ADC attempts to reassemble. If one of the fragments is missing, the whole packet is dropped.
		"""
		try :
			return self._iptotreassemblyattempt
		except Exception as e:
			raise e

	@property
	def iptottxpkts(self) :
		r"""IP packets transmitted.
		"""
		try :
			return self._iptottxpkts
		except Exception as e:
			raise e

	@property
	def iptxpktsrate(self) :
		r"""Rate (/s) counter for iptottxpkts.
		"""
		try :
			return self._iptxpktsrate
		except Exception as e:
			raise e

	@property
	def iptotbadchecksums(self) :
		r"""Packets received with an IP checksum error.
		"""
		try :
			return self._iptotbadchecksums
		except Exception as e:
			raise e

	@property
	def iptotfixheaderfail(self) :
		r"""Packets received that contain an error in one or more components of the IP header.
		"""
		try :
			return self._iptotfixheaderfail
		except Exception as e:
			raise e

	@property
	def iproutedmbitsrate(self) :
		r"""Rate (/s) counter for iptotroutedmbits.
		"""
		try :
			return self._iproutedmbitsrate
		except Exception as e:
			raise e

	@property
	def iptotudpfragmentsfwd(self) :
		r"""UDP fragments forwarded to the client or the server.
		"""
		try :
			return self._iptotudpfragmentsfwd
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolip_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolip
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all protocolip_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = protocolip_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocolip_response(base_response) :
	def __init__(self, length=1) :
		self.protocolip = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolip = [protocolip_stats() for _ in range(length)]

