stopwatch
=========
Python context manager for timing blocks of code. Simply wrap any code you want to time with a `with Stopwatch('task name'):` context. Stopwatch will measure how long the execution took and log the results.


## Example
```python
from stopwatch import Stopwatch

with Stopwatch('data retrieval'):
	db.connect()
	data = db.getData()

with Stopwatch('analysis'):
	results = analyze(data)

with Stopwatch('report generation'):
	report = generateReport(results)
	reports.save('report.pdf')
```

This code might produce a log output like this:

```
[2014-02-10 09:58:50,936][stopwatch][DEBUG] "data retrieval" done in 0.577 seconds.
...
[2014-02-10 09:59:06,161][stopwatch][DEBUG] "analysis" done in 14.780 seconds.
...
[2014-02-10 09:59:13,032][stopwatch][DEBUG] "report generation" done in 6.117 seconds.
```
