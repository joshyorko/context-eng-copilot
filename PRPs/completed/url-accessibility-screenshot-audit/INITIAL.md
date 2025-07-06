## FEATURE:

A robot that turns any bulk list of URLs into a stream of PNG screenshots + Lighthouse accessibility scores.

Producer ingests CSV/Excel feeds or API payloads and queues each URL as a Work Item. 
robocorp.com
github.com

Consumer spins up a headless Chromium session, captures a full-page screenshot, runs a Lighthouse "Accessibility" audit, and writes {url, wcag_score, screenshot_path} to GitHub Actions artifacts for archival and download.

GitHub Actions workflow uploads the enriched data as build artifacts, allowing automated storage and retrieval of accessibility reports and screenshots.


## Workflow in Two Tasks

| Stage | Action | Libraries / References |
|-------|--------|----------------------|
| Producer | Read URL list → workitems.outputs.create({"url": …}) | Robocorp Work Items API<br>https://sema4.ai/docs/automation/python/robocorp/robocorp-workitems |
| Consumer | • for item in workitems.inputs:<br>• browser.new_page(url) via robocorp-browser<br>• page.screenshot()<br>• Run lighthouse --only-categories=accessibility in headless mode; parse JSON score | robocorp-browser (Playwright wrapper)<br>https://pypi.org/project/robocorp-browser/<br>Lighthouse CLI<br>https://developer.chrome.com/docs/lighthouse/ |

**Horizontal scale**: Launch additional consumer workers using patterns from `examples/` directory; Work Items queue guarantees safe parallelism across multiple robot instances.


## EXAMPLES:

[Provide and explain examples that you have in the `examples/` folder]

## DOCUMENTATION:

[List out any documentation (web pages, sources, APIs, etc.) that will need to be referenced during development]

Robocorp WorkItem Documentation: https://sema4.ai/docs/automation/python/robocorp/robocorp-workitems

                                https://sema4.ai/docs/automation/python/robocorp/robocorp-workitems/guides

## OTHER CONSIDERATIONS:

---

*To generate a PRP from this file, use the `/generate-prp` prompt in GitHub Copilot chat, or reference this file when asking Copilot to create a comprehensive implementation plan.*
