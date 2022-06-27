from selene import be, have
from selene.support.shared import browser

browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
