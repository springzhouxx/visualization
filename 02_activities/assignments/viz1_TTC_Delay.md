For each visualization, describe and justify: 
TTC Subway Delay Since 2025
https://open.toronto.ca/dataset/ttc-subway-delay-data/
A bar chart of subway delay counts by hour of day.
> What software did you use to create your data visualization?
Python ( pandas for data processing, matplotlib for plotting)
> Who is your intended audience? 
TTC riders, transit planners, and city officials who want to understand when subway delays are most likely to happen, so they can plan commutes or prioritize service improvements.    
> What information or message are you trying to convey with your visualization? 
The bar chart shows how the number of subway delays is distributed across the 24 hours of the day. The message here is delays aren't evenly spread out. Very few happen overnight (when service is mostly closed), then they climb sharply once service resumes, peaking around 6am, with another large clusters at 8am or from 4pm–6pm.    
> What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
I used a single solid color for the bars so the focus stays on the shape of the distribution. A bold title and clear axis labels make the chart self-explanatory. A light dashed horizontal grid helps read approximate values without clutter. I annotated the peak hour (6am) directly on the chart in a contrasting color to draw the eye to the most important point, and set x-ticks to show every hour since hourly granularity matters here. 
To make sure the data is more accurate, I also filtered to Min Delay > 0 to show the real delays, because some of the points have a delay logged but the actual minutes delayed recorded as 0, which would distort the true picture of when delays occur if left in.
> How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
The whole pipeline is written as discrete code cells in a notebook, so anyone with the same CSV and Python environment can re-run it and get an identical result. The figure is also saved to a PNG file via plt.savefig, preserving the output alongside the generating code. I also captioned the chart with its data source, so any reader can trace the visualization back to the original dataset.      
> How did you ensure that your data visualization is accessible?  
High-contrast colors, a bold readable title, and explicit axis labels will make the visualation easy to understand and get the information. The annotation is placed near the relevant bar, reducing the need to cross-reference.    
> Who are the individuals and communities who might be impacted by your visualization?  
I believe TTC riders, especially morning commuters might be impacted by this visualization since the chart highlights when they're most likely to hit delays. TTC operations staff and the City of Toronto could also use this to justify staffing or maintenance scheduling decisions around peak delay hours.    
> How did you choose which features of your chosen dataset to include or exclude from your visualization? 
I actually listed all the variables in the dataset and make a table to see what questions we can focus on. As I use TTC bascially every single day, the hours that may mostly hit delay attracts me a lot. So our goal is to focus on when delays happens. 
Once decided the goal, I used the "Time" and "Min Delay" columns. Rows with Min Delay == 0 were excluded because they didn't cause an actual delay. Other columns (line, station, delay code) were excluded since the goal was answering time of delays.  
> What ‘underwater labour’ contributed to your final data visualization product?
Cleaning before plotting: filtering zero-delay rows, parsing the "Time" string into an integer "Hour" field, and aggregating thousands of records into hourly counts via groupby. I also iterated on visual choices (colors, gridlines, annotation placement) and manually checked that the labeled peak hour matched the underlying grouped counts before finalizing.