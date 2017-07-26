#!/usr/bin/env python

# Copyright (C) 2017 Luc H
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function

import argparse
import os.path
import json

import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file
import sys
import signal

# setup detector
model = 'jarvis.pmdl'
import snowboydecoder
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)




# interrupt handler (unneeded?)

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


signal.signal(signal.SIGINT, signal_handler)




# mostly debug event processing
def process_event(event):

    """Pretty prints events.

    Prints all events that occur with two spaces between each new
    conversation and a single space between turns of a conversation.

    Args:
        event(event.Event): The current event to process.
    """

    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        print()

    print(event)

    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        print()


# parse credentials
def main():
    global credentials
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,**json.load(f))
        print(credentials)


# default assistant left in for debugging

 #   with Assistant(credentials) as assistant:
  #      for event in assistant.start():
   #         process_event(event)


if __name__ == '__main__':
    main()



# when detector detects hotword.

def detect_callback():
    with Assistant(credentials) as assistant:
      print('yes boss?')
      detector.terminate()
      print("google will help you")
      snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)
      assistant.start_conversation()
      snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)
      print("bye")
      detector.start(detected_callback=detect_callback, interrupt_check=interrupt_callback, sleep_time=0.03)
      print("Listening for next wakewors")




# start assistant non-listening so a conversation can be started
# this part may give problems.

with Assistant(credentials) as assistant:
  assistant.start()
  assistant.set_mic_mute(True)


# start first wakewors detection
detector.start(detected_callback=detect_callback, interrupt_check=interrupt_callback, sleep_time=0.03)






# terminates on interrupt, may be unneeded.
detector.terminate()
