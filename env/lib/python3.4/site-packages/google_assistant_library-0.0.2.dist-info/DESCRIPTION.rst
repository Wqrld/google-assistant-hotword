Python bindings for the Google Assistant Library.
=================================================

High level Python bindings for the Google Assistant Library.

It supports the following features:
- recording of audio query.
- playback of assistant answer.
- "Ok Google" and "Hey Google" hotword detection.

Prerequisites
-------------

- `Python <https://www.python.org/>`_ (3.x prefered)
- `Google API Console Project <https://console.developers.google.com>`_ w/ Google Assistant API `enabled <https://console.developers.google.com/apis>`_.
- `OAuth client ID credentials <https://console.developers.google.com/apis/credentials>`_ with application type ``Other``.
- Use a new virtualenv (recommended)::

        # python3 (recommended)
        sudo apt-get update
        sudo apt-get install python3-dev python3-venv
        python3 -m venv env
        env/bin/python -m pip install --upgrade pip setuptools
        source env/bin/activate

        # python2
        sudo apt-get update
        sudo apt-get install python-dev python-virtualenv
        virtualenv env --no-site-packages
        env/bin/python -m pip install --upgrade pip setuptools
        source env/bin/activate

Install
-------

- Install the package and its dependencies::

       python -m pip install --upgrade google-assistant-library

Run the demo
------------

- Authenticate (this step only needs to be run once)::

        python -m pip install google-auth-oauthlib[tool]
        google-oauthlib-tool --client-secrets path/to/client_secret_XXXXX.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save

- Run the demo::

        google-assistant-demo

- Say "Ok Google", followed by a voice query: the demo should
  playback the assistant answer and log events to the screen.

For Maintainers
---------------

See `MAINTAINER.md <MAINTAINER.md>`_ for more documentation on the
development, maintainance and release of the Python package itself.

License
-------

See `LICENSE <LICENSE>`_ and `google/assistant/library/LICENSE.third_party <google/assistant/library/LICENSE.third_party>`_.


