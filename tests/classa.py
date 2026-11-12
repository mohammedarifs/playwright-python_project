import time
from idlelib import browser
from tkinter import dialog

import syncio
from playwright.sync_api import  Playwright, sync_playwright


def runtestcase(Playwright: Playwright):
    browser=Playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.pause()
    page.goto("https://demoqa.com/browser-windows")
    new_pages = []
    context.on("page", lambda pg:new_pages.append(pg))

    # print("get the title of applcaiotion ", page.title())
    # page.get_by_placeholder("Username").fill("standard_user")
    # page.get_by_placeholder("Password").fill("secret_sauce")
    # page.expect_event("page") as pagei:

    # new_page_tasks = [context.expect_event("page") for _ in range(3)]
    # with context.expect_event("page") as  pagenew:
    #
    # # 2. Click the button that opens multiple tabs
    #     page.get_by_role("button", name="New Window").click()
    #     # page.get_by_role("button", name="New Tab").click()
    # new_page = pagenew.value
    # print(new_page)
    # new_page.bring_to_front()
    # print(f"New Page Title: {new_page.get_by_text("This is a sample page").text_content()}")
    #
    # 3. Wait for all tabs to finish popping up
    # new_pages = syncio.gather(*new_page_tasks)

    # 4. Control and switch to each page independently
    # for index, new_tab in enumerate(new_pages):
    #     # new_tab.wait_for_load_state()
    #
    #     # Visually switch to the tab (brings it to the front focus)
    #     # new_tab.bring_to_front()
    #
    #     print(f"Tab {index + 1} Title: {new_tab.title()}")

    # opened_tabs = []
    #
    # def on_page_opened(new_page):
    #     opened_tabs.append(new_page)

    # 2. Start listening to the context for new pages
    # context.on("page", on_page_opened)
    #
    # # 3. Trigger the multi-tab click
    page.get_by_role("button", name="New Tab").click()
    #
    # # 4. Wait briefly for the browser process to catch all events
    # # (Adjust time or check len(opened_tabs) in a short loop if pages take time)
    time.sleep(5)
    print(f"Number of opened tabs: {len(new_pages)}")
    for pg in new_pages:
        pg.wait_for_load_state()
        print(f"New Page Title: {pg.url()}")

    def dailoghandle(dailog):
        print(f"Dialog message: {dialog.message}")
        dialog.dismiss()

    page.on("daialog", dailoghandle)

    # # 5. Stop listening
    # context.remove_listener("page", on_page_opened)
    # print(f"Number of opened tabs: {len(opened_tabs)}")
    # # 6. Switch and control each page
    # for index, new_tab in enumerate(opened_tabs):
    #     new_tab.wait_for_load_state()
    #
    #     # Bring the tab into visual focus
    #     new_tab.bring_to_front()
    #
    #     print(f"Tab {index + 1} Title: {new_tab.title()}")

    browser.close()
with sync_playwright() as playwright:
    runtestcase(playwright)