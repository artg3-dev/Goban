# SGF File data types
from datetime import datetime
DATA_TYPES = {
	"simpletext": str,
	"color": str,
	"number | numberpair": int,
	"move": tuple,
	"number": int,
	"real": float,
	"text": str,
	"time": datetime,
	"labellist": list,
	"pointlist": list
	}