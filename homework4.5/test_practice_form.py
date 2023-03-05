import os
from selene import browser, be, have
from selenium.webdriver import Keys


def test_form(chrome_browser):
    browser.open(browser.config.base_url + "/automation-practice-form")
    browser.element("#firstName").should(be.blank).type("FirstName")
    browser.element("#lastName").should(be.blank).type("LastName")
    browser.element("#userEmail").should(be.blank).type("name@example.com")
    browser.element('[for="gender-radio-1"]').should(have.text("Male")).click()
    browser.element("#userNumber").should(be.blank).type("7800000000")
    browser.element("#dateOfBirthInput").send_keys(Keys.CONTROL, "a").type(
        "01 Jan 2000"
    ).press_enter()
    browser.element("#dateOfBirthInput").click()
    browser.element("select > [value='0']").should(have.text("January")).click()
    browser.element("select > [value='1990']").should(have.text("1990")).click()
    browser.element(".react-datepicker__day--001").should(have.text("1")).click()
    browser.element("#subjectsInput").should(be.blank).type(
        "Computer Science"
    ).press_enter()
    browser.element("[for ='hobbies-checkbox-1']").should(have.text("Sports")).click()
    browser.element("[for ='hobbies-checkbox-2']").should(have.text("Reading"))
    browser.element("[for ='hobbies-checkbox-3']").should(have.text("Music"))
    browser.element("#uploadPicture").send_keys(os.getcwd() + "/homework.png")
    browser.element("#currentAddress").should(be.blank).type(
        "Main St, Apt 2, SPb, Russia, 190000"
    )
    browser.element("#state").click()
    browser.element("#react-select-3-option-0").should(have.text("NCR")).click()
    browser.element("#city").click()
    browser.element("#react-select-4-option-0").should(have.text("Delhi")).click()
    browser.element("#submit").click()
    browser.element("tr:nth-child(1) td:nth-child(2)").should(
        have.text("FirstName LastName")
    )
    browser.element("tr:nth-child(2) td:nth-child(2)").should(
        have.text("name@example.com")
    )
    browser.element("tr:nth-child(3) td:nth-child(2)").should(have.text("Male"))
    browser.element("tr:nth-child(4) td:nth-child(2)").should(have.text("7800000000"))
    browser.element("tr:nth-child(5) td:nth-child(2)").should(
        have.text("01 January,1990")
    )
    browser.element("tr:nth-child(6) td:nth-child(2)").should(
        have.text("Computer Science")
    )
    browser.element("tr:nth-child(7) td:nth-child(2)").should(have.text("Sports"))
    browser.element("tr:nth-child(8) td:nth-child(2)").should(have.text("homework.png"))
    browser.element("tr:nth-child(9) td:nth-child(2)").should(
        have.text("Main St, Apt 2, SPb, Russia, 190000")
    )
    browser.element("tr:nth-child(10) td:nth-child(2)").should(have.text("NCR Delhi"))
    browser.element("#closeLargeModal").click()
