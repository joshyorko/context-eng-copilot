---
name: "URL Accessibility Screenshot & Audit Robot"
description: |
  A scalable producer-consumer robot that processes bulk URL lists into PNG screenshots and Lighthouse accessibility scores, with GitHub Actions artifact storage.
---

# URL Accessibility Screenshot & Audit Robot

## Goal

### What
Build a two-stage robot automation system that:
1. **Producer**: Ingests URL lists from CSV/Excel files and creates Work Items for each URL
2. **Consumer**: Processes each URL by capturing full-page screenshots and running Lighthouse accessibility audits
3. **Artifacts**: Stores enriched data with {url, wcag_score, screenshot_path} in GitHub Actions artifacts

### Why
- **Automated Accessibility Testing**: Bulk process websites for WCAG compliance monitoring
- **Visual Documentation**: Create screenshot archives alongside accessibility scores  
- **Scalable Architecture**: Leverage Robocorp Work Items for parallel processing
- **CI/CD Integration**: Store results as GitHub Actions artifacts for automated archival

### Success Criteria
- [ ] Producer reads CSV/Excel files containing URL lists and creates Work Items
- [ ] Consumer processes Work Items: captures screenshots + runs Lighthouse accessibility audits
- [ ] Results stored with format: `{url, wcag_score, screenshot_path, timestamp}`
- [ ] Artifacts uploadable to GitHub Actions for download/storage
- [ ] Horizontal scaling via multiple consumer instances
- [ ] Comprehensive error handling for failed URLs/audits

## Context

### Documentation & References

**Core Libraries:**
- **Robocorp Work Items**: https://sema4.ai/docs/automation/python/robocorp/robocorp-workitems
  - Producer-consumer pattern for scalable processing
  - Work Items API for queue management
- **Robocorp Browser**: https://pypi.org/project/robocorp-browser/
  - Playwright wrapper with lifecycle management
  - Full-page screenshot capabilities
- **Lighthouse CLI**: https://developer.chrome.com/docs/lighthouse/
  - Accessibility audit JSON output
  - Command: `lighthouse --only-categories=accessibility --output=json`

**Reference Implementation Files:**
- `examples/fetch-repos-bot/tasks.py` - Producer-consumer pattern
- `examples/fetch-repos-bot/robot.yaml` - Multi-task configuration
- `examples/fetch-repos-bot/conda.yaml` - Dependencies structure

**Screenshot Examples:**
- GitHub: `robocorp/example-full-page-website-screenshots`
- Key pattern: `page.screenshot(path=str(OUTPUT_DIR / f"{domain}.png"), full_page=True)`

### Critical Implementation Details

**Lighthouse JSON Output Structure:**
```json
{
  "categories": {
    "accessibility": {
      "score": 0.95,
      "title": "Accessibility"
    }
  }
}
```

**Work Item Payload Structure:**
```python
# Producer output
{
  "url": "https://example.com",
  "source": "batch_001.csv",
  "timestamp": "2025-01-03T10:00:00Z"
}

# Consumer output
{
  "url": "https://example.com", 
  "wcag_score": 0.95,
  "screenshot_path": "output/example_com.png",
  "lighthouse_path": "output/example_com_lighthouse.json",
  "status": "success",
  "timestamp": "2025-01-03T10:05:00Z"
}
```

## Context Assembly

| Context Element | File/URL | Purpose |
|-----------------|----------|---------|
| Producer Pattern | `examples/fetch-repos-bot/tasks.py` | Work Item creation and CSV processing |
| Browser Screenshot | `robocorp/example-full-page-website-screenshots/tasks.py` | Full-page screenshot implementation |
| Robocorp Work Items | https://sema4.ai/docs/automation/python/robocorp/robocorp-workitems | Queue management API |
| Lighthouse CLI | https://developer.chrome.com/docs/lighthouse/ | Accessibility audit commands |
| Environment Setup | `examples/fetch-repos-bot/conda.yaml` | Dependencies and RCC configuration |
| Multi-task Config | `examples/fetch-repos-bot/robot.yaml` | Producer-Consumer-Reporter structure |

## Implementation Blueprint

### Data Models
```python
from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class URLWorkItem(BaseModel):
    url: HttpUrl
    source: str
    timestamp: datetime

class AuditResult(BaseModel):
    url: HttpUrl
    wcag_score: Optional[float]
    screenshot_path: str
    lighthouse_path: str
    status: str  # success, failed, timeout
    error_message: Optional[str]
    timestamp: datetime
```

### Task Implementation Order

1. **Producer Task** (`producer()`)
   - Read CSV/Excel input files (use pandas for Excel support)
   - Validate URL format and reachability
   - Create Work Items with URL payload
   - Handle batch processing with source tracking

2. **Consumer Task** (`consumer()`)
   - Initialize robocorp-browser with headless mode
   - Process Work Items in parallel-safe manner
   - Capture full-page screenshots (follow `example-full-page-website-screenshots` pattern)
   - Run Lighthouse CLI subprocess for accessibility audit
   - Parse JSON results and extract WCAG score
   - Create output Work Items with enriched data

3. **Reporter Task** (`reporter()`)
   - Aggregate results from consumer outputs
   - Generate summary statistics
   - Create final artifact manifest for GitHub Actions

### Core Implementation Patterns

