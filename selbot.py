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
    driver.implicitly_wait(5)
    driver.maximize_window()

    try:
        t = None
        likes = 0
        driver.get("http://www.instagram.com")

        time.sleep(3)
        cookies = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
        cookies.click()
        user = driver.find_element("name", "username")
        pasw = driver.find_element("name", "password")
        time.sleep(1)
        button = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")

        time.sleep(3)
        user.send_keys(usuario)
        pasw.send_keys(pwd)
        button.submit()
        time.sleep(5)
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

        # try:
        #     notif = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/button[1]")
        #     notif.click()
        # except:
        #     pass
        # try:
        #     cookies = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/button[1]")
        #     cookies.click()
        # except:
        #     pass

        for t in tag:
            print("#######################################################  {}".format(t))
            driver.get("http://www.instagram.com/explore/tags/{}/".format(t))

            time.sleep(5)
            driver.execute_script("window.scrollTo(0, 1200)")
            time.sleep(5)

            try:
                print("POST")
                post = driver.find_element("xpath", 
                    '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[1]/a/div')
                post.click()
            except:
                time.sleep(10)
                post = driver.find_element("xpath",
                                           '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[1]/a/div')
                post.click()

            for ind in range(50, 100):
                try:
                    time.sleep(7)
                    print("NAME")
                    try:
                        name = driver.find_element("xpath", 
                            '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/div/a')
                    except:
                        name = driver.find_element("xpath", 
                            '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/a')

                    if name.text != usuario:
                        found = False
                        try:
                            element = driver.find_element("css selector", '[aria-label="Me gusta"]')
                            no = None
                        except:
                            no = driver.find_element("css selector", '[aria-label="Ya no me gusta"]')

                        lk = ""
                        if not no:
                            lk = element.get_attribute("aria-label")
                            if lk in ["Me gusta", "Like"]:
                                found = True
                            if not found:
                                print("WHAT THE FUCK IS GOING ON...? SOMETHING WRONG")
                        else:
                            print("LIKED...???")
                            print(datetime.now())

                        if lk in ("Like", "Me gusta"):
                            liked = 0
                            # att.click()
                            try:
                                print("LIKE")
                                blike = driver.find_element("xpath", 
                                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
                                time.sleep(random.choice(range(1, 2)))
                                blike.click()
                                likes += 1
                            except Exception as e:
                                print(1)
                                print(e)
                            print("LIKES: {}/{}".format(likes, maxlikes))
                            print(datetime.now())
                            time.sleep(random.choice(range(0, 3)))
                            if BOOL_COMMENT:
                                comment = driver.find_element("xpath", 
                                    "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
                                comment.click()

                                if comments == 0 or likes % 20 == 0 or already == True:

                                    if already or not skip:
                                        if already:
                                            already = False
                                        elem_text = driver.find_element("xpath", 
                                            "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
                                        text = random.choice(emojis)
                                        driver.execute_script(JS_ADD_TEXT_TO_INPUT, elem_text, text)
                                        elem_text.send_keys(" ")
                                        elem_text.send_keys(Keys.BACKSPACE)

                                        post = driver.find_element("xpath", 
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
                    try:
                        #next = driver.find_element("xpath", "/html/body/div[6]/div[1]/div/div/a[2]")
                        print("NEXT")
                        next = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
                        next.click()
                        time.sleep(2)
                    except Exception as e:
                        print(2)
                        print(e)
                except BaseException as e:
                    next = driver.find_element("xpath",
                                               "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
                    next.click()
                    time.sleep(2)
                    # print("CLOSE")
                    # close = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div")
                    # close.click()
                    # time.sleep(2)
                    # scroll = (ind / 9) * 200
                    # driver.execute_script("window.scrollTo(0, {})".format(scroll))
                    # time.sleep(2)
                    # try:
                    #     post = driver.find_element("xpath",
                    #         '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div')
                    #     time.sleep(2)
                    #     post.click()
                    # except Exception as e:
                    #     print(3)
                    #     print(e)
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
        ran = range(490, 590)
    else:
        ran = range(450, 499)

    filename = "IG"

    while True:
        file = os.getcwd() + "\\" + filename

        with open(file, "+r") as f:
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
            r = range(0, 8)
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
        "hardenduro", "endurospain", "enduro", "enduropro", "endurofun",
        "endurox", "malaga", "endurocross",
        "offroad", "endurolove", "endurorider", "motoenduro", "enduromoto",
        "endurolife", "endurobike", "enduroadventure",
        "endurolifestyle", "endurotraining", "endurodelverano", "endurotrail",
        "2t", "2tiempos", "2stroke", "ktmenduro", "ktmexc", "ktm300tpi", "ktm300", "goprohero",
        "motocross", "motocrosslife", "motocrosslove", "motocrossrider", "motocrossaction", "motocrossgirl",
        "dirtbike", "dirtbikes", "dirtbikeporn", "dirtbikegirl", "dirtbikesarefun", "dirtbikesarecool",
        "endureros", "enduroespaña", "endurospain", "endurotraining", "endurofim",
        "motos", "dosruedas", "rutasenmoto", "moto", "spain", "españa", "moteros", "moteras", "instamoto",
        "pasionporlasmotos", "moteras", "moterosespaña", "locosporlasmotos", "amorporlasmotos",
        "soymotero",
        "motoadictos", "motopasion", "andalucia",

        # "Malaga", "Madrid", "Sevilla", "LaCoruña", "Valencia", "Asturias", "Andalucia",
        #     "Extremadura", "Castillalamancha", "CastillaLeon", "Aragon", "Galicia", "Zaragoza",
        #     "Pontevedra", "Granada", "Alicante", "Cordoba", "Almeria", "Murcia", "Cadiz", "Toledo",
        #     "Badajoz", "Navarra", "Jaen", "Castellon", "Cantabria", "Huelva", "Valladolid", "CiudadReal",
        #     "Caceres", "Albacete", "Burgos", "Álava", "Salamanca", "Lugo", "LaRioja", "Orense", "Guadalajara",
        #     "Huesca", "Cuenca", "Zamora", "Palencia", "Avila", "Segovia", "Teruel", "Soria", "Baleares",
        #     "Barcelona", "Vizcaya", "LasPalmas", "SantaCruzdeTenerife", "Tarragona", "Gerona", "Guipuzcoa", "Lerida",
    ]


    main(usr, pwd, tags)
