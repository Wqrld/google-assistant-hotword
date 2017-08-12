Currently broken! 
===============================================

This repository contains a way to use a custom hotword with google assistant.

It demonstrates: - Initialization of the Assistant - Basic event handling including hotword detection.

Prerequisites
-------------

-   [Python] &gt;= 3.4
-   Raspberry Pi 3 running Rasbian (or any other `linux-arm7l` SBC)
-   A [Google API Console Project]
-   A [Google account]

Setup
-----

-   Install Python 3

    > -   Ubuntu/Debian GNU/Linux:
    >
    >         sudo apt-get update
    >         sudo apt-get install python3 python3-venv
    >
    > -   [MacOSX, Windows, Other]

-   Create a new virtual environment (recommended):

        python3 -m venv env
        env/bin/python -m pip install --upgrade pip setuptools
        source env/bin/activate

Authorization
-------------

-   Follow [the steps to configure the project and the Google account].
-   Download the `client_secret_XXXXX.json` file from the [Google API Console Project credentials section] and generate credentials using `google-oauth-tool`:

        pip install --upgrade google-auth-oauthlib[tool]
        google-oauthlib-tool --client-secrets path/to/client_secret_XXXXX.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless

Run the sample
--------------

-   Install the sample dependencies using [pip]:

        pip install --upgrade -r requirements.txt

-   Run the hotword sample. The sample waits for the “Ok Google” hotword, then records a voice query and plays back the Google Assistant’s answer:

        python -m hotword

-   If that works, execute:

>         python3 -m jarvis




Changing the hotword
--------------------

-   The hotword can be changed in jarvis.py

Troubleshooting
---------------

-   If audio is not working, verify the ALSA setup:

        # Play a test sound
        speaker-test -t wav

        # Record and play back some audio using ALSA command-line tools
        arecord --format=S16_LE --duration=5 --rate=16k --file-type=raw out.raw
        aplay --format=S16_LE --rate=16k --file-type=raw out.raw

See also the [troubleshooting section] of the official documentation.

License
-------

Copyright (C) 2017 Google Inc, Kitt\_ai And aycgit

See the LICENCE file distributed with this work for additional information regarding copyright ownership.

  [package]: https://github.com/googlesamples/assistant-sdk-python/tree/master/google-assistant-library
  [Python]: https://www.python.org/
  [Google API Console Project]: https://console.developers.google.com
  [Google account]: https://myaccount.google.com/
  [MacOSX, Windows, Other]: https://www.python.org/downloads/
  [the steps to configure the project and the Google account]: https://developers.google.com/assistant/sdk/prototype/getting-started-other-platforms/config-dev-project-and-account
  [Google API Console Project credentials section]: https://console.developers.google.com/apis/credentials
  [pip]: https://pip.pypa.io/
  [troubleshooting section]: https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/troubleshooting
