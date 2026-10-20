const { chromium } = require("playwright");

const baseURL = process.env.BASE_URL || "http://127.0.0.1:4173";
const routes = [
  "/", "/about/", "/affiliate-disclosure/", "/contact/", "/editorial-policy/",
  "/guides/", "/guides/bonus-terms-explained/", "/guides/how-to-check-a-casino-licence/",
  "/guides/how-to-read-casino-terms/", "/guides/online-gambling-self-exclusion/",
  "/guides/what-wagering-requirements-mean/", "/guides/withdrawal-terms/",
  "/how-we-review/", "/market-research/", "/partners/", "/privacy/",
  "/responsible-gambling/", "/reviews/", "/tools/terms-checklist/",
  "/tools/wagering-calculator/"
];

(async () => {
  const browser = await chromium.launch({ headless: true });
  const errors = [];
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    page.on("pageerror", error => errors.push(error.message));

    for (const route of routes) {
      const response = await page.goto(baseURL + route, { waitUntil: "domcontentloaded" });
      if (!response || response.status() !== 200) {
        throw new Error(route + " returned " + (response ? response.status() : "no response"));
      }
      const title = (await page.title()).trim();
      const h1 = (await page.locator("h1").first().textContent().catch(() => "") || "").trim();
      if (!title) throw new Error(route + " has no document title");
      if (!h1) throw new Error(route + " has no visible H1");
      const mobileOverflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      if (mobileOverflow > 1) throw new Error(route + " has horizontal overflow at mobile width (" + mobileOverflow + "px)");
      const description = await page.locator('meta[name="description"]').getAttribute("content");
      const ogDescription = await page.locator('meta[property="og:description"]').getAttribute("content");
      if (description && description !== ogDescription) {
        throw new Error(route + " search/social descriptions differ");
      }
    }

    await page.goto(baseURL + "/", { waitUntil: "domcontentloaded" });
    const menu = page.locator(".menu-toggle");
    const nav = page.locator("#primary-nav");
    await menu.click();
    if (await menu.getAttribute("aria-expanded") !== "true") throw new Error("mobile menu did not open");
    if (!(await nav.getAttribute("class") || "").includes("open")) throw new Error("mobile navigation is not visible");
    await page.keyboard.press("Escape");
    if (await menu.getAttribute("aria-expanded") !== "false") throw new Error("Escape did not close mobile menu");

    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto(baseURL + "/", { waitUntil: "domcontentloaded" });
    const desktopOverflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    if (desktopOverflow > 1) throw new Error("homepage has horizontal overflow at desktop width (" + desktopOverflow + "px)");

    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(baseURL + "/tools/wagering-calculator/", { waitUntil: "domcontentloaded" });
    await page.locator("#eligible").fill("100");
    await page.locator("#multiplier").fill("35");
    await page.locator("#currency").selectOption("EUR");
    if (!(await page.locator("#turnover").textContent()).includes("3,500.00")) {
      throw new Error("wagering calculator did not calculate 100 × 35");
    }
    await page.locator("#eligible").fill("0");
    if (!(await page.locator("#turnover").textContent()).includes("0.00")) throw new Error("wagering calculator did not accept zero amount");
    await page.locator("#eligible").fill("-1");
    if (await page.locator("#eligible").getAttribute("aria-invalid") !== "true") {
      throw new Error("wagering calculator did not mark invalid amount");
    }
    await page.locator("#eligible").fill("100000001");
    if (await page.locator("#eligible").getAttribute("aria-invalid") !== "true") {
      throw new Error("wagering calculator did not reject an amount above its limit");
    }
    await page.locator("#eligible").fill("");
    if (await page.locator("#eligible").getAttribute("aria-invalid") !== "true") {
      throw new Error("wagering calculator did not reject an empty amount");
    }

    await page.goto(baseURL + "/tools/terms-checklist/", { waitUntil: "domcontentloaded" });
    const boxes = page.locator('.checklist-main input[type="checkbox"]');
    await boxes.first().check();
    if ((await page.locator("#checked-count").textContent()).trim() !== "1") {
      throw new Error("terms checklist progress did not update after checking an item");
    }
    await page.locator("#reset-checklist").click();
    if ((await page.locator("#checked-count").textContent()).trim() !== "0") {
      throw new Error("terms checklist reset did not clear progress");
    }

    if (errors.length) throw new Error("browser runtime errors: " + errors.join(" | "));
    console.log("PASS: " + routes.length + " public routes, mobile/desktop overflow checks, mobile navigation, calculator valid/zero/invalid/extreme inputs, checklist progress/reset, and no page errors.");
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error.stack || error);
  process.exit(1);
});
