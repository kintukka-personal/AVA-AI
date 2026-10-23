# Analytics

Snapshots from Copilot Studio › Activity (analytics summary). Add a new dated section each time; don't overwrite old ones.

## 2026-10-23 · Last 180 days (2026-04-27 → 2026-10-23)

Screenshots: [`screenshots/2026-10-23/`](../screenshots/2026-10-23/). Studio's AI summary is unavailable for this range ("Date range exceeds 90 days").

### Overview

| Metric | Value |
|---|---|
| Conversation sessions | 3,113 |
| Total reactions | 14 |
| Engagement | 18% |
| Average daily active users | 11 |
| Copilot credits consumed | 50,158.16 (≈ 16 per session) |
| Time saved (Studio estimate) | 511 hrs (≈ 85 hrs/month) |

The pilot business case modelled ≈ 1,000 hrs/month (200 users × 1 query/day × 15 min). Studio's estimate is about 8.5% of that.

### Custom metrics (preview)

| Blocker Status | Share |
|---|---|
| Not Blocked | 57.1% |
| Blocked | 41.6% |
| Other | 1.3% |

| Issue Resolution Outcome | Share |
|---|---|
| Guidance Provided | 91.1% |
| Escalation Required | 6% |
| Other | 2.6% |
| Resolved | 0.2% |

The repo doesn't hold the definitions of these two custom metrics yet. Capture them from Studio › Activity › Custom metrics before reading much into "Blocked 41.6%".

### Reactions and satisfaction

| Metric | Value |
|---|---|
| Reactions | 14 total: 92.9% thumbs up, 7.1% thumbs down |
| Satisfaction survey | 1 survey, 4/5.0 |
| Satisfaction by session | Satisfied 100, Neutral 0, Dissatisfied 0 |

### Generated answers

| Metric | Value |
|---|---|
| Total questions | 496 |
| Answered | 100% |
| Unanswered | 0% |
| Quality: good | 94.6% |
| Quality: poor | 5.4% |

Studio scores quality from a sample, and only on days with at least 10 answers.

### Knowledge source use (top 5 of 20)

| Source | Type | Questions | Good quality |
|---|---|---|---|
| D365 Procedure Guides | SharePoint | 420 | 95% |
| https://learn.microsoft.com/en-us/ | Public website | 190 | 93% |
| D365 Quick Reference Cards | SharePoint | 65 | 80% |
| D365 Financial Dimension Decision Support Tool.pdf | SharePoint | 11 | 67% |
| D365 QRC - Procurement Subcategories – Main Account Mappings.pdf | SharePoint | 2 | 0% |

One answer can cite several sources, so the question counts add up to more than 496.

- **The PG and QRC libraries are AVA's most-used sources**, but the Knowledge tab captured on 2026-10-16 didn't list either of them. See [`open-items.md`](open-items.md) item 2.
- **MAP's only source was barely used:** 2 questions in 180 days, 0% good quality.
- The usage table counts 20 sources, but the Knowledge tab listed 18. The other 15 sources are behind "See all (20)".
