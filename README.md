# csvmerge

Join two csv files on a specific column.  Command line wrapper around Pandas merge
defaults to outer join
    
Usage:

   Outer Join two files on a column named 'id'
   ```poetry run python ./src/csvmerge.py ./data/left.csv ./data/right.csv  id --join outer --output output_output.csv --verbose```


   Left Join two files on a column named 'id'
   ```poetry run python ./src/csvmerge.py ./data/left.csv ./data/right.csv  id --join left --output left_output.csv --verbose```
