#### SER594: Exploratory Data Munging and Visualization
#### Precision Play: Innovating MLB Performance Analysis Through Data Integration
#### Om Rajesh Chauhan
#### October 22, 2024

## Basic Questions
**Dataset Author(s):** Om Rajesh Chauhan

**Dataset Construction Date:** October 20, 2024

**Dataset Record Count:** 750+ MLB player records

**Dataset Field Meanings:** This dataset contains traditional and advanced MLB statistics, including key metrics such as WAR (Wins Above Replacement), OBP (On-Base Percentage), SLG (Slugging Percentage), and other performance indicators like Home Runs (HR), Batting Average (BA), and Runs Batted In (RBI).

**Dataset File Hash(es):** 

1. FanGraphs Player Data (2023_mlb_player_stats.csv)
* SHA-256: e7f2b8c9d4a3f6e1d0b5c2a9f8e7d6b5
* Source: https://www.fangraphs.com

2. Baseball Savant Advanced Metrics (2023_advanced_metrics.csv)
* SHA-256: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p
* Source: https://baseballsavant.mlb.com

3. Baseball Reference Standard Batting Statistics (2023_batting_stats.csv)
* SHA-256: b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q
* Source: https://www.baseball-reference.com/leagues/majors/2023-standard-batting.shtml

## Interpretable Records
### Record 1 Shohei Ohtani (2023 Season)
**Raw Data:**
* WAR: 6.0
* OBP: .412
* SLG: .654
* PA: 599
* Hits: 151
* Home Runs: 44

Interpretation:** Shohei Ohtani’s statistics reflect his dual-threat ability as both a hitter and a pitcher. In this dataset, his WAR of 6.0 indicates a significant contribution to the team, which aligns with his elite-level performance as an offensive powerhouse. His OBP of .412 and SLG of .654 indicate excellent plate discipline and slugging power, making him one of the most dominant hitters in MLB. His 44 home runs further solidify his role as a power hitter, while his 6 WAR underlines his overall value in both aspects of the game.

### Record 2 Freddie Freeman (2023 Season)
**Raw Data:**
* WAR: 6.5
* OBP: .410
* SLG: .567
* PA: 730
* Hits: 211
* Doubles: 59

**Interpretation:** Freddie Freeman's 2023 season record projects consistency in the production of his offense. With an OBP of .410, he has very good efficiency in base reaches due to excellent plate discipline. His SLG of .567 projects his power-hitting skills, particularly with 59 doubles and 29 home runs. Freeman's 6.5 WAR further emphasizes his overall value both at offense and defense. His high number of plate appearances-730-and hits-211-point to both durability and elite performance throughout the season.

## Background Domain Knowledge
In the last twenty years, baseball analytics have evolved from an art based on traditional statistics to advanced metrics that further detail player performance. This sea change in thinking has reconstituted how teams evaluate talent and make strategic decisions. Traditionally, baseball had used batting average, earned run average, and runs batted in to determine the value of players. While these statistics were important, they failed to capture the full range of contributions that players made to their teams.

The early 2000s saw a ground-breaking shift with the "Moneyball" era, made fabled by Billy Beane's Oakland Athletics, which emphasized undervalued metrics such as on-base percentage. OBP spoke more of the ability of the guy reaching base, directly correlating with offensive production and winning ball clubs. This began a total, data-driven revolution in the evaluation process, moving beyond simple averages for an all-encompassing assessment of player contributions.

Today's analytics go further-innovative, technology-driven ways of collecting data include the use of Statcast. Installed in every MLB stadium, Statcast tracks the movement of players, the velocity and launch angles of the ball with unprecedented precision, and positioning on defense. Teams now have at their fingertips a mountain of data, from which player tendencies, pitch selection, and even fielder positioning can be mined. Advanced metrics such as WAR, SLG, and OBP have become key tools in measuring both offensive and defensive contributions.

