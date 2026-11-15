from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys, os

# ===== 配置 =====
HTML_PATH = "cards.html"       # 待截图的 HTML 文件
OUT_DIR = "."                  # 输出目录
CHROMEDRIVER = None            # 可选：指定 chromedriver 路径，留空自动查找
SCALE = 2                      # retina 倍率（输出 960x1280 @2x）

def main():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=600,800")
    opts.add_argument(f"--force-device-scale-factor={SCALE}")
    opts.add_argument("--hide-scrollbars")

    if CHROMEDRIVER:
        svc = Service(executable_path=CHROMEDRIVER)
        driver = webdriver.Chrome(service=svc, options=opts)
    else:
        driver = webdriver.Chrome(options=opts)
    print("Chrome headless started")

    driver.get("file://" + os.path.abspath(HTML_PATH))
    import time
    time.sleep(3)

    cards = driver.find_elements(By.CSS_SELECTOR, ".card")
    print(f"Found {len(cards)} cards")

    for i, card in enumerate(cards, 1):
        driver.execute_script("arguments[0].scrollIntoView({block:'start'});", card)
        time.sleep(0.4)
        png = card.screenshot_as_png
        fname = os.path.join(OUT_DIR, f"P{i:02d}.png")
        with open(fname, "wb") as f:
            f.write(png)
        print(f"Saved {fname} ({len(png)} bytes)")

    driver.quit()
    print("Done")

if __name__ == "__main__":
    main()
