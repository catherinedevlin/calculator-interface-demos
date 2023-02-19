
# CLIs, REPLs, GUIs, APIs, webapps

Materials from DDL's 
[December 2022](http://d8ndl.org/meeting/2022/12/14/cli-repl-gui-api.html) meeting on CLIs, REPLs, GUIs, and webapps.

    calc
    calc-repl 
    calc-gui
    calc-web 

For the API:

    uvicorn calculator.api:api --reload
    curl "127.0.0.1:8000/add?x=9&y=1.9"
    # the quotes are crucial!

    vivaldi http://127.0.0.1:8000/docs

Not shown (yet): TUIs...

    python -m textual 



