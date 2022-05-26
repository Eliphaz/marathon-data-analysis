import streamlit as st
import pandas as pd
import plotly.express as px


boston_2015 = pd.read_csv('master_boston_2015')
all_ages_avg = pd.read_csv('all_ages_avg_boston_2015')
age_group_avg = pd.read_csv('age_group_avg_boston_2015')
berlin_2019 = pd.read_csv('clean_berlin_2019')
berlin_weather = pd.read_csv('berlin_weather_master')

finishing_times_scatter = px.scatter(boston_2015.iloc[::25], x='Time in Seconds', y='Age', color='Sex', trendline='ols', hover_data=["Name", "Country"], title='Finishing Times at Boston 2015', labels={
    'Time in Seconds': 'Finishing Time'
})
finishing_times_scatter.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=[7200, 9000, 10800, 12600, 14400, 16200, 18000, 19800, 21600],
        ticktext=['2:00', '2:30', '3:00', '3:30',
                  '4:00', '4:30', '5:00', '5:30', '6:00']
    )
)

avg_by_age_bar = px.bar(all_ages_avg, x='Age', y='Average Time',
                        color='Average Time', title='Average finishing times at Boston 2015')
avg_by_age_bar.update_layout(
    yaxis=dict(
        tickmode='array',
        tickvals=[0, 1800, 3600, 5400, 7200, 9000, 10800,
                  12600, 14400, 16200, 18000, 19800, 21600],
        ticktext=['0:00', '0:30', '1:00', '1:30', '2:00', '2:30',
                  '3:00', '3:30', '4:00', '4:30', '5:00', '5:30', '6:00']
    )
)

split_times_scatter = px.scatter(boston_2015.iloc[::27], x='first/second_half_split', y='Age', color='Sex', hover_data=["Name", "Country"], title='Split Times at Boston 2015', labels={
    'first/second_half_split': 'Overall Split'
})

experience_scatter = px.scatter(berlin_2019.iloc[::50], x='Net_time', y='overall_split', color='Sex', title='Split Times at Berlin 2019', trendline='ols', labels={
    'Net_time': 'Finishing Time',
    'overall_split': 'Overall Split'
}, hover_data=['First_Name', 'Last_Name', 'Country'])
experience_scatter.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=[7200, 9000, 10800, 12600, 14400,
                  16200, 18000, 19800, 21600, 23400, 25200],
        ticktext=['2:00', '2:30', '3:00', '3:30', '4:00',
                  '4:30', '5:00', '5:30', '6:00', '6:30', '7:00']
    )
)

split_times_avg_bar = px.bar(age_group_avg, x='Age', y='Average split', color='Sex', barmode='group', title='Average split times at Boston 2015', labels={
    'Average split': 'Average overall split (seconds)'
})

weather_median_scatter = px.scatter(
    berlin_weather, x='MAX_TEMP_C', y='median_time', trendline='ols', title='Relationship Between Median Finishing Time and Temperature', labels={
        'MAX_TEMP_C': 'Normalized Max Temp on race day (celcius)',
        'median_time': 'Normalized Median Finishing Time (seconds)'
    })

weather_fastest_scatter = px.scatter(
    berlin_weather, x='MAX_TEMP_C', y='fastest', trendline='ols', title='Relationship Between Fastest Finishing Time and Temperature', labels={
        'MAX_TEMP_C': 'Normalized Max Temp on race day (celcius)',
        'fastest': 'Normalized Fastest Finishing Time (seconds)'
    })

st.title('Marathon Pacing Analysis')
st.text('By Eli Ahlander')

st.header('Why Marathons?')
st.markdown("Honestly, I couldn't tell you why I love running so much. To me, marathoning is such a spectacle. Thousands of people of all ages and shapes paying money to run outside for extended periods of time? A large frontal lobe has its flaws I suppose.")
st.markdown("To begin my analysis, I gathered multiple public data sources; historic finishing averages and weather data from the Berlin Marathon since 1974, and pacing data from the 2015 Boston Marathon. I then used Selenium and Beautiful Soup to scrape over 40,000 entries for the 2019 Berlin Marathon. After cleaning the data using pandas, I used plotly to visualize how age, gender, and weather affect pacing and overall finishing times.")

st.header('Age, Gender and Finishing Time')
st.plotly_chart(finishing_times_scatter)
st.markdown("Above we can see that the first runners tend to be men in their upper 20's this wont be suprising to many, but more intresting things start to happen as we look through the data.")
#graphs and explenation
st.plotly_chart(avg_by_age_bar)
st.markdown("This bar chart takes the average finishing time of each age. The slowest average finishing time is almost always the oldest group in the dataset. The fastest average varies depending on the year, but normally sits around 30 years old. What’s surprising is how well we maintain our fitness as we age. In this particular race (boston 2015), 18 year olds were on average slower than everyone older than them up to 57 years.")

