import os
from idlelib import browser
from pathlib import Path

import dotenv
from playwright.sync_api import sync_playwright, Page, expect  # fixture
import pytest




@pytest.fixture
# @pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def setup(request):
        with sync_playwright() as playwright:
                browser = playwright.chromium.launch(headless=False)
                context = browser.new_context()
                page = context.new_page()
                yield page
                browser.close()
                # browser = getattr(playwright, "chromium").launch(headless=False)
                # context=browser.new_context()
                # context.tracing.start(screenshots=True, snapshots=True, sources=True)
                # page = context.new_page()
                # yield page
                # trace_path = f"custom_traces/{request.node.name}_trace.zip"
                # context.tracing.stop(path=trace_path)
                # browser.close()


@pytest.fixture
def load_data():
        env_file = Path(__file__).resolve().parent / "sauseproject" / "testdata" / "qa.env"
        if not env_file.is_file():
                raise FileNotFoundError(f"Environment data file not found: {env_file}")
        dotenv.load_dotenv(env_file)
