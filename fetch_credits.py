import requests
import pandas as pd
w1 = "https://www.dunkest.com/api/stats/table?season_id=23&mode=dunkest&stats_type=tot&weeks%5B%5D=1&rounds%5B%5D=1&rounds%5B%5D=2&teams%5B%5D=32&teams%5B%5D=33&teams%5B%5D=34&teams%5B%5D=35&teams%5B%5D=36&teams%5B%5D=37&teams%5B%5D=38&teams%5B%5D=39&teams%5B%5D=40&teams%5B%5D=41&teams%5B%5D=42&teams%5B%5D=43&teams%5B%5D=44&teams%5B%5D=45&teams%5B%5D=46&teams%5B%5D=47&teams%5B%5D=48&teams%5B%5D=56&teams%5B%5D=60&teams%5B%5D=75&positions%5B%5D=1&positions%5B%5D=2&positions%5B%5D=3&player_search=&min_cr=4&max_cr=35&sort_by=pdk&sort_order=desc&iframe=yes"


response = requests.get(w1)

data = response.json()

df = pd.DataFrame(data)


df = df[df.columns.sort_values()]

df.set_index("id", inplace=True)
keys = ["first_name", "last_name", "position", "cr", "pdk"]

df = df[keys]
df[["cr", "pdk"]] = df[["cr", "pdk"]].astype(float)

df["pdk_per_cr"] = df["pdk"].div(df["cr"])
df.to_csv("euroleague_credits.csv")

