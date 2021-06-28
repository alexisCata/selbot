import os
import random
import sys
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# pip install selenium
# pip install webdriver-manager


def sel_bot(usuario, pwd, tag, maxlikes):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()

    try:

        driver.get("http://www.instagram.com")
        user = driver.find_element_by_name("username")
        pasw = driver.find_element_by_name("password")
        button = driver.find_element_by_class_name("HmktE")

        user.send_keys(usuario)
        pasw.send_keys(pwd)
        button.submit()

        # buton_n = driver.find_element_by_class_name("mt3GC")
        #
        # actions = ActionChains(driver)
        # a = "🤟"
        # a = "🔥"
        # actions.move_to_element(buton_n).perform()
        # actions.move_by_offset(20, -20).perform()
        # actions.click()

        JS_ADD_TEXT_TO_INPUT = """
          var elm = arguments[0], txt = arguments[1];
          elm.value += txt;
          elm.dispatchEvent(new Event('change'));
          """

        emojis = get_emojis()

        likes = 0
        comments = 0

        liked = 0
        skip = False
        already = False

        time.sleep(5)

        try:
            notif = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
            notif.click()
        except:
            pass
        # try:
        #     cookies = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
        #     cookies.click()
        # except:
        #     pass


        for t in tag:
            print("#######################################################  {}".format(t))
            driver.get("http://www.instagram.com/explore/tags/{}/".format(t))

            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 1300)")
            time.sleep(1)

            try:
                post = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]')
                post.click()
            except:
                post = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[2]/a/div[1]")
                post.click()

            for ind in range(0, 250):
                try:
                    name = driver.find_element_by_xpath(
                        '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a')

                    if name.text != usuario:
                        time.sleep(2)
                        try:
                            elements = driver.find_elements_by_css_selector('[aria-label="Me gusta"]')
                        except:
                            elements = driver.find_elements_by_css_selector('[aria-label="Like"]')
                        found = False
                        lk = ""
                        # t1 = time.perf_counter()
                        try:
                            no = None
                            no = driver.find_element_by_css_selector('[aria-label="Ya no me gusta"]')
                        except:
                            pass
                        # t2 = time.perf_counter()
                        # print("Time:" + str(round(t2-t1,1)))
                        if not no:
                            for e in elements:
                                lk = e.get_attribute("aria-label")
                                if lk in ["Me gusta", "Like"]:
                                    found = True
                                    break
                            if not found:
                                print("WHAT THE FUCK IS GOING ON...? SOMETHING WRONG")
                        else:
                            print("LIKED...???")

                        if lk in ("Like", "Me gusta"):
                            liked = 0
                            # att.click()
                            blike = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                            time.sleep(random.choice(range(1, 2)))
                            blike.click()
                            likes += 1
                            print("LIKES: {}/{}".format(likes, maxlikes))
                            time.sleep(random.choice(range(0, 4)))
                            if BOOL_COMMENT:
                                comment = driver.find_element_by_xpath(
                                    "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
                                comment.click()

                                if comments == 0 or likes % 20 == 0 or already == True:

                                    if already or not skip:
                                        if already:
                                            already = False
                                        elem_text = driver.find_element_by_xpath(
                                            "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
                                        text = random.choice(emojis)
                                        driver.execute_script(JS_ADD_TEXT_TO_INPUT, elem_text, text)
                                        elem_text.send_keys(" ")
                                        elem_text.send_keys(Keys.BACKSPACE)

                                        post = driver.find_element_by_xpath(
                                            "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button")
                                        post.click()
                                        comments += 1
                                        print("COMMENTS: {}".format(comments))
                                        time.sleep(random.choice(range(1, 3)))
                                    else:
                                        already = True

                                    skip = random.choice([True, False])
                                    print(skip)
                        else:
                            liked += 1
                            if liked == 10:
                                liked = 0
                                break
                    next = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")
                    next.click()
                    time.sleep(2)
                except BaseException as e:
                    try:
                        close = driver.find_element_by_xpath("/html/body/div[5]/div[3]/button")
                    except:
                        close = driver.find_element_by_xpath("/html/body/div[4]/div[3]/button")
                    close.click()
                    time.sleep(2)
                    scroll = (ind / 9) * 2000
                    driver.execute_script("window.scrollTo(0, {})".format(scroll))
                    time.sleep(2)
                    try:
                        post = driver.find_element_by_xpath(
                            '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]')
                        post.click()
                    except:
                        post = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[2]/a/div[1]")
                        post.click()
                if likes > maxlikes:
                    break
            if likes > maxlikes:
                break
    except Exception as e:
        print("ERRORRRRR...." + str(e))
    driver.close()

    return t, likes


def get_emojis():
    cuernos = u"\ud83e\udd18\ud83e\udd18\ud83e\udd18\ud83d\udcaa"
    rock = u"\ud83e\udd1f\ud83e\udd1f\ud83e\udd1f\ud83d\udcaa"
    ok = u"\ud83d\udc4c\ud83d\udc4c\ud83d\udc4c\ud83d\udcaa"
    fire = u"\ud83d\udd25\ud83d\udd25\ud83d\udd25\ud83d\udcaa"
    manos = u"\ud83d\ude4c\ud83d\ude4c\ud83d\ude4c\ud83d\udcaa"
    biceps = u"\ud83d\udcaa\ud83d\udcaa\ud83d\udcaa\ud83d\udd25"
    colision = u"\ud83d\udca5\ud83d\udca5\ud83d\udca5\ud83d\udcaa"
    voltage = u"\u26a1\u26a1\u26a1\ud83d\udcaa\ud83d\udd25"
    dale = u"\ud83d\udc4a\u270a\ud83d\udc4a\u270a\ud83d\udca5\ud83d\udca8"
    gafas = u"\ud83e\udd1f\ud83e\udd1f\ud83e\udd1f\ud83d\ude0e"
    fire2 = u"\ud83d\udd25\ud83d\udd25\ud83d\udd25\ud83d\ude0e"

    init = [cuernos, rock, ok, fire, manos, biceps, colision, voltage, dale, gafas, fire2]

    cuerno = u"\ud83e\udd18"
    roc = u"\ud83e\udd1f"
    oc = u"\ud83d\udc4c"
    fir = u"\ud83d\udd25"
    mano = u"\ud83d\ude4c"
    bicep = u"\ud83d\udcaa"
    rayo = u"\u26a1\u26a1"
    colis = u"\ud83d\udca5"
    voltage = u"\u26a1"
    gafas = u"\ud83e\udd1f"
    li = [cuerno, roc, oc, fir, mano, bicep, rayo, colis, voltage, gafas, cuerno, roc, oc, fir, mano, bicep, rayo,
          colis, voltage, gafas, cuerno, roc, oc, fir, mano, bicep, rayo, colis, voltage, gafas, cuerno, roc, oc, fir,
          mano, bicep, rayo, colis, voltage, gafas]

    random_list = init

    for i in li:
        times = random.choice(range(3, 6))

        if times == 3:
            icon = random.choice(li)
            random_list.append(random.choice(li) + random.choice(li) + random.choice(li))
        if times == 4:
            icon = random.choice(li)
            random_list.append(icon + icon + random.choice(li) + random.choice(li))
        if times == 5:
            icon = random.choice(li)
            random_list.append(icon + icon + icon + random.choice(li) + random.choice(li))

    return random_list


def main(usuario, pwd, tags):
    if BOOL_COMMENT:
        ran = range(590, 690)
    else:
        ran = range(690, 790)

    filename = "IG2"

    while True:

        file = os.getcwd() + "\\" + filename

        with open(file, "+w") as f:
            last = f.readline().split(",")[0]

        tag = []
        prev = []
        for t in tags:
            if (t != last and last not in prev) or t == last:
                prev.append(t)
            else:
                tag.append(t)

        tag += prev

        maxlikes = random.choice(ran)

        last_tag, likes = sel_bot(usuario, pwd, tag, maxlikes)

        file = os.getcwd() + "\\" + filename

        with open(file, "+w") as f:
            f.write("{},{}".format(last_tag, likes))

        if likes > 500:
            r = range(0, 8)
        else:
            r = range(0, 4)
        for a in r:
            print(".........." + str(a))
            print(".........." + str(datetime.now()))
            time.sleep(4320)


if __name__ == "__main__":
    # BOOL_COMMENT = True
    BOOL_COMMENT = False
    usr = sys.argv[1]
    pwd = sys.argv[2]
    # tags = sys.argv[3]

    tags = [
        "tag1", "tag2", "tag3..."
    ]

    tags = [
        "perroygato", "perrosygatos", "perrosygatosjuntos", "perrosdeinstagram", "gatosdeinstagram",
        "dogsofinstagram", "catsofinstagram", "perrosinstagram", "perrosfelices", "perrosgraciosos", "perrosespaña",
        "dogs", "perros", "perro", "perrito", "cachorro", "cachorros",
        "gato", "gatos", "kitten", "kittens", "streetcat",
        "bordercollie", "bordercollies", "bordercolliepuppy", "bordercollieworld", "bordercollielover",
        "bordercolliesofinstagram",
        "puppy", "puppylove", "puppyworld", "puppyface", "puppyfun", "puppystagram", "puppypic", "instadog", "instacat",

    ]

    main(usr, pwd, tags)
