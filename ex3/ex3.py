# %% [markdown]
# Dependencies

# %%
!uv add numpy
!uv add pandas
!uv add ipykernel

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# # Task 1
# Q1

# %%
with open('mobile_price_1.csv') as f:
    data_frame = pd.read_csv(f)

# %% [markdown]
# Q2

# %% [markdown]
# nominal:
# * bluetooth
# * screen

# ordinal:
# * gen
# * cores
# * sim
# * speed
# * wifi


# %% [markdown]
# Q3

# %%
data_frame = data_frame.assign(resolution=data_frame["px_width"] * data_frame["px_height"])

# %% [markdown]
# Q4

# %%
data_frame = data_frame.assign(DPI_w=data_frame["px_width"]/data_frame["sc_w"])
data_frame.replace({"DPI_w":[np.inf, -np.inf, np.nan]}, 0, inplace=True)

# %% [markdown]
# Q5

# %%
data_frame.assign(call_ratio=data_frame["battery_power"]/data_frame["talk_time"])
data_frame.replace({"call_ratio":[np.inf, -np.inf, np.nan]}, 0, inplace=True)

# %% [markdown]
# Q6

# %%
# 6. Change the memory column to hold the memory in GB instead of MB.

# %% [markdown]
# Q7

# %%
# 7. Include the output of the `describe()` function of the dataframe.

# %% [markdown]
# Q8

# %%
# 8. Convert the following features into categorical series in the Dataframe: speed,screen,cores


# %% [markdown]
# # Task 2
# Q1

# %% [markdown]
# 1. How many phones do not have a camera at all (front or back)?

# %%
# Q2

# %%
# 2. What is the average battery power for single-sim phones that have a camera or front camera  with a higher resolution than 12 megapixels?

# %% [markdown]
# Q3

# %%
# 3. What is the ID and price of the most expensive phone that has no wifi, a touch screen and  weighs more than 145 grams?

# %% [markdown]
# Q4

# %%
# 4. Create a pivot table that shows the percentage of phones with Bluetooth per generation,  pivoted around the phone generation and split by “ram” quartiles. (i.e. the rows are the  generation number and the columns are 4 quartiles of ram size).

# %% [markdown]
# 5. Create a new Dataframe based on the original that has the following features: [id,  battery_power, ram, talk_time, Bluetooth, cores, sim, memory, price], and contains a random  sampling of half of the medium speed phones.

# %% [markdown]
#

6. Using this new dataset, what is the maximum total talk time you can achieve if you use 3  phones, and which 3 phones will you use?
