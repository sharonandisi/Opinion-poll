# Gatundu South Opinion Poll Report
*Updated: November 18, 2025*

## Data & Method
- Source: `responses.csv` (n = 660). Cleaning steps included column normalization, timestamp parsing, dropping all-null fields (`Score`, `Other_Comments`), categorical standardization, alias grouping for parties/leaders, and tidying multi-select responses. The cleaned table is saved as `cleaned_responses.csv` and the full workflow lives in `gatundu_poll_analysis.ipynb`.
- Charts exported to `figures/` are referenced throughout this summary.

## Key Findings
1. **MP Job Performance & Mandate**
   - Ratings skew negative: 27% "Very Poor", 25% "Poor", 28% "Fair", 17% "Good", 3% "Excellent".
   - Only 21% want the MP re-elected; 58% say "No" and 22% are undecided.
   - Ngenda ward is the harshest (51% "Very Poor"), while Kiganjo records the highest outright rejection of re-election at 41%.
   - Gender split: 63% of men oppose re-election versus 47% of women. Youth (18–24) are the lone cohort favoring re-election (62% "Yes").
   - See `figures/mp_performance_by_ward.png`, `figures/reelection_by_gender.png`, and `figures/reelection_by_age.png`.

2. **Political Alignment & Vote Intent**
   - Party support: Undecided/None (37%), Jubilee (21%), DCP (19%), UDA (15%), ODM (5%).
   - Trusted leaders: Fred Matiangi (27%), Kalonzo Musyoka (22%), Rigathi Gachagua (14%), William Ruto (11%), Undecided/None (31%).
   - Preferred candidate today: Undecided (42%), Njinji Murigi (27%), Kungu Kibathi (15%), Moses Kuria (8%).
   - Charts: `figures/party_support.png`, `figures/trusted_leaders.png`.

3. **National Mood**
   - President Ruto performance: 38% "Poor", 22% "Very Poor", 30% "Fair", 9% "Good", 1% "Excellent".
   - 60% believe the country is on the wrong track, 29% are unsure, 11% say "Yes". Positive direction sentiment is confined to respondents who rate the president Good/Excellent.
   - Chart: `figures/national_mood_heatmap.png`.

4. **Issue Agenda & Qualitative Signals**
   - Top concerns (mentions): Education (401), Healthcare (331), Roads & Infrastructure (327), Jobs & Youth Empowerment (297), Agriculture/Farming (236).
   - Desired MP qualities: Development record (582), Honesty (264), Accessibility (116), Education level (29), Party affiliation (15).
   - Charts: `figures/top_voting_issues.png`, `figures/important_mp_qualities.png`.

## Strategic Implications
- **Service Delivery Narrative**: Campaign messaging must prioritize education, healthcare, infrastructure, and youth jobs. These four issues cover >75% of all mentions and cut across wards.
- **Trust & Accountability**: The incumbency backlash centers on perceived non-performance and honesty gaps. Demonstrating tangible development achievements and openness is critical.
- **Youth Opportunity**: Younger voters are comparatively optimistic about re-electing the MP; targeted youth employment and empowerment initiatives could convert them into vocal advocates.
- **Opposition Fragmentation**: High undecided rates on party choice and candidate preference indicate room for persuasion. Jubilee and DCP have meaningful footholds, but no group commands a majority.
- **National Discontent**: Align constituency messaging with local delivery rather than national government performance, given negative Ruto ratings and pessimism about Kenya's direction.

## Next Steps
1. Validate insights with qualitative FGDs in Ngenda (most dissatisfied) and Ndarugu (largest sample).
2. Layer voter-file data to understand turnout potential of undecided and pro-incumbent youth clusters.
3. Track shifts by re-running the poll monthly and appending new CSVs to the notebook pipeline (simply drop the file into the project and rerun `gatundu_poll_analysis.ipynb`).
