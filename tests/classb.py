# from playwright.sync_api import sync_playwright, Playwright
#
# def run(playwright: Playwright):
#     webkit = playwright.webkit
#     browser = webkit.launch(headless=False)
#     context = browser.new_context()
#     context.expose_binding("pageURL", lambda source: source["page"].url)
#     page = context.new_page()
#     page.pause()
#     page.set_content("""
#     <script>
#       async function onClick() {
#         document.querySelector('div').textContent = await window.pageURL();
#       }
#     </script>
#     <button onclick="onClick()">Click me</button>
#     <div></div>
#     """)
#     page.get_by_role("button").click()
#
# with sync_playwright() as playwright:
#     run(playwright)
from _pyrepl import keymap

# dict1 = {"a": 1, "c": 3, "b": 2}
# print(dict1)
# print()


# list1 = list("aeiou")
# list2 = list("bangalore")
# print(list1,list2)
# print(list1  list2)


list = ['Volvo\nSaab\nOpel\nAudi']

print(list[0])
print(len(list))
l2 = list[0].split("\n")
print(l2)
l2.remove("Volvo")
print(l2)