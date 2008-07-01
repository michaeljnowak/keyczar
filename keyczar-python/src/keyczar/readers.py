# Copyright 2008 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" 
A Reader supports reading metadata and key info for key sets. 

@author steveweis@gmail.com (Steve Weis)
@author arkajit.dey@gmail.com (Arkajit Dey)
"""

import kmd
import keys
import simplejson

class Reader:
  """ Interface providing supported methods (no implementation). """

  def metadata(self):
    """Return the KeyMetadata for the key set being read.
    
    @return KeyMetadata object
    """
    pass
  
  def key(self, version):
    """Return the Key corresponding to the given version.
    
    @param version, the integer version number
    @return Key object
    """
    pass

class FileReader(Reader):
  def __init__(self, location):
    self.location = location
    
  def metadata(self):
    metadata = simplejson.loads(open(self.location + "/meta").read())
    return kmd.KeyMetadata.read(metadata)

  def key(self, version):
    keyData = simplejson.loads(open(self.location + "/" + str(version)).read())
    return keys.Key.read(keyData)