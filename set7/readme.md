TODO: Reflect on what you learned this week and what is still unclear.

### for the column:

1. describe by recording/ measuring / graphing

   1. name
   2. what the column describes
   3. how the data was mesured?
   4. is it continuous or categorical data?
      1. continuous is [ 1, 2, 3, -5.6 ]
      2. categorical is ["cat", "dog", "mouse", "food"]

   ### How to deal with the categorical data?

2. try `df["column_name"].value_countes()` to get the numbers
3. try `df["column_name"].value_counts().plot(kind="bar")` to get the distribution of the counts
   ---- I can distribute the numbers per postcode/lhd/lha
4. you need to fold the things, eg: `sydeny`, `Syd`, `Sydney`, and `SYD`, they should be the same but how to let the computer understand?
   ---- this dataset is clean, so no issues for this
   ---- but the categorical data might be too accurate, I needs to merge some of them, eg: Burwood (A) + Burwood (B) ===> Burwood
5. how to express the distribution shape of the graph?
   ---- how accurate and why this number

one problem with my dataset is the post code and the locations

for example :

notification_date 2020-01-25
postcode 2134
likely_source_of_infection Overseas
lhd_2010_code X700
lhd_2010_name Sydney
lga_code19 11300.0
lga_name19 Burwood (A)
Name: 0, dtype: object

lhd: local health district,
lga: local government area

some area are big and some are small, where can I get the detailed map?
maybe form the government or google map
