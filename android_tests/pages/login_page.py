from android_tests.pages.base_page import BasePage


def split_str(s):
    return [ch for ch in s]


class LoginPage(BasePage):
    """Login page representation."""

    MAIL_LOC = "et_email"
    PASSWORD_LOC = "et_code"
    CONTINUE_LOC = "btn_continue"

    def enter_email(self, email):
        email_field = self.driver.find_element_by_id(self.MAIL_LOC)
        email_field.click()
        email_field.send_keys(email)

    def click_on_continue(self):
        continue_btn = self.driver.find_element_by_id(self.CONTINUE_LOC)
        continue_btn.click()

    def enter_password(self, password):
        i = 0
        old_loc = self.PASSWORD_LOC
        while i < 4:
            self.driver.find_element_by_id(self.PASSWORD_LOC +
                                           str(i+1)).send_keys(split_str(password)[i])
            self.PASSWORD_LOC = old_loc
            i += 1
