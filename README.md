# Lego: visualisation and exploration
Exploration and visualisation of the [Rebrickable](https://rebrickable.com/about/) database of Lego sets, accurate as of 2019-05-08.

## Database creation
Rebrickable has released their database in the form of 9 `.csv` files and the database schema. The most recent release can be downloaded [here](https://rebrickable.com/downloads/). An sqlite version of the original Rebrickable dataset can be recreated in `data/db` by running:

```
pip3 install pandas
python3 src/database/create_db.py
```

TODO: implement the `part_relationships` table.
