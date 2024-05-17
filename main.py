import os
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
    errorTask()

@tracer.start_as_current_span("childTask")
def childTask(val):
    span = trace.get_current_span()
    span.set_attribute("val", val)
    pass

@tracer.start_as_current_span("errorTask")
def errorTask():
    raise KeyError()

someTask()