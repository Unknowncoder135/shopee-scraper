import os
import re
import time
import urllib
import urllib.request

# upadeted newest



import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
# SOPEE SCRIPT................................................................
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

master_list = []
# main_url = "https://shopee.sg/Augustine%E2%80%99s-SuperBoost-Certified-Organic-Supplement-i.369396274.7474062692?adsid=0&campaignid=0&position=18"
# main_url = "https://shopee.com.my/Local-shipment-Fashion-ethnic-traditional-panda-fat-man-loose-large-size-short-sleeve-T-shirt-panda-fat-printing-T-shirt-i.162168798.3014835472?ads_keyword=t%20shirt&adsid=28890058&campaignid=15326919&position=2"
# main_url = "https://shopee.com.my/-FREE-GIFTS-A6-Thermal-Sticker-Thermal-Paper-Shopee-Waybill-Shipping-Label-Consignment-Note-Sticker-100*150mm-10*15cm-i.17814982.6229533411?position=2"
# main_url = 'https://shopee.sg/%E3%80%90Ready-stock%E3%80%91Women-Fashion-One-Piece-Seamless-Ice-Silk-Panties-Girls-Clothing-Underwear-Panty-i.237477596.4620519607?position=12'
# main_url = "https://shopee.com.my/%F0%9F%9B%91-Kenko-Water-Filter-OFFER%E2%80%BC-FULL-PAKEJ-1-SET-NANO-FILTER-EXTRA-FREE-GIFT-WASHING-MACHINE-FILTER-i.33367584.1172942862?position=12"
# main_url = "https://shopee.sg/%E3%80%90Ready-stock%E3%80%91Women-Fashion-One-Piece-Seamless-Ice-Silk-Panties-Girls-Clothing-Underwear-Panty-i.237477596.4620519607?position=12"
# main_url = "https://shopee.ph/Silver-Letter-Foil-balloon-Number-balloons-letter-balloons-16-inch-metallic-silver-foil-balloon-i.261018.3160724773?position=2"
# main_url = "https://shopee.com.my/(Ready-Stock)Stitched-Large-Leather-Mousepad-Keyboard-Mat-with-Anti-slip-Suede-Backing-Smooth-Mouse-Pad-of-Pu-Leather-Waterproof-Desk-Mat-i.300535890.4657022580?position=8"
# main_url = "https://shopee.com.my/Annona-Bird-Nest-On-The-Go-%E2%9D%A4%EF%B8%8F-Semudah-Koyak-Minum-Cantik-Sesuai-bagi-Mereka-yang-Sibuk-%F0%9F%91%8D%F0%9F%8F%BB-i.459304558.11623918246?adsid=0&campaignid=0&position=22"
# main_url = "https://shopee.com.my/SELUAR-SLEK-WANITA-3838-STRAIGHT-CUT-URBAN-DESIGN-SLACK-PANTS-WOMEN-SELUAR-KERJA-WANITA-FEMALE-FORMAL-WORK-PANTS-i.198874596.5617755396?position=3"
main_url = "https://shopee.com.my/-2-3-4mm-Charm-Czech-Glass-Seed-Beads-DIY-Bracelet-Necklace-For-Jewelry-Making-Accessories-i.190957605.7736332638?position=1"


driver.get(main_url)
time.sleep(5)
hh = main_url.split(".")
item_id = str(hh[-1])
item_id = item_id.split('?')
item_id = int(item_id[0])
print(item_id)

main_list = []

try:
    lan = driver.find_element_by_class_name("shopee-button-outline--primary-reverse").click()
    time.sleep(3)
except:
    pass

try:                                        
    
    name = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span"))).text
                                    
except:
    try:
        name = driver.find_element_by_class_name("attM6y").text
    except:
        name = "Not found"
print(name)

try:
    rating = driver.find_element_by_class_name("_1mYa1t").text
    rating = float(rating)
except:
    try:
        rating =  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]'))).click()
        rating = float(rating)
    except:
        rating = "Not found"
