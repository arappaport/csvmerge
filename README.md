# csvmerge

Join two csv files on a specific column.  Command line wrapper around Pandas merge. 
  Defaults to outer join
    
##Usage

Usage: csvmerge.py [OPTIONS] LEFT RIGHT

   Join 2 csv files on a specific column.

   defaults to outer join

    Join 2 csv files on a specific column. Wrapper around pandas dataframe merge().
    See [pandas dataframe.merge doc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) for join behavior.


   Usage:

  Left Join two files on a column named 'id' 
  
```
poetry run python ./src/csvmerge.py ./data/left.csv ./data/right.csv  --join left --on id
  --output left_output.csv --verbose
```

  Outer Join two files.   Left file join on column named 'id', right file on
  'alt_id' 
  
```
poetry run python ./src/csvmerge.py ./data/left.csv
  ./data/right.csv  --join outer --left_on id  --right_on alt_id --output
  outer_output.csv --verbose
  ```



Usage Options: <br>
  --left_on TEXT                  Column to join on from left file <br>
  --right_on TEXT                 Column to join on from right file.  If not,
                                  present then the --left_on is used <br>
  --join [outer|inner|left|right]
                                  join type: inner, outer.   Defaults to outer <br>
  -o, --output TEXT               (optional) name of file to write data into.<br>
  -d, --dryrun                    If set, will only gather data and not write<br>
  -v, --verbose                   Enables verbose logging mode<br>
  -q, --quiet                     Limits logging output to warnings and
                                  errors.<br>
  --version                       Show the version and exit. <br>
  --help                          Show this message and exit.<br>
