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

python3 main.py
```

# Contributing

Please feel free to raise PR for any enhancements - additional service integrations, library version updates, documentation updates, etc.
