#  genny.py
#  
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

import os
import warnings  
from strgen import StringGenerator
'''
from .__about__ import (
    __author__, __copyright__, __email__, __license__, __summary__, __title__,
    __uri__, __version__,
)


__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
    "genid","nameid",
]
'''

name="genny"
version=1.0


def genid(doc_tag):
    """ 
    	Doc Tags: String( doc, app, key, job, user, item, code,task,name)
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
    tags = dict(
        doc='[h-z5-9]{8:16}',
        app='[a-z0-9]{16:32}',
        key='[a-z0-9]{32:32}',
        job='[a-j0-7]{8:8}',
        user='[0-9]{4:6}',
        item='[a-n1-9]{8:8}',
        code='[a-x2-8]{24:32}'
    )
    if doc_tag == 'user':
        u_id = StringGenerator(str(tags[doc_tag])).render(unique=True)
        u_id = 'U{}'.format(u_id)
    else:
        u_id = StringGenerator(str(tags[doc_tag])).render(unique=True)
    return u_id
    

def nameid(fn='Jane',ln='Dear',sec=5):
    """ 
    	Name Identification by initials fn='Jane', ln='Dear' and given number sequence sec=5.
    	
        UseCase: 
			  		>>> import genny
			  		>>> from genny import nameid
			  		>>> from genny import nameid as nid
			  		
			  		>>> id = genny.nameid('Peter','Built',6)
			  		>>> id = nameid('Peter','Built',5)
			  		>>> id = nid('Peter','Built',4)
                    >>> id = nid() # default false id 
                    
			 Yeilds ... PB474390
			 		... PB77301
			 		... PB1593
                    ... JD1951
    
    """
    code = '[0-9]{4:%s}'% int(sec)
    prefix = '{fni}{lni}'.format(fni=fn[0].capitalize(),lni=ln[0].capitalize())
    u_id = StringGenerator(str(code)).render(unique=True)
    u_id = '{pre}{id}'.format(pre=prefix,id=u_id)
    
    return u_id
    
    

def eventid(event,event_code,sec=8):
    """ 
    	Event Identification by initials fn='Jane', ln='Dear' and given number sequence sec=5.
    	
        UseCase: 
			  		>>> import genny
			  		>>> from genny import nameid
			  		>>> from genny import nameid as nid
			  		
			  		>>> id = genny.nameid('Peter','Built',6)
			  		>>> id = nameid('Peter','Built',5)
			  		>>> id = nid('Peter','Built',4)
                    >>> id = nid() # default false id 
                    
			 Yeilds ... PB474390
			 		... PB77301
			 		... PB1593
                    ... JD1951
    
    """
    code = '[0-9]{5:%s}'% int(sec)
    prefix = '{fni}{lni}'.format(fni=event[:3].upper(),lni=event_code)
    u_id = StringGenerator(str(code)).render(unique=True)
    u_id = '{pre}-{id}'.format(pre=prefix,id=u_id)
    
    return u_id

