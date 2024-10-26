const express = require('express');
const puppeteer = require('puppeteer');
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.set('view engine', 'ejs');

app.post('/visit', async (req, res) => {
    const id = req.body.id;

    const browser = await puppeteer.launch({
        executablePath: '/usr/bin/chromium-browser',
        headless: true,
        args: [
            '--disable-dev-shm-usage',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-gpu',
            '--no-gpu',
            '--disable-default-apps',
            '--disable-translate',
            '--disable-device-discovery-notifications',
            '--disable-software-rasterizer',
            '--disable-xss-auditor'
        ],
        ignoreHTTPSErrors: true,
    });

    try {
        const context = await browser.createBrowserContext();
        const page = await context.newPage();

        await page.setCookie({
            name: 'flag',
            value: process.env.FLAG || 'COMPFEST16{test_flag}',
            url: 'http://copasbin-web/',
            httpOnly: false,
        });

        await page.goto('http://copasbin-web:3000/copas/' + id, { waitUntil: 'networkidle2' });
        await new Promise((resolve) => setTimeout(resolve, 15000));

        await context.close();
    } catch (e) {
        console.log(e);
    }

});

const port = 9999;
app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
