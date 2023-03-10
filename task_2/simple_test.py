from selene.support.shared import browser
from selene import be, have


def test_positive(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene yashaka').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser'))


def test_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('olololololololoадынадын').press_enter()
    browser.element('[class="card-section"]').should(have.text('did not match any documents.'))


# new comment added

def test_merge_conflict2(open_browser):
    browser.element('[name="q"]').should(be.blank).type('сырники').press_enter()
    browser.element('[id="search"]').should(have.text('Сырники домашние, пошаговый рецепт с фото'))
