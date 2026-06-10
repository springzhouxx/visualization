# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      Good Example: Obesity vs Education by Andy Kriebel 
      https://public.tableau.com/app/profile/andy.kriebel/viz/ObesityvsEducation/Intro
      Reason: This visualization examines the relationship between education attainment and obesity rates across U.S. states, guiding viewers through multiple tabs. The author is a well-known Tableau Public figure.
      1. Accurate encoding: The scatter plot excels by utilizing accurate, position-based encoding, which significantly minimizes cognitive load (Lecture 4 Slide 42). This is very important especially in causal effect research. Human vision decodes spatial positioning along a common scale with the highest degree of precision. By mapping the two variables on a familiar 2D axis, the design achieves high perceptual message clarity, allowing viewers to instantly identify the strong negative correlation.
      2. The design acts as a powerful rhetorical object (D'Ignazio & Klein, 2020). The Story format walks viewers step by step through the data, making the persuasive and exploratory purpose clear. Rather than dumping all the visual variables onto a single, overwhelming dashboard, the storyboard acts as a guided rhetorical argument. It begins by establishing geographic context (the maps) to answer where the issue is concentrated. Once the viewer is oriented, it transitions to the scatter plot to answer how the variables interact systemically. The story format walks viewers step by step through the data, making the persuasive and exploratory purpose clear.
      3. Good balance of aesthetic/substantive/perceptual by prioritizing substantive accuracy and perceptual clarity over unnecessary aesthetic flair. The visualization maintains a clean layout, uses simple geometric shapes, and completely avoids unnecessary 3D distortion. The minimalist aesthetic lowers the barrier to entry, ensuring that viewers with varying levels of quantitative literacy can engage with the data without being distracted by "chart junk."

      Bad Example：CFP Exam Topics by US New Education
      https://public.tableau.com/app/profile/u.s.news.education/viz/CFPExamTopics/Dashboard1
      Reason: This visualization uses a single pie chart to display the topic weight breakdown of the CFP exam across 8 categories. I think it is a bad example,
      1. Pie chart with 8 slices relies on inaccurate encoding. Pie charts use angle and area encoding, as we learned from the lecture, it is less accurate than position-based encoding. In this example, with 8 similarly-sized slices, viewers cannot reliably distinguish which topic holds a greater proportion.
      2. Truncated labels increase extraneous cognitive load (Lecture 4 Slides 41-42). Every legend label is cut off with ellipses in this example. Viewers need to click the label to get the full category names. Thus, the message cannot be clearly conveyed, creating high cognitive friction and turning the act of reading the chart into a frustrating matching game.
      3. No percentage values and no data source citation (Lecture 4 Slides 26, 45-46): The chart omits numerical labels on each slice, so viewers have no way to accurately read the proportions.There is also no data source citation, violating Kennedy et al.'s (2016) provenance convention. the visualization lacks provenance rhetoric (Slide 46). Additionally, because data visualizations are non-neutral rhetorical objects (D'Ignazio & Klein, 2020), they must establish authority and trust with the audience. This complete absence of provenance severely undermines the chart's substantive accuracy and trustworthiness.
      ```
    - How could this data visualization have been improved?  
      ```
      Good Example:
      1. Strengthen Provenance Rhetoric: Adding a visible data source citation would immediately signal academic trustworthiness and authority to the viewer; The slope graph is a less common chart type, a brief one-line annotation explaining would also reduce cognitive load for audiences unfamiliar with this format.
      2. Incorporate the Gestalt Principle of Similarity: The scatter plot currently uses uniform coloring for all data points. The visualization could be improved by color-coding the circles based on geographic regions. This would introduce the principle of similarity, allowing viewers to decode a secondary layer of regional patterns.

      Bad Example: 
      1. Replace the pie chart with a horizontal bar chart sorted by percentage. Bar charts use position-based encoding, which is more accurate, making comparison across 8 categories immediate. Sorting from largest to smallest would directly serve the intended purpose: helping students prioritize study time. 
      2. Display full category names and add percentage labels on each bar, and include a data source citation. Full labels eliminate the truncation problem and reduce extraneous cognitive load. Percentage values satisfy the substantive quality standard. A source citation fulfils the provenance convention, signalling transparency and trustworthiness to the viewer.
      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 -  2026-06-09`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
