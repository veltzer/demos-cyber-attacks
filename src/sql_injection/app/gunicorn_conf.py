"""
This is a configuration file for gunicorn
"""

# Access log configuration
# pylint: disable=invalid-name
# Log to standard output (stdout) for now (change to a file if needed)
accesslog = '-'
access_log_format = '%(h)s %(r)s %(s)s %(b)s %(f)s %(a)s'
