# Python_logs


## Logging

directory: `logging_`

Consists of 2 parts:

<details>
<summary>tutorial</summary>

Consists of 6 files
1. `singleton.py`
2. `handlers.py`
3. `configurations.py`
4. `errors_logging.py`
5. `filters.py`
6. `custom_handler.py`

### Singleton (1st file)

Description:
Get a basic understanding of the `logging` library
- what is a logger and a handler
- logging levels
- how this module works.

Dependencies: 
- requests

___
`logger = logging.getLogger()` -
Gets (if already exists) or creates a logger (singleton pattern).
We don't pass a name to the logger, in this case the logger named 'root' is taken.
When we set a name, we will actually have 2 loggers:
- 'root'
- named logger
___

#### Logger & Handler levels
- NOTSET is **_`0`_** eq
- DEBUG is **_`10`_** eq
- INFO is **_`20`_** eq
- WARNING is **_`30`_** eq
- ERROR is **_`40`_** eq
- Critical is **_`50`_** eq

`logger.setLevel("DEBUG")` - this is how the level is set


P.S. default logger eq is WARNING
___
`logging.basicConfig(level="DEBUG")` -
let's write this line, it sets up the root's handler
(3rd file will tell you more about it).
___

Let's write a main function that will send requests to the browser.
There will be a lot of logs on startup since 
`requests` has its own built-in loggers 
(loggers are processed since it is a singleton).

`logging.getLogger("urllib3").setLevel("ERROR")` -
disable built-in loggers (root and child users disabled)

#### Logger naming
`app` - parent logger
`app.services` - child
___
### Singleton (2nd file)
...

</details>



<details>
<summary>template</summary>
<br>
Well, you asked for it!
</details>