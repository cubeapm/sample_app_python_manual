# OpenTelemetry Instrumentation

This branch contains code for OpenTelemetry instrumentation.

Running the application will generate the corresponding traces. Traces are printed to the console by default. If you want to send traces to a backend tool, update the configuration by commenting out the `OTEL_LOG_LEVEL` line and uncommenting the `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` line.

And also update [main.py](main.py):

`if os.getenv('OTEL_LOG_LEVEL', '') == 'debug':` to `if os.getenv('OTEL_LOG_LEVEL', '') == 'otlp':`

This ensures that traces are sent to the backend tool instead of being printed to the console."

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
opentelemetry-bootstrap -a install


export OTEL_SERVICE_NAME=cube_sample_python_manual_otel
export OTEL_EXPORTER_OTLP_COMPRESSION=gzip
# print traces on console
export OTEL_LOG_LEVEL=debug
# send traces to CubeAPM
# export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://<ip_address_of_cubeapm_server>:4318/v1/traces
python3 main.py
```

# Contributing

Please feel free to raise PR for any enhancements - additional service integrations, library version updates, documentation updates, etc.