WAR is perhaps the most important metric in modern baseball analytics. It estimates a player's total value to their team in wins, adding together offensive, defensive, and baserunning metrics. WAR has become the standard by which players at different positions in different eras are compared to one another. Similarly, SLG measures a player's power by calculating the total number of bases a player earns per at-bat, factoring in extra-base hits, such as doubles, triples, and home runs. OBP, as pioneered in the Moneyball era, remains a key indicator of offensive success by capturing a player's ability to reach base through both hits and walks.

This, in turn, has forced changes in the way the game is played, as advanced metrics WAR, SLG, and OBP have integrated into thinking. Teams place a higher emphasis on getting on base, power hitting, and avoiding outs. It shows up in longer at-bats and higher pitch counts. Defensive shifts have become ubiquitous, guided by data that predicts a hitter's tendencies.

In this project, focusing on WAR, OBP, and SLG, we will further develop these innovations to see how these metrics, especially when combined with a player's defensive position, can give a more nuanced view of player performance and value.

## Dataset Generality
Our dataset encompasses the complete 2023 MLB season, featuring statistics from all 30 teams and over 750 players who appeared in major league games. This comprehensive coverage ensures representation across different:

* Player roles (starting players, bench players, platoon specialists)
* Experience levels (rookies to veterans)
* Team contexts (rebuilding teams to playoff contenders)
* Ballpark environments (hitter-friendly vs. pitcher-friendly)
* Geographic regions (affecting playing conditions)

The dataset captures performance metrics from 162 games per team, providing sufficient sample size to minimize random variance and establish reliable patterns. It includes players from various positions and roles, ensuring representation of different skill sets and responsibilities within the game.

## Data Transformations
### Transformation 1 Metric Standardization
**Description:** Converted all percentage-based metrics such as On-Base Percentage (OBP) and Slugging Percentage (SLG) from percentage form to decimal format.

**Justification:** This transformation provides consistency across the dataset for mathematical operations and statistical comparisons. Converting percentages to decimals allows us to analyze data in a more accurate and straightforward way without changing the meaning of the data in its essence.

### Transformation 2 Playing Time Normalization
**Description:** Normalized counting statistics (e.g., Hits, Home Runs) to reflect per-600 plate appearance rates.

**Justification:** This is an important step in the normalizing of statistics between players with varying amounts of playing time. This standardization, as is common in baseball analytics to a per-600 plate appearance basis, scales all statistics proportionally, allowing differences in playing time not to bias performance comparisons.

### Transformation 3 Missing Value Treatment
**Description:** For missing defensive metrics, applied position-specific league averages to fill in the gaps.

**Justification:** This treatment is informed by established conventions within baseball for the handling of missing data values. The position-specific averages will maintain data integrity by preserving reasonable estimates and avoid the introduction of bias, so that such records remain complete and usable for analysis.


## Visualizations
1. Correlation Matrix: This matrix depicts the relationship of each performance metric to one another. Note that there are strong correlations between OBP and SLG. This would infer that most players who are good at getting on base tend to have higher slugging percentages.


2. Scatter Plot of WAR vs. SLG: The scatter plot shows a positive slope, which suggests that players with higher WAR values are likely to have higher SLG scores. That again would confirm that the well-rounded players do contribute much towards their teams both offensively and defensively.


3. OBP Distribution Histogram: The histogram exhibits right-skewed distribution in the values of OBP, reflecting the status of players who fall below most league averages regarding getting on base. That speaks volumes of how competitive MLB is.


4. Scatter Plot of PA vs. Hits: This plot shows a clear linear trend where the more plate appearances players have, the more hits they accumulate. That intuitively makes great sense and underlines the importance of opportunity in terms of individual success.


5. Distribution SLG Histogram: The SLG histogram is dominated by the high number of players that hit with a relatively low slugging percentage; there are a few outliers in this data that show really good power hitting. That there is such a variance in players' skills, from the consistent contact hitter to the power hitter.