try:
    rating_count = driver.find_elements_by_class_name("_3A3c6_")
    for x in rating_count:
        ks = x.text
    rating_count = ks.strip() 
    rating_count = rating_count.split("\n")[0]
    rating_count = rating_count
except:
    rating_count = "Not found"




# try:                                                    
#     for x in range(0,20):
#         try:
#             clicker = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/button[2]')
#             clicker.click()
#             time.sleep(3)
#         except:
#             clicker = driver.find_element_by_class_name('_1Z42SM')
#             clicker.click()
#             time.sleep(3)


# except:
#     print("madad")
#     pass


imgs = []

temp = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]')
temp.click()
time.sleep(3)
try:                                
    for x in range(1, 25):      
        my_property = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, f"//*[@id='modal']/div[2]/div[1]/div/div[2]/div[2]/div[{x}]/div[1]/div"))).value_of_css_property("background-image")
        tem = re.split('[()]', my_property)[1]
        tem = tem.replace('"','')
        imgs.append(tem)
    
except:
    print("ok done")
    pass

driver.get(main_url)
time.sleep(1)


imgs = set(imgs)
print(len(imgs))
print(imgs)


try:
    description = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div[2]/div[2]/div').text
    description = description.replace('\n')
except:
    try:
        description = driver.find_element_by_class_name('_3yZnxJ').text
    except:
        description = "Not found"


modf = driver.find_elements_by_css_selector('._2oeDUI')
print(len(modf))

two_first=[]
two_second  = []



vatiants= []
try:                                        
    lable1 = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/label").text
except:
    try:
        lable1 = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/label').text
    except:
        try:                                        
            lable1 = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/label').text
        except:
            lable1 = 'size'
try:
    lable2  = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[2]/label").text
except:
    try:
        lable2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[2]/label').text
    except:
        try:
            lable2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[2]/label').text
        except:
            lable2 = 'color'
# print(lable2,lable1)

ss = 'sold out'
dd = 0


