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


class vpnsfconfig_args :
	r""" Provides additional arguments required for fetching the vpnsfconfig resource.
	"""
	def __init__(self) :
		self._vserver = None

	@property
	def vserver(self) :
		r"""Name of Gateway virtual server.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		r"""Name of Gateway virtual server.
		"""
		try :
			self._vserver = vserver
		except Exception as e:
			raise e

