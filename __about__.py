#  Copyright 2018 ian moncrieffe <ian@allhome620>
#  
# Author:: Ian Moncrieffe (<ian@allhome620>)
# Copyright:: Copyright (c) 2018 Ian Moncrieffe
# License:: Apache License, Version 2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "genny"
__summary__ = """ Unique Identity number generator for your application's users, documents, applications,
			 software and your servers.			 
			  Doc Tags: String( doc, app, key, job, user, item, code)
			  UseCase: 
			  		>>> import genny
			  		>>> from genny import genid
			  		>>> from genny import genid as gi
			  		
			  		>>> id = genny.genid('user')
			  		>>> id = genid('user')
			  		>>> id = gi('user')
			 Yeilds ... U474390
			 		... U77301642
			 		... U1593055		 
						  
			  """
			  
__uri__ = "https://github.com/centry/genny/"

__version__ = "2.3.6"

__author__ = "CentrySoft developers"
__email__ = "centryplan@outlook.com"

__license__ = "Apache License, Version 2.0"
__copyright__ = "Copyright 2018-2020 {0}".format(__author__)
