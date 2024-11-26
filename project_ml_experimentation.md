#### SER594: Experimentation
#### Precision Play: Innovating MLB Performance Analysis Through Data Integration
#### Om Rajesh Chauhan
#### November 25, 2024


## Explainable Records
### Record 1
**Raw Data:** 
* WAR (Actual): 8.3
* OPS (Actual): 0.987
* SLG (Actual): 0.579

Other Relevant Stats:
* Games Played: 152
* Plate Appearances: 693
* Home Runs: 39
* Batting Average (BA): 0.307
* Runs Batted In (RBI): 107
* Stolen Bases: 14

**Prediction Explanation:** Mookie Betts is known for the combination of contact, power, and defense. The high WAR represents his value both offensively and defensively. His batting average and power-39 HRs-drive his OPS, making him a well-rounded offensive player. The predicted WAR, OPS, and SLG should reflect these qualities. That should be reasonable if the model predicts similar or somewhat lower numbers, considering Betts' general performance, but any large deviation would have to be investigated as far as features are chosen that could not properly represent his full abilities.



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

**Prediction Explanation:** Ronald Acuña Jr. had a season where the elite power-41 HR-was complemented by exceptional base-running skills, having swiped 73 SBs. The OPS and SLG should reflect the combo of speed and power, reflected in his high WAR. Model-predicted WAR, OPS, and SLG should be reflective of those contributions made. With the strong balance between power and speed for Acuña, he is considered a top-tier player, and the model should ideally predict values as close as possible to the actual numbers. Large deviations from the actual figures would need to be justified by analyzing which features are influencing the predictions.

## Interesting Features
### Feature A
**Feature:** Batting Average (BA)

**Justification:** BA is a base offensive statistic that calculates how well players reach a base by hitting the ball. In general, a high BA-like 0.337 for Acuña and 0.307 for Betts-would have a good correlation with OPS and SLG because a player who continually hit would have high rates on-base and slugging percentages. At the same time, when speaking about WAR, a higher BA automatically increases the contribution made by a player to his team's success. We would thus anticipate that the model relies most heavily on BA when predicting OPS and WAR.

### Feature B
**Feature:** Home Runs (HR)

**Justification:** Home Runs are a major contributor to the player's slugging percentage, SLG, which directly contributes to OPS. A player with a high number of HRs, like Acuña with 41 and Betts with 39, has more power and results in higher run production, thus giving way to a higher SLG and WAR. The model should consider HR as a robust indicator of offensive output, especially for predictions concerning SLG and OPS.

## Experiments 
### Varying A (Batting Average)
**Prediction Trend Seen:** With an increase in Batting Average (BA), we find that the model produces greater values for both OPS and WAR. This is as we'd expect, since BA should tell us how often a player manages to get on base consistently, thereby contributing towards the offensive production of his team. The model's prediction seems to align with this, showing a positive relationship between BA and the target metrics.

### Varying B (Home Runs)
**Prediction Trend Seen:** If Home Runs (HR) are increased, the model predicts a steep rise in SLG, and by extension, OPS. This makes intuitive sense, since HRs are, by far and away, the largest contributor to SLG. WAR also rises slightly, given the correlation between power hitting and overall contribution to the team. The model uses HR as an important factor for predicting SLG and OPS.

### Varying A and B together
**Prediction Trend Seen:** The model would predict that when BA and HR are increased together, there will be even stronger increases in OPS and WAR. Players with both a high BA and high HR are few but very valuable; this is because they can both reach base consistently and hit for power. This synergy ensures that the overall offensive contributions become higher, and the model reproduces such a dynamic rather well by predicting that players with high values in both metrics will have superior overall performance.


### Varying A and B inversely
**Prediction Trend Seen:** When BA and HR are opposites, the model predicts players with a high BA but lower HR will have a higher OPS than players with a low BA but high HR. In terms of WAR, though, the high-HR/low-BA players might still contribute a great deal because power hitters tend to drive in more runs. The model correctly reflects this trade-off, yet a marked depreciation of predicted values occurs for those players who are only good at one of the skills.
