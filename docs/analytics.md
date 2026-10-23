# Analytics

Snapshots from Copilot Studio › Activity (analytics summary). Add a new dated section each time; don't overwrite old ones. Newest window first.

## 2026-10-23 · Last 90 days (2026-07-26 → 2026-10-23)

Screenshots: [`screenshots/2026-10-23/90d-*.png`](../screenshots/2026-10-23/).

### Studio's AI summary (verbatim)

> Agent handled 353 sessions with 63% engagement and 100% answered quality responses.
> - Out of 353 total sessions, 63% showed user engagement with 206 sessions resolved.
> - All 199 sampled responses were answered, with 41 rated as high quality, reflecting strong AI quality.
> - No autonomous runs were recorded, indicating no autonomous agent activity during this period.
> - Knowledge utilization was at 100%, with a 55% answer rate and zero knowledge errors reported.
> - Plugin actions were used 74 times with an 84% success rate, mainly for Azure DevOps tasks.

The summary is AI-generated and contradicts itself: "41 rated as high quality" against the 100% good shown on the answer-quality chart below.

### Overview

| Metric | Value |
|---|---|
| Conversation sessions | 353 (206 resolved) |
| Total reactions | 2 |
| Engagement | 63% |
| Average daily active users | 3 |
| Copilot credits consumed | 45,086.96 (≈ 128 per session) |
| Time saved (Studio estimate) | 206 hrs (≈ 69 hrs/month) |

### Custom metrics (preview)

| Blocker Status | Share |
|---|---|
| Not Blocked | 67.5% |
| Blocked | 31.9% |
| Other | 0.6% |

| Issue Resolution Outcome | Share |
|---|---|
| Guidance Provided | 90.8% |
| Escalation Required | 6.1% |
| Other | 2.8% |
| Resolved | 0.3% |

### Conversation outcomes

A daily chart split into Resolved, Escalated, Abandoned, and Unengaged. Most days have under 10 sessions. The peaks are about 18 sessions in early August and about 15 around 2 September. Escalations are rare (small spikes around 21 August and 2 September).

### Reactions and sentiment

| Metric | Value |
|---|---|
| Reactions | 2 total, 100% thumbs up |
| Sentiment analysis coverage (preview) | 12% |
| Sentiment | Negative 11.7 · Neutral 83.2 · Positive 5.1 |

### Child agents

| Agent | Calls | Success rate | Status |
|---|---|---|---|
| WIA — Work Item Assistant (for ADO) | 22 | **36%** | Enabled |
| MAP — Mapping Assistant | 19 | 105% (as shown by Studio) | Enabled |
| FIN — Financial Dimensions Selector | 17 | 88% | Enabled |
| TAM — Template Access Manager | 6 | 100% | Enabled |
| SIMMY — D365 Simulation provider | 0 | 0% | Disabled |

64 child calls across 353 sessions. Studio shows MAP's success rate as above 100%.

### Generated answers

| Metric | Value |
|---|---|
| Total questions | 199 |
| Answered | 100% |
| Quality: good / poor | 100% / 0% |

### Tool use

| Metric | Value |
|---|---|
| Total tool calls | 74 |
| Success rate | 84% |
| Tools used | Get work item details, Get work item comments, Search for work items |

Tool calls cluster in a spike of about 40 around 23 August and a smaller one of about 12 around 5 September. Get work item attachment and List work item fields don't appear in the chart.

### Knowledge source use (all 20 sources)

| Source | Type | Questions | Good quality |
|---|---|---|---|
| D365 Procedure Guides | SharePoint | 167 | 100% |
| https://learn.microsoft.com/en-us/ | Public website | 94 | 100% |
| D365 Quick Reference Cards | SharePoint | 20 | 100% |
| D365 Financial Dimension Decision Support Tool.pdf | SharePoint | 4 | 100% |
| D365 Templates | SharePoint | 1 | 100% |
| D365 Financial Dimension Decision Support Tool.pdf (2nd copy) | SharePoint | 1 | 0% |
| D365 QRC - What are Financial Dimensions.pdf | SharePoint | 1 | 0% |
| D365 QRC - Procurement Subcategories – Main Account Mappings.pdf | SharePoint | 1 | 0% |
| D365 Simulations | SharePoint | 0 | — |
| 30-Vendor Onboarding and Maintenance PG.pdf | SharePoint | 0 | — |
| https://support.microsoft.com/en-us | Public website | 0 | — |
| WTG - AU Legal Entities.xlsx | SharePoint | 0 | — |
| Financial Dimensions Codes.xlsx | SharePoint | 0 | — |
| 33-Procurement (Purchase Requisitions) PG.pdf | SharePoint | 0 | — |
| 31-Vendor Invoices PG.pdf | SharePoint | 0 | — |
| https://learn.microsoft.com/en-us/dynamics365/ | Public website | 0 | — |
| PAT | SharePoint | 0 | — |
| D365_FinDims_PR_CodingGuide.xlsx | SharePoint | 0 | — |
| _2 rows below the screenshot_ | | | |

The 20 sources are the 18 on the Knowledge tab plus the two libraries the tab doesn't show: D365 Procedure Guides and D365 Quick Reference Cards. The 2 rows below the screenshot are 32-Vendor Payments PG and 34-Procurement (Purchase Agreements) PG, the only Knowledge-tab sources not visible above.

## Comparison: first vs second 90 days

Derived from the 180-day and 90-day snapshots above (first half = 180-day total minus last 90 days).

| | 2026-04-27 → 07-25 | 2026-07-26 → 10-23 | Change |
|---|---|---|---|
| Sessions | 2,760 | 353 | −87% |
| Copilot credits | 5,071 | 45,087 | ×8.9 |
| Credits per session | ≈ 1.8 | ≈ 128 | ×70 |
| Time saved | 305 hrs | 206 hrs | −32% |

- **Cost per session rose about 70-fold while sessions fell 87%.** The last 90 days used 90% of the 180-day credits from 11% of the sessions. This snapshot doesn't show the cause. Candidates in the repo's history include the model now set to Claude Opus 4.6 (a "Deep" reasoning model, which costs more per call), parent-to-child routing, and the ADO tool calls. Check Studio › Activity › Billing ("See billing") for the breakdown.
- Engagement rose from 18% (180-day) to 63% (90-day), so fewer users are having more engaged sessions.

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
- The usage table counts 20 sources, but the Knowledge tab listed 18. The 90-day snapshot above lists all 20.
