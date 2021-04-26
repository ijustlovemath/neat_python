'''Sometimes it's nice to turn key-value pairs into objects
where you use the key name as an attribute name, for example
after receiving a JSON object over the wire'''

class Reporter:
    def __init__(self):
        self.cache = set()
    def report(self, item):
        self.cache.add(item)
    def __repr__(self):
        return str(self.cache)

class SerialPortContainer:
    attributes = {
        "timeout"
        , "baud_rate"
    }
    def __init__(self, data, reporter=None):
        # data is a dict we want to turn into this object
        # data could come from a json.loads() call, or elsewhere
        for attribute in self.attributes:
            self.__dict__[attribute] = None
        for attribute, value in data.items():
            if attribute not in self.attributes:
                # Use a nice helper object to keep track of attributes we
                # do not have implemented
                if reporter:
                    reporter.report(attribute)
                else:
                    raise AttributeError(f"Unhandled attribute '{attribute}'")
            self.__dict__[attribute] = value
    def __repr__(self):
        return '\n'.join(f'{key}: {value}' for key, value in self.__dict__.items())

# Case 1: you give it a dict which doesnt contain the expected attributes, it raises an error (ignored)
from contextlib import suppress
with suppress(AttributeError):
    serial_port = SerialPortContainer({"data_bits": 8})

# Case 2: you want to know about the missing attributes, but maybe just as a report
from pprint import pprint
reporter = Reporter()
serial_port = SerialPortContainer({"stop_bits": 1}, reporter=reporter)
print(f"missing attributes: {reporter}")
print(serial_port)

# Case 3: you provide all the attributes in the dict and access them normally:
serial_port = SerialPortContainer({"timeout": 100, "baud_rate": 9600})
print(serial_port)
print(serial_port.baud_rate) # <-- here's the magic part!
