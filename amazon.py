


from selenium import webdriver
import time
import selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("C:\\Users\\Administrator\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnavm_hdr_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=anywhere_v2_us&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

time.sleep(1)

create_new = driver.find_element_by_class_name("a-accordion-row-a11y")
create_new.click()

time.sleep(1)

name = 'Benefactor'
phone = input("Enter your phone number: ")
password = 'beneop'

name_textbox = driver.find_element_by_id("ap_customer_name")
name_textbox.send_keys(name)

phone_textbox = driver.find_element_by_id("ap_email")
phone_textbox.send_keys(phone)

password_textbox = driver.find_element_by_id("ap_password")
password_textbox.send_keys(password)

time.sleep(5)

verify_element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/form/div[7]').click()
time.sleep(1)
verify_element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/form/div[7]').click()
time.sleep(20)

a = "A text with a One Time Password (OTP) has been sent to the number above."

try:
    if a == driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/p[3]').text:
        otp = input("Please enter the OTP: ")
        otp_textbox = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/form[1]/div[1]/input')
        otp_textbox.send_keys(otp)
        account = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/form[1]/span/span/input')
        account.click()
        time.sleep(5)

except selenium.common.exceptions.NoSuchElementException:
    print('Number already exists.. Creating with same number..')
    time.sleep(2)

    create_account = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[4]/span')
    create_account.click()
    time.sleep(2)

    create_account_anyway = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/form/span/span/input')
    create_account_anyway.click()

    otp = input("Please enter the OTP: ")
    otp_textbox = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/form[1]/div[1]/input')
    otp_textbox.send_keys(otp)

    time.sleep(5)

    create_amazon_account_login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/form[1]/span/span/input')
    create_amazon_account_login.click()



time.sleep(3)

new_url = "https://gaming.amazon.com/intro"
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)
time.sleep(1)

try_prime = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[4]/button/span/div')
try_prime.click()
cont = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[5]/button/span')
cont.click()
time.sleep(1)

file = open('cc.txt', 'r')
f = file.readline()

cc_name = "David"
cc_num = f[:16]


ccname_textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[2]/div/div/form/div[3]/div[1]/input')
ccname_textbox.send_keys(cc_name)

ccnum_textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[2]/div/div/form/div[3]/div[2]/div/input')
ccnum_textbox.send_keys(cc_num)

# exp_m = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[2]/div/div/form/div[3]/div[4]/div/div[1]/span[1]/span/span/span/span')
# exp_m.click()
# exp_06 = driver.find_element_by_xpath('/html/body/div[5]/div/div/ul/li[6]/a')
# exp_06.click()
# time.sleep(1)
#
# exp_y = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[2]/div/div/form/div[3]/div[4]/div/div[1]/span[3]/span/span/span')
# exp_y.click()
# exp_24 = driver.find_element_by_xpath('/html/body/div[4]/div/div/ul/li[4]/a')
# exp_24.click()
# time.sleep(1)

# add_your_card = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[2]/div/div/form/div[3]/div[5]/span/span/input')
# add_your_card.click()
time.sleep(10)

# address here..
f_name = "Benefactor"
address_1 = "451 constellation blvd"
city = "LEAGUE CITY"
state = "Texas"
zip_code = "77573"
ph_no = "6235896523"

# fname_textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[2]/div[1]/input')
# fname_textbox.send_keys(f_name)

address_textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[2]/div[2]/input')
address_textbox.send_keys(address_1)

city_textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[2]/div[4]/input')
city_textbox.send_keys(city)

state_textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[2]/div[5]/input')
state_textbox.send_keys(state)

zip_textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[2]/div[6]/input')
zip_textbox.send_keys(zip_code)

phone_number_textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[2]/div[8]/input')
phone_number_textbox.send_keys(ph_no)

use_this_address = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div/div/div[2]/div/span/span/input')
use_this_address.click()
time.sleep(2)

join_prime = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[7]/form/fieldset/button/span[1]')
join_prime.click()
time.sleep(5)

srch = "battlefield"
search = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div/input')
search.send_keys(srch)

claim = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/button/span/div/p')
claim.click()

claim_now = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/button')
claim_now.click()

code_game = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/input')
game_code = code_game.text

fh = open('output.txt', 'r')
fh.writelines(game_code)

time.sleep(1000)