**Browser Screenshot Pattern:**
```python
from robocorp import browser
from pathlib import Path

def capture_screenshot(url: str, output_dir: Path) -> str:
    browser.goto(url)
    page = browser.page()
    # Wait for page load
    page.wait_for_load_state("networkidle", timeout=30000)
    
    domain = urlparse(url).netloc.replace(".", "_")
    screenshot_path = output_dir / f"{domain}.png"
    page.screenshot(path=str(screenshot_path), full_page=True)
    return str(screenshot_path)
```

**Lighthouse Audit Pattern:**
```python
import subprocess
import json
from pathlib import Path

def run_lighthouse_audit(url: str, output_dir: Path) -> dict:
    domain = urlparse(url).netloc.replace(".", "_")
    output_path = output_dir / f"{domain}_lighthouse.json"
    
    cmd = [
        "lighthouse", url,
        "--only-categories=accessibility",
        "--output=json",
        f"--output-path={output_path}",
        "--chrome-flags=--headless",
        "--quiet"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise Exception(f"Lighthouse failed: {result.stderr}")
    
    with open(output_path, 'r') as f:
        return json.load(f)
```

### Environment Configuration

**Dependencies (conda.yaml):**
```yaml
dependencies:
  - python=3.12.8
  - nodejs=18.17.0  # Required for Lighthouse
  - pip:
    - robocorp==3.0.0
    - robocorp-browser==2.3.0
    - pandas==2.3.0
    - pydantic==2.5.0
    - python-dateutil==2.8.2
```

**Post-install setup:**
```bash
# Install Lighthouse CLI
npm install -g lighthouse@latest
# Install Playwright browsers
playwright install chromium
```

### Error Handling Strategy

**Timeout Handling:**
- Page load timeout: 30 seconds
- Lighthouse audit timeout: 60 seconds
- Screenshot capture timeout: 15 seconds

**Retry Logic:**
- Network failures: 3 retries with exponential backoff
- Rate limiting: Respect site robots.txt and implement delays
- Lighthouse failures: Mark as failed but continue processing

**Failure Categories:**
- `NETWORK_ERROR`: DNS resolution, connection timeout
- `LIGHTHOUSE_ERROR`: Audit execution failure
- `BROWSER_ERROR`: Screenshot capture failure
- `VALIDATION_ERROR`: Invalid URL format

## Validation Requirements

### Level 1: Syntax & Style
```bash
# Purpose: Validate code syntax and style
rcc holotree vars  # Build environment
rcc task run --task validate-syntax
```

### Level 2: Unit Tests
```bash
# Purpose: Run unit tests for core functionality
rcc task run --task test-unit
```

### Level 3: Integration Tests
```bash
# Purpose: Test complete producer-consumer workflow
rcc task run --task test-integration
```

### Level 4: End-to-End Validation
```bash
# Purpose: Test with real URLs and validate artifacts
rcc task run --task Producer
rcc task run --task Consumer  
rcc task run --task Reporter
# Validate artifacts in output/ directory
```

## Integration Points

### File Structure
```
accessibility-audit-robot/
├── robot.yaml              # Multi-task configuration
├── conda.yaml             # Dependencies with Node.js
├── tasks.py               # Producer, Consumer, Reporter tasks
├── tools.py               # Screenshot & Lighthouse utilities
├── models.py              # Pydantic data models
├── devdata/
│   └── sample-urls.csv    # Test data
├── output/                # Artifacts directory
│   ├── screenshots/       # PNG files
│   ├── lighthouse/        # JSON audit reports
│   └── reports/           # Summary files
└── tests/
    ├── test_producer.py   # Producer unit tests
    ├── test_consumer.py   # Consumer unit tests
    └── test_integration.py # E2E tests
```

### GitHub Actions Integration
```yaml
# .github/workflows/accessibility-audit.yml
- name: Upload Accessibility Artifacts
  uses: actions/upload-artifact@v4
  with:
    name: accessibility-audit-results
    path: |
      output/screenshots/
      output/lighthouse/
      output/reports/
```

## Quality Standards

### Performance Targets
- Process 100 URLs within 10 minutes (single consumer)
- Screenshot capture: <15 seconds per URL
- Lighthouse audit: <60 seconds per URL
- Memory usage: <2GB per consumer instance

### Error Handling Completeness
- [ ] Network timeout handling
- [ ] Invalid URL validation
- [ ] Browser crash recovery
- [ ] Lighthouse execution failure
- [ ] Disk space monitoring
- [ ] Rate limiting compliance

### Test Coverage Requirements
- [ ] Producer: CSV/Excel parsing, Work Item creation
- [ ] Consumer: Screenshot capture, Lighthouse execution
- [ ] Integration: Complete workflow with mock data
- [ ] Error scenarios: Network failures, malformed URLs

## Implementation Confidence Score: 8/10

**Strengths:**
- Clear producer-consumer pattern from existing examples
- Well-documented robocorp-browser screenshot capabilities
- Lighthouse CLI integration is straightforward
- Comprehensive error handling strategy

**Risk Factors:**
- Lighthouse Node.js dependency in conda environment
- Potential memory usage with large URL batches
- Browser automation stability with diverse websites

**Mitigation Strategy:**
- Start with basic implementation, add complexity incrementally
- Implement comprehensive timeout and retry logic
- Use existing robocorp patterns for reliability
