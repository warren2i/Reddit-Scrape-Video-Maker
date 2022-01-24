from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image

ser = Service("C:/Users/warren/PycharmProjects/youtube upload/chromedriver.exe")
op = webdriver.ChromeOptions()
op.headless = True
driver = webdriver.Chrome(service = ser, options = op)


def screenshotcomments(limit):
    driver.get("C:/Users/warren/PycharmProjects/youtube upload/screenshot/comments.html")
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
    driver.find_element_by_id('fullpage').screenshot(
        'C:/Users/warren/PycharmProjects/youtube upload/screenshot/screenshot.png')

    for d in range(limit + 1):
        s = driver.find_element_by_id("id_" + str(d))
        location = s.location
        size = s.size
        print(size)
        x = location['x']
        y = location['y']
        height = location['y'] + size['height']
        width = location['x'] + size['width']
        imgOpen = Image.open("screenshot/screenshot.png")
        imgOpen = imgOpen.crop((int(x), int(y), int(width), int(height)))
        final_size = 1080
        size = imgOpen.size
        ratio = float(final_size) / max(size)
        new_image_size = tuple([int(x * ratio) for x in size])
        imgOpen = imgOpen.resize(new_image_size)
        new_im = Image.new("RGB", (final_size, final_size))
        new_im.paste(imgOpen, ((final_size - new_image_size[0]) // 2, (final_size - new_image_size[1]) // 2))
        new_im.save("redditpost/" + str(d) + ".png")
