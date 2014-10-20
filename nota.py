#!/usr/bin/env python
# Copyright 2014 Yummy Melon Software
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
#
# Author: Charles Y. Choi

import os
import sys
import getopt
import subprocess
import shutil
import Cocoa
import objc
import Foundation

usageString = '%s -hvat:s:i:' % os.path.basename(sys.argv[0])
helpString = """
nota is a command line utility to send an OS X notification to the OS X Notification Center.

-h, --help                                 help
-v, --version                              version
-a, --audio                                if present, play audio 
-t <title>, --title=<title>                title
-s <stitle>, --subtitle=<stitle>           subtitle
-i <itext>, --informativetext=<itext>      informativetext
"""

class NotaApp():
    def __init__(self):
        self.version = 1.0
        self.options = {}
        self.options['title'] = None
        self.options['informative text'] = None
        self.options['subtitle'] = None
        self.options['sound name'] = False
        
    def run(self, optlist, args):
        for o, i in optlist:
            if o in ('-h', '--help'):
                sys.stderr.write(usageString)
                sys.stderr.write(helpString)
                sys.exit(1)

            elif o in ('-v', '--version'):
                sys.stdout.write('%s\n' % str(self.version))
                sys.exit(0)

            elif o in ('-t', '--title'):
                self.options['title'] = i

            elif o in ('-i', '--informativetext'):
                self.options['informative text'] = i

            elif o in ('-s', '--subtitle'):
                self.options['subtitle'] = i

            elif o in ('-a', '--audio'):
                self.options['sound name'] = True
                
                
        if len(args) < 1:
            pass

        if not self.options['title']:
            sys.stderr.write('ERROR: no title specified\n')
            sys.exit(1)

        userNotification = Cocoa.NSUserNotification.alloc().init()

        userNotification.setTitle_(self.options['title'])

        if self.options['subtitle']:
            userNotification.setSubtitle_(self.options['subtitle'])
        
        if self.options['informative text']:
            userNotification.setInformativeText_(self.options['informative text'])

        if self.options['sound name']:
            userNotification.setSoundName_(Cocoa.NSUserNotificationDefaultSoundName)
            
        defaultNotificationCenter = Cocoa.NSUserNotificationCenter.defaultUserNotificationCenter()
        defaultNotificationCenter.deliverNotification_(userNotification)

         
if __name__ == '__main__':
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'hvt:i:s:a',
                                      ('help'
                                       , 'version'
                                       , 'title='
                                       , 'informativetext='
                                       , 'subtitle='
                                       , 'audio'
                                       ))
    except getopt.error, msg:
        sys.stderr.write(msg[0] + '\n')
        sys.stderr.write(usageString + '\n')
        sys.exit(1)

    app = NotaApp()
    app.run(optlist, args)

