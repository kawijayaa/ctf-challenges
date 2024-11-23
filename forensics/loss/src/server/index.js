const express = require('express');
const rateLimit = require('express-rate-limit');

const app = express();

app.use(rateLimit({
    windowMs: 2 * 60 * 1000,
    max: 30,
    legacyHeaders: false,
}));

app.use((req, res, next) => {
    console.log("Request: " + req.method + " " + req.url + " from " + req.ip);
    next();
})

app.use('/.git', express.static('git'));

app.listen(3000, () => {
    console.log('Server started on :3000');
});
