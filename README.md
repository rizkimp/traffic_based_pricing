### instalation

1. clone the repository

    ```bash
    git https://github.com/rizkimp/saucelab-playwright.git
    cd traffic_based_pricing
    ```

2. install the required packages

   ```bash
    pip install -r requirements.txt
    playwright install
    ```

3. run the automation test

    ```bash
    behave /features/test-name.feature
    ```

4. open test report from browser

    ```bash
    allure serve
    ```