st.header('Age, Gender and Pace')
st.markdown('In the previous scatterplot, we showed that men are typically a bit faster than women for a given age, but who paces better?')
st.plotly_chart(split_times_scatter)
st.markdown("This chart shows the difference between the first and last half of the race. Hats off to any runners plotted below 0, as they 'negative split' or ran a faster second half. As you can see, the battle for who paces better is much closer than the battle for fastest.")
st.plotly_chart(split_times_avg_bar)
st.markdown("Here we see that young men in particular pace themselves too fast in the first half, resulting in a significantly slower pace during the second half. On average, the data shows that after around 60 years old, pacing slows significantly in the second half.")

st.header('Experience and Pace')
st.plotly_chart(experience_scatter)
st.markdown('What we see here is that faster runners tend to have a overall split close to zero. This means that they ran a first half in about the same time as their second, if not faster. In fact, 9 out of the last 10 world records were negative split, but only by a few seconds. This indicates that better trained runners can maintain high intensity for a longer duration than average trained runners. This also suggests that faster runners go out at a relativly lower exertion than the average runner, in order to save energy to hold pace the final miles.')

st.header('Visualizing Every Runner')
st.image('images/boston_splits.jpg')
st.markdown("Here we can see clear grouping at common time goals. As you can see above 4 hours (341 seconds/km) the grouping thins out.")
st.image('images/ba60679b-b8b2-492a-8517-7fb64cead758.jpg')
st.markdown('With the Berlin Marathon course having a leveled terrain, pace groups seem to make it slightly further, but still break apart at the end. Note the distribution of runners at the start vs at the finish.')
st.markdown("One observation is that while we may expect an even distribution, with a solid line in the fading out from the middle, what we see is that people like to run in groups, or they like to run for round number time goals. The biggest thing I noticed is that these groups only stay together till about 30k, where they begin to spread out and the grouping falls apart. Prehaps instead of chosing a round number, a better time goal might be to use Peter Reigels endurance running formula, T2=T1×(D2÷D1)1.06 where T2 is the predicted time and T1 is a previously run time, and D1 is the previously run distance.")

st.header("How Does Weather Effect Overall Times?")
st.markdown(
    'Here I used a linear regression model to see how weather has effected median finishing times historically at the Berlin Marathon. The results of the spearmanr test on these variables result in a strong correlation of .76 with a highly significant p value of 1.1e-09')
st.plotly_chart(weather_median_scatter)
st.markdown("This model predicts that for every increase in degrees celsius, the median runner will lose about 54 seconds off their overall marathon time. The relationship is stronger when normalizing for more runners over time. More intresting is this is also the case when normalizing for max temperature over time, indicating that there is a trend in temperature as well as finishing time.")
st.plotly_chart(weather_fastest_scatter)
st.markdown("One very interesting finding was the lack of correlation between the fastest time and max temperature, indicating that the fastest athletes are less bothered by warmer weather conditions.")

st.header("Insights")
st.markdown("Fastest runners are most likely to be men in their upper 20s. But, if you want to run a fast second half, (and probably a fast race) you shouldn't follow an 18 year old male, as he's likely to slow down towards the end. Rather one should find an experienced female runner in her upper 30's who has a similar time goal to you, she is more likely to make it to the end without slowing down too much. There is also an indicated correlation with experience in running and pace times. More experienced runners tend to have a more even split than those who are less experienced. Weather proved to have an effect on overall pace times, as the linear regression model indicated that the warmer the temperature got, the slower the median runner will finish their marathon. Indicating that if you come from a low temperature training environment, and plan to race on a warm day, you should adjust your time goals accordingly.")
st.markdown("The biggest thing I think one should take from this report is that endurance running is a lifetime sport, and life is an endurance event in its own right. It's never too late to start, in fact, you probably would have been bad at pacing in your youth anyways. So here's to longevity, and putting some hard earned wisdom to use, in the words of English novelist George Eliot, 'It's never too late to be what you might have been.'")
st.subheader('Limitations of this Data')
st.markdown("It should be noted that both of these datasets are about 60% male which can skew the visualizations a bit. However both datasets are large enough that I believe much analysis can still be made on both genders. Also as the weather is concerned, I'm sure at some point colder temperatures will have a negative effect on finishing times, but the coldest max temperature on the day of the Berlin Marathon was 8 degrees celsius or 46 fahrenheit, which is a bit chilly but still considered good running weather by many.")
