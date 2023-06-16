# valo-proj
Valorant Project and experimentation.

## Steps for Project Completion

### Valorant API Understanding
Play around with the Valorant API, get familiar with the parameters and endpoint calls

### How to Get Match Details Data
1. Figure out how to get match details
2. Write up a function that does this cleanly and saves match detail data to a json
   1. Get a list of X matches, pass that into the get_match_details endpoint 
   2. Better solution...?

### Data Cleaning
Once I have a json, find a good way to convert json to user-friendly data format, possible option is using pandas 
DataFrame. Additionally, figure out the structure of the DataFrame. One idea is to have each row for kill/death instance
and columns representing which gun, which skin, was it kill or death, location, etc...

### Data Analysis Work
Figure out the big project that I want to work on. For now, to get practice with the Valo API and using key data science
python libraries, I plan on working with strictly python for both endpoint work and data visualization.

I plan on transitioning to a bigger project where the tech stack will be javascript for the endpoint and API calls, 
and staying on python for the data processing portion where I expect I will use pandas, NumPy, and sci-kit learn. 
Project description: heatmap of where I get kills/death on each map, make it customizable: sort by whether it be kills 
vs deaths, sort by agent, sort by map, sort by avg enemy rank, etc...

### Question I Am Solving
Which Valorant skins give me better aim? Likewise, which skins lead to a poorer performance?