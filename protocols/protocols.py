from typing import Any
from typing import Protocol as ProtocolistProtocol
from typing import runtime_checkable

@runtime_checkable
class ASubscript(ProtocolistProtocol):
	identity: Any
	mass: Any
	range: Any
	type: Any
	
@runtime_checkable
class RobotvectorSubscript(ProtocolistProtocol):
	resolution: Any
	
@runtime_checkable
class RvectorSubscript(ProtocolistProtocol):
	identity: Any
	mass: Any
	range: Any
	resolution: Any
	type: Any
	
@runtime_checkable
class SortedrobotsSubscriptSubscript(ProtocolistProtocol):
	mass: Any
	range: Any
	resolution: Any
	type: Any
