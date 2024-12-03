#### SER594: Experimentation
#### Precision Play: Innovating MLB Performance Analysis Through Data Integration
#### Om Rajesh Chauhan
#### November 25, 2024


## Explainable Records
### Record 1
**Raw Data:** 
* WAR (Actual): 8.3
* OBP (Actual): 0.408
* SLG (Actual): 0.579

Other Relevant Stats:
* Games Played: 152
* Plate Appearances: 693
* Home Runs: 39
* Batting Average (BA): 0.307
* Runs Batted In (RBI): 107
* Stolen Bases: 14

**Prediction Explanation:** Mookie Betts is a player who excels both offensively and defensively; that is why his WAR is very high. His 0.408 OBP indicates excellent plate discipline, meaning he generally reaches base frequently. The 0.579 SLG reflects his strong power hitting, with a total of 39 home runs hit. The model should predict values for WAR, OBP, and SLG close to these actual numbers. This would require further investigation into identifying what features are not fully capturing Betts' all-around skill set if there is a significant deviation.


### Record 2
**Raw Data:** 
* WAR (Actual): 8.2
* OPS (Actual): 1.012
* SLG (Actual): 0.596

Other Relevant Stats:
* Games Played: 159
* Plate Appearances: 735
* Home Runs: 41
* Batting Average (BA): 0.337
* Stolen Bases: 73

**Prediction Explanation:** Ronald Acuña Jr. had an outstanding season, combining elite power (41 home runs) with exceptional speed (73 stolen bases). His On-Base Percentage (OBP) of 0.416 indicates his ability to get on base frequently, while his Slugging Percentage (SLG) of 0.596 reflects his power-hitting prowess. The model’s predictions for WAR, OBP, and SLG should capture both his speed and power contributions. Large discrepancies between predicted and actual values would need analysis to determine which features may not have fully captured Acuña's unique skill set.


## Interesting Features
### Feature A
**Feature:** Batting Average (BA)

**Justification:** BA is a fundamental offensive statistic that measures how well players hit to get on base. A high BA—like 0.337 for Acuña and 0.307 for Betts—often correlates with other important metrics like On-Base Percentage (OBP) and Slugging Percentage (SLG). Players with higher BA are likely to reach base more frequently, which directly contributes to their OBP. Additionally, since BA impacts a player's overall offensive production, a higher BA will also influence a player’s WAR, reflecting their overall contribution to team success. Therefore, we expect the model to rely heavily on BA when predicting OBP and WAR.

### Feature B
**Feature:** Home Runs (HR)

**Justification:** Home Runs are a significant factor in a player’s Slugging Percentage (SLG), as they represent the highest value hit a player can achieve. For players like Acuña (41 HR) and Betts (39 HR), HRs are key drivers of offensive production and influence their SLG and WAR. A high HR count also helps improve a player's ability to score or drive in runs, thus boosting their contribution to the team's overall success. The model should treat HR as a key indicator for predicting SLG and, to a lesser extent, OBP, while playing a crucial role in predicting overall offensive output reflected in WAR.

## Experiments 
### Varying A (Batting Average)
**Prediction Trend Seen:** With an increase in Batting Average (BA), the model predicts greater values for both OBP and WAR. This makes sense, as BA directly affects how often a player gets on base, which in turn influences OBP. A higher OBP means the player is contributing significantly to the team’s offensive success. The model accurately captures this relationship, showing a positive correlation between BA and the target metrics (OBP and WAR).

### Varying B (Home Runs)
**Prediction Trend Seen:** It increases the SLG, with great increments in a manner expected from a higher-scoring hit type like HRs. Correspondingly, it increases in terms of power production toward higher WARs since power hitters are normally very valuable toward team outcomes. SLG and WAR increase, accordingly, in accordance with the role that home runs have as leading indicators of offensive impact.

### Varying A and B together
**Prediction Trend Seen:** When both Batting Average (BA) and Home Runs (HR) increase, the model predicts a significant rise in both OBP, SLG, and WAR. Players who excel in both areas (high BA and high HR) are rare but extremely valuable because they combine consistent hitting with power. The model accurately reflects this synergy, predicting that players with high values in both metrics will have outstanding overall offensive performance and team contributions.

### Varying A and B inversely
**Prediction Trend Seen:** When BA and HR vary inversely (e.g., high BA but low HR or vice versa), the model predicts that players with a high BA but fewer HRs will have a higher OBP compared to those with a low BA but many HRs. However, power hitters with a lower BA but more HRs may still contribute significantly to SLG and WAR because HRs provide substantial run production. The model captures this trade-off, but there is a clear reduction in predicted values for players excelling in only one of these areas (either BA or HR), rather than both.
