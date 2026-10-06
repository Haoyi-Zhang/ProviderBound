"""Standard-library telemetry; unavailable OS counters remain null."""
from __future__ import annotations
import sys
try:
    import resource
except ImportError:
    resource = None


def usage(children=False):
    if resource is None:
        return {'cpu_seconds': None, 'peak_rss_kib': None,
                'scope': 'unavailable: resource.getrusage is not provided on this OS'}
    value = resource.getrusage(resource.RUSAGE_CHILDREN if children else resource.RUSAGE_SELF)
    rss = value.ru_maxrss / 1024 if sys.platform == 'darwin' else value.ru_maxrss
    return {'cpu_seconds': value.ru_utime + value.ru_stime, 'peak_rss_kib': rss,
            'scope': 'getrusage child high-water mark' if children else 'getrusage process-lifetime high-water mark'}
