import allure

@allure.step("Opening browser")
def open_browser():
    ...

def create_course_study(title: str):
    with allure.step(f"'Creating course with title' {title}"):
        ...

def close_browser():
    ...

@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    pass


def test_feature():
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwright")