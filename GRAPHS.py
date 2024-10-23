import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#First, we will load the CSV file
file_path ='MoviesOnStreamingPlatforms.csv'

# Next we will update with the local file
movies_data = pd.read_csv(file_path)

# we will clean the rotten tomatoes scores and convert it to numeric
movies_data['Rotten Tomatoes'] =movies_data['Rotten Tomatoes'].str.replace('/100','')
movies_data['Rotten Tomatoes'] =pd.to_numeric(movies_data['Rotten Tomatoes'],errors='coerce')

#In the next step, we will filter data for both Netflix and Disney+
netflix_data = movies_data[movies_data['Netflix']==1]
disney_data = movies_data[movies_data['Disney+']==1]

# Next, we will drop NA values for the Rotten Tomatoes Score
netflix_rt_clean = netflix_data['Rotten Tomatoes'].dropna()
disney_rt_clean = disney_data['Rotten Tomatoes'].dropna()

#We will get the age statistics for this next step
netflix_age_stats = netflix_data['Age'].value_counts().reset_index()
disney_age_stats = disney_data['Age'].value_counts().reset_index()
netflix_age_stats.columns = ['Age','Count']
disney_age_stats.columns = ['Age','Count']

#Next we will Plot the following graphs
# 1. Bar Plot-Age Distribution for Netflix
bar_netflix = px.bar(netflix_age_stats,x='Age',y='Count',
                     title='Age Distribution of Netflix Movies',
                     labels={'Count':'Number of Movies','Age':'Age Restriction'},
                     color='Age')

# 2.Bar Plot-Age Distribution for Disney+
bar_disney = px.bar(disney_age_stats,x='Age',y='Count',
                    title='Age Distribution of Disney+ Movies',
                    labels={'Count':'Number of Movies','Age':'Age Restriction'},
                    color='Age')

# 3.Histogram-Rotten Tomatoes Scores for Netflix
hist_netflix = px.histogram(netflix_rt_clean,nbins=20,
                            title='Rotten Tomatoes Score for Netflix Movies',
                            labels={'value':'Rotten Tomatoes Score','count':'Frequency'},
                            color_discrete_sequence=['skyblue'])
hist_netflix.update_layout(xaxis_title='Rotten Tomatoes Score',yaxis_title='Frequency')

# 4.Histogram-Rotten Tomatoes Scores for Disney+
hist_disney = px.histogram(disney_rt_clean,nbins=20,
                           title='Rotten Tomatoes Scores for Disney+ Movies',
                           labels={'value':'Rotten Tomatoes Score','count':'Frequency'},
                           color_discrete_sequence=['lightgreen'])
hist_disney.update_layout(xaxis_title='Rotten Tomatoes Score',yaxis_title='Frequency')

# 5.Box Plot-Rotten Tomatoes Scores Comparison
box_plot=go.Figure()
box_plot.add_trace(go.Box(y=netflix_rt_clean,name='Netflix',marker_color='skyblue'))
box_plot.add_trace(go.Box(y=disney_rt_clean,name='Disney+',
                          marker_color='lightgreen'))
box_plot.update_layout(title='Box Plot of Rotten Tomatoes Scores',
                       yaxis_title='Rotten Tomatoes Score')

# 6.Pie Chart-Proportion of Age Categories on Netflix
netflix_age_props = netflix_age_stats.set_index('Age')['Count']
netflix_age_stats['Count'].sum()
pie_netflix =px.pie(netflix_age_stats,names='Age',values='Count',
                    title='Proportion of Age Categories on Netflix',
                    color_discrete_sequence=px.colors.sequential.Blues)

# Lastly we show the plots
bar_netflix.show()
bar_disney.show()
hist_netflix.show()
hist_disney.show()
box_plot.show()
pie_netflix.show()
