# AVA — Topics

Status: **partial**. The Overview tab shows Goodbye, Greeting, and Start Over, then "See all". The rest comes from the Aug 2026 design document. Re-confirm against the Topics tab.

## Custom topics

| Topic | Trigger phrases | Behaviour |
|---|---|---|
| Goodbye | Bye, Bye for now, Bye now, Good bye, No thank you. Goodbye. | Asks whether the user wants to end the conversation. |
| Greeting | Good afternoon, Good morning, Hello, Hey, Hi | "Hello, how can I help you today?" then ends all topics. |
| Start Over | let's begin again, start over, start again, restart | Confirms restart; if no, "Ok. Let's carry on." |
| Thank you | thanks, thank you, thanks so much, ty | "You're welcome." |

## System topics

| Topic | Trigger |
|---|---|
| Conversation Start | On Conversation Start |
| Conversational boosting | Unknown topic |
| End of Conversation | Redirect |
| Escalate | On Talk to Representative |
| Fallback | Unknown topic |
| Multiple Topics Matched | Selection |
| On Error | On error |
| Reset Conversation | Redirect |
| Sign in | On Sign In |
