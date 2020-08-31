df=None

area_under_directory='Area_Under_Curve/'

count=0

for filename in os.listdir(area_under_directory):
    df=pd.read_csv(area_under_directory + filename)
    if count == 0:
        yearly_final = df
    else:
        yearly_final=pd.concat([yearly_final,df])
    count += 1


plt.figure(figsize=(20, 9))

sns.set(font_scale=2)
sns.set_style("whitegrid")

ax= sns.catplot(x="Snow_Patch", y="AUC", hue="Year", data=yearly_final,
                 kind="bar",order=["An_Stuc","Carn_na_Caim",
                                                    "Coire_Cruach_Sneachda",
                                                    "Beinn_Mhanach","Gael_Charn",
                                                   "Creag_Meagaidh","An_Riabhachan",
                                                   "Beinn_a_Bhuird","Coire_Domhain",
                                                   "Nevis_Gullys"],height=15, aspect=1.5,
               palette=sns.color_palette(['firebrick', 'darkorchid', 'maroon', 'steelblue']))


ax.set_xticklabels(rotation=45)



ax.set(ylabel='Approximate Seasonal Area (m$^2$)(AUC)')

plt.title('Melt Season (MJJASO) Total Area 2017-2020',fontsize=30)

