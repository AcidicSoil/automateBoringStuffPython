# Click the link to activate the alert
#driver.find_element_by_css_selector('body > center > button').click()

# Wait for the alert to be displayed and store it in a variable
#alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
#text = alert.text

# Press the OK button
#alert.accept()

search_form = driver.find_element(By.CLASS_NAME, "table_sortable")
search_box = search_form.find_element(By.CLASS_NAME, "AlternatingRowStyle")
search_table = search_form.find_element(By.CLASS_NAME, "RowStyle")

tables = len(driver.find_elements_by_class_name("table_sortable"))

rows = 1+len(driver.find_elements_by_class_name(
    "AlternatingRowStyle"))

Item_name = (driver.find_elements_by_xpath(
    "//*[@id='ctl00_BodyContentPlaceHolder_gridCOMBOM']/tbody/tr[2]/td"))

print("Number of Tables:", tables)
print("Number of Rows:", rows)
print("Number of Columns:", Item_name)

driver.execute_script("""
  return document.querySelectorAll('#table_id tr').length
""")
#while part_name() not true:
#for r in range(2, rows):
#    for p in range(1,cols+1):
#        value = driver.find_element_by_xpath(
#            "//*[@id='ctl00_BodyContentPlaceHolder_gridCOMBOM']/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
#if value == part:
#   break
#        print(value, end='      ')
#    print()
#driver.quit()
#time.sleep(5)
#elementRows = driver.find_elements_by_xpath(
#   )
#print(elementList)
#try:
#    cookies = WebDriverWait(driver, 15).until(
#        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
#       )
#finally:
#driver.quit()
#.find_element_by_id('onetrust-accept-btn-handler').click()
#print('nothing yet')
#except NoSuchElementException:
#   print('dunno')