try:
    for x in range(1,200):                      
        # try:
        #     tem = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[{x}]').text
        #     print(tem)
        
        # except:
        #     try:
        #         tem = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[{x}]').text
        #     except:
        #         print(tem)
        #         continue

        try:                                       
            size = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[{x}]')
            tem = size.text
            size.click()
        except:
            try:
                size = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[{x}]')
                tem = size.text
                size.click()
            except:
                try:                                        
                    size = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[{x}]')
                    tem = size.text
                    size.click()
                except:
                    print("sdk")
                    break


        time.sleep(2)
        two_first.append(tem)
        # imgs = []
        try:
            for z in range(0, 1):
                my_property = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div'))).value_of_css_property("background-image")
                tems = re.split('[()]', my_property)[1]
                imgsd = tems.replace('"','')
                # print(imgsd)

        except:
            imgsd = "nn"
            pass

        try:
            is_up = "product-variation--disabled" in size.get_attribute("class")
            print(is_up)
        except:
            print("jjs")
        driver.execute_script("window.stop()")
        time.sleep(1)
        try:
            for y in range(1,200):
                try:                                
                    color = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[2]/div/button[{y}]')
                    hhs = color.text
                    color.click()                           
                except:
                    try:
                        color = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[2]/div/button[{y}]')
                        hhs = color.text
                        color.click()
                    except:
                        try:
                            color = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[2]/div/button[{y}]')
                            hhs = color.text
                            color.click()
                            
                        except:                                            
                            # try:                                        //*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[1]
                            #     color = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[{y}]')
                            #     hhs = color.text
                            #     color.click()
                            # except:                                   
                            try:
                                color = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[2]/div/button[{y}]')
                                hhs = color.text
                                color.click()
                            except:
                                print("second")
                                break
                time.sleep(2)
                
                try:
                    is_active = "product-variation--disabled" in color.get_attribute("class")
                    print(is_active)
                except:
                    print("sjdhfj")
                
                 

               
                try:
                    variant_price = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[1]').text
                    variant_price = variant_price.replace('RM','')
                    variant_price = variant_price.replace('$','')
                    variant_price = float(variant_price)
                    
                except:
                    variant_price = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[1]').text
                    variant_price = variant_price[1:]

                try:
                    final_price = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]').text
                    final_price = final_price.replace('RM','')
                    final_price = final_price.replace('$','')
                    final_price = float(final_price)

                except:
                    final_price = variant_price

                try:                                            
                    stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[3]/div[2]/div[2]').text
                    stock_count = stock_count.split(' ')[0]
                    stock_count = int(stock_count)
                    print(stock_count)
                except:
                    try:
                        stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[4]/div[2]/div[2]').text
                        stock_count = stock_count.split(' ')[0]
                        stock_count = int(stock_count)
                        print(stock_count)
                    except:                                             
                        try:                                            
                            stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[3]/div[2]/div[2]').text
                            stock_count = stock_count.split(' ')[0]
                            stock_count = int(stock_count)
                            print(stock_count)

                        except:
                            try:
                                stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[3]/div[2]/div[2]').text
                                stock_count = stock_count.split(' ')[0]
                                stock_count = int(stock_count)
                                print(stock_count)
                            except:
                                stock_count = 1
                two_second.append(hhs)
                try:
                    if stock_count ==1:
                        stock_status = 'low'
                    elif stock_count > 5:
                        stock_status = 'available'
                    elif stock_count <= 4:
                        stock_status = 'low '
                    elif stock_count == 0:
                        stock_status = 'sold out'
                except:
                    stock_status = 'low'
            
                try:
                    discount = driver.find_element_by_class_name("_3LRxdy").text
    
                except:
                    discount = "Not found"
                color.click()
                print(stock_status)
                variant = {
                 f'{lable1}':tem,
                f'{lable2}':hhs,
                }
                
                if is_active == True or is_up == True:
                    stock_status = ss
                    stock_count = dd
                mains_dir = {
                'original_price':variant_price,
                'final_price':final_price,
                'stock_status':stock_status,
                'stock_count':stock_count,
                'variant':variant,
                }
                if imgsd !='nn':
                    mains_dir['image']= imgsd
                if discount != 'Not found':
                    if (is_active == False and  is_up == False) or  (is_active == True and is_up == False):
                        mains_dir['discount']= discount
                else:
                    pass
                vatiants.append(mains_dir)
                print(mains_dir)
        except:
            print("loop over")
            pass
    
except:
    print("done")
    pass
print(vatiants)
print(len(vatiants))
two_second = set(two_second)
two_first = set(two_first)


# models=[]
# modes = driver.find_elements_by_class_name("product-variation")
# for x in modes:
#     models.append(x.text)

