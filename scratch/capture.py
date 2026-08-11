from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    # LOCAL FILE CAPTURE
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto("file:///mnt/c/Users/franc/.gemini/antigravity/scratch/analisis-cba-rio4/index.html", wait_until="networkidle")
    page.screenshot(path="local_desktop.png", full_page=True)
    
    page.set_viewport_size({"width": 375, "height": 812})
    page.screenshot(path="local_mobile.png", full_page=True)
    
    browser.close()

print("Captured local screenshots successfully!")
