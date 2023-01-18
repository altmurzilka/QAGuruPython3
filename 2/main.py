from selene import browser
from selene import be, have


browser.open_url('https://google.com/ncr')
browser.element('[name="q"]').should(be.blank).type('selene yashaka').press_enter()
browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser'))