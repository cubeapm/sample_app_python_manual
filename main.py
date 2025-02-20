import os
import time
import newrelic.agent

# Reference documentation:
# https://docs.newrelic.com/docs/apm/agents/python-agent/python-agent-api/guide-using-python-agent-api/

# Initialize New Relic agent
newrelic.agent.initialize()

@newrelic.agent.background_task(name="my_span_name")
def someTask():
    with newrelic.agent.FunctionTrace(name="child_task"):
        childTask(2)

    try:
        with newrelic.agent.FunctionTrace(name="error_task"):
            errorTask()
    except Exception as ex:
        transaction = newrelic.agent.current_transaction()
        if transaction:
            newrelic.agent.notice_error(error=ex)

    try:
        with newrelic.agent.FunctionTrace(name="error_task_with_span"):
            errorTaskWithSpan()
    except:
        pass

    with newrelic.agent.FunctionTrace(name="inline_span"):
        time.sleep(0.1)

@newrelic.agent.background_task(name="child_task")
def childTask(val):
    transaction = newrelic.agent.current_transaction()
    if transaction:
        transaction.add_custom_parameter("val", val)

def errorTask():
    raise KeyError()

@newrelic.agent.background_task(name="error_task_with_span")
def errorTaskWithSpan():
    raise KeyError()

if __name__ == "__main__":
    for i in range(2):
        someTask()
        time.sleep(1)