flag=0
if len(vatiants) == 0:
    two_first = []
    try:
        print("ssss")
        for x in range(1,200):
            flag=1
            try:                                    
                tem = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[{x}]').text
                size = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[{x}]')
                size.click()                        
            except:
                try:
                    size = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[{x}]') 
                    size.click() 
                    tem = size.text
                except:

                    try:
                        size = driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[{x}]')
                        size.click()
                        tem  = size.text
                    except:
                        break
            is_lisa = "product-variation--disabled" in size.get_attribute("class")
            print(is_lisa)
            
            time.sleep(3)
            print(tem)
            two_first.append(tem)
   
            try:                                              
                variant_price = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div/div').text
                try:
                    hhss = variant_price[1:]
                    variant_price = float(hhss)
                except:
                    hhdd = variant_price[2:]
                    variant_price = float(hhdd)
                print(variant_price)
            except:
               
                variant_price = "Not found"                                       
            


            try:
                final_price = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]').text
                try:
                    hhss = final_price[1:]
                    final_price = float(hhss)
                except:
                    hhdd = final_price[2:]
                    final_price = float(hhdd)
            except:
                final_price = variant_price
            # imgs = []
            # try:
            #     for z in range(0, 1):
            #         my_property = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            #             (By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div'))).value_of_css_property("background-image")
            #         tems = re.split('[()]', my_property)[1]
            #         imgsd = tems.replace('"','')
            #         print(imgsd)

            # except:
            #     imgsd = "nn"
                # pass   
            try:                                            
                stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[2]/div[2]/div[2]').text
                stock_count = stock_count.split(' ')[0]
                stock_count = int(stock_count)
                print(stock_count) 
            except:
                try:
                    stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[4]/div[2]/div[2]').text
                    stock_count = stock_count.split(' ')[0]
                    stock_count = int(stock_count)
                    print(stock_count) 
                except:
                    try:
                        stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[2]/div[2]/div[2]').text
                        stock_count = stock_count.split(' ')[0]
                        stock_count = int(stock_count)
                        print(stock_count)                          
                    except:
                        try:
                            stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[2]/div[2]/div[2]').text
                            stock_count = stock_count.split(' ')[0]
                            stock_count = int(stock_count)
                            print(stock_count)
                        except:
                            stock_count = 1

            try:
                if stock_count == 1:
                    stock_status = 'low'
                elif stock_count >= 5:
                    stock_status = 'available'
                elif stock_count <= 4:
                    stock_status = 'low '
                elif stock_count == 0:
                    stock_status = 'sold out'
            except:
                stock_status = 'available'
            if is_lisa == True:
                    stock_status = ss
                    stock_count = dd
            variantt = {
                f'{lable1}':tem,
            }
            mins_s = {
                'original_price':variant_price,
                'final_price':final_price,
                'stock_status':stock_status,
                'stock_count':stock_count,
                'variant':variantt,
                }
            print(mins_s)
            # if imgsd != 'nn':
            #     mins_s['image']= imgsd
            vatiants.append(mins_s)
    except:
        print("dones")
        pass


print(len(vatiants))


# if no variant found
if len(vatiants) == 0:
    try:
        variant_price = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div/div').text
        variant_price = variant_price.replace('$', '')
        variant_price = variant_price.replace('RM','')
        variant_price = float(variant_price)
    except:
        variant_price = "Not found"
    try:
        final_price = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]').text
        final_price = final_price.replace('$', '')
        final_price = final_price.replace('RM','')
        final_price = float(final_price)

    except:
        final_price = 'null'

    try:                                            
        stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]').text
        stock_count = stock_count.split(' ')[0]
        stock_count = int(stock_count)
        print(stock_count)
    except:
        try:                                            
            stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[3]/div[2]/div[2]').text
            stock_count = stock_count.split(' ')[0]
            stock_count = int(stock_count)
            print(stock_count)

        except:
            try:
                stock_count = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[3]/div[2]/div[2]').text
                stock_count = stock_count.split(' ')[0]
                stock_count = int(stock_count)
                print(stock_count)
            except:
                stock_count = 1

    try:
        if stock_count ==1:
            stock_status = 'low'
        elif stock_count > 5:
            stock_status = 'available'
        elif stock_count <= 4:
            stock_status = 'low '
        elif stock_count == 0:
            stock_status = 'sold out'
    except:
        stock_status = 'low'
    try:
        discount = driver.find_element_by_class_name("_3LRxdy").text
    except:
        discount = "Not found"
    print(stock_status)
    mainsss_dir = {
    'original_price':variant_price,
    'final_price':final_price,
    'stock_status':stock_status,
    'stock_count':stock_count,
    'variant':'null',
    'discount':discount,
    }
    vatiants.append(mainsss_dir)
    print(mainsss_dir)



vvs = {
    f'{lable1}' : two_first,
    f'{lable2}' : two_second,
}
if flag==1:
    del vvs[f'{lable2}']


item_parent = {
    'name':  name,
    'description': description,
    'rating': rating,
    'rating_count': rating_count,
    'url': main_url,
    'item_id': item_id,
    'variants':vvs,
    'images': imgs,

}





# item_variants1 = []
# item_variants1.append(item_variants)
main_dir = {
    "item_parent": item_parent,
    "item_variants": vatiants,
}

main_list.append(main_dir)
df = pd.DataFrame(main_list)
df.to_json('SopeeOutput.json', orient='records', lines=True)

driver.quit()
print('script run successfully')