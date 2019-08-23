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

class nstcpprofile(base_resource) :
	""" Configuration for TCP profile resource. """
	def __init__(self) :
		self._name = None
		self._ws = None
		self._sack = None
		self._wsval = None
		self._nagle = None
		self._ackonpush = None
		self._mss = None
		self._maxburst = None
		self._initialcwnd = None
		self._delayedack = None
		self._oooqsize = None
		self._maxpktpermss = None
		self._pktperretx = None
		self._minrto = None
		self._slowstartincr = None
		self._buffersize = None
		self._syncookie = None
		self._kaprobeupdatelastactivity = None
		self._flavor = None
		self._dynamicreceivebuffering = None
		self._ka = None
		self._kaconnidletime = None
		self._kamaxprobes = None
		self._kaprobeinterval = None
		self._sendbuffsize = None
		self._mptcp = None
		self._establishclientconn = None
		self._tcpsegoffload = None
		self._rstwindowattenuate = None
		self._rstmaxack = None
		self._spoofsyndrop = None
		self._ecn = None
		self._mptcpdropdataonpreestsf = None
		self._mptcpfastopen = None
		self._mptcpsessiontimeout = None
		self._timestamp = None
		self._dsack = None
		self._ackaggregation = None
		self._frto = None
		self._maxcwnd = None
		self._fack = None
		self._tcpmode = None
		self._tcpfastopen = None
		self._hystart = None
		self._dupackthresh = None
		self._burstratecontrol = None
		self._tcprate = None
		self._rateqmax = None
		self._drophalfclosedconnontimeout = None
		self._dropestconnontimeout = None
		self._applyadaptivetcp = None
		self._feature = None
		self._tcpfastopencookiesize = None
		self._taillossprobe = None
		self._refcnt = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for a TCP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a TCP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my tcp profile" or 'my tcp profile'\).<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for a TCP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a TCP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my tcp profile" or 'my tcp profile'\).<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ws(self) :
		r"""Enable or disable window scaling.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ws
		except Exception as e:
			raise e

	@ws.setter
	def ws(self, ws) :
		r"""Enable or disable window scaling.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ws = ws
		except Exception as e:
			raise e

	@property
	def sack(self) :
		r"""Enable or disable Selective ACKnowledgement (SACK).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sack
		except Exception as e:
			raise e

	@sack.setter
	def sack(self, sack) :
		r"""Enable or disable Selective ACKnowledgement (SACK).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sack = sack
		except Exception as e:
			raise e

	@property
	def wsval(self) :
		r"""Factor used to calculate the new window size.
		This argument is needed only when window scaling is enabled.<br/>Default value: 4<br/>Maximum length =  14.
		"""
		try :
			return self._wsval
		except Exception as e:
			raise e

	@wsval.setter
	def wsval(self, wsval) :
		r"""Factor used to calculate the new window size.
		This argument is needed only when window scaling is enabled.<br/>Default value: 4<br/>Maximum length =  14
		"""
		try :
			self._wsval = wsval
		except Exception as e:
			raise e

	@property
	def nagle(self) :
		r"""Enable or disable the Nagle algorithm on TCP connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nagle
		except Exception as e:
			raise e

	@nagle.setter
	def nagle(self, nagle) :
		r"""Enable or disable the Nagle algorithm on TCP connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nagle = nagle
		except Exception as e:
			raise e

	@property
	def ackonpush(self) :
		r"""Send immediate positive acknowledgement (ACK) on receipt of TCP packets with PUSH flag.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ackonpush
		except Exception as e:
			raise e

	@ackonpush.setter
	def ackonpush(self, ackonpush) :
		r"""Send immediate positive acknowledgement (ACK) on receipt of TCP packets with PUSH flag.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ackonpush = ackonpush
		except Exception as e:
			raise e

	@property
	def mss(self) :
		r"""Maximum number of octets to allow in a TCP data segment.<br/>Maximum length =  9176.
		"""
		try :
			return self._mss
		except Exception as e:
			raise e

	@mss.setter
	def mss(self, mss) :
		r"""Maximum number of octets to allow in a TCP data segment.<br/>Maximum length =  9176
		"""
		try :
			self._mss = mss
		except Exception as e:
			raise e

	@property
	def maxburst(self) :
		r"""Maximum number of TCP segments allowed in a burst.<br/>Default value: 6<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._maxburst
		except Exception as e:
			raise e

	@maxburst.setter
	def maxburst(self, maxburst) :
		r"""Maximum number of TCP segments allowed in a burst.<br/>Default value: 6<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._maxburst = maxburst
		except Exception as e:
			raise e

	@property
	def initialcwnd(self) :
		r"""Initial maximum upper limit on the number of TCP packets that can be outstanding on the TCP link to the server.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  44.
		"""
		try :
			return self._initialcwnd
		except Exception as e:
			raise e

	@initialcwnd.setter
	def initialcwnd(self, initialcwnd) :
		r"""Initial maximum upper limit on the number of TCP packets that can be outstanding on the TCP link to the server.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  44
		"""
		try :
			self._initialcwnd = initialcwnd
		except Exception as e:
			raise e

	@property
	def delayedack(self) :
		r"""Timeout for TCP delayed ACK, in milliseconds.<br/>Default value: 100<br/>Minimum length =  10<br/>Maximum length =  300.
		"""
		try :
			return self._delayedack
		except Exception as e:
			raise e

	@delayedack.setter
	def delayedack(self, delayedack) :
		r"""Timeout for TCP delayed ACK, in milliseconds.<br/>Default value: 100<br/>Minimum length =  10<br/>Maximum length =  300
		"""
		try :
			self._delayedack = delayedack
		except Exception as e:
			raise e

	@property
	def oooqsize(self) :
		r"""Maximum size of out-of-order packets queue. A value of 0 means no limit.<br/>Default value: 64<br/>Maximum length =  65535.
		"""
		try :
			return self._oooqsize
		except Exception as e:
			raise e

	@oooqsize.setter
	def oooqsize(self, oooqsize) :
		r"""Maximum size of out-of-order packets queue. A value of 0 means no limit.<br/>Default value: 64<br/>Maximum length =  65535
		"""
		try :
			self._oooqsize = oooqsize
		except Exception as e:
			raise e

	@property
	def maxpktpermss(self) :
		r"""Maximum number of TCP packets allowed per maximum segment size (MSS).<br/>Maximum length =  1460.
		"""
		try :
			return self._maxpktpermss
		except Exception as e:
			raise e

	@maxpktpermss.setter
	def maxpktpermss(self, maxpktpermss) :
		r"""Maximum number of TCP packets allowed per maximum segment size (MSS).<br/>Maximum length =  1460
		"""
		try :
			self._maxpktpermss = maxpktpermss
		except Exception as e:
			raise e

	@property
	def pktperretx(self) :
		r"""Maximum limit on the number of packets that should be retransmitted on receiving a partial ACK.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  512.
		"""
		try :
			return self._pktperretx
		except Exception as e:
			raise e

	@pktperretx.setter
	def pktperretx(self, pktperretx) :
		r"""Maximum limit on the number of packets that should be retransmitted on receiving a partial ACK.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  512
		"""
		try :
			self._pktperretx = pktperretx
		except Exception as e:
			raise e

	@property
	def minrto(self) :
		r"""Minimum retransmission timeout, in milliseconds, specified in 10-millisecond increments (value must yield a whole number if divided by  10).<br/>Default value: 1000<br/>Minimum length =  10<br/>Maximum length =  64000.
		"""
		try :
			return self._minrto
		except Exception as e:
			raise e

	@minrto.setter
	def minrto(self, minrto) :
		r"""Minimum retransmission timeout, in milliseconds, specified in 10-millisecond increments (value must yield a whole number if divided by  10).<br/>Default value: 1000<br/>Minimum length =  10<br/>Maximum length =  64000
		"""
		try :
			self._minrto = minrto
		except Exception as e:
			raise e

	@property
	def slowstartincr(self) :
		r"""Multiplier that determines the rate at which slow start increases the size of the TCP transmission window after each acknowledgement of successful transmission.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._slowstartincr
		except Exception as e:
			raise e

	@slowstartincr.setter
	def slowstartincr(self, slowstartincr) :
		r"""Multiplier that determines the rate at which slow start increases the size of the TCP transmission window after each acknowledgement of successful transmission.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._slowstartincr = slowstartincr
		except Exception as e:
			raise e

	@property
	def buffersize(self) :
		r"""TCP buffering size, in bytes.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  20971520.
		"""
		try :
			return self._buffersize
		except Exception as e:
			raise e

	@buffersize.setter
	def buffersize(self, buffersize) :
		r"""TCP buffering size, in bytes.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  20971520
		"""
		try :
			self._buffersize = buffersize
		except Exception as e:
			raise e

	@property
	def syncookie(self) :
		r"""Enable or disable the SYNCOOKIE mechanism for TCP handshake with clients. Disabling SYNCOOKIE prevents SYN attack protection on the Citrix ADC.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._syncookie
		except Exception as e:
			raise e

	@syncookie.setter
	def syncookie(self, syncookie) :
		r"""Enable or disable the SYNCOOKIE mechanism for TCP handshake with clients. Disabling SYNCOOKIE prevents SYN attack protection on the Citrix ADC.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._syncookie = syncookie
		except Exception as e:
			raise e

	@property
	def kaprobeupdatelastactivity(self) :
		r"""Update last activity for the connection after receiving keep-alive (KA) probes.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._kaprobeupdatelastactivity
		except Exception as e:
			raise e

	@kaprobeupdatelastactivity.setter
	def kaprobeupdatelastactivity(self, kaprobeupdatelastactivity) :
		r"""Update last activity for the connection after receiving keep-alive (KA) probes.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._kaprobeupdatelastactivity = kaprobeupdatelastactivity
		except Exception as e:
			raise e

	@property
	def flavor(self) :
		r"""Set TCP congestion control algorithm.<br/>Default value: Default<br/>Possible values = Default, Westwood, BIC, CUBIC, Nile.
		"""
		try :
			return self._flavor
		except Exception as e:
			raise e

	@flavor.setter
	def flavor(self, flavor) :
		r"""Set TCP congestion control algorithm.<br/>Default value: Default<br/>Possible values = Default, Westwood, BIC, CUBIC, Nile
		"""
		try :
			self._flavor = flavor
		except Exception as e:
			raise e

	@property
	def dynamicreceivebuffering(self) :
		r"""Enable or disable dynamic receive buffering. When enabled, allows the receive buffer to be adjusted dynamically based on memory and network conditions.
		Note: The buffer size argument must be set for dynamic adjustments to take place.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dynamicreceivebuffering
		except Exception as e:
			raise e

	@dynamicreceivebuffering.setter
	def dynamicreceivebuffering(self, dynamicreceivebuffering) :
		r"""Enable or disable dynamic receive buffering. When enabled, allows the receive buffer to be adjusted dynamically based on memory and network conditions.
		Note: The buffer size argument must be set for dynamic adjustments to take place.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dynamicreceivebuffering = dynamicreceivebuffering
		except Exception as e:
			raise e

	@property
	def ka(self) :
		r"""Send periodic TCP keep-alive (KA) probes to check if peer is still up.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ka
		except Exception as e:
			raise e

	@ka.setter
	def ka(self, ka) :
		r"""Send periodic TCP keep-alive (KA) probes to check if peer is still up.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ka = ka
		except Exception as e:
			raise e

	@property
	def kaconnidletime(self) :
		r"""Duration, in seconds, for the connection to be idle, before sending a keep-alive (KA) probe.<br/>Minimum length =  1<br/>Maximum length =  4095.
		"""
		try :
			return self._kaconnidletime
		except Exception as e:
			raise e

	@kaconnidletime.setter
	def kaconnidletime(self, kaconnidletime) :
		r"""Duration, in seconds, for the connection to be idle, before sending a keep-alive (KA) probe.<br/>Minimum length =  1<br/>Maximum length =  4095
		"""
		try :
			self._kaconnidletime = kaconnidletime
		except Exception as e:
			raise e

	@property
	def kamaxprobes(self) :
		r"""Number of keep-alive (KA) probes to be sent when not acknowledged, before assuming the peer to be down.<br/>Minimum length =  1<br/>Maximum length =  254.
		"""
		try :
			return self._kamaxprobes
		except Exception as e:
			raise e

	@kamaxprobes.setter
	def kamaxprobes(self, kamaxprobes) :
		r"""Number of keep-alive (KA) probes to be sent when not acknowledged, before assuming the peer to be down.<br/>Minimum length =  1<br/>Maximum length =  254
		"""
		try :
			self._kamaxprobes = kamaxprobes
		except Exception as e:
			raise e

	@property
	def kaprobeinterval(self) :
		r"""Time interval, in seconds, before the next keep-alive (KA) probe, if the peer does not respond.<br/>Minimum length =  1<br/>Maximum length =  4095.
		"""
		try :
			return self._kaprobeinterval
		except Exception as e:
			raise e

	@kaprobeinterval.setter
	def kaprobeinterval(self, kaprobeinterval) :
		r"""Time interval, in seconds, before the next keep-alive (KA) probe, if the peer does not respond.<br/>Minimum length =  1<br/>Maximum length =  4095
		"""
		try :
			self._kaprobeinterval = kaprobeinterval
		except Exception as e:
			raise e

	@property
	def sendbuffsize(self) :
		r"""TCP Send Buffer Size.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  20971520.
		"""
		try :
			return self._sendbuffsize
		except Exception as e:
			raise e

	@sendbuffsize.setter
	def sendbuffsize(self, sendbuffsize) :
		r"""TCP Send Buffer Size.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  20971520
		"""
		try :
			self._sendbuffsize = sendbuffsize
		except Exception as e:
			raise e

	@property
	def mptcp(self) :
		r"""Enable or disable Multipath TCP.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mptcp
		except Exception as e:
			raise e

	@mptcp.setter
	def mptcp(self, mptcp) :
		r"""Enable or disable Multipath TCP.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mptcp = mptcp
		except Exception as e:
			raise e

	@property
	def establishclientconn(self) :
		r"""Establishing Client Client connection on First data/ Final-ACK / Automatic.<br/>Default value: AUTOMATIC<br/>Possible values = AUTOMATIC, CONN_ESTABLISHED, ON_FIRST_DATA.
		"""
		try :
			return self._establishclientconn
		except Exception as e:
			raise e

	@establishclientconn.setter
	def establishclientconn(self, establishclientconn) :
		r"""Establishing Client Client connection on First data/ Final-ACK / Automatic.<br/>Default value: AUTOMATIC<br/>Possible values = AUTOMATIC, CONN_ESTABLISHED, ON_FIRST_DATA
		"""
		try :
			self._establishclientconn = establishclientconn
		except Exception as e:
			raise e

	@property
	def tcpsegoffload(self) :
		r"""Offload TCP segmentation to the NIC. If set to AUTOMATIC, TCP segmentation will be offloaded to the NIC, if the NIC supports it.<br/>Default value: AUTOMATIC<br/>Possible values = AUTOMATIC, DISABLED.
		"""
		try :
			return self._tcpsegoffload
		except Exception as e:
			raise e

	@tcpsegoffload.setter
	def tcpsegoffload(self, tcpsegoffload) :
		r"""Offload TCP segmentation to the NIC. If set to AUTOMATIC, TCP segmentation will be offloaded to the NIC, if the NIC supports it.<br/>Default value: AUTOMATIC<br/>Possible values = AUTOMATIC, DISABLED
		"""
		try :
			self._tcpsegoffload = tcpsegoffload
		except Exception as e:
			raise e

	@property
	def rstwindowattenuate(self) :
		r"""Enable or disable RST window attenuation to protect against spoofing. When enabled, will reply with corrective ACK when a sequence number is invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rstwindowattenuate
		except Exception as e:
			raise e

	@rstwindowattenuate.setter
	def rstwindowattenuate(self, rstwindowattenuate) :
		r"""Enable or disable RST window attenuation to protect against spoofing. When enabled, will reply with corrective ACK when a sequence number is invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rstwindowattenuate = rstwindowattenuate
		except Exception as e:
			raise e

	@property
	def rstmaxack(self) :
		r"""Enable or disable acceptance of RST that is out of window yet echoes highest ACK sequence number. Useful only in proxy mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rstmaxack
		except Exception as e:
			raise e

	@rstmaxack.setter
	def rstmaxack(self, rstmaxack) :
		r"""Enable or disable acceptance of RST that is out of window yet echoes highest ACK sequence number. Useful only in proxy mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rstmaxack = rstmaxack
		except Exception as e:
			raise e

	@property
	def spoofsyndrop(self) :
		r"""Enable or disable drop of invalid SYN packets to protect against spoofing. When disabled, established connections will be reset when a SYN packet is received.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._spoofsyndrop
		except Exception as e:
			raise e

	@spoofsyndrop.setter
	def spoofsyndrop(self, spoofsyndrop) :
		r"""Enable or disable drop of invalid SYN packets to protect against spoofing. When disabled, established connections will be reset when a SYN packet is received.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._spoofsyndrop = spoofsyndrop
		except Exception as e:
			raise e

	@property
	def ecn(self) :
		r"""Enable or disable TCP Explicit Congestion Notification.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ecn
		except Exception as e:
			raise e

	@ecn.setter
	def ecn(self, ecn) :
		r"""Enable or disable TCP Explicit Congestion Notification.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ecn = ecn
		except Exception as e:
			raise e

	@property
	def mptcpdropdataonpreestsf(self) :
		r"""Enable or disable silently dropping the data on Pre-Established subflow. When enabled, DSS data packets are dropped silently instead of dropping the connection when data is received on pre established subflow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mptcpdropdataonpreestsf
		except Exception as e:
			raise e

	@mptcpdropdataonpreestsf.setter
	def mptcpdropdataonpreestsf(self, mptcpdropdataonpreestsf) :
		r"""Enable or disable silently dropping the data on Pre-Established subflow. When enabled, DSS data packets are dropped silently instead of dropping the connection when data is received on pre established subflow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mptcpdropdataonpreestsf = mptcpdropdataonpreestsf
		except Exception as e:
			raise e

	@property
	def mptcpfastopen(self) :
		r"""Enable or disable Multipath TCP fastopen. When enabled, DSS data packets are accepted before receiving the third ack of SYN handshake.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mptcpfastopen
		except Exception as e:
			raise e

	@mptcpfastopen.setter
	def mptcpfastopen(self, mptcpfastopen) :
		r"""Enable or disable Multipath TCP fastopen. When enabled, DSS data packets are accepted before receiving the third ack of SYN handshake.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mptcpfastopen = mptcpfastopen
		except Exception as e:
			raise e

	@property
	def mptcpsessiontimeout(self) :
		r"""MPTCP session timeout in seconds. If this value is not set, idle MPTCP sessions are flushed after vserver's client idle timeout.<br/>Default value: 0<br/>Maximum length =  86400.
		"""
		try :
			return self._mptcpsessiontimeout
		except Exception as e:
			raise e

	@mptcpsessiontimeout.setter
	def mptcpsessiontimeout(self, mptcpsessiontimeout) :
		r"""MPTCP session timeout in seconds. If this value is not set, idle MPTCP sessions are flushed after vserver's client idle timeout.<br/>Default value: 0<br/>Maximum length =  86400
		"""
		try :
			self._mptcpsessiontimeout = mptcpsessiontimeout
		except Exception as e:
			raise e

	@property
	def timestamp(self) :
		r"""Enable or Disable TCP Timestamp option (RFC 1323).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._timestamp
		except Exception as e:
			raise e

	@timestamp.setter
	def timestamp(self, timestamp) :
		r"""Enable or Disable TCP Timestamp option (RFC 1323).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._timestamp = timestamp
		except Exception as e:
			raise e

	@property
	def dsack(self) :
		r"""Enable or disable DSACK.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dsack
		except Exception as e:
			raise e

	@dsack.setter
	def dsack(self, dsack) :
		r"""Enable or disable DSACK.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dsack = dsack
		except Exception as e:
			raise e

	@property
	def ackaggregation(self) :
		r"""Enable or disable ACK Aggregation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ackaggregation
		except Exception as e:
			raise e

	@ackaggregation.setter
	def ackaggregation(self, ackaggregation) :
		r"""Enable or disable ACK Aggregation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ackaggregation = ackaggregation
		except Exception as e:
			raise e

	@property
	def frto(self) :
		r"""Enable or disable FRTO (Forward RTO-Recovery).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._frto
		except Exception as e:
			raise e

	@frto.setter
	def frto(self, frto) :
		r"""Enable or disable FRTO (Forward RTO-Recovery).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._frto = frto
		except Exception as e:
			raise e

	@property
	def maxcwnd(self) :
		r"""TCP Maximum Congestion Window.<br/>Default value: 524288<br/>Minimum length =  8190<br/>Maximum length =  20971520.
		"""
		try :
			return self._maxcwnd
		except Exception as e:
			raise e

	@maxcwnd.setter
	def maxcwnd(self, maxcwnd) :
		r"""TCP Maximum Congestion Window.<br/>Default value: 524288<br/>Minimum length =  8190<br/>Maximum length =  20971520
		"""
		try :
			self._maxcwnd = maxcwnd
		except Exception as e:
			raise e

	@property
	def fack(self) :
		r"""Enable or disable FACK (Forward ACK).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._fack
		except Exception as e:
			raise e

	@fack.setter
	def fack(self, fack) :
		r"""Enable or disable FACK (Forward ACK).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._fack = fack
		except Exception as e:
			raise e

	@property
	def tcpmode(self) :
		r"""TCP Optimization modes TRANSPARENT / ENDPOINT.<br/>Default value: TRANSPARENT<br/>Possible values = TRANSPARENT, ENDPOINT.
		"""
		try :
			return self._tcpmode
		except Exception as e:
			raise e

	@tcpmode.setter
	def tcpmode(self, tcpmode) :
		r"""TCP Optimization modes TRANSPARENT / ENDPOINT.<br/>Default value: TRANSPARENT<br/>Possible values = TRANSPARENT, ENDPOINT
		"""
		try :
			self._tcpmode = tcpmode
		except Exception as e:
			raise e

	@property
	def tcpfastopen(self) :
		r"""Enable or disable TCP Fastopen. When enabled, NS can receive or send Data in SYN or SYN-ACK packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tcpfastopen
		except Exception as e:
			raise e

	@tcpfastopen.setter
	def tcpfastopen(self, tcpfastopen) :
		r"""Enable or disable TCP Fastopen. When enabled, NS can receive or send Data in SYN or SYN-ACK packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tcpfastopen = tcpfastopen
		except Exception as e:
			raise e

	@property
	def hystart(self) :
		r"""Enable or disable CUBIC Hystart.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._hystart
		except Exception as e:
			raise e

	@hystart.setter
	def hystart(self, hystart) :
		r"""Enable or disable CUBIC Hystart.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._hystart = hystart
		except Exception as e:
			raise e

	@property
	def dupackthresh(self) :
		r"""TCP dupack threshold.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  15.
		"""
		try :
			return self._dupackthresh
		except Exception as e:
			raise e

	@dupackthresh.setter
	def dupackthresh(self, dupackthresh) :
		r"""TCP dupack threshold.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  15
		"""
		try :
			self._dupackthresh = dupackthresh
		except Exception as e:
			raise e

	@property
	def burstratecontrol(self) :
		r"""TCP Burst Rate Control DISABLED/FIXED/DYNAMIC. FIXED requires a TCP rate to be set.<br/>Default value: DISABLED<br/>Possible values = DISABLED, FIXED, DYNAMIC.
		"""
		try :
			return self._burstratecontrol
		except Exception as e:
			raise e

	@burstratecontrol.setter
	def burstratecontrol(self, burstratecontrol) :
		r"""TCP Burst Rate Control DISABLED/FIXED/DYNAMIC. FIXED requires a TCP rate to be set.<br/>Default value: DISABLED<br/>Possible values = DISABLED, FIXED, DYNAMIC
		"""
		try :
			self._burstratecontrol = burstratecontrol
		except Exception as e:
			raise e

	@property
	def tcprate(self) :
		r"""TCP connection payload send rate in Kb/s.<br/>Default value: 0<br/>Maximum length =  10000000.
		"""
		try :
			return self._tcprate
		except Exception as e:
			raise e

	@tcprate.setter
	def tcprate(self, tcprate) :
		r"""TCP connection payload send rate in Kb/s.<br/>Default value: 0<br/>Maximum length =  10000000
		"""
		try :
			self._tcprate = tcprate
		except Exception as e:
			raise e

	@property
	def rateqmax(self) :
		r"""Maximum connection queue size in bytes, when BurstRateControl is used.<br/>Default value: 0<br/>Maximum length =  1000000000.
		"""
		try :
			return self._rateqmax
		except Exception as e:
			raise e

	@rateqmax.setter
	def rateqmax(self, rateqmax) :
		r"""Maximum connection queue size in bytes, when BurstRateControl is used.<br/>Default value: 0<br/>Maximum length =  1000000000
		"""
		try :
			self._rateqmax = rateqmax
		except Exception as e:
			raise e

	@property
	def drophalfclosedconnontimeout(self) :
		r"""Silently drop tcp half closed connections on idle timeout.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._drophalfclosedconnontimeout
		except Exception as e:
			raise e

	@drophalfclosedconnontimeout.setter
	def drophalfclosedconnontimeout(self, drophalfclosedconnontimeout) :
		r"""Silently drop tcp half closed connections on idle timeout.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._drophalfclosedconnontimeout = drophalfclosedconnontimeout
		except Exception as e:
			raise e

	@property
	def dropestconnontimeout(self) :
		r"""Silently drop tcp established connections on idle timeout.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dropestconnontimeout
		except Exception as e:
			raise e

	@dropestconnontimeout.setter
	def dropestconnontimeout(self, dropestconnontimeout) :
		r"""Silently drop tcp established connections on idle timeout.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dropestconnontimeout = dropestconnontimeout
		except Exception as e:
			raise e

	@property
	def applyadaptivetcp(self) :
		r"""Apply Adaptive TCP optimizations.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._applyadaptivetcp
		except Exception as e:
			raise e

	@applyadaptivetcp.setter
	def applyadaptivetcp(self, applyadaptivetcp) :
		r"""Apply Adaptive TCP optimizations.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._applyadaptivetcp = applyadaptivetcp
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	@feature.setter
	def feature(self, feature) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			self._feature = feature
		except Exception as e:
			raise e

	@property
	def tcpfastopencookiesize(self) :
		r"""TCP FastOpen Cookie size. This accepts only even numbers. Odd number is trimmed down to nearest even number.<br/>Default value: 8<br/>Minimum length =  4<br/>Maximum length =  16.
		"""
		try :
			return self._tcpfastopencookiesize
		except Exception as e:
			raise e

	@tcpfastopencookiesize.setter
	def tcpfastopencookiesize(self, tcpfastopencookiesize) :
		r"""TCP FastOpen Cookie size. This accepts only even numbers. Odd number is trimmed down to nearest even number.<br/>Default value: 8<br/>Minimum length =  4<br/>Maximum length =  16
		"""
		try :
			self._tcpfastopencookiesize = tcpfastopencookiesize
		except Exception as e:
			raise e

	@property
	def taillossprobe(self) :
		r"""TCP tail loss probe optimizations.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._taillossprobe
		except Exception as e:
			raise e

	@taillossprobe.setter
	def taillossprobe(self, taillossprobe) :
		r"""TCP tail loss probe optimizations.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._taillossprobe = taillossprobe
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		r"""Number of entities using this profile.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstcpprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstcpprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nstcpprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = nstcpprofile()
				addresource.name = resource.name
				addresource.ws = resource.ws
				addresource.sack = resource.sack
				addresource.wsval = resource.wsval
				addresource.nagle = resource.nagle
				addresource.ackonpush = resource.ackonpush
				addresource.mss = resource.mss
				addresource.maxburst = resource.maxburst
				addresource.initialcwnd = resource.initialcwnd
				addresource.delayedack = resource.delayedack
				addresource.oooqsize = resource.oooqsize
				addresource.maxpktpermss = resource.maxpktpermss
				addresource.pktperretx = resource.pktperretx
				addresource.minrto = resource.minrto
				addresource.slowstartincr = resource.slowstartincr
				addresource.buffersize = resource.buffersize
				addresource.syncookie = resource.syncookie
				addresource.kaprobeupdatelastactivity = resource.kaprobeupdatelastactivity
				addresource.flavor = resource.flavor
				addresource.dynamicreceivebuffering = resource.dynamicreceivebuffering
				addresource.ka = resource.ka
				addresource.kaconnidletime = resource.kaconnidletime
				addresource.kamaxprobes = resource.kamaxprobes
				addresource.kaprobeinterval = resource.kaprobeinterval
				addresource.sendbuffsize = resource.sendbuffsize
				addresource.mptcp = resource.mptcp
				addresource.establishclientconn = resource.establishclientconn
				addresource.tcpsegoffload = resource.tcpsegoffload
				addresource.rstwindowattenuate = resource.rstwindowattenuate
				addresource.rstmaxack = resource.rstmaxack
				addresource.spoofsyndrop = resource.spoofsyndrop
				addresource.ecn = resource.ecn
				addresource.mptcpdropdataonpreestsf = resource.mptcpdropdataonpreestsf
				addresource.mptcpfastopen = resource.mptcpfastopen
				addresource.mptcpsessiontimeout = resource.mptcpsessiontimeout
				addresource.timestamp = resource.timestamp
				addresource.dsack = resource.dsack
				addresource.ackaggregation = resource.ackaggregation
				addresource.frto = resource.frto
				addresource.maxcwnd = resource.maxcwnd
				addresource.fack = resource.fack
				addresource.tcpmode = resource.tcpmode
				addresource.tcpfastopen = resource.tcpfastopen
				addresource.hystart = resource.hystart
				addresource.dupackthresh = resource.dupackthresh
				addresource.burstratecontrol = resource.burstratecontrol
				addresource.tcprate = resource.tcprate
				addresource.rateqmax = resource.rateqmax
				addresource.drophalfclosedconnontimeout = resource.drophalfclosedconnontimeout
				addresource.dropestconnontimeout = resource.dropestconnontimeout
				addresource.applyadaptivetcp = resource.applyadaptivetcp
				addresource.feature = resource.feature
				addresource.tcpfastopencookiesize = resource.tcpfastopencookiesize
				addresource.taillossprobe = resource.taillossprobe
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nstcpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].ws = resource[i].ws
						addresources[i].sack = resource[i].sack
						addresources[i].wsval = resource[i].wsval
						addresources[i].nagle = resource[i].nagle
						addresources[i].ackonpush = resource[i].ackonpush
						addresources[i].mss = resource[i].mss
						addresources[i].maxburst = resource[i].maxburst
						addresources[i].initialcwnd = resource[i].initialcwnd
						addresources[i].delayedack = resource[i].delayedack
						addresources[i].oooqsize = resource[i].oooqsize
						addresources[i].maxpktpermss = resource[i].maxpktpermss
						addresources[i].pktperretx = resource[i].pktperretx
						addresources[i].minrto = resource[i].minrto
						addresources[i].slowstartincr = resource[i].slowstartincr
						addresources[i].buffersize = resource[i].buffersize
						addresources[i].syncookie = resource[i].syncookie
						addresources[i].kaprobeupdatelastactivity = resource[i].kaprobeupdatelastactivity
						addresources[i].flavor = resource[i].flavor
						addresources[i].dynamicreceivebuffering = resource[i].dynamicreceivebuffering
						addresources[i].ka = resource[i].ka
						addresources[i].kaconnidletime = resource[i].kaconnidletime
						addresources[i].kamaxprobes = resource[i].kamaxprobes
						addresources[i].kaprobeinterval = resource[i].kaprobeinterval
						addresources[i].sendbuffsize = resource[i].sendbuffsize
						addresources[i].mptcp = resource[i].mptcp
						addresources[i].establishclientconn = resource[i].establishclientconn
						addresources[i].tcpsegoffload = resource[i].tcpsegoffload
						addresources[i].rstwindowattenuate = resource[i].rstwindowattenuate
						addresources[i].rstmaxack = resource[i].rstmaxack
						addresources[i].spoofsyndrop = resource[i].spoofsyndrop
						addresources[i].ecn = resource[i].ecn
						addresources[i].mptcpdropdataonpreestsf = resource[i].mptcpdropdataonpreestsf
						addresources[i].mptcpfastopen = resource[i].mptcpfastopen
						addresources[i].mptcpsessiontimeout = resource[i].mptcpsessiontimeout
						addresources[i].timestamp = resource[i].timestamp
						addresources[i].dsack = resource[i].dsack
						addresources[i].ackaggregation = resource[i].ackaggregation
						addresources[i].frto = resource[i].frto
						addresources[i].maxcwnd = resource[i].maxcwnd
						addresources[i].fack = resource[i].fack
						addresources[i].tcpmode = resource[i].tcpmode
						addresources[i].tcpfastopen = resource[i].tcpfastopen
						addresources[i].hystart = resource[i].hystart
						addresources[i].dupackthresh = resource[i].dupackthresh
						addresources[i].burstratecontrol = resource[i].burstratecontrol
						addresources[i].tcprate = resource[i].tcprate
						addresources[i].rateqmax = resource[i].rateqmax
						addresources[i].drophalfclosedconnontimeout = resource[i].drophalfclosedconnontimeout
						addresources[i].dropestconnontimeout = resource[i].dropestconnontimeout
						addresources[i].applyadaptivetcp = resource[i].applyadaptivetcp
						addresources[i].feature = resource[i].feature
						addresources[i].tcpfastopencookiesize = resource[i].tcpfastopencookiesize
						addresources[i].taillossprobe = resource[i].taillossprobe
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nstcpprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nstcpprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nstcpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nstcpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nstcpprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = nstcpprofile()
				updateresource.name = resource.name
				updateresource.ws = resource.ws
				updateresource.sack = resource.sack
				updateresource.wsval = resource.wsval
				updateresource.nagle = resource.nagle
				updateresource.ackonpush = resource.ackonpush
				updateresource.mss = resource.mss
				updateresource.maxburst = resource.maxburst
				updateresource.initialcwnd = resource.initialcwnd
				updateresource.delayedack = resource.delayedack
				updateresource.oooqsize = resource.oooqsize
				updateresource.maxpktpermss = resource.maxpktpermss
				updateresource.pktperretx = resource.pktperretx
				updateresource.minrto = resource.minrto
				updateresource.slowstartincr = resource.slowstartincr
				updateresource.buffersize = resource.buffersize
				updateresource.syncookie = resource.syncookie
				updateresource.kaprobeupdatelastactivity = resource.kaprobeupdatelastactivity
				updateresource.flavor = resource.flavor
				updateresource.dynamicreceivebuffering = resource.dynamicreceivebuffering
				updateresource.ka = resource.ka
				updateresource.kaconnidletime = resource.kaconnidletime
				updateresource.kamaxprobes = resource.kamaxprobes
				updateresource.kaprobeinterval = resource.kaprobeinterval
				updateresource.sendbuffsize = resource.sendbuffsize
				updateresource.mptcp = resource.mptcp
				updateresource.establishclientconn = resource.establishclientconn
				updateresource.tcpsegoffload = resource.tcpsegoffload
				updateresource.rstwindowattenuate = resource.rstwindowattenuate
				updateresource.rstmaxack = resource.rstmaxack
				updateresource.spoofsyndrop = resource.spoofsyndrop
				updateresource.ecn = resource.ecn
				updateresource.mptcpdropdataonpreestsf = resource.mptcpdropdataonpreestsf
				updateresource.mptcpfastopen = resource.mptcpfastopen
				updateresource.mptcpsessiontimeout = resource.mptcpsessiontimeout
				updateresource.timestamp = resource.timestamp
				updateresource.dsack = resource.dsack
				updateresource.ackaggregation = resource.ackaggregation
				updateresource.frto = resource.frto
				updateresource.maxcwnd = resource.maxcwnd
				updateresource.fack = resource.fack
				updateresource.tcpmode = resource.tcpmode
				updateresource.tcpfastopen = resource.tcpfastopen
				updateresource.hystart = resource.hystart
				updateresource.dupackthresh = resource.dupackthresh
				updateresource.burstratecontrol = resource.burstratecontrol
				updateresource.tcprate = resource.tcprate
				updateresource.rateqmax = resource.rateqmax
				updateresource.drophalfclosedconnontimeout = resource.drophalfclosedconnontimeout
				updateresource.dropestconnontimeout = resource.dropestconnontimeout
				updateresource.applyadaptivetcp = resource.applyadaptivetcp
				updateresource.tcpfastopencookiesize = resource.tcpfastopencookiesize
				updateresource.taillossprobe = resource.taillossprobe
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nstcpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ws = resource[i].ws
						updateresources[i].sack = resource[i].sack
						updateresources[i].wsval = resource[i].wsval
						updateresources[i].nagle = resource[i].nagle
						updateresources[i].ackonpush = resource[i].ackonpush
						updateresources[i].mss = resource[i].mss
						updateresources[i].maxburst = resource[i].maxburst
						updateresources[i].initialcwnd = resource[i].initialcwnd
						updateresources[i].delayedack = resource[i].delayedack
						updateresources[i].oooqsize = resource[i].oooqsize
						updateresources[i].maxpktpermss = resource[i].maxpktpermss
						updateresources[i].pktperretx = resource[i].pktperretx
						updateresources[i].minrto = resource[i].minrto
						updateresources[i].slowstartincr = resource[i].slowstartincr
						updateresources[i].buffersize = resource[i].buffersize
						updateresources[i].syncookie = resource[i].syncookie
						updateresources[i].kaprobeupdatelastactivity = resource[i].kaprobeupdatelastactivity
						updateresources[i].flavor = resource[i].flavor
						updateresources[i].dynamicreceivebuffering = resource[i].dynamicreceivebuffering
						updateresources[i].ka = resource[i].ka
						updateresources[i].kaconnidletime = resource[i].kaconnidletime
						updateresources[i].kamaxprobes = resource[i].kamaxprobes
						updateresources[i].kaprobeinterval = resource[i].kaprobeinterval
						updateresources[i].sendbuffsize = resource[i].sendbuffsize
						updateresources[i].mptcp = resource[i].mptcp
						updateresources[i].establishclientconn = resource[i].establishclientconn
						updateresources[i].tcpsegoffload = resource[i].tcpsegoffload
						updateresources[i].rstwindowattenuate = resource[i].rstwindowattenuate
						updateresources[i].rstmaxack = resource[i].rstmaxack
						updateresources[i].spoofsyndrop = resource[i].spoofsyndrop
						updateresources[i].ecn = resource[i].ecn
						updateresources[i].mptcpdropdataonpreestsf = resource[i].mptcpdropdataonpreestsf
						updateresources[i].mptcpfastopen = resource[i].mptcpfastopen
						updateresources[i].mptcpsessiontimeout = resource[i].mptcpsessiontimeout
						updateresources[i].timestamp = resource[i].timestamp
						updateresources[i].dsack = resource[i].dsack
						updateresources[i].ackaggregation = resource[i].ackaggregation
						updateresources[i].frto = resource[i].frto
						updateresources[i].maxcwnd = resource[i].maxcwnd
						updateresources[i].fack = resource[i].fack
						updateresources[i].tcpmode = resource[i].tcpmode
						updateresources[i].tcpfastopen = resource[i].tcpfastopen
						updateresources[i].hystart = resource[i].hystart
						updateresources[i].dupackthresh = resource[i].dupackthresh
						updateresources[i].burstratecontrol = resource[i].burstratecontrol
						updateresources[i].tcprate = resource[i].tcprate
						updateresources[i].rateqmax = resource[i].rateqmax
						updateresources[i].drophalfclosedconnontimeout = resource[i].drophalfclosedconnontimeout
						updateresources[i].dropestconnontimeout = resource[i].dropestconnontimeout
						updateresources[i].applyadaptivetcp = resource[i].applyadaptivetcp
						updateresources[i].tcpfastopencookiesize = resource[i].tcpfastopencookiesize
						updateresources[i].taillossprobe = resource[i].taillossprobe
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nstcpprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nstcpprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
					unsetresource.applyadaptivetcp = resource.applyadaptivetcp
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nstcpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nstcpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
							unsetresources[i].applyadaptivetcp = resource[i].applyadaptivetcp
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nstcpprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nstcpprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nstcpprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nstcpprofile() for _ in range(len(name))]
						obj = [nstcpprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nstcpprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nstcpprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nstcpprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nstcpprofile resources configured on NetScaler.
		"""
		try :
			obj = nstcpprofile()
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
		r""" Use this API to count filtered the set of nstcpprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nstcpprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Kaprobeupdatelastactivity:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mptcpdropdataonpreestsf:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ecn:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"

	class Spoofsyndrop:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dsack:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mptcp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Frto:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Taillossprobe:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Establishclientconn:
		AUTOMATIC = "AUTOMATIC"
		CONN_ESTABLISHED = "CONN_ESTABLISHED"
		ON_FIRST_DATA = "ON_FIRST_DATA"

	class Flavor:
		Default = "Default"
		Westwood = "Westwood"
		BIC = "BIC"
		CUBIC = "CUBIC"
		Nile = "Nile"

	class Tcpmode:
		TRANSPARENT = "TRANSPARENT"
		ENDPOINT = "ENDPOINT"

	class Mptcpfastopen:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dynamicreceivebuffering:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tcpsegoffload:
		AUTOMATIC = "AUTOMATIC"
		DISABLED = "DISABLED"

	class Ws:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sack:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ackonpush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Syncookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Applyadaptivetcp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Timestamp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tcpfastopen:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ka:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Hystart:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Burstratecontrol:
		DISABLED = "DISABLED"
		FIXED = "FIXED"
		DYNAMIC = "DYNAMIC"

	class Rstmaxack:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dropestconnontimeout:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rstwindowattenuate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ackaggregation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Drophalfclosedconnontimeout:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nagle:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Fack:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nstcpprofile_response(base_response) :
	def __init__(self, length=1) :
		self.nstcpprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstcpprofile = [nstcpprofile() for _ in range(length)]

