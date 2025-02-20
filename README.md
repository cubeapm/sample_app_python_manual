# New Relic Instrumentation

This branch contains code for New Relic instrumentation.

CubeAPM works with New Relic agents as described in [using CubeAPM with New Relic agents](https://docs.cubeapm.com/instrumentation#using-cubeapm-with-new-relic-agents).

For testing, **ngrok** can be used in place of load balancer. Run `ngrok http 3130` to create a tunnel and use the domain name provided by ngrok to set `NEW_RELIC_HOST=xxxx.ngrok-free.app`.

Refer the project README below for more details.

---

# Python Manual Instrumentation

This is a sample app to demonstrate how to instrument Python Manual app with **New Relic** and **OpenTelemetry**. It contains source code for the Python Manual app.

The code is organized into multiple branches. The main branch has the Python Manual app without any instrumentation. Other branches then build upon the main branch to add specific instrumentations as below:

| Branch                                                                                         | Instrumentation | Code changes for instrumentation                                                                                |
| ---------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------- |
| [main](https://github.com/cubeapm/sample_app_python_manual/tree/main)         | None            | -                                                                                                               |
| [newrelic](https://github.com/cubeapm/sample_app_python_manual/tree/newrelic) | New Relic       | [main...newrelic](https://github.com/cubeapm/sample_app_python_manual/compare/main...newrelic) |
| [otel](https://github.com/cubeapm/sample_app_python_manual/tree/otel)         | OpenTelemetry   | [main...otel](https://github.com/cubeapm/sample_app_python_manual/compare/main...otel)         |

# Setup

Clone this repository and go to the project directory. Then run the following commands

```
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt

# New Relic agent will send data on https://<domain_of_cubeapm_server>:443
export NEW_RELIC_HOST=<domain_of_cubeapm_server>
export NEW_RELIC_APP_NAME=cube_sample_python_manual_newrelic
export NEW_RELIC_LICENSE_KEY=ABC4567890ABC4567890ABC4567890ABC4567890
python3 main.py
```

# Contributing

Please feel free to raise PR for any enhancements - additional service integrations, library version updates, documentation updates, etc.
