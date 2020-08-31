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



plt.figure(figsize=(14, 9))

sns.set(font_scale=1.2)
sns.set_style("whitegrid")

ax = sns.scatterplot(x="Year", y='AUC', data=yearly_final,hue=yearly_final.Snow_Patch.tolist(),legend='full', palette="deep", marker = 's',s=70)

ax = sns.lineplot(x="Year", y='AUC', data=yearly_final,hue="Snow_Patch",legend=None, palette="deep")


for x in range (0,11):


    ax.lines[x].set_linestyle(":")


ax.set_xticks([2017,2018,2019,2020])
ax.set_xticklabels(['2017','2018','2019','2020',])

ax.set(xlabel='Year)', ylabel='Approximate Seasonal Area (m$^2$)(AUC)')

plt.title('Melt Season (MJJASO) Total Area 2017-2020',fontsize=15)

