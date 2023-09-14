import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# List of phone numbers
phone_numbers = ["911111444455"]

options = Options()
options.add_argument("--window-size=1000,800")
# Message to be sent
message = "Link To Cse Section A Unofficial Group - https://chat.whatsapp.com/CV6b6teHpyb4sdXI8ioP0M \n This Message Was Sent To Everyone By A Python Program I Made, Its Open Source On GitHub - https://github.com/Emon69420/MultipleMessagesWhatsapp/blob/main/multiplemessagesBot.py\n Quick Q&A \n Am I Dumb To Make A Group Before The Section Is Finalised? \n Nope, I Was Added To The Unofficial CSE B Group And They Got A Lot Of Study Material There, So I Made This So We Are On Par With Them \n Also Im Sorry For The Disturbance If I Woke You Up, But My Bot Is Hosted On Microsoft Azure US Instance And Its Daytime There, Thanks, Your Welcome - Your's Truly Emon"

# Path to chromedriver
driver_path = 'C:/Users/emong/Desktop/chromedriver.exe'

# Start the browser
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Scan the QR code and then press ENTER in the console
input("Press ENTER after scanning the QR code")


for phone_number in phone_numbers:
    # Open chat
    driver.get(f'https://web.whatsapp.com/send?phone={phone_number}')

    # Wait for the page to load
    time.sleep(30)

    # Find the message input box
    message_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')

    # Send the message
    message_box.send_keys(message)

    # Find the send button

    send_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]')

    time.sleep(3)

    # Click the send button
    send_button.click()

    # Wait a bit before sending the next message
    time.sleep(2)

# Close the browser
driver.quit()