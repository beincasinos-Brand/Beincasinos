const { chromium } = require("playwright");
const axeSource = require.resolve("axe-core");

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
  const axeIssues = [];
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    page.on("pageerror", error => errors.push(error.message));
    page.on("console", message => { if (message.type() === "error") errors.push("console: " + message.text()); });

    for (const route of routes) {
      const response = await page.goto(baseURL + route, { waitUntil: "domcontentloaded" });
      if (!response || response.status() !== 200) {
        throw new Error(route + " returned " + (response ? response.status() : "no response"));
      }
      const accessibilityIssues = await page.evaluate(() => {
        const issues = [];
        if (!document.documentElement.lang) issues.push("missing document language");
        if (document.querySelectorAll("main").length !== 1) issues.push("expected exactly one main landmark");
        if (!document.querySelector('a.skip-link[href="#main"]')) issues.push("missing skip-to-content link");
        for (const control of document.querySelectorAll("input:not([type=hidden]), select, textarea")) {
          const id = control.id;
          const labelledBy = control.getAttribute("aria-labelledby");
          const hasLabel = id && document.querySelector('label[for="' + CSS.escape(id) + '"]');
          const hasAriaLabel = (control.getAttribute("aria-label") || "").trim();
          const hasLabelledBy = labelledBy && labelledBy.split(/\s+/).some(token => document.getElementById(token));
          const wrappedLabel = control.closest("label");
          if (!hasLabel && !hasAriaLabel && !hasLabelledBy && !wrappedLabel) {
            issues.push("unlabelled form control: " + (id || control.tagName.toLowerCase()));
          }
        }
        for (const button of document.querySelectorAll("button")) {
          if (!(button.innerText || "").trim() && !(button.getAttribute("aria-label") || "").trim() && !(button.getAttribute("aria-labelledby") || "").trim()) {
            issues.push("button has no accessible name");
          }
        }
        return issues;
      });
      if (accessibilityIssues.length) throw new Error(route + " accessibility smoke checks: " + accessibilityIssues.join("; "));
      await page.addScriptTag({ path: axeSource });
      const axeResults = await page.evaluate(async () => window.axe.run(document, {
        runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"] }
      }));
      if (axeResults.violations.length) {
        const summary = axeResults.violations.map(v => v.id + " (" + v.impact + ", " + v.nodes.length + " element(s)): " + v.nodes.slice(0, 6).map(n => n.target.join(" ") + " — " + n.failureSummary).join(" || ")).join("; ");
        axeIssues.push(route + ": " + summary);
      }
      const title = (await page.title()).trim();
      const h1 = (await page.locator("h1").first().textContent().catch(() => "") || "").trim();
      if (!title) throw new Error(route + " has no document title");
      if (!h1) throw new Error(route + " has no visible H1");
      const mobileOverflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      if (mobileOverflow > 1) throw new Error(route + " has horizontal overflow at mobile width (" + mobileOverflow + "px)");
      for (const width of [320, 375, 768, 1024, 1440]) {
        await page.setViewportSize({ width, height: width <= 375 ? 812 : 900 });
        const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
        if (overflow > 1) throw new Error(route + " has horizontal overflow at " + width + "px (" + overflow + "px)");
      }
      await page.setViewportSize({ width: 390, height: 844 });
      const description = await page.locator('meta[name="description"]').getAttribute("content");
      const ogDescription = await page.locator('meta[property="og:description"]').getAttribute("content");
      if (description && description !== ogDescription) {
        throw new Error(route + " search/social descriptions differ");
      }
    }

    if (axeIssues.length) throw new Error("axe WCAG 2.1 A/AA violations:\n" + axeIssues.join("\n"));

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
    console.log("PASS: " + routes.length + " public routes at 320/375/390/768/1024/1440px widths, axe WCAG 2.1 A/AA automated scans, accessibility smoke checks, mobile navigation, calculator valid/zero/invalid/extreme inputs, checklist progress/reset, and no page errors.");
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error.stack || error);
  process.exit(1);
});
