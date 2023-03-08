from rethinkdb import r

r.set_loop_type("asyncio")

# constants
ALL = 0
DECLARED_ONLY = 1
UNDECLARED_ONLY = 2

from .version import *
from .errors import *
from .db import *
from .values_and_valuetypes import *
from .field import *
from .document import *
