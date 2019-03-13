# Lego: visualisation and exploration
Exploration and visualisation of the [Rebrickable](https://rebrickable.com/about/) database of Lego sets, accurate as of 2017. Dataset downloaded from [Kaggle](https://www.kaggle.com/rtatman/lego-database).

## Database creation
The Kaggle dataset comprises 8 csv files and the schema of the original Rebrickable dataset. An sqlite version of the original DB can be recreated in `data/db` by running:

```
pip3 install pandas
python3 src/database/create_db.py
```
