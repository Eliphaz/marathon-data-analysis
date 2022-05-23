import streamlit as st

st.title('Marathon Pacing Analysis')
st.text('By Eli Ahlander')

st.header('Why Marathons?')
st.markdown("Honestly, I couldn't tell you why I love running so much. To me, marathoning is such a spectacle. Thousands of people of all ages and shapes paying money to run outside for extended periods of time? A large frontal lobe has its flaws I suppose.")
st.markdown("To begin my analysis, I gathered multiple public data sources; historical averages and weather data from the Berlin Marathon since 1974, and pacing data from the 2015 Boston Marathon. I then used Selenium and Beautiful Soup to scrape over 40,000 entries for the 2019 Berlin Marathon. After cleaning the data using pandas, I used seaborn to visualize how age, gender, and weather affect pacing and overall finishing times.")

st.header('Age, Gender and Finishing Time')
st.image('images/af59a145-ebcc-4291-ab1c-58b1d8210b4f.png')
st.markdown("Above we can see that the first runners tend to be men in their mid 20's this wont be suprising to many, but more intresting things start to happen as we look through the data.")
#graphs and explenation
st.image('images/a9d9c711-e31e-4ef5-a823-de7fe69137f6.png')
st.markdown("This bar chart takes the average finishing time of each age. The slowest average finishing time is almost always the oldest group in the dataset.The fastest average varies depending on the year, but normally sits around 30 years old. What’s surprising is how well we maintain our fitness as we age. In this particular race (boston 2015) 18 year olds were on average slower than everyone older than them up to 57 years.")

st.header('Age, Gender and Pace')
st.markdown('In the previous scatterplot, we showed that men are typically a bit faster than women for a given age, but who paces better?')
st.image('images/2dd2783d-5f18-469d-b830-9668a1052d4b.png')
st.markdown("This chart shows the difference between the first and last half of the race. Hats off to any runners plotted below 0, as they 'negative split' or ran a faster second half. As you can see, the battle for who paces better is much closer than the battle for fastest.")
st.image('images/1eac6d04-325a-4eec-9aed-2be64dad3132.png')
st.markdown("Here we see that young men in particular pace themselves too fast in the first half, resulting in a significantly slower pace during the second half. On average, the data shows that after around 60 years old, pacing slows significantly in the second half.")

st.header('Experience and Pace')
st.image('images/99d40299-eabf-4b5f-bfe5-6fadf4d9ae24.png')
st.markdown('What we see here is that faster runners tend to have a overall split close to zero. In fact, 9 out of the last 10 world records were negative split, but only by a few seconds. This indicates that better trained runners can maintain a high intensity for a longer duration, and possibly go out at a relativly lower exertion than the average runner, in order to save energy to hold pace the final miles.')

st.header('Visualizing Every Runner')
st.image('images/boston_splits.jpg')
st.markdown("Here we can see clear grouping at common time goals. As you can see above 4 hours (341 seconds/km) the grouping gets thinner and thinner.")
st.image('images/ba60679b-b8b2-492a-8517-7fb64cead758.png')
st.markdown('On a flatter course such as Berlin, these groups seem to make it a little further, but still break apart at the end. Note the distribution of runners at the start vs at the finish.')
st.markdown("One observation is that while we may expect an even distribution, with a solid line in the fading out from the middle, what we see is that people like to run in groups, or they like to run for round number time goals. The biggest thing I noticed is that these groups only stay together till about 30k, where they begin to spread out and the grouping falls apart. Prehaps instead of chosing a round number, a better time goal might be to use Peter Reigels endurance running formula, T2=T1×(D2÷D1)1.06 where T2 is the predicted time and T1 is a previously run time, and D1 is the previously run distance.")

st.header("How Does Weather Effect Overall Times?")
st.markdown(
    'Here I used a linear regression model to see how weather effects median finishing times.')
st.image("images/7b77f1c5-b735-40fa-92d2-baf002529629.png")
st.markdown("This model predicts that for every degree celsius, the median runner will lose about 54 seconds off their marathon time, a more interesting finding is that the relationship is stronger when I not only normalize for more runners over time but also for max temperature, indicating that there is a trend in temperature as well as finishing time.")
st.image('images/9aa373bb-72e0-40f2-ab3b-c39b9573354d.png')
st.markdown("One very interesting finding was the lack of correlation between the fastest time and max temperature, indicating that the top athletes are less bothered by weather conditions.")

st.header("Insights")
st.markdown("Some takeaways from this analysis is that if you come from a cool training environment, and are going to run on a hot day, you should adjust your time goals accordingly. Also, if you want to run a fast second half, (and probably a fast race) you shouldn't follow an 18 year old male, as he's likely to blow up at the end. Rather one should find an experienced runner in her upper 30's who has a similar time goal to you, she is more likely to make it to the end without slowing down too much, this also may provide some psychological insight into what demographic is best at planning for the future, but I'm not a doctor.")
st.markdown("The biggest thing I think one should take from this report is that endurance running is a lifetime sport, and life is an endurance event in its own right. It's never too late to start, in fact, you probably would have been bad at pacing in your youth anyways. So here's to longevity, and putting some hard earned wisdom to use, in the words of English novelist George Eliot, 'It's never too late to be what you might have been.'")
