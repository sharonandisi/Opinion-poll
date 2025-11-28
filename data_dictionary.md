# Data Dictionary (Sanitized Dataset)

This table documents the columns expected by `gatundu_poll_analysis.ipynb`. Only include these fields in any dataset you publish—remove or mask personally identifiable information before sharing.

| Column | Type | Description | Notes / Privacy Guidance |
| --- | --- | --- | --- |
| `timestamp` | datetime | Original survey submission timestamp. | Round to date (`survey_date`) before sharing externally if precise times could re-identify respondents. |
| `survey_date` | date | Derived date portion of `timestamp`. | Safe to publish. |
| `survey_weekday` | string | Day name derived from `timestamp`. | Safe to publish. |
| `gender` | categorical | Respondent gender (standardized title case). | Do not combine with other rare attributes if sample size <5. |
| `age_group` | categorical | Age bracket (e.g., `18-24`, `25-34`). | Ensure bins are broad enough to protect privacy. |
| `education_level` | categorical | Highest education level completed. | Collapse sparse categories before sharing. |
| `employment_status` | categorical | Employment segment (Employed, Self-employed, Student, etc.). | Same as above. |
| `ward` | categorical | Respondent ward within Gatundu South. | Keep only if each ward has ≥10 respondents; otherwise aggregate. |
| `mp_performance_rating` | categorical | Likert scale rating of MP job performance. | Values: `Very Poor`, `Poor`, `Fair`, `Good`, `Excellent`. |
| `mp_represents_interests_effectively` | categorical | Whether the MP represents respondent interests. | Values: `Yes`, `No`, `Unsure`. |
| `mp_should_be_reelected` | categorical | Re-election support (`Yes`, `No`, `Undecided`). | — |
| `supported_political_party` | string | Raw text party preference. | Keep private; use `supported_party_clean` for publication. |
| `supported_party_clean` | categorical | Normalized party preference (`UDA`, `Jubilee`, `Undecided/None`, etc.). | Safe to publish in aggregate. |
| `trusted_political_leader` | string | Raw leader preference text. | Keep private; use normalized field. |
| `trusted_leader_clean` | categorical | Normalized leader preference (e.g., `Fred Matiangi`). | Publish aggregated counts only. |
| `preferred_candidate_if_election_today` | categorical | Candidate preference for immediate election. | Collapse to top candidates + `Undecided`. |
| `president_ruto_performance_rating` | categorical | Rating of presidential performance. | Likert values as above. |
| `country_heading_right_direction` | categorical | Perceived national trajectory (`Yes`, `No`, `Unsure`). | — |
| `top_voting_issues` | string | Raw comma-separated list of issues. | Keep private; publish aggregated tallies from list column. |
| `top_voting_issues_list` | list | Tokenized list used for counts. | Not meant for row-level release; share only aggregated totals. |
| `important_mp_qualities` | string | Raw comma-separated MP qualities. | Keep private; publish aggregated tallies. |
| `important_mp_qualities_list` | list | Tokenized list for aggregation. | Same guidance as above. |

## Usage Notes

- If you create a **synthetic** dataset for the public repo, ensure the distributions mimic the real data without mapping to actual respondents.  
- For partial data releases, remove any free-text columns that could contain identifiers.  
- Document any additional engineered fields you add so collaborators can reproduce the pipeline.

