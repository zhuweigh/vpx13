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


class gslbservicegroup_args :
	r""" Provides additional arguments required for fetching the gslbservicegroup resource.
	"""
	def __init__(self) :
		self._includemembers = None

	@property
	def includemembers(self) :
		r"""Display the members of the listed GSLB service groups in addition to their settings. Can be specified when no service group name is provided in the command. In that case, the details displayed for each service group are identical to the details displayed when a service group name is provided, except that bound monitors are not displayed.
		"""
		try :
			return self._includemembers
		except Exception as e:
			raise e

	@includemembers.setter
	def includemembers(self, includemembers) :
		r"""Display the members of the listed GSLB service groups in addition to their settings. Can be specified when no service group name is provided in the command. In that case, the details displayed for each service group are identical to the details displayed when a service group name is provided, except that bound monitors are not displayed.
		"""
		try :
			self._includemembers = includemembers
		except Exception as e:
			raise e

