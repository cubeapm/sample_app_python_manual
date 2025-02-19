import os
import time
from opentelemetry import trace, context
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.propagate import extract
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.semconv.trace import SpanAttributes
from opentelemetry.trace.status import Status, StatusCode


# Reference documentation:
# https://opentelemetry.io/docs/languages/python/instrumentation/


# Initialize tracing
provider = TracerProvider()
if os.getenv('OTEL_LOG_LEVEL', '') == 'debug':
    processor = SimpleSpanProcessor(ConsoleSpanExporter())
else:
    processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# uncomment the following line to attach context propagation headers if needed
# context.attach(extract(req.headers))


@tracer.start_as_current_span("my_span_name", kind=trace.SpanKind.SERVER)
def someTask():
    childTask(2)
    try:
        errorTask()
    except Exception as ex:
        span = trace.get_current_span()
        span.record_exception(ex)
        span.set_status(Status(StatusCode.ERROR))
    try:
        errorTaskWithSpan()
    except:
        pass

    with tracer.start_as_current_span("inline-span"):
        time.sleep(0.1)


@tracer.start_as_current_span("childTask")
def childTask(val):
    span = trace.get_current_span()
    span.set_attribute("val", val)
    pass

def errorTask():
    raise KeyError()

@tracer.start_as_current_span("errorTask_withSpan")
def errorTaskWithSpan():
    raise KeyError()

if __name__ == "__main__":
    for i in range(2):
        someTask()
        time.sleep(1)
        